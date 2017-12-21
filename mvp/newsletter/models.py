from django.db import models

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255, default='Enter text', blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email #, str(self.timestamp)