FROM python:3.9

EXPOSE 8000

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# ENV PYTHONENV_ROOT_PATH=/api/v1

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--access-log", "--use-colors"]
