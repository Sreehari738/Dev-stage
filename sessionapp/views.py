from django.shortcuts import render


# Create your views here.
def Welcome(request):
    return render(request,'show.html')
def setAttributes(request):

    request.session["value1"] = request.POST["t1"]
    request.session["value2"] = request.POST["t2"]
    request.session.set_expiry(30)
    return render(request,'getvalue.html')
def getAttributes(request):
    val3= request.session["value1"]

    val4 = request.session["value2"]
    return render(request,'showvalue.html',locals())


