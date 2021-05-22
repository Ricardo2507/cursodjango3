from django.shortcuts import render
from . models import Post

# Create your views here.


def hello_blog(request):
    lista = ['Ricardo', 'Patrícia', 'Necy', ' Carolina', 'Da Paz']

    list_posts = Post.objects.all()

    data = {'name': 'Curso de Django 3', 
            'lista_nomes': lista, 
            'posts': list_posts}

    return render(request, 'index.html', data)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})

