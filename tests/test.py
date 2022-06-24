from main import *
import unittest

class Test(unittest.TestCase):
    def successful_login(self):
        token = get_token(url=f"{root_url}/token?email={email}")
        print(token)
        self.assertIsNotNone(token)
        # self.assertEqual(response.status_code, 200)

    def error_login(self):
        email = "juanito@gmail.com"
        token = get_token(url=f"{root_url}/token?email={email}")
        self.assertNotEqual(token, 200)

    def make_get_request(self):
        token = make_get_request(url=f"{root_url}/token?email={email}", get="token")
        print(token)
        print(type(token))
        self.assertIsInstance(token,str)

    def error_make_get_request(self):
        email = ""
        token = make_get_request(url=f"{root_url}/token?email={email}", get="token")
        print(token)
        print(type(token))
        self.assertIsInstance(token, type(None))

if __name__ == '__main__':
    unittest.main()