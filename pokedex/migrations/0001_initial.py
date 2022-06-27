# Generated by Django 4.0.5 on 2022-06-27 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('names', models.CharField(max_length=100, unique=True)),
                ('height', models.IntegerField(null=True)),
                ('weight', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Pokemon',
                'verbose_name_plural': 'Pokemons',
            },
        ),
        migrations.CreateModel(
            name='PokemonTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'PokemonType',
                'verbose_name_plural': 'PokemonTypes',
            },
        ),
        migrations.CreateModel(
            name='PokemonStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('effort', models.IntegerField()),
                ('base_stat', models.IntegerField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='pokedex.pokemon')),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='types', to='pokedex.pokemontypes'),
        ),
    ]
