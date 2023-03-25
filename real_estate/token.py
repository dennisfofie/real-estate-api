from real_estate.models import User
from rest_framework_simplejwt.tokens import RefreshToken



def generate_token(user:User):
    refresh = RefreshToken().for_user(user)

    tokens = {
        "access_token": str(refresh.access_token),
        "refresh": str(refresh)
    }

    return tokens