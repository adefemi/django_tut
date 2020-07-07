from rest_framework.viewsets import ModelViewSet
from .serializers import EventMain, EventMainSerializer, AddressGlobalSerializer, EventFeatureSerializer
from rest_framework.response import Response
from user.models import AddressGlobal


class EventMainView(ModelViewSet):
    serializer_class = EventMainSerializer
    queryset = EventMain.objects.select_related(
        "author", "address_info").prefetch_related("event_features")

    def create(self, request, *args, **kwargs):
        a_serializer = AddressGlobalSerializer(data=request.data)
        a_serializer.is_valid(raise_exception=True)
        a_serializer.save()

        data = {**request.data, "address_info_id": a_serializer.data["id"]}

        e_serializer = self.serializer_class(data=data)
        if not e_serializer.is_valid():
            AddressGlobal.objects.filter(id=a_serializer.data["id"]).delete()
            raise Exception(e_serializer.errors)
        e_serializer.save()

        features = request.data.get("features", None)
        if not features:
            AddressGlobal.objects.filter(
                id=a_serializer.data["id"]).delete()
            raise Exception("features field is required")

        if not isinstance(features, list):
            features = [features]

        data = []
        for f in features:
            if not isinstance(f, dict):
                AddressGlobal.objects.filter(
                    id=a_serializer.data["id"]).delete()
                raise Exception("Feature instance must be an object")
            data.append({
                **f, "eventmain_id": e_serializer.data["id"]
            })

        f_serializer = EventFeatureSerializer(data=data, many=True)
        if not f_serializer.is_valid():
            AddressGlobal.objects.filter(id=a_serializer.data["id"]).delete()
            raise Exception(f_serializer.errors)
        f_serializer.save()

        return Response(self.serializer_class(self.get_queryset().get(id=e_serializer.data["id"])).data, status=201)
