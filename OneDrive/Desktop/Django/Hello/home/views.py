from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request , 'index.html',context)
    #return HttpResponse("this is homepage")
def contacts(request):
    return render(request , 'contact.html' )
    #return HttpResponse("You can contact me through these")    
def about(request):
    return render(request , 'about.html')   
def softy(request):
    return render(request , 'softy.html')      