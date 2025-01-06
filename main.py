import base64
import json
import re
import sys


def convert_to_dict(key: str) -> dict:
    base64code, server_info = key.split("@")
    base64code = base64code.replace("ss://", "")
    server_info = server_info.replace("/?outline=1", "")
    decoded = base64.b64decode(base64code).decode("utf-8")
    method, password = decoded.split(":")
    server_ip, server_port = server_info.split(":")
    converted_data = {
        "server": server_ip,
        "server_port": int(server_port),
        "local_port": 1080,
        "password": password,
        "method": method
    }
    return converted_data


def write_to_file(data: dict) -> None:
    file_name = "server_info.json"
    with open(file_name, "w") as file:
        file.write(json.dumps(data))
    print(f"Saved to file: {file_name}")


def main():
    try:
        assert sys.version_info >= (3, 10), "Need install Python 3 version 10 or more"
        outline_key = input("Enter you key here: ")
        matched = re.match(r"ss:\/\/\w+@((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}:\d{4,5}\/\?outline=1", outline_key)
        assert matched, "Invalid Outline key"
        converted = convert_to_dict(outline_key)
        write_to_file(converted)
    except AssertionError as error:
        print(f"Error: {error}", file=sys.stderr)


if __name__ == "__main__":
    main()
