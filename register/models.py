from django.db import models

# Create your models here.
class RegisterForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def get_details(self):
        data = {
            "id":self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_no": self.phone_no,
            "email": self.email,
            "password":self.password
        }
        return data