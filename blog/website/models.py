from django.db import models


class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )
    deleted = models.BooleanField(default=True)
    # para gravarmos a imagem vinculada ao Post  no BD
    # a imagem irá subir para uma pasta 'posts', dentro da pasta 'media
    imagem = models.ImageField(upload_to='posts', null=True, blank=True)


    def __str__(self):
        return self.title

    # apesar de não ser uma coluna da tabela, podemos
    # colocado no admin
    def full_name(self):
        return self.title + self.sub_title

    def get_categoty_label(self):
            return self.get_categories_display()


    # podemos colocar uma ordenação como segue
    full_name.admin_order_field = 'title'
