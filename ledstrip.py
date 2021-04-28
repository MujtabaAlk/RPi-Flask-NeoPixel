"""
    This is a module that houses a singleton class that houses the led strand object
"""

from time import sleep

from rpi_ws281x.rpi_ws281x import Adafruit_NeoPixel, Color

# LED strip configuration:
LED_COUNT = 16  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10          # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53


class LedStrip:
    """
        This is a singleton class that contains a single instance of Adafruit_NeoPixel.
        It is designed in a singleton pattern to avoid potential hardware issues that might arise
        form having more than one instance of Adafruit_NeoPixel running at a time.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating object')
            cls._instance = super(LedStrip, cls).__new__(cls)
            # Create NeoPixel object with appropriate configuration.
            print('Initializing strip')
            cls._strip = Adafruit_NeoPixel(
                LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL
            )
            # Initialize the library (must be called once before other functions).
            cls._strip.begin()

        return cls._instance

    def color_wipe(self, red_intensity, green_intensity, blue_intensity, wait_ms=50):
        """
            this function displays the specified color on the led strip by wiping it pixel by pixel.
            :param red_intensity: intensity of red component of the color
            :param green_intensity: intensity of green component of the color
            :param blue_intensity: intensity of blue component of the color
            :param wait_ms: time delay between changing each pixel/led
        """
        if (not 0 <= red_intensity <= 255 or
                not 0 <= green_intensity <= 255 or
                not 0 <= blue_intensity <= 255):
            print('\033[91mError: intensity values must be between 0 & 255\033[0m')
            return
        color = Color(red_intensity, green_intensity, blue_intensity)
        # Wipe color across display a pixel at a time.
        for i in range(self._strip.numPixels()):
            self._strip.setPixelColor(i, color)
            self._strip.show()
            sleep(wait_ms / 1000.0)
