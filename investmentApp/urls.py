from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import TunnelList

urlpatterns = [
    path('', login_required(TunnelList.as_view())),
    path('update-tunnel/<int:tunnel_id>', views.update_tunnel),
    path('delete-tunnel/<int:tunnel_id>', views.delete_tunnel),
    path('show-cotation/<int:tunnel_id>', views.show_cotation)
]
