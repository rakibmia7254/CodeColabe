pip install -r requirements.txt

python manage.py migrate

uvicorn code_colabe.asgi:application