from django.shortcuts import render

# Create your views here.

def built_in_filters(request):
    import datetime
    dt=datetime.date.today()
    d={'data':'haI pyTHOn aND HOW are YOU DjanGo','dt':dt,'c':0}
    return render(request,'built_in_filters.html',d)


def user_defined_filters(request):
    d={'data':'HI Python HoW ARe yoU DjanGO'}
    return render(request,'user_defined_filters.html',d)