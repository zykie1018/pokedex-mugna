from django.db import models

from django.utils.translation import gettext_lazy as _


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    names = models.CharField(max_length=100, unique=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    type = models.ForeignKey(
        "pokedex.PokemonTypes",
        related_name="types",
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = _("Pokemons")

    def __str__(self):
        return self.names


class PokemonStats(models.Model):
    name = models.CharField(max_length=100)
    effort = models.IntegerField()
    base_stat = models.IntegerField()
    pokemon = models.ForeignKey(
        "pokedex.Pokemon", related_name="stats", on_delete=models.CASCADE
    )


class PokemonTypes(models.Model):
    name = models.CharField(_("Type"), max_length=50)

    class Meta:
        verbose_name = "PokemonType"
        verbose_name_plural = _("PokemonTypes")

    def __str__(self):
        return self.name


# class EvolutionChart(models.Model):
#     name = models.CharField(max_length=50)
#     type = models.ForeignKey(
#         "pokedex.PokemonTypes",
#         related_name="types",
#         on_delete=models.CASCADE,
#         null=True,
#     )
