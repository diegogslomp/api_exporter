from prometheus_client import start_http_server, Gauge
from dotenv import load_dotenv
import requests
import urllib3
import logging
import time
import os


class Sensor:
    """Class for sensors and Prometheus temperature gauges"""

    def __init__(self, sensor: dict):
        self.id = sensor["id"]
        self.name = sensor["name"]
        self.gauge = Gauge(self.get_gauge_name(), f"{self.name}")

    def get_gauge_name(self) -> str:
        prefix = self.name.lstrip().lower().replace(" ", "_")
        return f"{prefix}_temperature_api_requests"


class API:
    """Sitrad API request methods"""

    @staticmethod
    def get_results(path: str) -> list[dict]:
        """Return results from API"""
        host = os.getenv("API_HOST")
        port = os.getenv("API_PORT")
        user = os.getenv("API_USER")
        password = os.getenv("API_PASSWORD")
        url = f"https://{host}:{port}/api/v1/{path}"
        response = requests.get(
            url,
            auth=(user, password),
            verify=False,
        )
        response.raise_for_status()
        return response.json()["results"]

    @staticmethod
    def get_temperature(sensor_id: int) -> float:
        """Query API and return sensor temperature value"""
        results = API.get_results(f"instruments/{sensor_id}/values")
        for result in results:
            if result["code"] == "Temperature":
                return result["values"][0]["value"]

    @staticmethod
    def get_sensors() -> list[dict]:
        """Query API and return sensor list"""
        return API.get_results("instruments")


def loop() -> None:
    """Load prometheus sensor gauges and update from API every 60 seconds"""
    sensors = [Sensor(sensor) for sensor in API.get_sensors()]
    while True:
        try:
            for sensor in sensors:
                sensor.gauge.set(API.get_temperature(sensor.id))
        except Exception as ex:
            logging.error(ex)
        finally:
            time.sleep(60)


if __name__ == "__main__":
    # Disable cert warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # Load enviroment variables from .env file
    load_dotenv()
    # Start up the server to expose the metrics.
    start_http_server(8083)
    loop()
