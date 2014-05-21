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
from donations_6.models import donations_6
# Initializing variables
# Define controle de acesso para o DetailView e ListView.
# Todos objetos que nao pertencerem ao usuario ADMIN ou STAFF, sao controlados.
# DetailView e ListView do ADMIN e STAFF sao publicos. Para nao mostrar, cortar url e deixar so na interface admin.
# The order of this filters are important, since variables change according to the current status being checked.
from items_5.models import items_5
# Se tiver permissoes setadas, zera o controle do ChkObjOwnershipMixin
#import logging
#logger = logging.getLogger("mylog")




class CreateView_donations_6( CreateView ):
    return_403 = True    
    permission_required = 'donations_6.add_donations_6'

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        textos = {}
        textos['app_desc'] = ''
        textos['subtitulo'] = ''
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
        return super(CreateView_donations_6, self).form_valid(form)   
    # Se gravou com sucesso, chama a pag de detalhe do objeto de acordo com a interface que usa o sistema

    def get_success_url(self):
        #recupera o usuario com base no campo created_by do elemento que estah sendo criado.
        #created_by_items_5 = items_5.objects.get(created_by = self.request.user)
        #usuario_items_5 = created_by_items_5.created_by
        usuario_items_5 = self.user_field
        # Assinala a permissao.        
        assign_perm("view_donations_6", usuario_items_5, self.object)
        assign_perm("change_donations_6", usuario_items_5, self.object)
        assign_perm("delete_donations_6", usuario_items_5, self.object)
        media_saida = self.kwargs['media_saida']
        reverso = media_saida+'_donations_6_detail'
        return reverse(reverso, kwargs={'pk': (self.object.id)})            




class UpdateView_donations_6( PermissionRequiredMixin,   UpdateView ):
    return_403 = True        
    permission_required = 'donations_6.change_donations_6'
    # Se permissoes estao setadas, desabilita o created_by
    # Se tem grupo com permissao concedida eh porque a permissao eh requerida.
    # Enato aqui requere a permissao, com base no que foi configurado no create_project.pl
    permission_required = 'donations_6.change_donations_6'
    user_field = ''
    group_field = ''

    def form_valid(self, form):
        self.user_field = self.request.user
        return super(UpdateView_donations_6, self).form_valid(form)    

    def get_success_url(self):
        from django.db import connection, transaction
        cursor = connection.cursor()
        # Senao, apenas altera o fk do grupo no elemento em questao.
        # Nao tah reconhecendo o content_type. Acertar.
        content_type_id = cursor.execute("SELECT id FROM django_content_type WHERE model = 'donations_6'" )
        #cursor.execute("UPDATE guardian_userobjectpermission SET user_id = %s WHERE object_pk = %s AND content_type_id = %s" , [self.user_field.id, self.kwargs['pk'], content_type_id])
        cursor.execute("UPDATE guardian_userobjectpermission SET user_id = %s WHERE object_pk = %s " , [self.user_field.id, self.kwargs['pk']])
        transaction.commit_unless_managed()
        media_saida = self.kwargs['media_saida']
        reverso = media_saida+'_donations_6_detail'
        return reverse(reverso, kwargs={'pk': (self.object.id)})           




class ListView_donations_6(  ListView ):
    return_403 = True    

    def get_context_data(self, **kwargs):
        media_saida = self.kwargs['media_saida']
        self.template_name = 'bsct/plain/'+media_saida+'_list.html'
        object_list = self.model.objects.filter(  )
        reverso_detail = self.kwargs['reverso_detail']
        reverso_create = self.kwargs['reverso_create']
        context = super(ListView_donations_6, self).get_context_data(**kwargs)
        context.update({
            'reverso_detail': reverso_detail, 'reverso_create': reverso_create, 'object_list': object_list
        })
        return context




class DetailView_donations_6(  PermissionRequiredMixin,   DetailView ):
    return_403 = True        
    permission_required = 'donations_6.view_donations_6'




class DeleteView_donations_6( PermissionRequiredMixin,   DeleteView ):
    return_403 = True
    permission_required = 'donations_6.delete_donations_6'
    # Se permissoes estao setadas, desabilita o created_by
    # Se tem grupo com permissao concedida eh porque a permissao eh requerida.
    # Enato aqui requere a permissao, com base no que foi configurado no create_project.pl
    permission_required = 'donations_6.delete_donations_6'

