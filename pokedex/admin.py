from django.contrib import admin
from pokedex.models import Pokemon, PokemonStats, PokemonTypes


class PokemonAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "names",
        "weight",
        "height",
        "type",
    ]
    list_filter = ["id", "type"]
    search_fields = ["id", "names"]


class PokemonStatsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "effort",
        "base_stat",
        "pokemon",
    ]


class PokemonTypesAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonStats, PokemonStatsAdmin)
admin.site.register(PokemonTypes, PokemonTypesAdmin)
