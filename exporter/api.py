import requests
import urllib3
import dotenv
import os

dotenv.load_dotenv()


def get_api_results(url_suffix: str) -> list[dict]:
    # Disable certifcate warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = (
        f"https://{os.environ["API_HOST"]}:{os.environ["API_PORT"]}/api/v1/{url_suffix}"
    )
    response = requests.get(
        url=url,
        auth=(os.environ["API_USER"], os.environ["API_PASSWORD"]),
        verify=False,
        timeout=float(os.getenv("TIMEOUT", 5)),
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
