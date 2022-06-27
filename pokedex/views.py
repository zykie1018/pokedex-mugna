import requests

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, ListView

from pokedex.models import Pokemon, PokemonStats

from pokedex.forms import (
    PokemonListForm,
    PokemonDetailForm,
    PokemonCreateForm,
    PokemonUpdateForm,
    PokemonDeleteForm,
    PokemonSearchForm,
    PokemonSearchTypeForm,
)


class ListAllPokemons(View):
    form_class = PokemonListForm
    initial = {"key": "value"}
    template_name = "pokedex/pokemon_list.html"

    def get(self, request, *args, **kwargs):
        pokemon_list = Pokemon.objects.all()
        form = self.form_class(initial=self.initial)

        return render(
            request, self.template_name, {"form": form, "pokemon_list": pokemon_list}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            # Clean data here
            form.save()
            return HttpResponseRedirect(reverse("pokedex:list-pokemons"))

        return render(request, self.template_name, {"form": form})


class PokemonDetails(View):
    form_class = PokemonDetailForm
    initial = {"key": "value"}
    template_name = "pokedex/pokemon_detail.html"

    def get(self, request, id, *args, **kwargs):
        pokemon_details = Pokemon.objects.get(id=id)
        form = self.form_class(initial=self.initial)

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "pokemon_details": pokemon_details,
            },
        )

    def post(self, request, name, *args, **kwargs):
        form = self.form_class(request.POST, instance=name)
        pokemon = Pokemon.objects.get(name=name)
        if form.is_valid():
            # Clean data here
            form.save()
            return HttpResponseRedirect(reverse("pokedex:detail-pokemons"))

        return render(request, self.template_name, {"form": form})


class PokemonCreate(View):
    form_class = PokemonCreateForm
    initial = {"key": "value"}
    template_name = "pokedex/pokemon_create.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)

        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            # Clean data here
            form.save()
            messages.success(request, "Successfully created a new Pokemon")
            return HttpResponseRedirect(reverse("pokedex:create-pokemons"))

        return render(request, self.template_name, {"form": form})


class PokemonUpdate(View):
    form_class = PokemonUpdateForm
    initial = {"key": "value"}
    template_name = "pokedex/pokemon_update.html"

    def get(self, request, id, *args, **kwargs):
        pokemon_update = Pokemon.objects.get(id=id)
        form = self.form_class(initial=self.initial, instance=pokemon_update)

        return render(
            request,
            self.template_name,
            {"form": form, "pokemon_update": pokemon_update},
        )

    def post(self, request, id, *args, **kwargs):
        pokemon_update = Pokemon.objects.get(id=id)
        form = self.form_class(request.POST, instance=pokemon_update)

        if form.is_valid():
            # Clean data here
            form.save()
            messages.success(request, "Successfully updated the Pokemon")
            return HttpResponseRedirect(reverse("pokedex:create-pokemons"))

        return render(request, self.template_name, {"form": form})


class PokemonDelete(View):
    form_class = PokemonDeleteForm
    initial = {"key": "value"}
    template_name = "pokedex/pokemon_delete.html"

    def get(self, request, id, *args, **kwargs):
        pokemon_delete = Pokemon.objects.get(id=id)
        form = self.form_class(initial=self.initial, instance=pokemon_delete)

        return render(
            request,
            self.template_name,
            {"form": form, "pokemon_delete": pokemon_delete},
        )

    def post(self, request, id, *args, **kwargs):
        pokemon_delete = Pokemon.objects.get(id=id)
        form = self.form_class(request.POST, instance=pokemon_delete)

        if form.is_valid():
            # Clean data here
            pokemon_delete.delete()
            messages.success(request, "Successfully deleted the Pokemon")
            return HttpResponseRedirect(reverse("pokedex:delete-pokemons"))

        return render(
            request,
            self.template_name,
            {"form": form},
        )


class PokemonSearch(ListView):
    form_class = PokemonSearchForm
    initial = {"key": "value"}
    template_name = "pokedex/pokemon_search.html"

    def get(self, request, *args, **kwargs):
        error = False
        if "query" in request.GET:
            query = request.GET["query"]
            if not query:
                error = True
            else:
                pokemons = Pokemon.objects.filter(names__icontains=query)
                return render(
                    request,
                    "pokedex/pokemon_search_results.html",
                    {"pokemons": pokemons, "query": query},
                )
        return render(
            request,
            self.template_name,
            {"error": error},
        )


class PokemonSearchByType(ListView):
    form_class = PokemonSearchTypeForm
    initial = {"key": "value"}
    template_name = "pokedex/pokemon_search_type.html"

    def get(self, request, *args, **kwargs):
        error = False
        if "query" in request.GET:
            query = request.GET["query"]
            if not query:
                error = True
            else:
                pokemons = Pokemon.objects.filter(type__name__icontains=query)
                return render(
                    request,
                    "pokedex/pokemon_search_type_results.html",
                    {"pokemons": pokemons, "query": query},
                )
        return render(
            request,
            self.template_name,
            {"error": error},
        )


def pokemon_names_list(request):

    return render(request, "pokedex/index.html")