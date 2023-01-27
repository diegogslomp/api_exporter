# api_exporter

API Temperature Exporter for Prometheus. This script read temperatures from API and set Prometheus Gauges every minute.

<p align="center">
  <img src="https://raw.githubusercontent.com/diegogslomp/api_exporter/master/img.png" style="max-height: 440px;"/>
</p>

1. Run locally:
```
git clone --single-branch https://github.com/diegogslomp/api_exporter
cd api_exporter
# Copy and edit enviroment variables file
cp example.env .env
# Install requirements in a virtual environment
python -m pipenv install -r requirements.txt
# Run virtualenv loading .env vars
python -m pipenv shell
# Run script
python api_exporter.py
```

2. Or run as docker image:
```
docker run \
  -e API_HOST="10.0.0.10" \
  -e API_PORT="8002" \
  -e API_USER="admin" \
  -e API_PASSWORD="SecretTempP4ss!" \
  -p 8083:8083 \
  --name exporter diegogslomp/api_exporter
```

- 2.1. Access http://localhost:8083 for metrics


3. Or run Grafana + Prometheus + Exporter docker stack (Ctrl+c to exit logs):
```
git clone --single-branch https://github.com/diegogslomp/api_exporter
cd api_exporter
cp example.env .env
# Edit .env file variables
docker compose up -d
docker compose logs -f
```

- 3.1. Access http://localhost:3000 (user:admin pass:admin)
- 3.2. Add Prometheus http://prometheus:9090 as Data Source
- 3.3. Explore metrics and create dashboards
