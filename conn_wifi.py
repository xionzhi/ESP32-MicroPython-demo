import ubinascii
import network
import utime as time

WAIT_MAX, ESSID, PASSWORD = 15, '202', '8-1-202-11'

def do_connect(essid=None, passwd=None):
    if not essid or not passwd:
        essid, passwd = ESSID, PASSWORD
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ESSID, PASSWORD)
        i = 1
        while not wlan.isconnected():
            if i > WAIT_MAX:
                return
            print(f"connecting...count: {i}")
            i += 1
            time.sleep(1)
    wlan_mac = ubinascii.hexlify(wlan.config('mac')).decode()
    print('wlan_conf:', wlan.ifconfig(), wlan_mac.upper())

if __name__ == "__main__":
    do_connect()