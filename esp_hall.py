import esp
import esp32

# print('esp:', dir(esp))
# print('esp32:', dir(esp32))

def printer_flash_capacity():
    print(f'flash_size: {esp.flash_size() / 1024 / 1024} MB')

def printer_temperature():
    f_temperature = esp32.raw_temperature()
    c_temperature = round((f_temperature - 32) / 1.8, 1)
    print(f'hall_raw_temperature: {f_temperature}°F, {c_temperature}°C')

if __name__ == "__main__":
    printer_flash_capacity()
    printer_temperature()