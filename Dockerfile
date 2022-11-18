FROM python:alpine

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY sitrad_exporter.py sitrad_exporter.py
CMD python sitrad_exporter.py

EXPOSE 8083
