from django.contrib import admin
from . models import Post

class PostAdmin(admin.ModelAdmin):
    # passamos lista de campos que queremos que seja mostrado
    list_display =['title', 'sub_title', 'full_name',
                   'categories', 'deleted'] 
    # vai exibir um campo de pesquisa
    search_fields =['title', 'sub_title'] 
    # quando formos editar um Post, vai exibir só o título e o sub-título
    # fields =['title', 'sub_title'] 
    
    # consulta com filtro usando queryset
    ''' def get_queryset(self, request):
        return Post.objects.filter(deleted=True) '''


# Register your models here.
admin.site.register(Post, PostAdmin)
