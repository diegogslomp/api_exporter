# SITRAD API Temperature Exporter for Prometheus

Export sensor temperatures from SITRAD API for Prometheus

<p align="center">
  <img src="https://raw.githubusercontent.com/diegogslomp/sitrad_exporter/master/img.png" height=220 style="max-height: 440px;"/>
</p>

1. Run exporter locally:
```
git clone --single-branch https://github.com/diegogslomp/sitrad_exporter
cd sitrad_exporter
pip install -r requirements.txt
cp example.env .env
# Edit .env vars
python sitrad_exporter.py
```


2. Run as docker image:
```
docker run -d \
  -v $(pwd)/.env:/code/.env \
  -p 8083:8083 \
  --name exporter diegogslomp/sitrad_exporter
```

- 2.1. Access http://localhost:8083 for metrics


3. Or run `Grafana - Prometheus - Exporter` docker stack (Ctrl+c to exit logs):
```
git clone --single-branch https://github.com/diegogslomp/sitrad_exporter
cd sitrad_exporter
cp example.env .env
# Edit .env vars
docker compose up -d
docker compose logs -f
```

- 3.1. Access http://localhost:3000 for Grafana dashboard (user:admin pass:admin)
