import unittest
import xml.etree.ElementTree as ET

import requests


class TestInboundConnectionsJson(unittest.TestCase):

    def setUp(self):
        self.account_number = "ACC00000000000000000"

    def test_json(self):
        headers = {'Content-type': 'application/json'}
        data = '{"account_number": "ACC00000000000000000"}'

        r = requests.post('https://tntsfeqzp4a.sandbox.verygoodproxy.com/post', headers=headers,
                          data=data)  # TODO: Change to format
        self.assertEqual(r.status_code, 200)

        tokenized = eval(r.json()['data']).get('account_number')
        self.assertNotEqual(tokenized, self.account_number)


class TestInboundConnectionsXml(unittest.TestCase):

    def setUp(self) -> None:
        self.account_number = 'ACC00000000000000000'

    def test_xml(self):
        headers = {'Content-type': 'application/xml'}
        data = f'<account_number>{self.account_number}</account_number>'

        r = requests.post('https://tnts4a6y6fb.sandbox.verygoodproxy.com/post', headers=headers, data=data)

        root = ET.fromstring(r.json()['data'])
        self.assertEqual(r.status_code, 200)

        tokenized = root.text
        self.assertNotEqual(tokenized, self.account_number)


class TestInboundConnectionForm(unittest.TestCase):

    def setUp(self) -> None:
        self.account_number = 'ACC00000000000000000'

    def test_form(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = 'account_number=ACC00000000000000000'

        r = requests.post('https://tnts4a6y6fb.sandbox.verygoodproxy.com/post', headers=headers, data=data)
        self.assertEqual(r.status_code, 200)

        tokenized = r.json()['form'].get('account_number')
        self.assertNotEqual(tokenized, self.account_number)