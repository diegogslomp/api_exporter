from prometheus_client import start_http_server
from sensor import generate_sensor_list
import logging
import time
import os


def loop() -> None:
    while True:
        sensors = generate_sensor_list()
        if sensors:
            break
        else:
            seconds = 30
            msg = f"No sensors to iterate, waiting {seconds} seconds"
            logging.warning(msg)
            time.sleep(seconds)

    while True:
        [sensor.set_gauge_value() for sensor in sensors]
        time.sleep(60)


if __name__ == "__main__":
    format = "%(levelname)s: %(message)s"
    log_level = os.getenv("LOG_LEVEL", "INFO")
    logging.basicConfig(format=format, level=log_level)

    port = int(os.getenv("EXPORTER_PORT", 8083))
    logging.info(f"Starting web server at port {port}")
    start_http_server(port)

    loop()
