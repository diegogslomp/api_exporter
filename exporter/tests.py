import unittest
from gauge import generate_gauges, TemperatureGauge


class TestGauges(unittest.TestCase):
    def test_get_sensors_and_set_gauges(self):
        gauges = generate_gauges()
        [gauge.set_value() for gauge in gauges]

    def test_offline_sensor(self):
        offline = TemperatureGauge(sensor_id=999, sensor_name="Offline Sensor")
        offline.set_value()
        msg = "Offline sensors should be zero"
        self.assertEqual(offline._value.get(), 0.0, msg)


if __name__ == "__main__":
    unittest.main()
