from django.db import models

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.core.urlresolvers import resolve, Resolver404
import requests

class Reference(models.Model):

    def validate_link(link):
        try:
            requests.get(link)
        except:
            raise ValidationError("Reference link is not available.(https://..)")

    REFERENCE_TYPE_CHOICE = (
        ('img', 'image'),
        ('lik', 'link'),
        ('doc', 'Document'),
        ('vid', 'Video'),
    )
    REFERENCE_STATUS_CHOICE = (
        ('A', 'Alive'),
        ('NA', 'Not Available'),
        )

    reference_name = models.CharField(max_length=150, blank=True)
    reference_type = models.CharField(max_length=3,
                                      choices=REFERENCE_TYPE_CHOICE,
                                      default='link')
    reference_link = models.CharField(max_length=150,
                                      null=False,
                                      blank=False,
                                      validators=[validate_link]
                                      )
    reference_description = models.TextField(max_length=500, blank=True)
    reference_status = models.CharField(max_length=2,
                                      choices=REFERENCE_STATUS_CHOICE,
                                      default='A')

    def __str__(self):
       return self.reference_link

    @classmethod
    def alive_references(cls, ids):
      if ids == None:
        return cls.objects.filter(reference_status='A')
      else:
        return cls.objects.filter(reference_status='A', pk__in=ids)
