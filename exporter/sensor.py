import api
import gauge
import logging


class Sensor:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.gauge = gauge.new(self.name)

    def set_gauge_value(self) -> None:
        gauge.set_value(self.gauge, self.id)

    def __str__(self):
        return f"{self.id}: {self.name}"


def generate_sensor_list() -> list[Sensor]:
    sensors = []
    api_sensors = api.get_sensors()
    try:
        sensors = [Sensor(sensor["id"], sensor["name"]) for sensor in api_sensors]
        msg = "Sensors: " + str([sensor.__str__() for sensor in sensors])
        logging.info(msg)
    except Exception as e:
        logging.warning("Error creating sensor list")
        logging.debug(e)
    finally:
        return sensors
