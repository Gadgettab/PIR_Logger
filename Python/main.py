import time
import SQL
import serial
import datetime
i2c_addrs = [0x08, 0x09]
UART_addrs = ["/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyUSB2", "/dev/ttyUSB3"]
if __name__ == "__main__":
    SQL.check_tables(len(UART_addrs)*8)

    arduines = []
    for i in range(len(UART_addrs)):
        try:
            ser = serial.Serial(UART_addrs[i], 9600, timeout=1)
            print(f"Arduino on port {UART_addrs[i]} started!")
            arduines.append(ser)
        except serial.SerialException:
            print(f"Port {UART_addrs[i]} is offline!")
            arduines.append("None")
    time.sleep(2)
    while True:
        for i in range(len(UART_addrs)):
            if arduines[i] != "None":
                print()
                print(f"{UART_addrs[i]}: ", end="")
                for j in range(8):
                    arduines[i].write(f"{j}".encode('utf-8'))
                    val = int(arduines[i].readline().decode("utf-8").rstrip())
                    print(val, end="")
                    if val:
                        dt = "a" + str(datetime.datetime.now())
                        SQL.new_data(i * 8 + j, dt)

