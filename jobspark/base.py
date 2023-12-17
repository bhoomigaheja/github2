from .models import User

def authenticate_user(email):
    try:
        user = User.objects.get(email=email)
        return user
    except User.DoesNotExist:
        return None

