FROM python:3.7-alpine


ENV ASYNCWORKER_HTTP_HOST=0.0.0.0

WORKDIR /tmp
COPY Pipfile.lock /tmp/
COPY Pipfile /tmp/

RUN pip install -U pip==18.1 pipenv==2018.10.13 \
&& apk add --virtual .deps gcc g++ make python-dev \
&& pipenv install --system --deploy --ignore-pipfile \
&& apk del --purge .deps

COPY . /opt/app
WORKDIR /opt/app

CMD ["python", "-m", "baas"]
