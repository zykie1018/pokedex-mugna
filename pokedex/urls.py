from django.urls import path

from pokedex.views import (
    ListAllPokemons,
    PokemonDetails,
    PokemonCreate,
    PokemonSearchByType,
    PokemonUpdate,
    PokemonDelete,
    PokemonSearch,
)

from pokedex import views

app_name = "pokedex"
urlpatterns = [
    path("", views.pokemon_names_list, name="index"),
    path("list/", ListAllPokemons.as_view(), name="list-pokemons"),
    path("detail/<int:id>", PokemonDetails.as_view(), name="detail-pokemons"),
    path("pokemon/create/", PokemonCreate.as_view(), name="create-pokemons"),
    path("pokemon/update/<int:id>", PokemonUpdate.as_view(), name="update-pokemons"),
    path("pokemon/delete/<int:id>", PokemonDelete.as_view(), name="delete-pokemons"),
    path("pokemon/search/", PokemonSearch.as_view(), name="search-pokemons"),
    path(
        "pokemon/search/type",
        PokemonSearchByType.as_view(),
        name="search-pokemons-type",
    ),
]
