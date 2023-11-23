from gauge import new_gauge, get_temperature_and_set_gauge
from requests.exceptions import HTTPError
import logging
import api


class Sensor:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.gauge = new_gauge(self.name)

    def set_gauge(self) -> None:
        get_temperature_and_set_gauge(self.id, self.gauge)

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
