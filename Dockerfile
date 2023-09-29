# Basic nginx dockerfile starting with Ubuntu 20.04
FROM python:3.9
RUN apt-get -y update

RUN pip install --upgrade pip

ADD . /code
WORKDIR /code


RUN pip install -r requirements.txt

RUN chown -R nobody /code

USER nobody

RUN python manage.py migrate
RUN pytest .

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
