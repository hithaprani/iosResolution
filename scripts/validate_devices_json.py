import json
import sys

def validate_devices_json(json_data):
    required_keys = [
        "deviceid", 
        "model", 
        "physicalHeigth", 
        "physicalWidth", 
        "scale", 
        "size", 
        "viewportHeight", 
        "viewportWidth"
    ]
    for device in json_data:
        for key in required_keys:
            if key not in device:
                print(f"Missing key: {key} in {device}")
                sys.exit(1)
        if not isinstance(device["deviceid"], list):
            print("deviceid must be a list.")
            sys.exit(1)
        if not isinstance(device["physicalHeigth"], int) or not isinstance(device["physicalWidth"], int):
            print("physicalHeigth and physicalWidth must be integers.")
            sys.exit(1)
        if not (isinstance(device["scale"], int) or isinstance(device["scale"], float)):
            print("scale must be an integer or a float.")
            sys.exit(1)
        if not (isinstance(device["size"], int) or isinstance(device["size"], float)):
            print("size must be an integer or a float.")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_devices_json.py <path_to_json>")
        sys.exit(1)

    json_path = sys.argv[1]

    try:
        with open(json_path) as f:
            data = json.load(f)
        validate_devices_json(data)
        print("Validation successful.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        sys.exit(1)
