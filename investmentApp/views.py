from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader

# Create your views here.
from django.views.generic import ListView

from .forms import TunnelForm
from .models import Tunnel


class TunnelList(ListView):
    model = Tunnel

    def get_queryset(self, *args, **kwargs):
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
