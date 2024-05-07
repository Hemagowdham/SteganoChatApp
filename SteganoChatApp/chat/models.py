from django.db import models

# Create your models here.

class Emailwithattachment(models.Model):
	sender_email_address = models.EmailField(max_length = 254)
	sender_email_password = models.CharField(max_length=50)
	receiver_name = models.CharField(max_length=50)
	receiver_email_address = models.EmailField(max_length = 254)
	stegano_image = models.ImageField(upload_to='stegano_images/')
	