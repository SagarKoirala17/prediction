from django.shortcuts import render,redirect,get_object_or_404
from .models import Prediction
from django.contrib import messages
from .choice import sext,trestbpst,fbst,exangt,targett,restecgt
from .naive import *
from django.http import HttpResponse
# Create your views here.

def addpredict(request):
    if request.method=="POST":

        age=float(request.POST['Age'])
        sex=float(request.POST['sex'])
        cp=float(request.POST['CP'])
        trestps=float(request.POST['RestBPS'])
        restecg=float(request.POST['restecg'])
        chol=float(request.POST['Cholestrol'])
        fbs=float(request.POST['fbs'])
        thalch=float(request.POST['Thalach'])
        exang=float(request.POST['exang'])
        oldpeak=float(request.POST['oldpeak'])
        slope=float(request.POST['slope'])
        ca=float(request.POST['ca'])
        thal=float(request.POST['thal'])

        if request.user.is_authenticated:
            target = make_prediction([[
                age, sex, cp, trestps,chol,fbs, restecg,   thalch, exang, oldpeak, slope, ca, thal
            ]])
            prediction=Prediction(user=request.user,age=age,sex=sex,cp=cp,trestps=trestps,restecg=restecg,chol=chol,fbs=fbs,thalach=thalch,exang=exang,oldpeak=oldpeak,slope=slope,ca=ca,thal=thal, target = target)
            prediction.save()
            messages.success(request, "Your prediction has been submitted to the concerned one")
            # return HttpResponse(prediction.id)
            # return redirect('/prediction/', prediction_id=prediction.id, permanent=True)
            context = {
                'prediction': prediction
            }
            return render(request, 'predictionform/viewprediction.html', context)
        else:
            return redirect('login')

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
    # return HttpResponse(str(prediction_id))
    prediction=get_object_or_404(Prediction,pk=prediction_id)
    context={
        'prediction':prediction
    }
    return render(request,'predictionform/viewprediction.html',context)
