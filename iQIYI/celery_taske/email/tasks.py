import sys,os
sys.path.append(os.pardir)

from celery_taske.main import celery_app
from celery_taske.email.send_email import send_email




@celery_app.task(name='send_verify_email')
def send_verify_email(to_email, verify_url):
    try:
        send_email(to_email, verify_url)
        return 1
    except Exception as e:
        return 0
