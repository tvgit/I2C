#!/usr/bin/python
#
# TCA9548_I2C_Multiplexer
# Use TCA9548A to multiplex I2C channels with python and raspberry pi.
#
# based on: https://github.com/NNebus/TCA9548A-I2C-Multiplexter-Test/blob/master/TCA9548_I2C_Multiplexer.py
# which does not work with python 2.7. (Don't know if it works with python 3.x).
#
# vs 0.1
# tested with:
#
#  > lsb_release -a
#  No LSB modules are available.
#  Distributor ID:	Raspbian
#  Description:	Raspbian GNU/Linux 9.1 (stretch)
#  Release:	9.1
#  Codename:	stretch
#  > cat /proc/device-tree/model
#  Raspberry Pi 2 Model B Rev 1.1
#
# python 2.7 does not know the type 'byte'. 
# See: https://stackoverflow.com/questions/10814483/changing-string-to-byte-type-in-python-2-7
#
# usage:
# sudo ./TCA9548A.py 0
#
#
# HowTo
# 1. Connect device to channel:
#       sudo i2cdetect -y 1 will show channel of TCA9548A (0x70) and of device
# 2. set_TCA9548_channel(ch)  # 0 <= ch <= 7
# 3. call device as usual with its original (!) channel (not 0x70)
#

import smbus   # only on Raspberry
import time
import sys

TCA9548A_I2C_address    = 0x70
TCA9548A_I2C_bus_number = 1

I2C_channel = []
I2C_channel.append(0b00000001)
I2C_channel.append(0b00000010)
I2C_channel.append(0b00000100)
I2C_channel.append(0b00001000)
I2C_channel.append(0b00010000)
I2C_channel.append(0b00100000)
I2C_channel.append(0b01000000)
I2C_channel.append(0b10000000)


def set_TCA9548_channel(new_i2c_channel, test = False):
    bus = smbus.SMBus(TCA9548A_I2C_bus_number)
    if test:
        print type(new_i2c_channel), new_i2c_channel, '\n'
        for idx, val in enumerate(I2C_channel): print idx, val
        print "\nchannel = ", I2C_channel[new_i2c_channel], '\n'
    bus.write_byte(TCA9548A_I2C_address, I2C_channel[new_i2c_channel])
    time.sleep(0.1)
    print "TCA9548A I2C channel:", bin(bus.read_byte(TCA9548A_I2C_address))

if __name__ == "__main__":
    set_TCA9548_channel(int(sys.argv[1]))

