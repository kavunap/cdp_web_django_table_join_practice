from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Book(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='books')
    # variations = models.OneToManyField(Variation)

    def __str__(self):
        return f'{self.title}, {self.user.id}'

class Variation(models.Model):
    kind = models.CharField(max_length=255)
    book = models.ForeignKey('Book',on_delete=models.CASCADE, related_name='variations')

    def __str__(self):
        return f'{self.kind}, {self.book.id}'