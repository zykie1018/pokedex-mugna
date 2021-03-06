from django.urls import path

from pokedex.views import (
    ListAllPokemons,
    PokemonDetails,
    PokemonCreate,
    PokemonHome,
    PokemonLogin,
    PokemonSearchByType,
    PokemonUpdate,
    PokemonDelete,
    PokemonSearch,
    PokemonLogin,
    PokemonRegister,
    PokemonLogout,
)

from pokedex import views

app_name = "pokedex"
urlpatterns = [
    path("", PokemonHome.as_view(), name="index"),
    path("detail/<int:id>", PokemonDetails.as_view(), name="detail-pokemons"),
    path("login/", PokemonLogin.as_view(), name="login-form"),
    path("logout/", PokemonLogout.as_view(), name="logout"),
    path("list/", ListAllPokemons.as_view(), name="list-pokemons"),
    path("pokemon/create/", PokemonCreate.as_view(), name="create-pokemons"),
    path("pokemon/update/<int:id>", PokemonUpdate.as_view(), name="update-pokemons"),
    path("pokemon/delete/<int:id>", PokemonDelete.as_view(), name="delete-pokemons"),
    path("pokemon/search/", PokemonSearch.as_view(), name="search-pokemons"),
    path(
        "pokemon/search/type",
        PokemonSearchByType.as_view(),
        name="search-pokemons-type",
    ),
    path("register/", PokemonRegister.as_view(), name="register-form"),
]
