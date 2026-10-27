"""
WSGI config for SGSF project.
"""

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise  # <-- Importamos WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SGSF.settings')

application = get_wsgi_application()

# Envolvemos la aplicación con WhiteNoise.
# Le decimos que busque los estáticos en la carpeta 'staticfiles'
application = WhiteNoise(application, root=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles'))

# Vercel necesita esta variable
app = application