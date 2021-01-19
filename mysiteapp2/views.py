from django.shortcuts import render

# Create your views here.
def fnIndex(request):
    return render(request,'index.html')
def assginment1(request):
    return render(request, 'assignment1.html')

def assginment2(request):
    return render(request, 'assignment2.html')
def assginment3(request):
    return render(request, 'assignment3.html')
