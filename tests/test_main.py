from urllib import response
from main import *
import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from icecream import ic

class Test_Main(unittest.TestCase):
    @patch("requests.get")
    def test_successful_login(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"token": "1234"}
        token = get_token(url=f"{ROOT_URL}/token?EMAIL={EMAIL}")
        print("=== token ===")
        print(token)
        self.assertIsNotNone(token)

    @patch("requests.get")
    def test_error_login(self, mock_get):
        mock_get.return_value.status_code = 500
        token = get_token(url=f"{ROOT_URL}/token?EMAIL={EMAIL}")
        self.assertNotEqual(token.status_code, 200)

    @patch("requests.post")
    @patch("requests.get")
    def test_ok_check(self, mock_post, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"token": "1234", "message": True}
        token = get_token(url=f"{ROOT_URL}/token?EMAIL={EMAIL}")
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "blocks": ['rxVwnvhzoUlrKWBj2Lnm8mDeuuiSNfvSepES7xw2zJu8KbfEFPAQkrlwV2vgqHtOvRzFRuqpnXl61O9b7ryoqse6JlEIiSwqyfsM', 'OFSEneyo4T2BhInUEPYleIblA9vTt3INMxzhaIxrU4TFSNRLbhUZDgZUvIUoPBP3Jby0Fj7uB5JQOU3AcK7q86mCniYzlevkaxi3', '2enEWA4yNXEwZjX7hkEyJchP33gDHH7tJjyGJDYRWiZDLYbnqYQX7Ql766nHf3DT3tgyvWVH9sjKDWRCVrGYvd01c9YHcarepAeM', 'e7hKjsplWWgqRlZ7lwDjjjRPfLEGy57YkyRpWdTbF8yWkWRrSFcNHQd9L87zSztiSLevP8f2AwkYjG2Gsok4bFhCwRdduIJ2kjnW', 'FB9ylA7uBWyJSHb47Z6YX0YTNcyCwrqkovryLEZ2pm8Eu7GNgxKuEIj6HIkQ829hPGTzEsCE9Q2dukgWncvyto9dCpewJtzUfzxm', 'xGrYsHPt7LeCo2fFaI5nDwAWdNf8QvbHqC6gr3XjMtAiu7lVuPrkpcEmXkiGwfnr2v3JNcOOdFFL3k5w1gAJvpqagce7xLpTpvtd', 'hp1xTqUUjM2BSek0xpP81IxkGJPnxRmkgZ1OlhPqZhhyKf4ExY42PGeggwauXkvixJ2z3ZGvkNgrmABGzKHzjbSBzTcPvUlxt9Ji', 'Bfm6DNnz6rTYaKbOcy3a3rPxjqgU3B8ASaLqg9aSwtNwxpu6T8EnPYr2Cm2cthBXVWCacuuVR9UQO7qUnw0DWVurdjmbwVU692ym', 'zHLhejbtbF3mCOWZBoLmoByl9lMETmWJkGdBhgQJqcCFtpeCi26lGpmq2Sq0TV8pFDqhX0u3aVC5Ax8vjTzKZQ3YdQ9gYYEuPkMg']
        }
        blocks = ['rxVwnvhzoUlrKWBj2Lnm8mDeuuiSNfvSepES7xw2zJu8KbfEFPAQkrlwV2vgqHtOvRzFRuqpnXl61O9b7ryoqse6JlEIiSwqyfsM', 'OFSEneyo4T2BhInUEPYleIblA9vTt3INMxzhaIxrU4TFSNRLbhUZDgZUvIUoPBP3Jby0Fj7uB5JQOU3AcK7q86mCniYzlevkaxi3', '2enEWA4yNXEwZjX7hkEyJchP33gDHH7tJjyGJDYRWiZDLYbnqYQX7Ql766nHf3DT3tgyvWVH9sjKDWRCVrGYvd01c9YHcarepAeM', 'e7hKjsplWWgqRlZ7lwDjjjRPfLEGy57YkyRpWdTbF8yWkWRrSFcNHQd9L87zSztiSLevP8f2AwkYjG2Gsok4bFhCwRdduIJ2kjnW', 'FB9ylA7uBWyJSHb47Z6YX0YTNcyCwrqkovryLEZ2pm8Eu7GNgxKuEIj6HIkQ829hPGTzEsCE9Q2dukgWncvyto9dCpewJtzUfzxm', 'xGrYsHPt7LeCo2fFaI5nDwAWdNf8QvbHqC6gr3XjMtAiu7lVuPrkpcEmXkiGwfnr2v3JNcOOdFFL3k5w1gAJvpqagce7xLpTpvtd', 'hp1xTqUUjM2BSek0xpP81IxkGJPnxRmkgZ1OlhPqZhhyKf4ExY42PGeggwauXkvixJ2z3ZGvkNgrmABGzKHzjbSBzTcPvUlxt9Ji', 'Bfm6DNnz6rTYaKbOcy3a3rPxjqgU3B8ASaLqg9aSwtNwxpu6T8EnPYr2Cm2cthBXVWCacuuVR9UQO7qUnw0DWVurdjmbwVU692ym', 'zHLhejbtbF3mCOWZBoLmoByl9lMETmWJkGdBhgQJqcCFtpeCi26lGpmq2Sq0TV8pFDqhX0u3aVC5Ax8vjTzKZQ3YdQ9gYYEuPkMg']
        result = check(blocks=blocks, token=token)
        ic(result)
        self.assertTrue(result)

    @patch("requests.post")
    @patch("requests.get")
    def test_empty_blocks_check(self, mock_post, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"token": "1234"}
        token = get_token(url=f"{ROOT_URL}/token?EMAIL={EMAIL}")
        mock_get.stop()
        mock_post.return_value.status_code = 200
        result = check(blocks=[], token=token)
        ic(result)
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()