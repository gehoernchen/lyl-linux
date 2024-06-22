#!/bin/python

import os
import subprocess

profile_name = os.environ.get('profile_name') if os.environ.get('profile_name') else None

if not profile_name:
    print("Profile Name unset.")
    while not profile_name:
        profile_name = input("Profile Name: ").strip()


run_args = ["-noLauncher", "-connect=altis.lyl.gg", "-port=2302", "-noSplash", "-world=empty", "-skipIntro", "-noPause", f"-Name=\"{profile_name}\""]

# run arma 3
run_cmd = ["steam", "-applaunch", "107410"] + run_args
subprocess.run(run_cmd, stdin=None, stdout=None, close_fds=True)
