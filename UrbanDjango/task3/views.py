from django.shortcuts import render

# Главная страница
def platform(request):
    return render(request, 'third_task/platform.html')

# Страница "Магазин"
def games(request):
    games_list = {
        'Atomic Heart': 'купить',
        'Cyberpunk 2077': 'купить',
        'PayDay2': 'купить'
    }
    return render(request, 'third_task/games.html', {'games': games_list})

# Страница "Корзина"
def cart(request):
    return render(request, 'third_task/cart.html')
