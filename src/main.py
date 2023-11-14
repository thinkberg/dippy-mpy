from machine import RTC

import time
import network
import ntptime

import ledmatrix
import framebuf


class Display:
    _buf = None
    fb = None

    def __init__(self):
        self._buf = bytearray(64 * 64 * 2)
        self.fb = framebuf.FrameBuffer(self._buf, 64, 64, framebuf.RGB565)

    def show(self):
        ledmatrix.show(self._buf)


def localtime():
    '''https://github.com/orgs/micropython/discussions/11173'''
    year = time.localtime()[0]  # get current year
    hh_march = time.mktime(
        (year, 3, (31 - (int(5 * year / 4 + 4)) % 7), 1, 0, 0, 0, 0, 0))  # Time of March change to CEST
    hh_october = time.mktime(
        (year, 10, (31 - (int(5 * year / 4 + 1)) % 7), 1, 0, 0, 0, 0, 0))  # Time of October change to CET
    now = time.time()
    if now < hh_march:  # we are before last sunday of march
        cet = time.localtime(now + 3600)  # CET:  UTC+1H
    elif now < hh_october:  # we are before last sunday of october
        cet = time.localtime(now + 7200)  # CEST: UTC+2H
    else:  # we are after last sunday of october
        cet = time.localtime(now + 3600)  # CET:  UTC+1H
    return cet


def main():
    (ssid, password) = credentials["network"]

    nic = network.WLAN(network.STA_IF)
    if not nic.isconnected():
        nic.active(True)
        nic.connect(ssid, password)
        while not nic.isconnected():
            pass
    else:
        print("Already connected")

    print("Connection successful")
    print(nic.ifconfig())

    rtc = RTC()
    ntptime.settime()
    (year, month, day, weekday, hours, minutes, seconds, subseconds) = rtc.datetime()
    print("UTC Time: ")
    print((year, month, day, hours, minutes, seconds))

    # initialize the LED display
    ledmatrix.init(io_colors=(25, 26, 27, 14, 12, 13),
                   io_rows=(23, 19, 5, 17, 18), io_clk=16,
                   io_oe=15, io_lat=4, width=64)
    ledmatrix.set_brightness(62)

    display = Display()
    color = 0xffff

    while True:
        t = localtime()
        (year, month, day, hour, minute, seconds) = t[0:6]
        display.fb.fill(0)
        display.fb.rect(0, 0, 64, 64, 0xff20)
        display.fb.text(f"{day:02d}.{month:02d}.{year:04d}", 0, 24, color)
        display.fb.text(f"{hour:02d}:{minute:02d}:{seconds:02d}", 0, 34, color)
        display.show()
        time.sleep(0.1)


if __name__ == '__main__':
    main()
