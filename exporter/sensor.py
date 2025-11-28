from requests.exceptions import HTTPError
from prometheus_client import Gauge
import logging
import api


class Sensor:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.gauge = self.new_gauge()

    def new_gauge(self) -> Gauge:
        prefix = self.name.strip().lower().replace(" ", "_")
        name = f"{prefix}_temperature_api_requests"
        return Gauge(name=name, documentation=self.name)

    def set_gauge(self) -> None:
        value = 0.0
        try:
            value = api.get_temperature(self.id)
        except Exception as e:
            logging.error(e)
            logging.warning(f"Gauge {self.gauge._name} cleared")
        finally:
            self.gauge.set(value)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


def generate_sensor_list() -> list[Sensor]:
    api_sensors = api.get_sensors()
    sensors = []

    for api_sensor in api_sensors:
        try:
            sensor = Sensor(api_sensor["id"], api_sensor["name"])
            api.get_temperature(sensor.id)
            sensors.append(sensor)
        except ValueError:
            logging.warning(f"Invalid metric name {api_sensor['name']}, sensor skipped")
        except HTTPError:
            logging.warning(
                f"Bad request for sensor {api_sensor['name']}, sensor skipped"
            )

    msg = "Sensors: " + ", ".join(str(sensor) for sensor in sensors)
    logging.info(msg)
    return sensors
