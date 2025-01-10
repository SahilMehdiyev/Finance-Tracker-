from django.contrib import admin
from .models import Transaction,Category


admin.site.register(Transaction)
admin.site.register(Category)


class MyModelAdmin(admin.ModelAdmin):
    # ...
    fieldsets = [
        ("Section title", {
            "classes": ("collapse", "expanded"),
            "fields": (...),
        }),
    ]
    # ...