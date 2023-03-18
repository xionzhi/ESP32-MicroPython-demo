from microWebSrv import MicroWebSrv
from machine import Pin

# My handler

def handlerFunc_test_get(httpClient, httpResponse, routeArgs=None):
    print(httpClient.GetRequestQueryParams())
    u_name = httpClient.GetRequestQueryParams().get('name')
    resp = {'message': f'hello world {u_name}', 'status': 0}
    httpResponse.WriteResponseJSONOk(headers = None,
                                     obj     = resp)

def handlerFunc_test_post(httpClient, httpResponse, routeArgs=None):
    print(httpClient.GetRequestHeaders())
    print(httpClient.GetRequestContentType())
    print(httpClient.ReadRequestPostedFormData())
    print(httpClient.ReadRequestContentAsJSON())
    resp = {'message': 'hello world', 'status': 0}
    httpResponse.WriteResponseJSONOk(headers = None,
                                     obj     = resp)
    
def handlerFunc_led_get(httpClient, httpResponse, routeArgs=None):
    params = httpClient.GetRequestQueryParams()
    pin = int(params.get('pin', 2))
    value = int(params.get('value', 1))

    pin2 = Pin(pin, Pin.OUT)
    pin2.value(1 if value else 0)
    
    resp = {f'pin{pin}': pin2.value()}
    httpResponse.WriteResponseJSONOk(headers = None,
                                     obj     = resp)

routeHandlers = [
    ('/test', 'GET', handlerFunc_test_get),
    ('/test', 'POST', handlerFunc_test_post),
    
    ('/led',  'GET', handlerFunc_led_get),
]

def run_web_server():
    srv = MicroWebSrv(routeHandlers=routeHandlers,
                      port=80,
                      bindIP='0.0.0.0',
                      webPath='/')
    srv.MaxWebSocketRecvLen     = 256
    srv.WebSocketThreaded       = False
    srv.Start(threaded=False)

if __name__ == "__main__":
    run_web_server()