#!/usr/bin/python3

import pyvisa
from time import sleep
import argparse
import os

# Set default arguments
filename = "screen.bmp"

# Parse filename if provided
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', type=str, help='Specified filename.')
args = parser.parse_args()

if args.filename:
    filename, file_extension = os.path.splitext(args.filename)
    if file_extension:
        filename = filename + ".bmp"
    else:
        filename = args.filename + ".bmp"

dsa8xx_resource = ""

# Get Resources
rm = pyvisa.ResourceManager()

# Check DSA8 Connected
for resource in rm.list_resources():
    instrument = rm.open_resource(resource)
    if 'DSA8' in instrument.query('*IDN?'):
        dsa8xx_resource = resource

    instrument.close

if not dsa8xx_resource:
    print("Failed to detect DSA8")
    quit()

# Connect DSA8
dsa8xx = rm.open_resource(dsa8xx_resource)

# Take Screen Shot
dsa8xx.write(':MMEMory:STORe:SCReen E:\\' + filename)
sleep(15);

# Disconnect DSA8
dsa8xx.close