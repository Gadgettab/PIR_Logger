#!/usr/bin/env python
# coding: utf8

from smbus3 import SMBus
import time


def get_data(addr):
    with SMBus(3) as bus:
        value = []
        for chanel in range(4):
            bus.write_byte(addr, chanel)
            value.append(bus.read_byte(addr))
        return value

