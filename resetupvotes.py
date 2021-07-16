import psycopg2
import os
import urllib.parse as urlparse
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

url = urlparse.urlparse(os.environ["DATABASE_URL"])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

con = psycopg2.connect(
    dbname=dbname, user=user, password=password, host=host, port=port
)


@sched.scheduled_job("cron", hour=3)
def reset_upvotes():
    with con:
        with con.cursor() as cur:
            cur.execute("TRUNCATE news_blog_app_upvote")


sched.start()
