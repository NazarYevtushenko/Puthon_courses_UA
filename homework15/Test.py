import unittest
from homework15_nazar_yevtushenko import weather_now
from unittest.mock import patch
import json


class MyTestCase(unittest.TestCase):
    def test_city_not_found(self):
        self.assertEqual(weather_now(' '), 'city not found')

    def test_city_not_found2(self):
        self.assertEqual(weather_now('kharkv'), 'city not found')

    def test_nothing_to_geocode(self):
        self.assertEqual(weather_now(''), 'Nothing to geocode')

    def test_mock(self):
        with open('weather.json') as file:
            fake_json = json.load(file)
        with patch("homework15_nazar_yevtushenko.requests.get") as mocked_get:
            mocked_get.return_value.response = 200
            mocked_get.return_value.response = fake_json
            mocked_get.assert_called_with('http://api.openweathermap.org/data/2.5/weather?q=Kharkiv&appid=d82759ebf4a4a5ed987117c4027b9dfa&units=metric')
            weather = weather_now('kharkiv')
            self.assertEqual(weather, "temp = 30.38, pressure =1014, weather_description = 'moderate rain'")



if __name__ == '__main__':
    unittest.main()
