import os
import fcntl
import termios
import struct

async def get_dash():
    try:
        fd = os.open('/dev/tty', os.O_RDONLY)
        
        size = struct.unpack('HH', fcntl.ioctl(fd, termios.TIOCGWINSZ, b'\0' * 4))
        os.close(fd)
        
        print ("-" * (size[1]))
    except Exception as e:
        print("\n\n")
        