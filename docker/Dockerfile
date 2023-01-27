FROM python:alpine

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY exporter/*.py ./
CMD python exporter.py

EXPOSE 8083
