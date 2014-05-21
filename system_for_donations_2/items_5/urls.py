
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from items_5 import models
from bsct import views
#CloneView_items_5,
from items_5.views import CreateView_items_5, UpdateView_items_5, \
                                    ListView_items_5, DetailView_items_5, DeleteView_items_5
from system_for_donations_2.decorators import superuser_only, staff_only
urlpatterns = patterns('',
    #                       
    ## Conjunto de URLS para a aplicacao web default
    #
    # Se digitar o raiz da app, cai na pagina de instrucoes
    url(r'^$', RedirectView.as_view(url='flat/instrucoes/')), 
    url( r'^add$', (CreateView_items_5.as_view( model=models.items_5)),
        {'acao': 'Cadastrar', 'media_saida': 'web'}, name = 'web_items_5_create'),
    url( r'^update/(?P<pk>\d+)$', (UpdateView_items_5.as_view( model=models.items_5, success_url = reverse_lazy('fb_app_items_5_list'))),
        {'acao': 'Editar', 'media_saida': 'web',
         'reverso_detail': 'web_items_5_detail'}, name = 'web_items_5_update'),
    url( r'^delete/(?P<pk>\d+)$', (DeleteView_items_5.as_view( model=models.items_5, success_url = reverse_lazy('web_items_5_list'))),
        {'media_saida': 'web'}, name = 'web_items_5_delete'),
    url( r'^list$', (ListView_items_5.as_view( model=models.items_5, paginate_by = 10 )),
        {'media_saida': 'web',
         'reverso_detail': 'web_items_5_detail',
         'reverso_create': 'web_items_5_create'}, name = 'web_items_5_list'),
    url( r'^(?P<pk>\d+)$', (DetailView_items_5.as_view( model=models.items_5 )),
        {'media_saida': 'web',
         'reverso_update': 'web_items_5_update',
         'reverso_delete': 'web_items_5_delete',
         'reverso_list': 'web_items_5_list'}, name = 'web_items_5_detail'),
    # Se digitar o raiz de update, sem chamar objeto, cai na pagina de listagem
    url( r'^update/$', (ListView_items_5.as_view( model=models.items_5, paginate_by = 10 )),
        {'media_saida': 'web',
         'reverso_detail': 'web_items_5_detail',
         'reverso_create': 'web_items_5_create'}, name = 'web_items_5_update'),
    # Se digitar o raiz de delete, sem chamar objeto, cai na pagina de listagem
    url( r'^delete/$', (ListView_items_5.as_view( model=models.items_5, paginate_by = 10 )),
        {'media_saida': 'web',
         'reverso_detail': 'web_items_5_detail',
         'reverso_create': 'web_items_5_create'}, name = 'web_items_5_delete'),
    # Se digitar o raiz da app, cai na pagina de cadastro
    #url( r'^$', CreateView_items_5.as_view( model=models.items_5),
    #    {'acao': 'Cadastrar'}, name = 'items_5_create'),
    #                       
    ## Conjunto de URLS para a aplicacao facebook app
    #
    # Se digitar o raiz da app, cai na pagina de instrucoes
    url(r'^fb_app$', RedirectView.as_view(url='flat/fb_app/instrucoes/'), name = 'fb_app_instrucoes'),
    url( r'^fb_app/add$', (CreateView_items_5.as_view( model=models.items_5)),
        {'acao': 'Cadastrar', 'media_saida': 'fb_app'}, name = 'fb_app_items_5_create'),
    url( r'^fb_app/update/(?P<pk>\d+)$', (UpdateView_items_5.as_view( model=models.items_5, success_url = reverse_lazy('fb_app_items_5_list'))),
        {'acao': 'Editar', 'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_items_5_detail'}, name = 'fb_app_items_5_update'),
    url( r'^fb_app/delete/(?P<pk>\d+)$', (DeleteView_items_5.as_view( model=models.items_5, success_url = reverse_lazy('fb_app_items_5_list'))),
        {'media_saida': 'fb_app'}, name = 'fb_app_items_5_delete'),
    url( r'^fb_app/list$', (ListView_items_5.as_view( model=models.items_5, paginate_by = 10 )),
        {'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_items_5_detail',
         'reverso_create': 'fb_app_items_5_create'}, name = 'fb_app_items_5_list'),
    url( r'^fb_app/(?P<pk>\d+)$', (DetailView_items_5.as_view( model=models.items_5 )),
        {'media_saida': 'fb_app',
         'reverso_update': 'fb_app_items_5_update',
         'reverso_delete': 'fb_app_items_5_delete',
         'reverso_list': 'fb_app_items_5_list'}, name = 'fb_app_items_5_detail'),
    # Se digitar o raiz de update, sem chamar objeto, cai na pagina de listagem
    url( r'^fb_app/update/$', (ListView_items_5.as_view( model=models.items_5, paginate_by = 10 )),
        {'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_items_5_detail',
         'reverso_create': 'fb_app_items_5_create'}, name = 'fb_app_items_5_update'),
    # Se digitar o raiz de delete, sem chamar objeto, cai na pagina de listagem
    url( r'^fb_app/delete/$', (ListView_items_5.as_view( model=models.items_5, paginate_by = 10 )),
        {'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_items_5_detail',
         'reverso_create': 'fb_app_items_5_create'}, name = 'fb_app_items_5_delete'),
)

