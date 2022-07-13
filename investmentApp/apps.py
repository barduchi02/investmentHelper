from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig


def fetch_prices():
    # Buscar por cotações aqui, segundo o configurado no BD
    print('Buscando')


class InvestmentappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'investmentApp'
    hg_brasil_access_key = 'f2f1f066'

    # noinspection PyBroadException
    def ready(self):
        print('--------INIT-------')
        scheduler = BackgroundScheduler()
        scheduler.add_job(fetch_prices, 'interval', seconds=60)
        scheduler.start()
