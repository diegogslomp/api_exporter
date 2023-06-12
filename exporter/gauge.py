from prometheus_client import Gauge
from requests.exceptions import HTTPError
import logging
import api


def new(sensor_name: str) -> Gauge:
    prefix = sensor_name.strip().lower().replace(" ", "_")
    gauge_name = f"{prefix}_temperature_api_requests"
    return Gauge(gauge_name, sensor_name)


def set_value(gauge: Gauge, sensor_id: int) -> None:
    value = 0.0
    try:
        value = api.get_temperature(sensor_id)
    except HTTPError as e:
        msg = f"Error getting sensor {sensor_id} temp. Gauge cleared."
        logging.warning(msg)
        logging.debug(e)
    finally:
        gauge.set(value)
