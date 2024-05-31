#!/usr/bin/env python3
import pyvisa

rm = pyvisa.ResourceManager()

usb_attached_instruments = []
network_attached_instruments = []

for resource in rm.list_resources():
    instrument = rm.open_resource(resource)

    if 'USB' in resource:
        usb_attached_instruments.append(instrument.query('*IDN?'))

    if 'TCPIP' in resource:
        network_attached_instruments.append(instrument.query('*IDN?'))

    instrument.close

print('USB Attached Instruments:')

if usb_attached_instruments:
    for instrument in usb_attached_instruments:
        print('\t' + instrument)
else:
    print('\tNone\n')

print('Network Attached Instruments:')
if network_attached_instruments:
    for instrument in network_attached_instruments:
        print('\t' + instrument)
else:
    print('\tNone\n')