#!/usr/bin/env python3

import pyvisa
from time import sleep

dp8xx_resource = ""

# Get Resources
rm = pyvisa.ResourceManager()

# Check DP8 Connected
for resource in rm.list_resources():
    instrument = rm.open_resource(resource)
    if 'DP8' in instrument.query('*IDN?'):
        dp8xx_resource = resource

    instrument.close

if not dp8xx_resource:
    print("Failed to detect DP8")
    quit()

# Connect DP8
dp8xx = rm.open_resource(dp8xx_resource)

# Configure DP8
voltage = 2.4 # 2.4V
current = 0.5 # 500mA

dp8xx.write(':OUTP CH1,0')

dp8xx.write(':INST:NSEL 1')

dp8xx.write(':VOLT:PROT ' + str(voltage + 0.5))
dp8xx.write(':CURR:PROT ' + str(current + 0.5))
dp8xx.write(':VOLT:PROT:STAT 1')
dp8xx.write(':CURR:PROT:STAT 1')

dp8xx.write(':VOLT ' + str(voltage))
dp8xx.write(':CURR ' + str(current))

dp8xx.write(':OUTP CH1,1')

dp8xx = rm.close