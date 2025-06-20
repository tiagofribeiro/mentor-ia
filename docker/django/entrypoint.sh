echo "Aguardando o banco de dados ficar disponível..."

RETRIES=10
until python -c "
import psycopg
import os
import time

try:
    conn = psycopg.connect(
        dbname=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASS'],
        host=os.environ['POSTGRES_HOST'],
        port=os.environ['POSTGRES_PORT']
    )
except Exception as e:
    raise SystemExit(1)
" || [ $RETRIES -eq 0 ]; do
  echo "Banco indisponível, tentando novamente em 3 segundos..."
  RETRIES=$((RETRIES - 1))
  sleep 3
done

echo "Banco disponível! Aplicando migrações..."

python manage.py makemigrations user
python manage.py makemigrations chatbot
python manage.py migrate

echo "Criando superusuário..."

python manage.py createsuperuser --noinput || true

echo "Iniciando servidor Django..."

exec "$@"
