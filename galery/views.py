from urllib import response
from django.shortcuts import render
#from django.http import HttpResponse
#from django.shortcuts import render #pour python montreal

# def hello(request):

#     if "nom" in request.GET:
#         nom = request.GET['nom']
#         msg = f"salut {nom}"
#     else:
#         msg ="Salut Montreal!"    
#     response = HttpResponse(msg)
#     return response




#this function is responsible for the main page of our application to be able to respond to a request
def index(request):
    return render(request, 'galery/index.html')

def imagem(request):
    return render(request, 'galery/imagem.html' )


