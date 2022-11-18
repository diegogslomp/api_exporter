# sitrad_exporter

SITRAD API Temperature Exporter for Prometheus

<p align="center">
  <img src="https://raw.githubusercontent.com/diegogslomp/sitrad_exporter/master/img.png" style="max-height: 440px;"/>
</p>

1. Run exporter locally:
```
git clone --single-branch https://github.com/diegogslomp/sitrad_exporter
cd sitrad_exporter
pip install -r requirements.txt
cp example.env .env
# Edit .env file variables
python sitrad_exporter.py
```

2. Run as docker image:
```
docker run \
  -e API_HOST="10.0.0.10" \
  -e API_PORT="8002" \
  -e API_USER="admin" \
  -e API_PASSWORD="SecretTempP4ss!" \
  -p 8083:8083 \
  --name exporter diegogslomp/sitrad_exporter
```

- 2.1. Access http://localhost:8083 for metrics


3. Or run `Grafana - Prometheus - Exporter` docker stack (Ctrl+c to exit logs):
```
git clone --single-branch https://github.com/diegogslomp/sitrad_exporter
cd sitrad_exporter
cp example.env .env
# Edit .env file variables
docker compose up -d
docker compose logs -f
```

- 3.1. Access http://localhost:3000 (user:admin pass:admin)
- 3.2. Add Prometheus http://prometheus:9090 as Data Source
- 3.3. Explore metrics and create dashboards
