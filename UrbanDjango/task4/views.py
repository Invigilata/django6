from django.shortcuts import render

# Главная страница
def platform(request):
    return render(request, 'fourth_task/platform.html')

# Страница "Магазин"
def games(request):
    games_list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2']
    return render(request, 'fourth_task/games.html', {'games': games_list})

# Страница "Корзина"
def cart(request):
    return render(request, 'fourth_task/cart.html')
