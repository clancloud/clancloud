FROM python:3.13
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# CMD ["gunicorn", "-c", "python:config.gunicorn", "hello.app:create_app()"]
CMD ["gunicorn","-w", "4", "-b", "0.0.0.0", "app:app"]
