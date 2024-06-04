#!/bin/bash

# please provide the path to the file extract_transform.py and selenium_load_2020.py
selenium_path="C:\Users\asude\Desktop\FAU Summer Semester 2024\MADE\FAU-MADE\project\selenium_load_2020.py"
extract_transform_path="C:\Users\asude\Desktop\FAU Summer Semester 2024\MADE\FAU-MADE\project\extract_transform.py"

python "$selenium_path"
python "$extract_transform_path"