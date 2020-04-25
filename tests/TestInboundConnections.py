import unittest

import requests


class TestInboundConnectionsJson(unittest.TestCase):

    def setUp(self):
        self.account_number = "ACC00000000000000000"

    def test_json(self):
        headers = {'Content-type': 'application/json'}
        data = '{"account_number": "ACC00000000000000000"}'

        r = requests.post('https://tntsfeqzp4a.sandbox.verygoodproxy.com/post', headers=headers,
                          data=data)  # TODO: Change to format
        tokenized = eval(r.json()['data']).get('account_number')

        self.assertEqual(r.status_code, 200)
        self.assertNotEqual(tokenized, self.account_number)


class TestInboundConnectionsXml(unittest.TestCase):

    def setUp(self) -> None:
        self.account_number = "ACC00000000000000001"

    def test_xml(self):
        headers = {'Content-type': 'application/xml'}
