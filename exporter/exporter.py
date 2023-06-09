from prometheus_client import start_http_server
from sensor import generate_sensor_list
import logging
import time
import os


def loop() -> None:
    sensors = generate_sensor_list()
    while True:
        [sensor.set_gauge_value() for sensor in sensors]
        time.sleep(60)


if __name__ == "__main__":
    format = "%(levelname)s: %(message)s"
    log_level = os.getenv("LOG_LEVEL", "INFO")
    port = int(os.getenv("EXPORTER_PORT", 8083))
    logging.basicConfig(format=format, level=log_level)
    logging.info(f"Starting web server at {port} port..")
    start_http_server(port)
    loop()
