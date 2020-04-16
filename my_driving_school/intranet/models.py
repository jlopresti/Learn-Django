from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class User(AbstractUser):
    is_secretary = models.BooleanField(default=False)
    is_inspector = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class StudentProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='student_profile')
	paid_hours = models.IntegerField(default=0)
	available_hours = models.IntegerField(default=0)
  
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if instance.is_student:
		StudentProfile.objects.get_or_create(user = instance)
	
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	if instance.is_student:
		instance.student_profile.save()