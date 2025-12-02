import requests
import urllib3
import dotenv
import os

dotenv.load_dotenv()

def get_api_results(path: str) -> list[dict]:
    # Disable certifcate warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    host = os.environ["API_HOST"]
    port = os.environ["API_PORT"]
    user = os.environ["API_USER"]
    password = os.environ["API_PASSWORD"]
    url = f"https://{host}:{port}/api/v1/{path}"
    response = requests.get(
        url=url,
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
