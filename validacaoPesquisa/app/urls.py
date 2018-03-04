from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^cadastrar_carro/', 'app.views.cadastrar_carro', name='cadastrar_carro'),
    url(r'^listar_carro/', 'app.views.listar_carro', name='carro_list'),
    url(r'^editar_carro/(?P<pk>[0-9]+)', 'app.views.editar_carro', name='editar_carro'),
    url(r'^deletar_carro/(?P<pk>[0-9]+)', 'app.views.deletar_carro', name='remover_carro'),
)

