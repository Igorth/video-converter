import unittest
from app import app


class VideoConverterTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_upload_video(self):
        with open('test_video.wmv', 'rb') as video:
            result = self.app.post('/', data={'file': video})
            print(result.data)
            self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
