from django.shortcuts import render

from django.shortcuts import redirect

from superheroes_site.models import Superhero

from django.http import HttpResponse

from superheroes_site.forms import CrudHeroesForm

from superheroes_site.utils import *

def index(request):

    superheroes = Superhero.objects.all()

    return render(
        request,
        'index.html',
        {
            "superheroes": superheroes,
            "range": range(1, 5)
        }
    )


def filterhero(request, text):
    superheroes = Superhero.objects.filter(name=text)

    return render(
        request,
        'index.html',
        {
            "superheroes": superheroes,
            "range": range(1, 5)
        }
    )


def favoritos(request):
    superheroes = Superhero.objects.filter(isFavorite=True)

    return render(request, 'favoritos.html',
        {
            "superheroes": superheroes
        })


def savehero(request):
    if request.method == 'POST':
        form = CrudHeroesForm(request.POST)

        if form.is_valid():
            dados_form = form.data

            hero = Superhero(
                name=dados_form['name'], 
                description=dados_form['description'],
                picture=stringToBase64(dados_form['picture'].replace('data:image/jpeg;base64,', '')))

            print(dados_form['picture'].replace('data:image/jpeg;base64,', ''))
            hero.save()

            return redirect('index')
        else:
            return HttpResponse('ERROR')
