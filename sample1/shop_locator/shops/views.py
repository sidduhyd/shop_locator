from django.shortcuts import render, get_object_or_404, redirect
from .models import Shop
from .forms import ShopForm

def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shops/shop_list.html', {'shops': shops})

def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'shops/shop_detail.html', {'shop': shop})

def shop_create(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            shop = form.save()
            return redirect('shop_detail', pk=shop.pk)
    else:
        form = ShopForm()
    return render(request, 'shops/shop_form.html', {'form': form})

def shop_update(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            shop = form.save()
            return redirect('shop_detail', pk=shop.pk)
    else:
        form = ShopForm(instance=shop)
    return render(request, 'shops/shop_form.html', {'form': form})
