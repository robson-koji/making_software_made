
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from projeto_3 import models
from bsct import views
from projeto_3.views import CreateView_projeto_3, UpdateView_projeto_3, CloneView_projeto_3,\
                                    ListView_projeto_3, DetailView_projeto_3, DeleteView_projeto_3
from amontoado_3.decorators import superuser_only, staff_only
urlpatterns = patterns('',
    #                       
    ## Conjunto de URLS para a aplicacao web default
    #
    # Se digitar o raiz da app, cai na pagina de instrucoes
    url(r'^$', RedirectView.as_view(url='flat/instrucoes/')), 
    url( r'^add$', (CreateView_projeto_3.as_view( model=models.projeto_3)),
        {'acao': 'Cadastrar', 'media_saida': 'web'}, name = 'web_projeto_3_create'),
    url( r'^clone/(?P<pk>\d+)$', (CloneView_projeto_3.as_view( model=models.projeto_3)),
        {'acao': 'Clonar', 'media_saida': 'web'}, name = 'web_projeto_3_clone'),
    url( r'^update/(?P<pk>\d+)$', (UpdateView_projeto_3.as_view( model=models.projeto_3, success_url = reverse_lazy('fb_app_projeto_3_list'))),
        {'acao': 'Editar', 'media_saida': 'web',
         'reverso_detail': 'web_projeto_3_detail'}, name = 'web_projeto_3_update'),
    url( r'^delete/(?P<pk>\d+)$', (DeleteView_projeto_3.as_view( model=models.projeto_3, success_url = reverse_lazy('web_projeto_3_list'))),
        {'media_saida': 'web'}, name = 'web_projeto_3_delete'),
    url( r'^list$', (ListView_projeto_3.as_view( model=models.projeto_3, paginate_by = 10 )),
        {'media_saida': 'web',
         'reverso_detail': 'web_projeto_3_detail',
         'reverso_create': 'web_projeto_3_create'}, name = 'web_projeto_3_list'),
    url( r'^(?P<pk>\d+)$', (DetailView_projeto_3.as_view( model=models.projeto_3 )),
        {'media_saida': 'web',
         'reverso_clone': 'web_projeto_3_clone',
         'reverso_update': 'web_projeto_3_update',
         'reverso_delete': 'web_projeto_3_delete',
         'reverso_list': 'web_projeto_3_list'}, name = 'web_projeto_3_detail'),
    # Se digitar o raiz de update, sem chamar objeto, cai na pagina de listagem
    url( r'^update/$', (ListView_projeto_3.as_view( model=models.projeto_3, paginate_by = 10 )),
        {'media_saida': 'web',
         'reverso_detail': 'web_projeto_3_detail',
         'reverso_create': 'web_projeto_3_create'}, name = 'web_projeto_3_update'),
    # Se digitar o raiz de delete, sem chamar objeto, cai na pagina de listagem
    url( r'^delete/$', (ListView_projeto_3.as_view( model=models.projeto_3, paginate_by = 10 )),
        {'media_saida': 'web',
         'reverso_detail': 'web_projeto_3_detail',
         'reverso_create': 'web_projeto_3_create'}, name = 'web_projeto_3_delete'),
    # Se digitar o raiz da app, cai na pagina de cadastro
    #url( r'^$', CreateView_projeto_3.as_view( model=models.projeto_3),
    #    {'acao': 'Cadastrar'}, name = 'projeto_3_create'),
    #                       
    ## Conjunto de URLS para a aplicacao facebook app
    #
    # Se digitar o raiz da app, cai na pagina de instrucoes
    url(r'^fb_app$', RedirectView.as_view(url='flat/fb_app/instrucoes/'), name = 'fb_app_instrucoes'),
    url( r'^fb_app/add$', (CreateView_projeto_3.as_view( model=models.projeto_3)),
        {'acao': 'Cadastrar', 'media_saida': 'fb_app'}, name = 'fb_app_projeto_3_create'),
    url( r'^fb_app/update/(?P<pk>\d+)$', (UpdateView_projeto_3.as_view( model=models.projeto_3, success_url = reverse_lazy('fb_app_projeto_3_list'))),
        {'acao': 'Editar', 'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_projeto_3_detail'}, name = 'fb_app_projeto_3_update'),
    url( r'^fb_app/delete/(?P<pk>\d+)$', (DeleteView_projeto_3.as_view( model=models.projeto_3, success_url = reverse_lazy('fb_app_projeto_3_list'))),
        {'media_saida': 'fb_app'}, name = 'fb_app_projeto_3_delete'),
    url( r'^fb_app/list$', (ListView_projeto_3.as_view( model=models.projeto_3, paginate_by = 10 )),
        {'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_projeto_3_detail',
         'reverso_create': 'fb_app_projeto_3_create'}, name = 'fb_app_projeto_3_list'),
    url( r'^fb_app/(?P<pk>\d+)$', (DetailView_projeto_3.as_view( model=models.projeto_3 )),
        {'media_saida': 'fb_app',
         'reverso_update': 'fb_app_projeto_3_update',
         'reverso_delete': 'fb_app_projeto_3_delete',
         'reverso_list': 'fb_app_projeto_3_list'}, name = 'fb_app_projeto_3_detail'),
    # Se digitar o raiz de update, sem chamar objeto, cai na pagina de listagem
    url( r'^fb_app/update/$', (ListView_projeto_3.as_view( model=models.projeto_3, paginate_by = 10 )),
        {'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_projeto_3_detail',
         'reverso_create': 'fb_app_projeto_3_create'}, name = 'fb_app_projeto_3_update'),
    # Se digitar o raiz de delete, sem chamar objeto, cai na pagina de listagem
    url( r'^fb_app/delete/$', (ListView_projeto_3.as_view( model=models.projeto_3, paginate_by = 10 )),
        {'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_projeto_3_detail',
         'reverso_create': 'fb_app_projeto_3_create'}, name = 'fb_app_projeto_3_delete'),
)

