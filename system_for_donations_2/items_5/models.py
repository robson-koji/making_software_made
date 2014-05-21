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




class items_5(BSCTModelMixin, Model_GetRelatedObject_Mixin, models.Model):
    created_by = models.ForeignKey(User,  related_name='items_5_created_by_set', verbose_name=u'Criado por', editable=False)

    def set_cloned_title(self, title):
        self.item_name = title

    def __unicode__( self ):
        return '%s' % ( self.item_name )
    item_name = models.CharField(max_length=100, verbose_name=u'Item name', help_text=u'')
    description = models.TextField(max_length=5000, verbose_name=u'Description', help_text=u'')
        #http://stackoverflow.com/questions/5776333/django-choices-for-models
        # there can be only one selection
    CHOICES_state_of_the_item = (    
        ('novo', 'Novo'),
        ('seminovo', 'Seminovo'),
        ('torto', 'Torto'),
        ('desconhecido', 'Desconhecido'),
        ('usado', 'Usado'),
    )

    def set_cloned_title(self, title):
        self.state_of_the_item = title

    def __unicode__( self ):
        return '%s' % ( self.state_of_the_item )
    state_of_the_item = models.CharField(max_length=50, choices=CHOICES_state_of_the_item, verbose_name=u'State of the item', help_text=u'')

    def set_cloned_title(self, title):
        self.item_image_upload = title

    def __unicode__( self ):
        return '%s' % ( self.item_image_upload )
    item_image_upload = models.ImageField(upload_to='items_5' ,null=True, blank=True , verbose_name=u'Item image upload', help_text=u'')

    def get_absolute_url(self):
        return reverse('items_5_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Items"
        verbose_name_plural = "Items"
        permissions = (
            ('view_items_5', 'View Items'),
            ('list_items_5', 'List Items'),
        )

    def meta(self):
        return self._meta
    # Esse metodo eh chamado nos templates detail.html e list.html

    def get_fields(self):
        # Definir os campos que nao serao mostrados no DetailView
        # Deve ser o atributo name, do field do model
        exclui_campo_da_view = ("")
        list_of_tuples = []
        for field in items_5._meta.fields:
            if not field.name in exclui_campo_da_view:
                # Esse nao consegue retornar o valor de FK
                #list_of_tuples.append((field.verbose_name, field.value_to_string(self)))
                list_of_tuples.append((field.verbose_name, getattr(self, field.name)))
        # Captura os valores dos campos relacionados m2m.
        #http://stackoverflow.com/questions/8474013/loop-in-manytomany-fields-in-django-model
        for field in items_5._meta.many_to_many:
                if not field.name in exclui_campo_da_view:
                    m2m_field = getattr(self, field.name)   
                    concatenados = ', '.join([str(i) for i in m2m_field.all()])
                    list_of_tuples.append((field.verbose_name, concatenados))
        return list_of_tuples   

    def __unicode__( self ):
        return '%s' % ( self.item_name )
