#!/usr/bin/env python3

import json

try:
    with open("json/macos.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    print("Key:")
    for _key in data["key"]:
        print("    " + _key)
    print("")

    print("File updated: " + data["updated"] + "\n")
    
    for _version in data["versions"]:
        print(_version["family"] + " " + _version["version"] + " " + _version["codename"] + "\n")

        print("    Announced: " + _version["announced"])
        print("    Initial Release: " + _version["released"] + "\n")

        print("    Platform(s):")
        for _platform in _version["platforms"]:
            print("        " + _platform)

        print("")

        print("    System Requirements:")
        for _requirement in _version["requirements"]:
            print("        " + _requirement)

        print("")

        print("    Releases:")
        print("        Version  Build      Darwin  Kernel                Released")
        for _release in _version["releases"]:
            print("        " + _release["version"].ljust(9) + _release["build"].ljust(11) + _release["darwin"].ljust(8) + _release["kernel"].ljust(22)+ _release["released"])

        print("\n")

    print("Key:")
    for _key in data["key"]:
        print("    " + _key)

except FileNotFoundError as error_message:

    print(error_message)
