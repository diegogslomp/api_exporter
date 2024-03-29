import unittest
from sensor import generate_sensor_list, Sensor


class TestGauges(unittest.TestCase):
    def test_get_api_sensor_list_and_set_gauge_values(self):
        sensors = generate_sensor_list()
        [sensor.set_gauge() for sensor in sensors]

    def test_offline_sensor(self):
        offline = Sensor(id=999, name="Offline Sensor")
        offline.set_gauge()
        msg = "Offline sensors should be zero"
        self.assertEqual(offline.gauge._value.get(), 0.0, msg)


if __name__ == "__main__":
    unittest.main()
