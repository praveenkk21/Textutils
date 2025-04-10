from django.http import HttpResponse
from django.shortcuts import render
from .models import textutils


def index(request):
    return render(request,'index.html')

def analyzer(request):
    text = request.POST.get("text", "default")
    uppercase = request.POST.get("uppercase", "off")
    extraspace = request.POST.get("extraspace", "off")
    count = request.POST.get("count", "off")

    Transformedtext = text

    if uppercase == "on":
        Transformedtext = Transformedtext.upper()

    if extraspace == "on":
        Transformedtext = " ".join(Transformedtext.split())

    if count == "on":
        countofchars = len(Transformedtext)
        Transformedtext += f"\n\nTotal character count (excluding extra spaces): {countofchars}"
        
    textutils.objects.create(
        text=text,
        extra_space=True if extraspace == 'on' else False,
        count=True if count == 'on' else False,
        uppercase=True if uppercase == 'on' else False
        )

    return render(request, 'analyzer.html', {'Transformedtext': Transformedtext})

def dashboard(request):
    records = textutils.objects.all()
    return render(request,'dashboard.html',{'records':records})


