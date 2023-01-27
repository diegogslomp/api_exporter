FROM python:alpine

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY api_exporter.py api_exporter.py
CMD python api_exporter.py

EXPOSE 8083
