from datetime import datetime, timezone
from apscheduler.schedulers.background import BackgroundScheduler
from .schedule import scheduled_crawl

def start():
    # automated and scheduled crawling
    scheduler = BackgroundScheduler(timezone='UTC')
    # setting default time interval = 5 mins
    scheduler.add_job(scheduled_crawl, 'interval', minutes=10)
    scheduler.start()
