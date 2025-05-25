import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class ResultVisualizer:
    def __init__(self):
        # Set the style using seaborn
        sns.set_theme(style="darkgrid")
        # Set larger font sizes
        plt.rcParams.update({'font.size': 12})

    def create_comparison_graphs(self, original_results, improved_results):
        # Create figure with subplots
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        
        # Prepare data
        sim_range = range(1, len(original_results) + 1)
        
        # Latency Comparison
        ax1.plot(sim_range, [r['latency'] for r in original_results], 'r-', label='Original', linewidth=2)
        ax1.plot(sim_range, [r['latency'] for r in improved_results], 'g-', label='Improved', linewidth=2)
        ax1.set_title('Latency Comparison')
        ax1.set_xlabel('Simulation Run')
        ax1.set_ylabel('Latency (ms)')
        ax1.legend()

        # Bandwidth Comparison
        ax2.plot(sim_range, [r['bandwidth'] for r in original_results], 'r-', label='Original', linewidth=2)
        ax2.plot(sim_range, [r['bandwidth'] for r in improved_results], 'g-', label='Improved', linewidth=2)
        ax2.set_title('Bandwidth Comparison')
        ax2.set_xlabel('Simulation Run')
        ax2.set_ylabel('Bandwidth (Mbps)')
        ax2.legend()

        # Packet Loss Comparison
        ax3.plot(sim_range, [r['packet_loss'] for r in original_results], 'r-', label='Original', linewidth=2)
        ax3.plot(sim_range, [r['packet_loss'] for r in improved_results], 'g-', label='Improved', linewidth=2)
        ax3.set_title('Packet Loss Comparison')
        ax3.set_xlabel('Simulation Run')
        ax3.set_ylabel('Packet Loss Rate')
        ax3.legend()

        # Playback Success Comparison
        orig_success = [int(r['smooth_playback']) for r in original_results]
        impr_success = [int(r['smooth_playback']) for r in improved_results]
        
        x = np.arange(2)
        width = 0.35
        ax4.bar(x[0], sum(orig_success)/len(orig_success)*100, width, label='Original', color='red', alpha=0.7)
        ax4.bar(x[1], sum(impr_success)/len(impr_success)*100, width, label='Improved', color='green', alpha=0.7)
        ax4.set_title('Playback Success Rate')
        ax4.set_ylabel('Success Rate (%)')
        ax4.set_xticks(x)
        ax4.set_xticklabels(['Original', 'Improved'])
        ax4.legend()

        # Adjust layout and save
        plt.tight_layout()
        plt.savefig('simulation_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()