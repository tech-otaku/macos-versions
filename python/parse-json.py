#!/usr/bin/env python3

import json

try:
    with open("json/macos.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    print("File updated: " + data["updated"] + "\n")
    
    for _version in data["versions"]:
        print(_version["family"] + " " + _version["version"] + " " + _version["codename"] + "\n")

        print("    Announced: " + _version["announced"])
        print("    Initial Release: " + _version["released"] + "\n")

        print("    System Requirements:")
        for _requirement in _version["requirements"]:
            print("        " + _requirement)

        print("")

        print("    Releases:")
        print("        Version  Build   Darwin  Released")
        for _release in _version["releases"]:
            print("        " + _release["version"].ljust(9) + _release["build"].ljust(8) + _release["darwin"].ljust(8) + _release["released"])

        print("\n")

except FileNotFoundError as error_message:

    print(error_message)
