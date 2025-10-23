from django.shortcuts import render,HttpResponse

# Create your views here.


def home_view(request):
    return HttpResponse("سلام! این اولین پست من است.")
def home_page(request):
    return render(request,'index.html')
