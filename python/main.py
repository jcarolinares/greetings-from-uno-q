# SPDX-FileCopyrightText: Copyright (C) 2025 ARDUINO SA <http://www.arduino.cc>
#
# SPDX-License-Identifier: MPL-2.0

from arduino.app_utils import *
import time
import datetime

while True:
    print("Time is: ", datetime.datetime.utcnow())
    Bridge.call("greet")
    time.sleep(20)


