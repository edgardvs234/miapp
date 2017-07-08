from django.contrib import admin
from users.models import Usuarios
from users.models import Categoria
from users.models import Perdidos
from users.models import Pista
from users.models import Denuncia
from users.models import Noticias
# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Pista)
admin.site.register(Categoria)
admin.site.register(Perdidos)
admin.site.register(Denuncia)
admin.site.register(Noticias)
