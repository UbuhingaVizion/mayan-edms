from django.contrib import admin

from .models import DocumentCheckout


@admin.register(DocumentCheckout)
class DocumentCheckoutAdmin(admin.ModelAdmin):
    list_display = (
        'document', 'checkout_datetime', 'expiration_datetime', 'user',
        'block_new_file'
    )
    list_display_links = None
