import unittest
import xml.etree.ElementTree as ET

import requests


class TestInboundConnections(unittest.TestCase):

    def setUp(self) -> None:
        self.account_number = "ACC00000000000000000"
        self.url = "https://tnts4a6y6fb.sandbox.verygoodproxy.com/post"

    def test_json(self):
        headers = {"Content-type": "application/json"}
        data = '{"account_number": "%s"}' % self.account_number  # this type of formatting because of the curly brackets

        r = requests.post(self.url, headers=headers, data=data)
        self.assertEqual(r.status_code, 200)

        tokenized = eval(r.json()['data']).get('account_number')
        self.assertNotEqual(tokenized, self.account_number)

    def test_xml(self):
        headers = {'Content-type': 'application/xml'}
        data = f'<account_number>{self.account_number}</account_number>'

        r = requests.post(self.url, headers=headers, data=data)

        root = ET.fromstring(r.json()['data'])
        self.assertEqual(r.status_code, 200)

        tokenized = root.text
        self.assertNotEqual(tokenized, self.account_number)

    def test_form(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = f'account_number={self.account_number}'

        r = requests.post(self.url, headers=headers, data=data)
        self.assertEqual(r.status_code, 200)

        tokenized = r.json()['form'].get('account_number')
        self.assertNotEqual(tokenized, self.account_number)
