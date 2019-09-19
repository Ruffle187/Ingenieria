from django.conf.urls import patterns, include, url

from aplication import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'entregaIng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^personas/',views.listarPersona),
    url(r'^personas/',views.listarProducto),
    url(r'^personas/',views.listarCompra),
)
