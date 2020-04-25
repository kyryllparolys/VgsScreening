import unittest

import requests


class TestInboundConnectionsJson(unittest.TestCase):

    def setUp(self):
        self.account_number = "ACC00000000000000000"

    def test_json(self):
        headers = {'Content-type': 'application/json'}
        data = '{"account_number": "{}"}'.format(self.account_number)

        r = requests.post('https://tntsfeqzp4a.sandbox.verygoodproxy.com/post', headers=headers,
                          data=data)  # TODO: Change to format
        tokenized = eval(r.json()['data']).get('account_number')

        self.assertEqual(r.status_code, 200)
        self.assertNotEqual(tokenized, self.account_number)


class TestInboundConnectionForm(unittest.TestCase):

    def setUp(self) -> None:
        self.account_number = 'ACC00000000000000000'

    def test_form(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = f'account_number={self.account_number}'

        r = requests.post('https://tnts4a6y6fb.sandbox.verygoodproxy.com/post', headers=headers, data=data)
        tokenized = r.json()['form'].get('account_number')

        self.assertEqual(r.status_code, 200)
        self.assertNotEqual(tokenized, self.account_number)