import serial

# connect your serial port
serialPort = serial.Serial(
    port="COM3",
    baudrate=115200,
    bytesize=8,
    parity="N",
    stopbits=1,
    timeout=0.03)
paper_status=""
while paper_status=="":
    get_paper_roll_sensor_status = serialPort.write(b'\x10\x04\x02')
    paper_status = serialPort.read().hex()
print(paper_status)

# Print according to the hexadecimal value returned by the printer
if paper_status == "12":
    print('Ok')
elif paper_status == "32":
    print('Paper is out')
elif paper_status == "36":
    print('Hood is opened')
else:
    print('other unset values')
