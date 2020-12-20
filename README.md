# Django_Shopify

### Steps to run this project:
- `virtualenv env`
- Activate environment:
    - Windows (cmd): `%CD%/env/scripts/activate.bat`
    - Linux: `source env/bin/activate`
- `pip install -r requirements.txt`
- Add keys.py file with following data in root dir (same level as requirements.txt):
    - API_KEY = 'api_key'
    - API_PASS = 'api_password'
- Start the Django dev server: `python manage.py runserver`
- Browse urls:
    - http://localhost:8000/customers/
    - http://localhost:8000/orders/
