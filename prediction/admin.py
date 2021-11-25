from django.contrib import admin
from .models import Prediction
# Register your models here.

class PredictionAdmin(admin.ModelAdmin):
    list_display=('id','sex','cp','trestps','chol','fbs','thalach','exang','oldpeak','slope','ca','thal','target',)
    list_display_links=('id',)
    search_fields=('id','sex','cp','trestps','chol','fbs','thalach','exang','oldpeak','slope','ca','thal','target',)
    list_per_page=25
admin.site.register(Prediction,PredictionAdmin)