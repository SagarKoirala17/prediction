from django.shortcuts import render
from .models import Prediction
from django.contrib import messages
from .choice import sext,trestbpst,fbst,exangt,targett,restecgt
from .naive import *
# Create your views here.

def addpredict(request):
    if request.method=="POST":
        age=request.POST['Age']
        sex=request.POST['sex']
        cp=request.POST['CP']
        trestps=request.POST['RestBPS']
        restecg=request.POST['restecg']
        chol=request.POST['Cholestrol']
        fbs=request.POST['fbs']
        thalch=request.POST['Thalach']
        exang=request.POST['exang']
        oldpeak=request.POST['oldpeak']
        slope=request.POST['slope']
        ca=request.POST['ca']
        thal=request.POST['thal']

        if request.user.is_authenticated:
            target = make_prediction([[
                age, sex, cp, trestps,chol,fbs, restecg,   thalch, exang, oldpeak, slope, ca, thal
            ]])
            prediction=Prediction(age=age,sex=sex,cp=cp,trestps=trestps,restecg=restecg,chol=chol,fbs=fbs,thalach=thalch,exang=exang,oldpeak=oldpeak,slope=slope,ca=ca,thal=thal, target = target)
            prediction.save()
            messages.success(request, "Your prediction has been submitted to the concerned one")
            return redirect('predict')
        else:
            return  redirect('login')


        

    else:
        context={
            'sext':sext,
            'trestbpst':trestbpst,
            'fbst':fbst,
            'restecgt':restecgt,
            'exangt':exangt,
        }
        return render(request,'predictionform/from.html',context)

def predict(request,prediction_id):
    prediction=get_object_or_404(Prediction,pk=prediction_id)
    context={
        'prediction':prediction
    }
    return render(request,'predictionform/viewprediction.html',context)
