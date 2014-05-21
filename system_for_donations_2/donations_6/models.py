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




class donations_6(BSCTModelMixin, Model_GetRelatedObject_Mixin, models.Model):
    created_by = models.ForeignKey(User,  related_name='donations_6_created_by_set', verbose_name=u'Criado por', editable=False)
    withdraw_place = models.TextField(max_length=5000, verbose_name=u'Withdraw place', help_text=u'')
    donation_description = models.TextField(max_length=5000, verbose_name=u'Donation description', help_text=u'')

    def get_absolute_url(self):
        return reverse('donations_6_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Donations"
        verbose_name_plural = "Donations"
        permissions = (
            ('view_donations_6', 'View Donations'),
            ('list_donations_6', 'List Donations'),
        )

    def meta(self):
        return self._meta
    # Esse metodo eh chamado nos templates detail.html e list.html

    def get_fields(self):
        # Definir os campos que nao serao mostrados no DetailView
        # Deve ser o atributo name, do field do model
        exclui_campo_da_view = ("")
        list_of_tuples = []
        for field in donations_6._meta.fields:
            if not field.name in exclui_campo_da_view:
                # Esse nao consegue retornar o valor de FK
                #list_of_tuples.append((field.verbose_name, field.value_to_string(self)))
                list_of_tuples.append((field.verbose_name, getattr(self, field.name)))
        # Captura os valores dos campos relacionados m2m.
        #http://stackoverflow.com/questions/8474013/loop-in-manytomany-fields-in-django-model
        for field in donations_6._meta.many_to_many:
                if not field.name in exclui_campo_da_view:
                    m2m_field = getattr(self, field.name)   
                    concatenados = ', '.join([str(i) for i in m2m_field.all()])
                    list_of_tuples.append((field.verbose_name, concatenados))
        return list_of_tuples   

    
