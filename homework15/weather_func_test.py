import unittest
from homework15_nazar_yevtushenko import weather_now
from unittest.mock import patch, MagicMock
import json


class MyTestCase(unittest.TestCase):
    def test_city_not_found(self):
        self.assertEqual(weather_now(' '), 'city not found')

    def test_city_not_found2(self):
        self.assertEqual(weather_now('kharkv'), 'city not found')

    def test_nothing_to_geocode(self):
        self.assertEqual(weather_now(''), 'Nothing to geocode')

    @patch('homework15_nazar_yevtushenko.requests')
    def test_mock_normal_result(self, mock_requests):
        with open('weather.json') as file:
            fake_json = json.load(file)
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = fake_json
        mock_requests.get.return_value = mock_response
        self.assertEqual(weather_now('kharkiv'), "temp = 30.38, pressure = 1014, weather_description = 'overcast clouds'")

    @patch('homework15_nazar_yevtushenko.requests')
    def test_400_status(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {'cod': '400', 'message': 'Bad Request'}

        mock_requests.get.return_value = mock_response
        self.assertEqual(weather_now('kharkiv'), "Bad Request")


if __name__ == '__main__':
    unittest.main()
