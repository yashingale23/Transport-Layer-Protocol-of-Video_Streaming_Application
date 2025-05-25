import unittest
from src.protocol.transport_protocol import TransportProtocol

class TestTransportProtocol(unittest.TestCase):

    def setUp(self):
        self.protocol = TransportProtocol(bandwidth=5000, buffer_size=10)

    def test_adapt_bitrate_high_bandwidth(self):
        self.protocol.adapt_bitrate(8000)
        self.assertEqual(self.protocol.current_bitrate, 5000)

    def test_adapt_bitrate_low_bandwidth(self):
        self.protocol.adapt_bitrate(2000)
        self.assertEqual(self.protocol.current_bitrate, 2000)

    def test_handle_packet_loss(self):
        initial_loss = self.protocol.packet_loss_rate
        self.protocol.handle_packet_loss(5)
        self.assertGreater(self.protocol.packet_loss_rate, initial_loss)

    def test_minimize_jitter(self):
        packets = [1, 2, 3, 4, 5]
        smoothed_packets = self.protocol.minimize_jitter(packets)
        self.assertEqual(len(smoothed_packets), len(packets))

if __name__ == '__main__':
    unittest.main()