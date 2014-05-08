# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from django.forms import ModelForm
from myMixins.mixins import Model_GetRelatedObject_Mixin
from django.core.validators import MinValueValidator, MaxValueValidator
# Pacotes de terceiro
from bsct.models import BSCTModelMixin
# Cria classe M2M qdo o campo eh MultipleChoiceField




class projeto_3(BSCTModelMixin, Model_GetRelatedObject_Mixin, models.Model):
    created_by = models.ForeignKey(User,  related_name='projeto_3_created_by_set', verbose_name=u'Criado por', editable=False)

    def set_cloned_title(self, title):
        self.titulo = title

    def __unicode__( self ):
        return '%s' % ( self.titulo )
    titulo = models.CharField(max_length=100, verbose_name=u'Titulo', help_text=u'')
    descricao = models.TextField(max_length=5000, verbose_name=u'Descricao', help_text=u'')
    # Precisa ficar abaixo da definicao do required, pq ele sobreescreve

    def set_cloned_title(self, title):
        self.projeto_xyz = title

    def __unicode__( self ):
        return '%s' % ( self.projeto_xyz )
    projeto_xyz = models.BooleanField(default=False , verbose_name=u'Projeto xyz?', help_text=u'')
    from itens_4.models import itens_4 # Se for User, nao precisa importar    
    itens_4_field = models.ManyToManyField(itens_4, verbose_name=u'Itens',)

    def itens_4_m2m_reverso(self):
        # Ao inves do id, precisa pegar o campo que mais convem, que eh o primeiro unicode field.
        # Eh muito foda pegar esse campo.
        # http://stackoverflow.com/questions/6611986/whats-the-difference-between-queryset-tuple-dictionary-in-django-template
        # Estah pegando o terceiro elemento (indice numero dois pq considera que o 0=id e 1=created_by e o proximo eh algum que
        # tenha unicode.
        return "\n".join([a[2] for a in self.itens_4_field.values_list()])
        #return ', '.join([a.id for a in self.itens_4_field.all()])
    itens_4_m2m_reverso.short_description = "Itens"

    def get_absolute_url(self):
        return reverse('projeto_3_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projeto"
        permissions = (
            ('view_projeto_3', 'View Projeto'),
            ('list_projeto_3', 'List Projeto'),
        )

    def meta(self):
        return self._meta
    # Esse metodo eh chamado nos templates detail.html e list.html

    def get_fields(self):
        # Definir os campos que nao serao mostrados no DetailView
        # Deve ser o atributo name, do field do model
        exclui_campo_da_view = ("")
        list_of_tuples = []
        for field in projeto_3._meta.fields:
            if not field.name in exclui_campo_da_view:
                # Esse nao consegue retornar o valor de FK
                #list_of_tuples.append((field.verbose_name, field.value_to_string(self)))
                list_of_tuples.append((field.verbose_name, getattr(self, field.name)))
        # Captura os valores dos campos relacionados m2m.
        #http://stackoverflow.com/questions/8474013/loop-in-manytomany-fields-in-django-model
        for field in projeto_3._meta.many_to_many:
                if not field.name in exclui_campo_da_view:
                    m2m_field = getattr(self, field.name)   
                    concatenados = ', '.join([str(i) for i in m2m_field.all()])
                    list_of_tuples.append((field.verbose_name, concatenados))
        return list_of_tuples   

    def __unicode__( self ):
        return '%s' % ( self.titulo )
