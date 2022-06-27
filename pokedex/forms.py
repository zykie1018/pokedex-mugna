from django import forms
from pokedex.models import Pokemon


class PokemonListForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ["id", "names"]


class PokemonDetailForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"


class PokemonCreateForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"


class PokemonUpdateForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"


class PokemonDeleteForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"


class PokemonSearchForm(forms.Form):
    name = forms.CharField(required=False)


class PokemonSearchTypeForm(forms.Form):
    name = forms.CharField(required=False)
