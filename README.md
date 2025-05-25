# Video Streaming Transport Protocol

This project implements a custom transport protocol designed specifically for video streaming applications. The protocol addresses varying network conditions, minimizes jitter, and ensures smooth playback, making it suitable for real-time video delivery.

## Project Structure

` ` `
video-streaming-transport-protocol
├── src
│   ├── main.py
│   ├── protocol
│   │   ├── __init__.py
│   │   └── transport_protocol.py
│   ├── simulation
│   │   ├── __init__.py
│   │   └── network_simulator.py
│   └── utils
│       └── metrics.py
├── tests
│   ├── test_protocol.py
│   └── test_simulation.py
├── requirements.txt
├── README.md
└── report
    └── transport_protocol_report.pdf
` ` `

## Features

- **Adaptive Bitrate Streaming**: The protocol dynamically adjusts the streaming bitrate based on current network bandwidth to optimize playback quality.
- **Packet Loss Handling**: Implements strategies to recover from packet loss, ensuring minimal disruption to the streaming experience.
- **Jitter Minimization**: Processes incoming packets to reduce jitter, providing a smoother playback experience.

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd video-streaming-transport-protocol
pip install -r requirements.txt
```

## Usage

To run the video streaming simulation, execute the main script:

```bash
python src/main.py
```

This will initialize the transport protocol and start the simulation under various network conditions.

## Testing

Unit tests are provided to ensure the functionality of both the transport protocol and the network simulator. To run the tests, use:

```bash
pytest tests/
```

## Report

A comprehensive report detailing the design, implementation, and evaluation of the transport protocol can be found in the `report` directory as `transport_protocol_report.pdf`. This document includes challenges faced during development and the solutions implemented.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.
