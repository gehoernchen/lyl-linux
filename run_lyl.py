#!/bin/python

import os
import subprocess

import insert
import config

protontricks_command = config.protontricks_command
lyl_executable_path = config.lyl_executable_path

if not protontricks_command:
    print("Protontricks command unset.")
    exit(1)

if not lyl_executable_path:
    print("Lyl launcher executable path unset.")
    exit(1)

# run lyl launcher
lyl_run_cmd = [f"{protontricks_command} -c 'wine {lyl_executable_path}' {insert.arma3_app_id}"]
subprocess.Popen(lyl_run_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)