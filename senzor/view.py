def format_radiation_data(data):
    return {
        "timestamp": data.timestamp,
        "radiation_level": data.level
    }