import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SGSF.settings')

django_app = get_wsgi_application()

# Le decimos a WhiteNoise que busque en 'staticfiles' (la carpeta que creará Vercel)
application = WhiteNoise(django_app, root=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles'))

app = application