from django.shortcuts import render

# Create your views here.
def hello_blog(request):
    lista = ['Ricardo', 'Patrícia', 'Necy',' Carolina', 'Da Paz']
    data = {'name': 'Curso de Django 3', 'lista_nomes': lista}
    return render(request, 'index.html', data)
