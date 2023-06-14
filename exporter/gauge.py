from prometheus_client import Gauge
import api
import logging


def new(sensor_name: str) -> Gauge:
    prefix = sensor_name.strip().lower().replace(" ", "_")
    gauge_name = f"{prefix}_temperature_api_requests"
    return Gauge(gauge_name, sensor_name)


def set_value(gauge: Gauge, sensor_id: int) -> None:
    value = 0.0
    try:
        value = api.get_temperature(sensor_id)
    except Exception as e:
        logging.error(e)
        logging.warning(f"Gauge {gauge._name} cleared")
    finally:
        gauge.set(value)
