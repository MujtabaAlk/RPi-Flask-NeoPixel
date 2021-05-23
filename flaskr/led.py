from flask import (
    Blueprint, render_template
)

from flaskr.auth import login_required, load_logged_in_user
from flaskr.ledstrip import LedStrip

bp = Blueprint('led', __name__, url_prefix='/led')
# Initialize LED strip
strip = LedStrip()
print('Color wipe Off.')
strip.color_wipe(0, 0, 0)

bp.before_request(load_logged_in_user)


# routes/pages to control LED strip
@bp.route('/white')
@login_required
def strip_white():
    led_strip = LedStrip()
    print('Color wipe white.')
    led_strip.color_wipe(255, 255, 255)  # white wipe
    return render_template('led/color.html', color='white')


@bp.route('/red')
@login_required
def strip_red():
    led_strip = LedStrip()
    print('Color wipe red.')
    led_strip.color_wipe(255, 0, 0)  # red wipe
    return render_template('led/color.html', color='red')


@bp.route('/green')
@login_required
def strip_green():
    led_strip = LedStrip()
    print('Color wipe green.')
    led_strip.color_wipe(0, 255, 0)  # green wipe
    return render_template('led/color.html', color='green')


@bp.route('/blue')
@login_required
def strip_blue():
    led_strip = LedStrip()
    print('Color wipe blue.')
    led_strip.color_wipe(0, 0, 255)  # blue wipe
    return render_template('led/color.html', color='blue')


@bp.route('/rainbow')
@login_required
def strip_rainbow():
    led_strip = LedStrip()
    print('Rainbow.')
    led_strip.rainbow()  # rainbow
    return render_template('led/color.html', color='rainbow')


@bp.route('/off')
@login_required
def strip_off():
    led_strip = LedStrip()
    print('Color wipe off.')
    led_strip.color_wipe(0, 0, 0)  # off wipe
    return render_template('led/color.html', color='off')
