from prometheus_client import Gauge
import api


def new(sensor_name: str) -> Gauge:
    prefix = sensor_name.strip().lower().replace(" ", "_")
    gauge_name = f"{prefix}_temperature_api_requests"
    return Gauge(gauge_name, sensor_name)


def set_value(gauge: Gauge, sensor_id: int) -> None:
    value = api.get_temperature(sensor_id)
    gauge.set(value)
