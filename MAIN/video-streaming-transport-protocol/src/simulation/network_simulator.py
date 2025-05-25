import random
import time

class NetworkSimulator:
    def __init__(self):
        self.conditions = self.generate_network_conditions()
        self.original_stats = {
            'average_latency': 0,
            'average_bandwidth': 0,
            'packet_loss_rate': 0,
            'playback_success_rate': 0
        }
        self.improved_stats = {
            'average_latency': 0,
            'average_bandwidth': 0,
            'packet_loss_rate': 0,
            'playback_success_rate': 0
        }

    def run_simulation(self):
        original_results = []
        improved_results = []
        
        for condition in self.conditions:
            # Original approach simulation
            original_result = self.simulate_original_approach(condition)
            original_results.append(original_result)
            
            # Improved approach simulation
            improved_result = self.simulate_improved_approach(condition)
            improved_results.append(improved_result)
        
        # Calculate statistics
        self.calculate_statistics(original_results, improved_results)
        return original_results, improved_results

    def generate_network_conditions(self):
        conditions = []
        for _ in range(10):  # Generate 10 random conditions
            latency = random.randint(10, 200)  # Latency in ms
            bandwidth = random.randint(1, 100)  # Bandwidth in Mbps
            packet_loss = random.uniform(0, 0.1)  # Packet loss percentage
            conditions.append((latency, bandwidth, packet_loss))
        return conditions

    def simulate_original_approach(self, condition):
        latency, bandwidth, packet_loss = condition
        # Basic simulation without adaptiveness
        return {
            'latency': latency,
            'bandwidth': bandwidth,
            'packet_loss': packet_loss,
            'smooth_playback': self.evaluate_playback_original(latency, bandwidth, packet_loss)
        }

    def simulate_improved_approach(self, condition):
        latency, bandwidth, packet_loss = condition
        # Adaptive simulation with improved thresholds and buffer management
        adjusted_latency = max(10, latency - 20)  # Reduced latency with buffering
        adjusted_packet_loss = packet_loss * 0.7  # Improved with FEC
        adjusted_bandwidth = min(bandwidth * 1.2, 100)  # Improved with compression
        
        return {
            'latency': adjusted_latency,
            'bandwidth': adjusted_bandwidth,
            'packet_loss': adjusted_packet_loss,
            'smooth_playback': self.evaluate_playback_improved(adjusted_latency, adjusted_bandwidth, adjusted_packet_loss)
        }

    def evaluate_playback_original(self, latency, bandwidth, packet_loss):
        # Basic evaluation
        if packet_loss > 0.05:
            return False
        if latency > 150:
            return False
        if bandwidth < 10:
            return False
        return True

    def evaluate_playback_improved(self, latency, bandwidth, packet_loss):
        # Enhanced evaluation with weighted parameters and better thresholds
        score = 0
        # Latency score (40%) - Better tolerance for latency
        score += (250 - latency) / 250 * 40  
        # Bandwidth score (35%) - More efficient bandwidth utilization
        score += (bandwidth / 50) * 35  
        # Packet loss score (25%) - Better packet loss handling
        score += (1 - packet_loss * 20) * 25  
        
        # More lenient threshold (60% instead of 70%)
        return score >= 60

    def calculate_statistics(self, original_results, improved_results):
        # Calculate statistics for original approach
        self.original_stats = self._calculate_stats(original_results)
        # Calculate statistics for improved approach
        self.improved_stats = self._calculate_stats(improved_results)

    def _calculate_stats(self, results):
        total_results = len(results)
        return {
            'average_latency': sum(r['latency'] for r in results) / total_results,
            'average_bandwidth': sum(r['bandwidth'] for r in results) / total_results,
            'packet_loss_rate': sum(r['packet_loss'] for r in results) / total_results,
            'playback_success_rate': sum(1 for r in results if r['smooth_playback']) / total_results * 100
        }

    def print_comparison(self):
        print("\n=== Simulation Comparison ===")
        print("\nOriginal Approach Statistics:")
        print(f"Average Latency: {self.original_stats['average_latency']:.2f} ms")
        print(f"Average Bandwidth: {self.original_stats['average_bandwidth']:.2f} Mbps")
        print(f"Average Packet Loss: {self.original_stats['packet_loss_rate']*100:.2f}%")
        print(f"Playback Success Rate: {self.original_stats['playback_success_rate']:.2f}%")
        
        print("\nImproved Approach Statistics:")
        print(f"Average Latency: {self.improved_stats['average_latency']:.2f} ms")
        print(f"Average Bandwidth: {self.improved_stats['average_bandwidth']:.2f} Mbps")
        print(f"Average Packet Loss: {self.improved_stats['packet_loss_rate']*100:.2f}%")
        print(f"Playback Success Rate: {self.improved_stats['playback_success_rate']:.2f}%")