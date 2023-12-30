from django.db import models

from user import models as user_models

# Create your models here.
class Calculator(models.Model):
    user_object = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    when_to_use = models.TextField()
    pearls_pitfalls = models.TextField()
    why_use = models.TextField()

class Category(models.Model):
    calculator_object = models.ForeignKey(Calculator, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)

class ChoiceQuestion(models.Model):
    
    question = models.CharField(max_length=255)
    supplement = models.CharField(max_length=255)

