import unittest
from sensor import generate_sensor_list, Sensor


class TestGauges(unittest.TestCase):
    def test_generate_sensor_list_and_get_values(self):
        sensors = generate_sensor_list()
        [sensor.set_gauge_value() for sensor in sensors]

    def test_wrong_sensor(self):
        wrong_sensor = Sensor(id=140, name="Wrong Sensor")
        wrong_sensor.set_gauge_value()


if __name__ == "__main__":
    unittest.main()
