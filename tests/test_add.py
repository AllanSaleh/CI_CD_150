import unittest
from app import app
from faker import Faker

class TestAddEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_successful_request(self):
        payload = {'num1': 30, 'num2': 20}
        response = self.app.post('/add', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['result'], 50)
    
    def test_random_add(self):
        fake = Faker()
        num1 = fake.random_number(digits=3) #creating mock (random) data for num1
        num2 = fake.random_number(digits=3)
        payload = {'num1': num1, 'num2':num2}
        response = self.app.post('/add', json=payload) #sending a mock post request to our apps testing clint's /add route with a payload
        data = response.get_json()
        self.assertEqual(data['result'], num1+num2)

    def test_no_payload(self):
        response = self.app.post('/add')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['error'], 'Content-Type must be application/json')

    def test_bad_payload(self):
        payload = {'num1': 'hello', 'num2': 'world'}
        response = self.app.post('/add', json=payload)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['error'], 'Bad data, values must be int or float')

if __name__ == '__main__':
    unittest.main()