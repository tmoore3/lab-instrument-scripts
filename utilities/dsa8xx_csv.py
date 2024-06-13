#!/usr/bin/python3

import pyvisa
from time import sleep
import argparse
import os

# Set default arguments
trace = 1
filename = "trace.csv"

# Parse filename if provided
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', type=str, help='Specified filename.')
parser.add_argument('-t', '--trace', type=int, help='Specified trace.')
args = parser.parse_args()

if args.filename:
    filename, file_extension = os.path.splitext(args.filename)
    if file_extension:
        filename = filename + ".csv"
    else:
        filename = args.filename + ".csv"

if args.trace:
        trace = args.trace

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
dsa8xx.write(':MMEMory:STORe:TRACe TRACE' + str(trace) +',E:\\' + filename)
sleep(10);

# Disconnect DSA8
dsa8xx.close
