from machine import Pin, PWM
import utime as time


def do_led():
    pin2 = Pin(2, Pin.OUT)
    for i in range(1, 101):
        pin2.value(i % 2)
        time.sleep(0.2)


def do_pwm():
    led2 = PWM(Pin(2))
    led2.freq(1000)

    for _ in range(10):
        for i in range(0, 1024):
            led2.duty(i)
            time.sleep_ms(2)
            
        for i in range(1023, -1, -1):
            led2.duty(i)
            time.sleep_ms(2)


def main():
    # do_led()
    do_pwm()


if __name__ == "__main__":
    main()
