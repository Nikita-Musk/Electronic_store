from django.contrib import admin

from store.models import Network, Product


@admin.action(description="Удаление задолженности перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    for network in queryset:
        network.debt = 0.00
        network.save()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "model",
        "supplier",
        "launch_date",
    )
    search_fields = ("name",)
    ordering = ("-launch_date",)
    list_display_links = ("supplier",)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "country",
        "city",
        "level",
        "supplier",
        "debt",
        "created_at",
    )
    actions = [clear_debt]
    list_filter = ("city",)
    search_fields = ("name",)
    ordering = ("-created_at",)
    list_display_links = ("supplier",)
