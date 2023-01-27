from prometheus_client import start_http_server
import logging
import time
import api
import gauge
from sensor import Sensor

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)


def mainloop() -> None:
    sensors = [
        Sensor(api_sensor["id"], api_sensor["name"]) for api_sensor in api.get_sensors()
    ]
    while True:
        [gauge.set_value(sensor.gauge, sensor.id) for sensor in sensors]
        time.sleep(60)


if __name__ == "__main__":
    # Start up the server to expose the metrics.
    start_http_server(8083)
    mainloop()
