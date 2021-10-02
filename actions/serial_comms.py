from time import sleep

def write_serial(context, message):
    message += "\r\n"
    context.ser.write(message.encode())
    sleep(0.1)

def read_serial(context):
    return (context.ser.read_all()).decode('ascii')