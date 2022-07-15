from datetime import datetime
import numpy as np

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from .forms import TunnelForm
from .models import Tunnel, Cotation


class TunnelList(ListView):
    model = Tunnel

    def get_queryset(self):
        qs = self.model.objects.filter(userid=self.request.user.pk)
        qs.order_by("-id")
        return qs


@login_required
def update_tunnel(request, tunnel_id):
    tunnel = None
    if tunnel_id > 0:
        tunnel = get_object_or_404(Tunnel, pk=tunnel_id)
    form = TunnelForm(instance=tunnel)

    if request.method == 'POST':
        form = TunnelForm(request.POST, request.FILES, instance=tunnel)
        if form.is_valid():
            tunnel = form.save(commit=False)
            tunnel.userid = request.user
            tunnel.date_updated = datetime.now()
            tunnel.save()
            return redirect('/investmentApp/')

    return render(request, 'investmentApp/update-tunnel.html', {'form': form, 'tunnel': tunnel})


@login_required
def delete_tunnel(request, tunnel_id):
    tunnel = get_object_or_404(Tunnel, pk=tunnel_id)
    tunnel.delete()
    return redirect('/investmentApp/')


@login_required
def show_cotation(request, tunnel_id):
    tunnel = get_object_or_404(Tunnel, pk=tunnel_id)

    cotation_qs = Cotation.objects.filter(assetid=tunnel.assetid)
    cotation_qs.order_by("-updated_at")
    cotation_list = list(cotation_qs)

    data_raw = list(map(lambda c: c.price, cotation_list))
    labels = list(map(lambda c: c.updated_at.strftime("%d/%m/%Y %H:%M:%S"), cotation_list))

    currency = ''
    min_price = list(np.full(shape=len(cotation_list), fill_value=tunnel.min_price))
    max_price = list(np.full(shape=len(cotation_list), fill_value=tunnel.max_price))
    if len(cotation_list) > 0:
        currency = cotation_list[0].currency

    return_dict = {
        'asset_code': tunnel.assetid.code,
        'asset_description': tunnel.assetid.description,
        'min_price': min_price,
        'max_price': max_price,
        'currency': currency,
        'labels': labels,
        'data_raw': data_raw
    }

    return render(request, 'investmentApp/show_cotation.html', {'data': return_dict})
