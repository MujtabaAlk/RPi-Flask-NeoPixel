"""
    This file is the entry pint for the project
    (currently it is being used for testing purposes).
     This file was written by and is a property of Mojtaba Alkhalifah, a humble Software Engineering
    graduate form King Fahd University of Petroleum and Minerals.
"""
from time import sleep

from flaskr.ledstrip import LedStrip


def main():
    """
        This is the main function of the program, it is used to avid any potential scope issues.
    """
    strip1 = LedStrip()

    try:
        print('Color wipe White.')
        strip1.color_wipe(255, 255, 255)  # white wipe
        sleep(5)
        print('running rainbow')
        strip1.rainbow()
        sleep(5)
        print('clearing')
        strip1.color_wipe(0, 0, 0, 10)

    except KeyboardInterrupt:
        strip1.color_wipe(0, 0, 0, 10)


if __name__ == "__main__":
    main()
