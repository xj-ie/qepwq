from celery_taske.main import celery_app


@celery_app.task(name='send_verify_email')
def send_verify_email(to_email, verify_url):
    pass