from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'fish': {
        'форель, шт.': 1,
        'соль, по вкусу': 0.2,
        'щепа ольхи, жменька': 0.05,
    },

}


def omlet(request):
    count = int(request.GET.get("servings", 1))
    result = servings(count, "omlet")
    context = {
        'dish': result,
    }
    return render(request, 'recipes.html', context)


def pasta(request):
    count = int(request.GET.get("servings", 1))
    result = servings(count, "pasta")
    context = {
        'dish': result,
    }
    return render(request, 'recipes.html', context)


def buter(request):
    count = int(request.GET.get("servings", 1))
    result = servings(count, "buter")
    context = {
        'dish': result,
    }
    return render(request, 'recipes.html', context)


def fish(request):
    count = int(request.GET.get("servings", 1))
    result = servings(count, "fish")
    context = {
        'dish': result,
    }
    return render(request, 'recipes.html', context)


def index(request):
    return HttpResponse('hello cooker')


def servings(count, name):
    if count != 1:
        buf = DATA[name].copy()
        for k, v in buf.items():
            buf[k] = v * count
        rez = buf
    else:
        rez = DATA[name]
    return rez

# перезапуск сервера  ^C%
# python manage.py runserver

