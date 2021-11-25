from django.db import models
from .choices import sext,trestbpst,fbst,exangt,targett,restecgt
from django.utils.translation import  gettext as _
# Create your models here.
class Prediction(models.Model):
    age=models.IntegerField(_("age"))
    sex=models.BooleanField(_("sex"),choices=sext)
    cp=models.IntegerField(_("cp"))
    trestps=models.IntegerField(_("trestbps"))
    restecg=models.BooleanField(_("restecg"),choices=restecgt,default=1)
    chol=models.IntegerField(_("chol"))
    fbs=models.BooleanField(_("fbs"),choices=fbst)
    thalach=models.IntegerField(_("thalach"))
    exang=models.BooleanField(_("exang"),choices=exangt)
    oldpeak=models.FloatField(_("oldpeak"))
    slope=models.IntegerField(_("slope"))
    ca=models.IntegerField(_("ca"))
    thal=models.IntegerField(_("thal"))
    target=models.BooleanField(_("target"),choices=targett)

    def __bool__(self):
        self.target