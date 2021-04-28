# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# app/models.py or create another file for custom validators, i.e. app/custom_validators.py
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _  # use if you support internationalization

class Candidate(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    candidate_reference = models.CharField(max_length=8)
    score = models.ForeignKey('artictest.Score', on_delete=models.CASCADE)


class Score(models.Model):
    score=models.FloatField(validators=[MinValueValidator(0.0, MaxValueValidator(100.0))])
    