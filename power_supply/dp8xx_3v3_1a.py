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
voltage = 3.3 # 3.3V
current = 1 # 1A

dp8xx.write(':OUTPut CH1,0')

dp8xx.write(':INSTrument:NSELect 1')

dp8xx.write(':VOLTage:PROTection ' + str(voltage + 0.5))
dp8xx.write(':CURRent:PROTection ' + str(current + 0.5))
dp8xx.write(':VOLTage:PROTection:STATe 1')
dp8xx.write(':CURRent:PROTection:STATe 1')

dp8xx.write(':VOLTage ' + str(voltage))
dp8xx.write(':CURRent ' + str(current))

dp8xx.write(':OUTPut CH1,1')

dp8xx = rm.close