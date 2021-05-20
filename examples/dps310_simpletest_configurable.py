# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_dps310.dps310_configurable import DPS310_Configurable

i2c = board.I2C()  # uses board.SCL and board.SDA
dps310 = DPS310_Configurable(i2c)

while True:
    print("Temperature = %.2f *C" % dps310.temperature)
    print("Pressure = %.2f hPa" % dps310.pressure)
    print("")
    time.sleep(1.0)
