# -*- coding: utf-8 -*-
from django.db.models.loading import get_model
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.urlresolvers import resolve
from guardian.mixins import PermissionRequiredMixin
from guardian.shortcuts import assign_perm
from django.views import generic
from bsct.views import *
from myMixins.mixins import ChkObjOwnershipMixin
from items_5.models import items_5
# Initializing variables
# Define controle de acesso para o DetailView e ListView.
# Todos objetos que nao pertencerem ao usuario ADMIN ou STAFF, sao controlados.
# DetailView e ListView do ADMIN e STAFF sao publicos. Para nao mostrar, cortar url e deixar so na interface admin.
# The order of this filters are important, since variables change according to the current status being checked.
#import logging
#logger = logging.getLogger("mylog")




class CreateView_items_5( CreateView ):
    return_403 = True    

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        textos = {}
        textos['app_desc'] = ''
        textos['subtitulo'] = 'Itens que serão doados'
        context.update({
            'textos': textos
        })
        # Configura o template de acordo com a interface que usa o sistema
        media_saida = self.kwargs['media_saida']
        self.template_name = 'bsct/plain/'+media_saida+'_form.html'
        return context
    group_field = ''
    user_field = ''

    def form_valid(self, form):
        self.user_field = self.request.user
        return super(CreateView_items_5, self).form_valid(form)   
    # Se gravou com sucesso, chama a pag de detalhe do objeto de acordo com a interface que usa o sistema

    def get_success_url(self):
        media_saida = self.kwargs['media_saida']
        reverso = media_saida+'_items_5_detail'
        return reverse(reverso, kwargs={'pk': (self.object.id)})            




class UpdateView_items_5(  ChkObjOwnershipMixin,  UpdateView ):
    return_403 = True        
    # Se tem grupo com permissao concedida eh porque a permissao eh requerida.
    # Enato aqui requere a permissao, com base no que foi configurado no create_project.pl
    permission_required = 'items_5.change_items_5'
    user_field = ''
    group_field = ''

    def form_valid(self, form):
        self.user_field = self.request.user
        return super(UpdateView_items_5, self).form_valid(form)    

    def get_success_url(self):
        from django.db import connection, transaction
        cursor = connection.cursor()
        # Senao, apenas altera o fk do grupo no elemento em questao.
        # Nao tah reconhecendo o content_type. Acertar.
        content_type_id = cursor.execute("SELECT id FROM django_content_type WHERE model = 'items_5'" )
        #cursor.execute("UPDATE guardian_userobjectpermission SET user_id = %s WHERE object_pk = %s AND content_type_id = %s" , [self.user_field.id, self.kwargs['pk'], content_type_id])
        cursor.execute("UPDATE guardian_userobjectpermission SET user_id = %s WHERE object_pk = %s " , [self.user_field.id, self.kwargs['pk']])
        transaction.commit_unless_managed()
        media_saida = self.kwargs['media_saida']
        reverso = media_saida+'_items_5_detail'
        return reverse(reverso, kwargs={'pk': (self.object.id)})           




class ListView_items_5(  ListView ):
    return_403 = True    

    def get_context_data(self, **kwargs):
        media_saida = self.kwargs['media_saida']
        self.template_name = 'bsct/plain/'+media_saida+'_list.html'
        object_list = self.model.objects.filter(  )
        reverso_detail = self.kwargs['reverso_detail']
        reverso_create = self.kwargs['reverso_create']
        context = super(ListView_items_5, self).get_context_data(**kwargs)
        context.update({
            'reverso_detail': reverso_detail, 'reverso_create': reverso_create, 'object_list': object_list
        })
        return context




class DetailView_items_5(    DetailView ):
    return_403 = True        




class DeleteView_items_5(  ChkObjOwnershipMixin,  DeleteView ):
    return_403 = True
    # Se tem grupo com permissao concedida eh porque a permissao eh requerida.
    # Enato aqui requere a permissao, com base no que foi configurado no create_project.pl
    permission_required = 'items_5.delete_items_5'

