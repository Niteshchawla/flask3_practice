FROM python:3.8-slim-buster

WORKDIR /flask-loan-app

COPY artefacts/requirements.txt .

RUN pip install -r requirements.txt

COPY . /flask-loan-app/

# python -m flask --app hello.py run --host=0.0.0.0 --port=8000

CMD ["python", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0.0", "--port=8000"]