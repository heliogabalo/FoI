python3 -c '
import fcntl, os

# _IO("L", 0) expande a 0x4C00 (19456 en decimal)
HWBUS_IOCRESET = 0x4C00 

try:
    fd = os.open("/dev/hwbusc", os.O_RDWR)
    fcntl.ioctl(fd, HWBUS_IOCRESET)
    print("IOCTL ejecutado con exito")
    os.close(fd)
except Exception as e:
    print(f"Error: {e}")
'