from rest_framework.viewset import ModelViewSet
from .serializers import EventMain, EventMainSerializer, AddressGlobalSerializer, EventFeatureSerializer
from rest_framework.response import Response


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
        e_serializer.is_valid(raise_exception=True)
        e_serializer.save()

        features = request.data.get("features", None)
        if not features:
            raise Exception("features field is required")

        if not isinstance(features, list):
            features = [features]

        data = []
        for f in features:
            data.append({
                **f, "eventmain_id": e_serializer.data["id"]
            })

        f_serializer = AddressGlobalSerializer(data=data, many=True)
        f_serializer.is_valid(raise_exception=True)
        f_serializer.save()

        return Response(e_serializer.data, status=201)
