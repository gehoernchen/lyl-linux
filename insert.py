#!/bin/python

from pathlib import Path

import os
import vdf
import config

steam_path_libraryfolders_vdf = f"{str(Path.home())}/.steam/root/steamapps/libraryfolders.vdf"
connection_log_path_pfx = "drive_c/Program Files (x86)/Steam/logs/connection_log.txt"
arma3_app_id = "107410"

user_steam_id = config.user_steam_id

def find_app_path(libraryfolders_vdf_path, app_id_to_search):
    with open(libraryfolders_vdf_path, 'r') as file:
        data = vdf.parse(file)
        libraryfolders = data['libraryfolders']
        for key in libraryfolders:
            if key.isdigit():
                apps = libraryfolders[key].get('apps', {})
                if app_id_to_search in apps:
                    return f"{libraryfolders[key]['path']}/steamapps/compatdata/{app_id_to_search}/pfx"
    return None


def create_connection_log(steam_id, arma3_id, libraryfolders_vdf_path, relative_connection_log_path):
    pfx_path = find_app_path(libraryfolders_vdf_path, arma3_id)

    if not os.path.exists(pfx_path):
        print(f"Could not find prefix path at {pfx_path}!")
        exit(1)

    absolute_path_to_connection_log = f"{pfx_path}{os.sep}{relative_connection_log_path}"

    if not os.path.exists(os.path.dirname(absolute_path_to_connection_log)):
        os.makedirs(os.path.dirname(absolute_path_to_connection_log))

    connection_log = open(absolute_path_to_connection_log, "w")
    connection_log.write(f"RecvMsgClientLogOnResponse() : {steam_id}")
    connection_log.close()


def main():
    global user_steam_id
    while not user_steam_id:
        user_steam_id = input("No Steam ID set. Enter Steam3 ID (e.g. https://steamdb.info/calculator/): ").strip()

    create_connection_log(user_steam_id, arma3_app_id, steam_path_libraryfolders_vdf, connection_log_path_pfx)
    print("Wrote to file, open launcher now.")


if __name__ == '__main__':
    main()
