"""
    This file is the entry pint for the project

    This file was written by and is a property of Mojtaba Alkhalifah, a humble Software Engineering
    graduate form King Fahd University of Petroleum and Minerals.
"""
from time import sleep

from ledstrip import LedStrip


def main():
    """
        This is the main function of the program, it is used to avid any potential scope issues.
    """
    strip1 = LedStrip()

    try:
        print('Color wipe White.')
        strip1.color_wipe(255, 255, 255)  # white wipe
        sleep(5)
        strip2 = LedStrip()
        print('Color wipe red.')
        strip2.color_wipe(255, 0, 0)  # red wipe
        sleep(5)
        print('Color wipe green.')
        strip2.color_wipe(0, 255, 0)  # green wipe
        sleep(5)
        print('Color wipe blue.')
        strip2.color_wipe(0, 0, 255)  # blue wipe
        sleep(5)
        print('Testing unsupported color values.')
        strip2.color_wipe(0, 0, 256)  # blue wipe
        sleep(5)
        print('Color wipe Off.')
        strip1.color_wipe(0, 0, 0)
    except KeyboardInterrupt:
        strip1.color_wipe(0, 0, 0, 10)


if __name__ == "__main__":
    main()
