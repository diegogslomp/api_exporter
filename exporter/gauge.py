from prometheus_client import Gauge
import api
import logging


def new_gauge(sensor_name: str) -> Gauge:
    prefix = sensor_name.strip().lower().replace(" ", "_")
    name = f"{prefix}_temperature_api_requests"
    return Gauge(name=name, documentation=sensor_name)


def get_temperature_and_set_gauge(sensor_id: int, gauge: Gauge) -> None:
    value = 0.0
    try:
        value = api.get_temperature(sensor_id)
    except Exception as e:
        logging.error(e)
        logging.warning(f"Gauge {gauge._name} cleared")
    finally:
        gauge.set(value)
