from datetime import datetime

# --------------------------------------------------
# Helper function
# Converts ISO 8601 timestamp to milliseconds
# Example: "2023-09-01T10:15:30Z" -> 1693563330000
# --------------------------------------------------
def iso_to_milliseconds(iso_time):
    # Replace 'Z' with '+00:00' so Python can parse it on Windows
    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


# --------------------------------------------------
# IMPLEMENT: Transform data format 1
# This format already uses milliseconds
# --------------------------------------------------
def transform_format_1(data):
    return {
        "deviceId": data["deviceId"],
        "timestamp": data["timestamp"],
        "telemetry": data["telemetry"]
    }


# --------------------------------------------------
# IMPLEMENT: Transform data format 2
# This format uses ISO timestamp (needs conversion)
# --------------------------------------------------
def transform_format_2(data):
    return {
        "deviceId": data["device_id"],
        "timestamp": iso_to_milliseconds(data["time"]),
        "telemetry": data["values"]
    }
