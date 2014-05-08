
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from itens_4 import models
from bsct import views
from itens_4.views import CreateView_itens_4, UpdateView_itens_4, CloneView_itens_4,\
                                    ListView_itens_4, DetailView_itens_4, DeleteView_itens_4
from amontoado_3.decorators import superuser_only, staff_only
urlpatterns = patterns('',
    #                       
    ## Conjunto de URLS para a aplicacao web default
    #
    # Se digitar o raiz da app, cai na pagina de instrucoes
    url(r'^$', RedirectView.as_view(url='flat/instrucoes/')), 
    url( r'^add$', (CreateView_itens_4.as_view( model=models.itens_4)),
        {'acao': 'Cadastrar', 'media_saida': 'web'}, name = 'web_itens_4_create'),
    url( r'^clone/(?P<pk>\d+)$', (CloneView_itens_4.as_view( model=models.itens_4)),
        {'acao': 'Clonar', 'media_saida': 'web'}, name = 'web_itens_4_clone'),
    url( r'^update/(?P<pk>\d+)$', (UpdateView_itens_4.as_view( model=models.itens_4, success_url = reverse_lazy('fb_app_itens_4_list'))),
        {'acao': 'Editar', 'media_saida': 'web',
         'reverso_detail': 'web_itens_4_detail'}, name = 'web_itens_4_update'),
    url( r'^delete/(?P<pk>\d+)$', (DeleteView_itens_4.as_view( model=models.itens_4, success_url = reverse_lazy('web_itens_4_list'))),
        {'media_saida': 'web'}, name = 'web_itens_4_delete'),
    url( r'^list$', (ListView_itens_4.as_view( model=models.itens_4, paginate_by = 10 )),
        {'media_saida': 'web',
         'reverso_detail': 'web_itens_4_detail',
         'reverso_create': 'web_itens_4_create'}, name = 'web_itens_4_list'),
    url( r'^(?P<pk>\d+)$', (DetailView_itens_4.as_view( model=models.itens_4 )),
        {'media_saida': 'web',
         'reverso_clone': 'web_itens_4_clone',
         'reverso_update': 'web_itens_4_update',
         'reverso_delete': 'web_itens_4_delete',
         'reverso_list': 'web_itens_4_list'}, name = 'web_itens_4_detail'),
    # Se digitar o raiz de update, sem chamar objeto, cai na pagina de listagem
    url( r'^update/$', (ListView_itens_4.as_view( model=models.itens_4, paginate_by = 10 )),
        {'media_saida': 'web',
         'reverso_detail': 'web_itens_4_detail',
         'reverso_create': 'web_itens_4_create'}, name = 'web_itens_4_update'),
    # Se digitar o raiz de delete, sem chamar objeto, cai na pagina de listagem
    url( r'^delete/$', (ListView_itens_4.as_view( model=models.itens_4, paginate_by = 10 )),
        {'media_saida': 'web',
         'reverso_detail': 'web_itens_4_detail',
         'reverso_create': 'web_itens_4_create'}, name = 'web_itens_4_delete'),
    # Se digitar o raiz da app, cai na pagina de cadastro
    #url( r'^$', CreateView_itens_4.as_view( model=models.itens_4),
    #    {'acao': 'Cadastrar'}, name = 'itens_4_create'),
    #                       
    ## Conjunto de URLS para a aplicacao facebook app
    #
    # Se digitar o raiz da app, cai na pagina de instrucoes
    url(r'^fb_app$', RedirectView.as_view(url='flat/fb_app/instrucoes/'), name = 'fb_app_instrucoes'),
    url( r'^fb_app/add$', (CreateView_itens_4.as_view( model=models.itens_4)),
        {'acao': 'Cadastrar', 'media_saida': 'fb_app'}, name = 'fb_app_itens_4_create'),
    url( r'^fb_app/update/(?P<pk>\d+)$', (UpdateView_itens_4.as_view( model=models.itens_4, success_url = reverse_lazy('fb_app_itens_4_list'))),
        {'acao': 'Editar', 'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_itens_4_detail'}, name = 'fb_app_itens_4_update'),
    url( r'^fb_app/delete/(?P<pk>\d+)$', (DeleteView_itens_4.as_view( model=models.itens_4, success_url = reverse_lazy('fb_app_itens_4_list'))),
        {'media_saida': 'fb_app'}, name = 'fb_app_itens_4_delete'),
    url( r'^fb_app/list$', (ListView_itens_4.as_view( model=models.itens_4, paginate_by = 10 )),
        {'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_itens_4_detail',
         'reverso_create': 'fb_app_itens_4_create'}, name = 'fb_app_itens_4_list'),
    url( r'^fb_app/(?P<pk>\d+)$', (DetailView_itens_4.as_view( model=models.itens_4 )),
        {'media_saida': 'fb_app',
         'reverso_update': 'fb_app_itens_4_update',
         'reverso_delete': 'fb_app_itens_4_delete',
         'reverso_list': 'fb_app_itens_4_list'}, name = 'fb_app_itens_4_detail'),
    # Se digitar o raiz de update, sem chamar objeto, cai na pagina de listagem
    url( r'^fb_app/update/$', (ListView_itens_4.as_view( model=models.itens_4, paginate_by = 10 )),
        {'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_itens_4_detail',
         'reverso_create': 'fb_app_itens_4_create'}, name = 'fb_app_itens_4_update'),
    # Se digitar o raiz de delete, sem chamar objeto, cai na pagina de listagem
    url( r'^fb_app/delete/$', (ListView_itens_4.as_view( model=models.itens_4, paginate_by = 10 )),
        {'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_itens_4_detail',
         'reverso_create': 'fb_app_itens_4_create'}, name = 'fb_app_itens_4_delete'),
)

