
FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    python3-tk 



RUN pip install virtualenv
RUN virtualenv /app/venv


COPY requirements.txt /app/
RUN /app/venv/bin/pip install  -r requirements.txt


COPY . /app


CMD ["/app/venv/bin/python", "frontend_gui.py"]
