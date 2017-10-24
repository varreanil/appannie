import unittest

from appannie.appannieapi import AppAnnieApi


class TestAppAnnie(unittest.TestCase):

    def setUp(self):
        self.goodKey = "306d7db159531f549f96cf178ad82bb737201d46"
        self.badKey = "abcd"


    def test_accounts_api_call(self):
       api = AppAnnieApi(self.goodKey)
       accounts = api.accounts()
       self.assertTrue(accounts)
       print(accounts)
       self.assertEquals(accounts["code"], 200)

    def test_api_call_with_bad_key(self):
        api = AppAnnieApi(self.badKey)
        with self.assertRaises(ValueError) as context :
            api.accounts()

if __name__ == '__main__':
    unittest.main()