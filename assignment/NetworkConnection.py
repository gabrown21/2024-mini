import network
import time


SSID = 'dawgs on three'
PASSWORD = 'bumen10s'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)


if wlan.isconnected():
    print('Connected to Wi-Fi')
    print('Network configuration:', wlan.ifconfig())
else:
    print('Failed to connect to Wi-Fi')