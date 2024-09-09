from django.contrib.auth.backends import ModelBackend
from pm.models import User

# 로그인 API에 사용되는 class
class LoginIdBackend(ModelBackend):
    def authenticate(self, request, userId=None, password=None, **kwargs):
        try:
            user = User.objects.get(userId=userId)
        except User.DoesNotExist:
            return None

        # 비밀번호 검증
        if user.check_password(password):
            return user
        return None
