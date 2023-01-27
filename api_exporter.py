from prometheus_client import start_http_server, Gauge
import requests
import urllib3
import logging
import time
import os

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


def create_new_gauge(sensor_name: str) -> Gauge:
    prefix = sensor_name.lstrip().lower().replace(" ", "_")
    gauge_name = f"{prefix}_temperature_api_requests"
    return Gauge(gauge_name, sensor_name)


class Sensor:
    def __init__(self, sensor: dict):
        self.id = sensor["id"]
        self.name = sensor["name"]
        self.gauge = create_new_gauge(self.name)


def set_gauge_value(sensor: Sensor) -> None:
    try:
        sensor.gauge.set(get_temperature(sensor.id))
    except Exception as e:
        msg = f"Error getting sensor {sensor.name} temp. Gauge cleared."
        logging.warning(msg)
        logging.debug(e)
        sensor.gauge.clear()


def get_api_results(path: str) -> list[dict]:
    host = os.environ["API_HOST"]
    port = os.environ["API_PORT"]
    user = os.environ["API_USER"]
    password = os.environ["API_PASSWORD"]
    url = f"https://{host}:{port}/api/v1/{path}"
    response = requests.get(
        url,
        auth=(user, password),
        verify=False,
    )
    response.raise_for_status()
    return response.json()["results"]


def get_temperature(sensor_id: int) -> float:
    results = get_api_results(f"instruments/{sensor_id}/values")
    for result in results:
        if result["code"] == "Temperature":
            return result["values"][0]["value"]


def get_sensors() -> list[dict]:
    return get_api_results("instruments")


def mainloop() -> None:
    sensors = [Sensor(api_sensor) for api_sensor in get_sensors()]
    while True:
        [set_gauge_value(sensor) for sensor in sensors]
        time.sleep(60)


if __name__ == "__main__":
    # Disable cert warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # Start up the server to expose the metrics.
    start_http_server(8083)
    mainloop()
