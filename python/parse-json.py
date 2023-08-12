#!/usr/bin/env python3

# NOTE: f-strings require Python 3.6 or later

import json

def printKey(indent):
    print("Key:")
    for _key in data["key"]:

        print(f'{indent}{_key}')
    print('')

try:
    indent='   '

    with open("json/macos.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    printKey(indent)

    print(f'File updated: {data["updated"]}\n')
    
    for _version in data["versions"]:
        print(f'{_version["family"]} {_version["version"]} {_version["external"]}\n')

        print(f'{indent}Internal Codename: {_version["internal"]}')
        print(f'{indent}Announced: {_version["announced"]}')
        print(f'{indent}Initial Release: {_version["released"]}\n')

        print(f'{indent}Platform(s):')
        for _platform in _version["platforms"]:
            print(f'{indent}{indent}{_platform}')

        print('')

        print(f'{indent}System Requirements:')
        for _requirement in _version["requirements"]:
            print(f'{indent}{indent}{_requirement}')

        print('')

        print(f'{indent}Releases:')
        print(f'{indent}{indent}Version  Platform        Build      Darwin  Kernel                   Released')
        for _release in _version["releases"]:
            platform = ''
            for _platform in _release["platforms"]:
                platform += f'{_platform}, '
            print(f'\
{indent}{indent}\
{_release["version"].ljust(9)}\
{platform[:len(platform) - 2].ljust(16)}\
{_release["build"].ljust(11)}\
{_release["darwin"].ljust(8)}\
{_release["kernel"].ljust(25)}\
{_release["released"]}\
            ')

        print('\n')

    printKey(indent)

except FileNotFoundError as error_message:

    print(error_message)
