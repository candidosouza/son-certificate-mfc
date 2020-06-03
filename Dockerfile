 FROM python:3.7.3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /app
 COPY requirements.txt /app/
 RUN pip install -r /app/requirements.txt
 ADD . /app/
 WORKDIR /app/
