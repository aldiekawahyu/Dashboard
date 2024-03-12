
from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(max_length=254)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        # Menggunakan Django's built-in password hashing
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        # Memverifikasi password dengan Django's built-in function
        return check_password(raw_password, self.password)
