import datetime
import json
from urllib.request import urlopen

from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig


class InvestmentappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'investmentApp'
    hg_brasil_url = 'https://api.hgbrasil.com/finance'
    hg_brasil_access_key = 'f2f1f066'

    # noinspection PyBroadException
    def ready(self):
        print('--------INIT-------')
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.fetch_prices, 'interval', seconds=60)
        scheduler.start()

    def fetch_prices(self):
        # Buscar por cotações aqui, segundo o configurado no BD
        print('Buscando')

        from .models import Tunnel, Cotation
        tunnel_buffer = Tunnel.objects.raw(
            'SELECT i.* FROM "investmentApp_tunnel" i '
            'LEFT JOIN "investmentApp_cotation" c ON i.cotationid_id = c.id '
            'WHERE i.cotationid_id IS NULL OR (i.period + c.date) <= now() '
        )

        fetch_url_generic = self.hg_brasil_url + '/stock_price?key=' + self.hg_brasil_access_key + '&symbol='

        for tunnel in tunnel_buffer:
            fetch_url = fetch_url_generic + tunnel.assetid.code
            response = urlopen(fetch_url)
            data_json = json.loads(response.read())
            cotation_json = data_json['results'][tunnel.assetid.code]
            tz = datetime.timezone(datetime.timedelta(hours=cotation_json['market_time']['timezone']))
            updated_at_split = cotation_json['updated_at'].split()
            updated_at = datetime.datetime.combine(datetime.datetime.strptime(updated_at_split[0], '%Y-%m-%d').date(),
                                                   datetime.datetime.strptime(updated_at_split[1], '%H:%M:%S').time(),
                                                   tzinfo=tz)

            if tunnel.cotationid is not None and tunnel.cotationid.updated_at == updated_at:
                tunnel.cotationid.date = datetime.datetime.now(tz=tz)
                tunnel.cotationid.save()
            else:
                cotation = Cotation(assetid=tunnel.assetid, date=datetime.datetime.now(tz=tz),
                                    price=cotation_json['price'], currency=cotation_json['currency'],
                                    change_percent=cotation_json['change_percent'], updated_at=updated_at)
                cotation.save()
                tunnel.cotationid = cotation
                tunnel.save()
