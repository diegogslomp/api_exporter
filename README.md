# api_exporter

API Exporter for [Prometheus](https://prometheus.io/). Read temperatures and set gauges every minute.

<p align="center">
  <img src="https://raw.githubusercontent.com/diegogslomp/api_exporter/master/docker/img.png" style="max-height: 440px;"/>
</p>


1. Run locally:
```
git clone --single-branch https://github.com/diegogslomp/api_exporter
cd api_exporter

# Create and activate a virtual environment (optional)
python -m pipenv install
python -m pipenv shell

# Copy and edit enviroment variables file
cp .example.env .env

# Install dependencies
pip install -r requirements

# Run script
python exporter/exporter.py
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

# Copy and edit enviroment variables file
cp .example.env .env

docker compose up -d
docker compose logs -f
```

- 3.1. Access http://localhost:3000 (user:admin pass:admin)
- 3.2. Add Prometheus http://prometheus:9090 as Data Source
- 3.3. Explore metrics and create dashboards
