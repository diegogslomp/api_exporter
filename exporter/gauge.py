from requests.exceptions import HTTPError
from prometheus_client import Gauge
import logging
import api


class TemperatureGauge(Gauge):
    def __init__(self, sensor_name: str, sensor_id: int):
        prefix = sensor_name.strip().lower().replace(" ", "_")
        self.name = f"{prefix}_temperature_api_requests"
        self.id = sensor_id
        super.__init__(name=self.name, documentation=sensor_name)

    def set_value(self) -> None:
        value = 0.0
        try:
            value = api.get_temperature(self.id)
        except Exception as e:
            logging.error(e)
            logging.warning(f"Gauge {self.name} cleared")
        finally:
            self.set(value)

    def __str__(self) -> str:
        return f"{self.name}"


def generate_gauges() -> list[TemperatureGauge]:
    gauges = []
    sensors = api.get_sensors()
    msg = "Sensors: "
    # For each api sensor, create a prometheus gauge to update every minute
    for sensor in sensors:
        try:
            gauge = TemperatureGauge(sensor_name=sensor["name"], sensor_id=sensor["id"])
            gauges.append(gauge)
            msg = ", ".join(f'{sensor["id"]}: {sensor["name"]}')
        except ValueError:
            logging.warning(f"Invalid metric {sensor["name"]}, skipped")
        except HTTPError:
            logging.warning(f"Bad request for {sensor["name"]}, skipped")
    logging.info(msg)
    return gauges
