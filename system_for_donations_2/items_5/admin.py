from django.contrib import admin
from items_5.models import items_5




class items_5_Admin(admin.ModelAdmin):
    list_display = ["id", "created_by", "item_name", "get_state_of_the_item_display", ]

    def get_actions(self, request):
        actions = super(items_5_Admin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()
admin.site.register(items_5, items_5_Admin)

