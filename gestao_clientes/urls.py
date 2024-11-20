
from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_urls
from home import urls as home_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', include(home_urls)),
    path('clientes/', include(clientes_urls)),
    path('home/', include(home_urls)),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  + debug_toolbar_urls()


admin.site.site_header = 'Gestão de Clientes'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Seja bem vindo ao Gestão de Clientes'