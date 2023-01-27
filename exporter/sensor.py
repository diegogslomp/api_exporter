import gauge


class Sensor:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.gauge = gauge.new(self.name)
