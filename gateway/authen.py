import jwt
from user.models import CustomUser
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from datetime import datetime


class CustomAuthenticationClass(BaseAuthentication):

    def authenticate(self, request):
        return self.validate_token(request.headers["Authorization"][7:]), None

    def validate_token(self, token):
        token_data = self.verify_jwt_token(token)
        if not token_data:
            return None
        try:
            user = CustomUser.objects.get(id=token_data["user_id"])
        except Exception:
            return None
        return user

    @staticmethod
    def verify_jwt_token(token):
        # try to decode the token
        try:
            decoded_data = jwt.decode(
                token, settings.SECRET_KEY, algorithm="HS256")
        except Exception:
            return None

        # check expiry
        exp = decoded_data["exp"]
        if datetime.now().timestamp() > exp:
            return None
        return decoded_data
