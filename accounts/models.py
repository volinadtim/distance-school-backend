from django.contrib.auth.models import AbstractUser
from django.db import models
import jwt
from datetime import datetime
from datetime import timedelta
from django.conf import settings


class User(AbstractUser):
    TYPES_PROF = (
        ('D', 'Director'),
        ('S', 'Student'),
        ('T', 'Teacher'),
        ('P', 'Parent'),
        ('A', 'Admin'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(blank=True, max_length=150)
    user_type = models.CharField(max_length=1, choices=TYPES_PROF)
    avatar = models.ImageField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(blank=True, max_length=15)

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def _generate_jwt_token(self):
        """
        Создает веб-токен JSON, в котором хранится идентификатор
        этого пользователя и срок его действия
        составляет 60 дней в будущем.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    @property
    def token(self):
        """
        Позволяет нам получить токен пользователя, вызвав `user.token` вместо
        `user.generate_jwt_token().

        Декоратор `@property` выше делает это возможным.
        `token` называется «динамическим свойством ».
        """
        return self._generate_jwt_token()