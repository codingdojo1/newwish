from django.db import models
from django.contrib.auth.models import User
from apps.users.models import UserLogin

# Create your models here.

class Wish(models.Manager):
  def validate(self, form_data):
    errors = []

    if len(form_data['name']) < 3:
      errors.append('Name must be at least three characters long.')

    if len(form_data['description']) < 1:
      errors.append('Description must be provided.')

    return errors

# def create_wish(self, form_data):
#     user = User.objects.get(id=users_id)
#     self.create(
#       name=form_data['name'],
#       description=form_data['description'],
#       creator=user,
# )



class Wish(models.Model):
  name = models.CharField(max_length=250)
  description = models.TextField()
  creator = models.ForeignKey(UserLogin, related_name="wishes")
  created_at = models.DateTimeField(auto_now_add=True)
  granted_at = models.DateTimeField(null=True, blank=True)
