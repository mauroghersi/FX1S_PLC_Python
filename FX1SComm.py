import serial

ser = serial.Serial('COM10', 9600, serial.SEVENBITS, serial.PARITY_EVEN, serial.STOPBITS_ONE)

#values = bytearray([2, 48, 49, 48, 48, 48, 48, 50, 3, 53, 54])
#enq = b'\x05'
#ser.write(enq)
#ser.write(values)

while True:
    #data = ser.read()
    #print(data)
    command = input("/>")
    
    if (command == "d0"):
        values = bytearray([2, 48, 49, 48, 48, 48, 48, 50, 3, 53, 54])
        ser.write(values)
        data = ser.read(8)
        print(data)

    if (command == "enq"):
        enq = b'\x05'
        ser.write(enq)
        data = ser.read()
        print(data)

    if (command == "y0on"):
        values = bytearray([2, 55, 56, 48, 48, 57, 3, 48, 66])
        ser.write(values)
        data = ser.read()
        print(data)

    if (command == "y0off"):
        values = bytearray([2, 56, 56, 48, 48, 57, 3, 48, 67])
        ser.write(values)
        data = ser.read()
        print(data)

    
