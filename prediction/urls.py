from django.urls import path
from .import views
urlpatterns=[
    path('',views.addpredict,name='addpredict'),
    path('<int:prediction_id>',views.predict,name='predict')
]