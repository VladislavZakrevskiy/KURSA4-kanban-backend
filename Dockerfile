FROM python:3.12

WORKDIR /app

COPY req.txt /app/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r req.txt

COPY ./project /app/project

ENV DJANGO_SETTINGS_MODULE=project.settings
ENV PYTHONUNBUFFERED=1

WORKDIR /app/project

RUN python manage.py collectstatic --noinput
# RUN python manage.py makemigrations
# RUN python manage.py migrate
# RUN python manage.py generate_swagger

EXPOSE 8000

CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
