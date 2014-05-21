
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from donations_6 import models
from bsct import views
#CloneView_donations_6,
from donations_6.views import CreateView_donations_6, UpdateView_donations_6, \
                                    ListView_donations_6, DetailView_donations_6, DeleteView_donations_6
from system_for_donations_2.decorators import superuser_only, staff_only
urlpatterns = patterns('',
    #                       
    ## Conjunto de URLS para a aplicacao web default
    #
    # Se digitar o raiz da app, cai na pagina de instrucoes
    url(r'^$', RedirectView.as_view(url='flat/instrucoes/')), 
    url( r'^add$', (CreateView_donations_6.as_view( model=models.donations_6)),
        {'acao': 'Cadastrar', 'media_saida': 'web'}, name = 'web_donations_6_create'),
    url( r'^update/(?P<pk>\d+)$', (UpdateView_donations_6.as_view( model=models.donations_6, success_url = reverse_lazy('fb_app_donations_6_list'))),
        {'acao': 'Editar', 'media_saida': 'web',
         'reverso_detail': 'web_donations_6_detail'}, name = 'web_donations_6_update'),
    url( r'^delete/(?P<pk>\d+)$', (DeleteView_donations_6.as_view( model=models.donations_6, success_url = reverse_lazy('web_donations_6_list'))),
        {'media_saida': 'web'}, name = 'web_donations_6_delete'),
    url( r'^list$', (ListView_donations_6.as_view( model=models.donations_6, paginate_by = 10 )),
        {'media_saida': 'web',
         'reverso_detail': 'web_donations_6_detail',
         'reverso_create': 'web_donations_6_create'}, name = 'web_donations_6_list'),
    url( r'^(?P<pk>\d+)$', (DetailView_donations_6.as_view( model=models.donations_6 )),
        {'media_saida': 'web',
         'reverso_update': 'web_donations_6_update',
         'reverso_delete': 'web_donations_6_delete',
         'reverso_list': 'web_donations_6_list'}, name = 'web_donations_6_detail'),
    # Se digitar o raiz de update, sem chamar objeto, cai na pagina de listagem
    url( r'^update/$', (ListView_donations_6.as_view( model=models.donations_6, paginate_by = 10 )),
        {'media_saida': 'web',
         'reverso_detail': 'web_donations_6_detail',
         'reverso_create': 'web_donations_6_create'}, name = 'web_donations_6_update'),
    # Se digitar o raiz de delete, sem chamar objeto, cai na pagina de listagem
    url( r'^delete/$', (ListView_donations_6.as_view( model=models.donations_6, paginate_by = 10 )),
        {'media_saida': 'web',
         'reverso_detail': 'web_donations_6_detail',
         'reverso_create': 'web_donations_6_create'}, name = 'web_donations_6_delete'),
    # Se digitar o raiz da app, cai na pagina de cadastro
    #url( r'^$', CreateView_donations_6.as_view( model=models.donations_6),
    #    {'acao': 'Cadastrar'}, name = 'donations_6_create'),
    #                       
    ## Conjunto de URLS para a aplicacao facebook app
    #
    # Se digitar o raiz da app, cai na pagina de instrucoes
    url(r'^fb_app$', RedirectView.as_view(url='flat/fb_app/instrucoes/'), name = 'fb_app_instrucoes'),
    url( r'^fb_app/add$', (CreateView_donations_6.as_view( model=models.donations_6)),
        {'acao': 'Cadastrar', 'media_saida': 'fb_app'}, name = 'fb_app_donations_6_create'),
    url( r'^fb_app/update/(?P<pk>\d+)$', (UpdateView_donations_6.as_view( model=models.donations_6, success_url = reverse_lazy('fb_app_donations_6_list'))),
        {'acao': 'Editar', 'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_donations_6_detail'}, name = 'fb_app_donations_6_update'),
    url( r'^fb_app/delete/(?P<pk>\d+)$', (DeleteView_donations_6.as_view( model=models.donations_6, success_url = reverse_lazy('fb_app_donations_6_list'))),
        {'media_saida': 'fb_app'}, name = 'fb_app_donations_6_delete'),
    url( r'^fb_app/list$', (ListView_donations_6.as_view( model=models.donations_6, paginate_by = 10 )),
        {'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_donations_6_detail',
         'reverso_create': 'fb_app_donations_6_create'}, name = 'fb_app_donations_6_list'),
    url( r'^fb_app/(?P<pk>\d+)$', (DetailView_donations_6.as_view( model=models.donations_6 )),
        {'media_saida': 'fb_app',
         'reverso_update': 'fb_app_donations_6_update',
         'reverso_delete': 'fb_app_donations_6_delete',
         'reverso_list': 'fb_app_donations_6_list'}, name = 'fb_app_donations_6_detail'),
    # Se digitar o raiz de update, sem chamar objeto, cai na pagina de listagem
    url( r'^fb_app/update/$', (ListView_donations_6.as_view( model=models.donations_6, paginate_by = 10 )),
        {'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_donations_6_detail',
         'reverso_create': 'fb_app_donations_6_create'}, name = 'fb_app_donations_6_update'),
    # Se digitar o raiz de delete, sem chamar objeto, cai na pagina de listagem
    url( r'^fb_app/delete/$', (ListView_donations_6.as_view( model=models.donations_6, paginate_by = 10 )),
        {'media_saida': 'fb_app',
         'reverso_detail': 'fb_app_donations_6_detail',
         'reverso_create': 'fb_app_donations_6_create'}, name = 'fb_app_donations_6_delete'),
)

