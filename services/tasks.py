from django_cron import CronJobBase, Schedule
from main.models import Currency
import feedparser

class UpdateCurrencyRates(CronJobBase):
    schedule = Schedule(run_every=3600)  # 1 hour

    def do(self):
        rss_url = "http://www.nationalbank.kz/rss/rates_all.xml"
        feed = feedparser.parse(rss_url)

        for entry in feed.entries:
            currency_name = entry.title
            currency_rate = float(entry.description)
            Currency.objects.update_or_create(
                name=currency_name, defaults={'rate': currency_rate})
