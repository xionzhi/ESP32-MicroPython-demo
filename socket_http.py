import machine
import urequests
import usocket as socket

def do_request(url: str):
    headers = {'user-agent': "I'm your father"}
    resp = urequests.get(url, headers=headers).json()
    print(f'response: {resp}')
    
def socket_http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(1024)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()

def http_server():
    pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]
    html = """<!DOCTYPE html>
    <html>
        <head> <title>ESP32 Pins</title> </head>
        <body> <h1>ESP32 Pins</h1>
            <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
        </body>
    </html>
    """
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    while True:
        cl, addr = s.accept()
        print('client connected from', addr)
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
        response = html % '\n'.join(rows)
        cl.send(response)
        cl.close()

if __name__ == "__main__":
    # do_request('http://45.32.40.94')
    # socket_http_get('http://45.32.40.94/')
    http_server()