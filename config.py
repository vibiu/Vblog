import os
BASE_PATH = os.path.dirname(os.path.abspath(__name__))

config = {
    'debug': True,
    'cookie_secret': 'tornado_app_secrete',
    'template_path': os.path.join(BASE_PATH, 'app/templates'),
    'static_path': os.path.join(BASE_PATH, 'app/static')
}
