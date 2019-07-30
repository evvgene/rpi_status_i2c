import os
import time
import RPi_I2C_driver
import psutil

mylcd = RPi_I2C_driver.lcd()

def pi_temp():
	temp = os.popen("vcgencmd measure_temp").readline()
	return (temp)

def ram_load():
    mem = psutil.virtual_memory()
    mem_list=list(mem)
    return ("RAM " + str(mem_list[2]) + "%")

def cpu_load():
    load = psutil.cpu_percent(interval=1)
    return ("CPU " + str(load) + "%")

def rom_load():
    rom = psutil.disk_usage('/')
    rom_list = list(rom)
    return ("ROM " + str(rom_list[3]) + "%")

while True:
    mylcd.lcd_display_string (pi_temp(),  1)
    mylcd.lcd_display_string (cpu_load(), 2)
    mylcd.lcd_display_string (ram_load(), 3)
    mylcd.lcd_display_string (rom_load(), 4)
    time.sleep(2)