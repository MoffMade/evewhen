from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
import uuid


# Create your models here.
@python_2_unicode_compatible
class Pilot(models.Model):
    ccp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    pilot_name = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    kills = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    corp = models.ForeignKey('Corporation', on_delete=models.DO_NOTHING)  # TODO: Change on_delete to get new corp
    alliance = models.ForeignKey('Alliance', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "[ "+self.pilot_name+", "+str(self.ccp_id)+"]"


@python_2_unicode_compatible
class Corporation(models.Model):
    ccp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    corp_name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=10)
    alliance = models.ForeignKey('Alliance', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "[ "+self.corp_name+", "+str(self.ccp_id)+"]"


@python_2_unicode_compatible
class Alliance(models.Model):
    ccp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    alliance_name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return "[ "+self.alliance_name+", "+str(self.ccp_id)+"]"

