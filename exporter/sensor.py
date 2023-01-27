import gauge
import api


class Sensor:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.gauge = gauge.new(self.name)

    def set_gauge_value(self) -> None:
        gauge.set_value(self.gauge, self.id)


def generate_list() -> list[Sensor]:
    return [Sensor(sensor["id"], sensor["name"]) for sensor in api.get_sensors()]
