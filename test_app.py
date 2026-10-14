import json
import threading
import unittest
from http.server import HTTPServer

from app import DevOpsHandler


class TestDevOpsApplication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), DevOpsHandler)
        cls.port = cls.server.server_address[1]

        cls.server_thread = threading.Thread(
            target=cls.server.serve_forever,
            daemon=True,
        )
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join(timeout=2)

    def test_homepage_returns_success(self):
        import urllib.request

        with urllib.request.urlopen(
            f"http://127.0.0.1:{self.port}/"
        ) as response:
            self.assertEqual(response.status, 200)
            html = response.read().decode("utf-8")

        self.assertIn("My First DevOps Project", html)

    def test_health_endpoint(self):
        import urllib.request

        with urllib.request.urlopen(
            f"http://127.0.0.1:{self.port}/health"
        ) as response:
            self.assertEqual(response.status, 200)
            self.assertIn(
                "application/json",
                response.headers.get("Content-Type", ""),
            )
            data = json.loads(response.read().decode("utf-8"))

        self.assertEqual(data["status"], "healthy")
        self.assertEqual(
            data["application"],
            "Python DevOps Pipeline",
        )


if __name__ == "__main__":
    unittest.main()