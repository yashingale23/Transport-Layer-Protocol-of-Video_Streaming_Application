# main.py

from protocol.transport_protocol import TransportProtocol
from simulation.network_simulator import NetworkSimulator
from utils.visualizer import ResultVisualizer

def main():
    # Create network simulator
    network_simulator = NetworkSimulator()
    
    # Run simulation
    original_results, improved_results = network_simulator.run_simulation()
    
    # Display Original Approach Results
    print("\n=== Original Approach Results ===")
    for i, result in enumerate(original_results, 1):
        print(f"\nSimulation {i}:")
        print(f"Latency: {result['latency']}ms")
        print(f"Bandwidth: {result['bandwidth']}Mbps")
        print(f"Packet Loss: {result['packet_loss']*100:.2f}%")
        print(f"Smooth Playback: {'Yes' if result['smooth_playback'] else 'No'}")

    # Display Improved Approach Results
    print("\n=== Improved Approach Results ===")
    for i, result in enumerate(improved_results, 1):
        print(f"\nSimulation {i}:")
        print(f"Latency: {result['latency']}ms")
        print(f"Bandwidth: {result['bandwidth']}Mbps")
        print(f"Packet Loss: {result['packet_loss']*100:.2f}%")
        print(f"Smooth Playback: {'Yes' if result['smooth_playback'] else 'No'}")

    # Print comparison statistics
    network_simulator.print_comparison()

    # Create and display visualization
    visualizer = ResultVisualizer()
    visualizer.create_comparison_graphs(original_results, improved_results)

if __name__ == "__main__":
    main()