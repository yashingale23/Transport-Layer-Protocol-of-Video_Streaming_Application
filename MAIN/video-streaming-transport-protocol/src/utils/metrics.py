def calculate_buffer_size(data_rate, duration):
    return data_rate * duration

def measure_playback_smoothness(playback_data):
    if not playback_data:
        return 0
    smoothness = sum(playback_data) / len(playback_data)
    return smoothness