import api
import logging
from gauge import new_gauge, get_temperature_and_set_gauge

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
    sensors = [Sensor(sensor["id"], sensor["name"]) for sensor in api_sensors]
    msg = "Sensors: " + ", ".join(str(sensor) for sensor in sensors)
    logging.info(msg)
    return sensors
