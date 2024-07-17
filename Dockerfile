FROM python:3.11.5

RUN mkdir app

WORKDIR /app/

COPY . ./


RUN pip install -r requirements.txt

CMD ["gunicorn", "movieHubProj.wsgi:application", "--bind", "0.0.0.0:8000"]