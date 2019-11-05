FROM ubuntu:16.04
MAINTAINER Your Name "youremail@domain.tld"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev libmysqlclient-dev && \
    pip install --upgrade pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "flask-app.py" ]
