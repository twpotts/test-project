# Import packages

import datetime as dt
import pytz
import time
from deta import Deta

# Global variables (using key for secondary email)

start_time = time.time()
local_tz = pytz.timezone("US/Central")
DETA_KEY = "b089hdga_o15KWFgyzXyJs3SuuPh7YuuUaa3uVWAL"
deta = Deta(DETA_KEY)
test_db = deta.Base("test_db")
active = bool(test_db.get("active")['value'])

# Run in loop

if active:
    print("Active")
    while active:
        stamp = dt.datetime.now(tz=local_tz).strftime("%X %d-%m-%Y")
        deta = Deta(DETA_KEY)
        test_db = deta.Base("test_db")
        test_db.put({"key": "Datetime1", "value": stamp})
        active = bool(test_db.get("active")['value'])
        end_time = time.time()
        total_time_sec = round(end_time - start_time, 0)
        total_time_min = round(total_time_sec / 60, 2)
        total_time_hour = round(total_time_min / 60, 4)
        print(f"{stamp}, running for {total_time_sec} seconds / {total_time_min} minutes / {total_time_hour} hours")
        time.sleep(1)
if not active:
    print("Not active")