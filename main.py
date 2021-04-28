"""
This file should be the entry pint for the project

This file was written by and is a property of Mujtaba Alkhalifah, a humble Software Engineering graduate form King Fahd University of Petroleum and Minerals

"""
from time import sleep

from rpi_ws281x import Color

from ledstrip import LedStrip


def main():
    strip1 = LedStrip()

    try:
        print('Color wipe White.')
        strip1.color_wipe(Color(255, 255, 255))  # white wipe
        sleep(10)
        strip2 = LedStrip()
        print('Color wipe red.')
        strip2.color_wipe(Color(255, 0, 0))  # red wipe
        sleep(10)
        print('Color wipe green.')
        strip2.color_wipe(Color(0, 255, 0))  # green wipe
        sleep(10)
        print('Color wipe blue.')
        strip2.color_wipe(Color(0, 0, 255))  # blue wipe
        sleep(10)
        print('Color wipe Off.')
        strip1.color_wipe(Color(0, 0, 0))
    except KeyboardInterrupt:
        strip1.color_wipe(Color(0, 0, 0), 10)


if __name__ == "__main__":
    main()
