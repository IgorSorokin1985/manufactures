from django.contrib import admin
from producers.models import Producer


class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'email', 'country', 'city', 'debt', 'date')
    list_filter = ('city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = "Clear debt for selected producers"

    def get_provider_link(self, obj):
        if obj.provider:
            return f'<a href="/admin/producers/producer/{obj.provider.id}/change/">Link to Provider</a>'
        else:
            return None

    get_provider_link.allow_tags = True
    get_provider_link.short_description = 'Provider Link'


admin.site.register(Producer, ProducerAdmin)
