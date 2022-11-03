from django.urls import path
from galery.views import index, imagem
#from galery.views import hello, index

urlpatterns = [
    
    #path('', hello)
     path('', index),
     path('imagem/',imagem, name='imagem'),
]