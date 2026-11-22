import unittest
import ipaddress
import socket


class TestNetworkScanner(unittest.TestCase):

    def test_valid_ip(self):
        ip = ipaddress.ip_address("127.0.0.1")
        self.assertEqual(str(ip), "127.0.0.1")

    def test_invalid_ip(self):
        with self.assertRaises(ValueError):
            ipaddress.ip_address("999.999.999.999")

    def test_localhost_connection(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("127.0.0.1", 0))
        server.listen(1)

        port = server.getsockname()[1]

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(2)

        result = client.connect_ex(("127.0.0.1", port))

        self.assertEqual(result, 0)

        client.close()
        server.close()


if __name__ == "__main__":
    unittest.main()
