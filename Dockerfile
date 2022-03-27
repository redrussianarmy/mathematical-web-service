FROM python:3.10.1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /root/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip3 install -r /root/requirements.txt

RUN mkdir -p /usr/web_service

COPY ./web_service /usr/web_service

WORKDIR /usr/web_service
EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000