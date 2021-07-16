import psycopg2
import os
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


con = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB_NAME"),
    user=os.getenv("POSTGRES_DB_USER"),
    password=os.getenv("POSTGRES_DB_PASSWORD"),
    host=os.getenv("POSTGRES_DB_HOST"),
    port=os.getenv("POSTGRES_DB_PORT"),
)


@sched.scheduled_job("cron", hour=3)
def reset_upvotes():
    with con:
        with con.cursor() as cur:
            cur.execute("TRUNCATE news_blog_app_upvote")


sched.start()
