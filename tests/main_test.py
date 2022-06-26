from main import *
import unittest
from icecream import ic

class MainTest(unittest.TestCase):
    def successful_login(self):
        token = get_token(url=f"{ROOT_URL}/token?EMAIL={EMAIL}")
        ic(token)
        self.assertIsNotNone(token)

    def error_login(self):
        EMAIL = "juanitogmail.com"
        token = get_token(url=f"{ROOT_URL}/token?EMAIL={EMAIL}")
        self.assertNotEqual(token, 200)

    def make_get_request(self):
        token = make_get_request(url=f"{ROOT_URL}/token?EMAIL={EMAIL}", get="token")
        ic(token)
        ic(type(token))
        self.assertIsInstance(token,str)

    def error_make_get_request(self):
        EMAIL = ""
        token = make_get_request(url=f"{ROOT_URL}/token?EMAIL={EMAIL}", get="token")
        ic(token)
        ic(type(token))
        self.assertIsInstance(token, type(None))

    def ok_check(self):
        token = get_token(url=f"{ROOT_URL}/token?EMAIL={EMAIL}")
        blocks = ['rxVwnvhzoUlrKWBj2Lnm8mDeuuiSNfvSepES7xw2zJu8KbfEFPAQkrlwV2vgqHtOvRzFRuqpnXl61O9b7ryoqse6JlEIiSwqyfsM', 'OFSEneyo4T2BhInUEPYleIblA9vTt3INMxzhaIxrU4TFSNRLbhUZDgZUvIUoPBP3Jby0Fj7uB5JQOU3AcK7q86mCniYzlevkaxi3', '2enEWA4yNXEwZjX7hkEyJchP33gDHH7tJjyGJDYRWiZDLYbnqYQX7Ql766nHf3DT3tgyvWVH9sjKDWRCVrGYvd01c9YHcarepAeM', 'e7hKjsplWWgqRlZ7lwDjjjRPfLEGy57YkyRpWdTbF8yWkWRrSFcNHQd9L87zSztiSLevP8f2AwkYjG2Gsok4bFhCwRdduIJ2kjnW', 'FB9ylA7uBWyJSHb47Z6YX0YTNcyCwrqkovryLEZ2pm8Eu7GNgxKuEIj6HIkQ829hPGTzEsCE9Q2dukgWncvyto9dCpewJtzUfzxm', 'xGrYsHPt7LeCo2fFaI5nDwAWdNf8QvbHqC6gr3XjMtAiu7lVuPrkpcEmXkiGwfnr2v3JNcOOdFFL3k5w1gAJvpqagce7xLpTpvtd', 'hp1xTqUUjM2BSek0xpP81IxkGJPnxRmkgZ1OlhPqZhhyKf4ExY42PGeggwauXkvixJ2z3ZGvkNgrmABGzKHzjbSBzTcPvUlxt9Ji', 'Bfm6DNnz6rTYaKbOcy3a3rPxjqgU3B8ASaLqg9aSwtNwxpu6T8EnPYr2Cm2cthBXVWCacuuVR9UQO7qUnw0DWVurdjmbwVU692ym', 'zHLhejbtbF3mCOWZBoLmoByl9lMETmWJkGdBhgQJqcCFtpeCi26lGpmq2Sq0TV8pFDqhX0u3aVC5Ax8vjTzKZQ3YdQ9gYYEuPkMg']
        result = check(blocks=blocks, token=token)
        ic(result)
        self.assertTrue(result)

    def empty_blocks_check(self):
        token = get_token(url=f"{ROOT_URL}/token?EMAIL={EMAIL}")
        ### Get blocks
        blocks = []
        result = check(blocks=blocks, token=token)
        ic(result)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()