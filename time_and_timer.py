import utime as time
from machine import Timer

def sleep_time():
    time.sleep(1)           # 睡眠1秒
    time.sleep_ms(500)      # 睡眠500毫秒
    time.sleep_us(10)       # 睡眠10微妙
    start = time.ticks_ms() # 获取毫秒计时器开始值
    delta = time.ticks_diff(time.ticks_ms(), start) # 计算从开始到当前时间的差值
    print(delta)

def setting_timer():
    print(dir(Timer))
    tim0 = Timer(0)
    tim0.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(0))
    # tim1 = Timer(1)
    # tim1.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(1))
    # tim2 = Timer(2)
    # tim2.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))
    # tim3 = Timer(3)
    # tim3.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(3))

if __name__ == "__main__":
    sleep_time()
    setting_timer()