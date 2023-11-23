from prometheus_client import start_http_server
from sensor import generate_sensor_list
import logging
import time
import os


def loop() -> None:
    sensors = generate_sensor_list()
    while True:
        [sensor.set_gauge() for sensor in sensors]
        time.sleep(60)


if __name__ == "__main__":
    format = "%(asctime)s %(levelname)s: %(message)s"
    level = os.getenv("LOG_LEVEL", "INFO")
    logging.basicConfig(format=format, level=level)

    port = int(os.getenv("EXPORTER_PORT", 8083))
    logging.info(f"Starting web server at port {port}")
    start_http_server(port)

    loop()
