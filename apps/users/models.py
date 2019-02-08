from django.db import models
import bcrypt
import re
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
  def validate_login(self, form_data):
    errors = []
    if len(form_data['email']) < 1:
      errors.append("Please enter your username")
    if len(form_data['password']) < 1:
      errors.append('Please enter your password')
      return errors

  def validate_reg(self, form_data):
    errors = []

    if len(form_data['first_name']) < 3:
      errors.append("First name must be at least 3 characters")
    if len(form_data['last_name']) < 3:
      errors.append("Last name must be at least 3 characters")
    if len(form_data['password']) < 8:
      errors.append("Password must be at least 8 characters")
    if len(form_data['email']) > 0:
      if not EMAIL_REGEX.match(form_data['email']):
        errors.append("Email must be valid")
    else:
        errors.append('Please provided an email')
    return errors


class UserLogin(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  pw_hash = models.CharField(max_length=500)
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  updated_at = models.DateTimeField(default=datetime.now, blank=True)


userManager = UserManager()
