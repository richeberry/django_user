from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# User 인스턴스 출력 시에 사용 _ email을 사용할 것이기 때문에 덮어씌움
class User(AbstractUser):
    nickname = models.CharField(max_length=15, unique=True, null=True)
    kakao_id = models.CharField(max_length=20, unique=False, null=True)
    address = models.CharField(max_length=40, unique=False, null=True)

    def __str__(self):
        return self.email