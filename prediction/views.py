from django.shortcuts import render

# Create your views here.

def addpredict(request):
    if request.method=="POST":
        pass
    else:
        return render(request,'predictionform/from.html')