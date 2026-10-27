import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SGSF.settings')

django_app = get_wsgi_application()

# Apuntamos a la carpeta 'static' original, no a 'staticfiles'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
application = WhiteNoise(django_app, root=os.path.join(BASE_DIR, 'static'))

app = application