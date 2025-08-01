import time

import SQL
import I2C
import datetime
i2c_addrs = [0x08]
if __name__ == "__main__":
    SQL.check_tables(len(i2c_addrs)*4)
    while True:
        log = ""
        for i in range(len(i2c_addrs)):
            data = I2C.get_data(i2c_addrs[i])
            dt = "a" + str(datetime.datetime.now())
            for j in range(4):
                log += str(data[j]) + "---"
                if data[j]:
                    SQL.new_data(i*4+j, dt)
        print(log)
        time.sleep(0.2)

