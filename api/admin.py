from django.contrib import admin
from .models import Artiest, Kunstwerk, OverheidsGebouw, Kamer


class KunstwerkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["titel", "locatie", "beschrijving", "artiesten"]}),
        ("Dimensies", {"fields": ["lengte", "breedte", "hoogte"]}),
    ]


admin.site.register(Artiest)
admin.site.register(Kunstwerk, KunstwerkAdmin)
admin.site.register(OverheidsGebouw)
admin.site.register(Kamer)

