from django.contrib import admin
from projeto_3.models import projeto_3




class projeto_3_Admin(admin.ModelAdmin):
    list_display = ["id", "created_by", "titulo", "itens_4_m2m_reverso", ]

    def get_actions(self, request):
        actions = super(projeto_3_Admin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()
admin.site.register(projeto_3, projeto_3_Admin)

