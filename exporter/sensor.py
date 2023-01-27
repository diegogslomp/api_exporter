import gauge

class Sensor:
    def __init__(self, sensor: dict):
        self.id = sensor["id"]
        self.name = sensor["name"]
        self.gauge = gauge.new(self.name)
