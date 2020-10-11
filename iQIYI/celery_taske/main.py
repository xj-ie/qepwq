import os,sys
from celery import Celery
# path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# sys.path.append(path)

# os.environ.setdefault("conf", r"C:\Users\ie\Desktop\qepwq\iQIYI\celery_taske\conf.py")
# paths = os.path.dirname(os.path.abspath(__file__))
# os.environ.setdefault("conf", os.path.join(paths, "conf.py"))
class COFING_LOGIN:
    broker_url = "redis://127.0.0.1/14"

celery_app = Celery("meiduo")

# celery_app.config_from_object("celery_taske.conf")
# celery_app.config_from_envvar("conf")
celery_app.config_from_object(COFING_LOGIN)
celery_app.autodiscover_tasks(["celery_taske.email"])
