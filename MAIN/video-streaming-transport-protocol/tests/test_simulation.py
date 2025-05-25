import unittest
from src.simulation.network_simulator import NetworkSimulator

class TestNetworkSimulator(unittest.TestCase):

    def setUp(self):
        self.simulator = NetworkSimulator(conditions={'latency': 50, 'packet_loss': 0.01})

    def test_initialization(self):
        self.assertIsNotNone(self.simulator)
        self.assertEqual(self.simulator.conditions['latency'], 50)
        self.assertEqual(self.simulator.conditions['packet_loss'], 0.01)

    def test_run_simulation(self):
        results = self.simulator.run_simulation()
        self.assertIn('throughput', results)
        self.assertIn('buffer_size', results)

    def test_generate_network_conditions(self):
        conditions = self.simulator.generate_network_conditions()
        self.assertIn('latency', conditions)
        self.assertIn('packet_loss', conditions)

if __name__ == '__main__':
    unittest.main()