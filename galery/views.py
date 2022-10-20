from django.shortcuts import render


#this function is responsible for the main page of our application to be able to respond to a request
def index(request):
    return render(request, 'galery/index.html')


