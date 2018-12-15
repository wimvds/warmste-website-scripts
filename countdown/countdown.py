import datetime
import time
import scrollphathd
from scrollphathd.fonts import font5x5

def displayTime(first, second):
    scrollphathd.clear()
    scrollphathd.write_string(
        '{:02d}:{:02d}'.format(first, second),
        x=0,  # Align to the left of the buffer
        y=0,  # Align to the top of the buffer
        font=font5x5,  # Use the font5x5 font we imported above
        brightness=BRIGHTNESS  # Use our global brightness value
    )
    if int(time.time()) % 2 == 0:
        scrollphathd.clear_rect(8, 0, 1, 5)
    scrollphathd.show()
    time.sleep(0.1)

def countdown(targetDateTime):
    timeLeft = targetDateTime - datetime.datetime.now()
    while timeLeft.seconds > 0:
        secondsLeft = timeLeft.seconds
        days = timeLeft.days
        hours, secondsLeft = divmod(secondsLeft, 3600)
        minutes, seconds = divmod(secondsLeft, 60)
        if days >= 1:
            hours += days * 24
        if hours >= 1:
            displayTime(hours, minutes)
        else:
            displayTime(minutes, seconds)
        timeLeft = targetDateTime - datetime.datetime.now()

def scrollMessage(message):
    scrollphathd.clear()  # Clear the display and reset scrolling to (0, 0)
    length = scrollphathd.write_string(message)  # Write out your message
    scrollphathd.show()  # Show the result
    time.sleep(0.5)  # Initial delay before scrolling

    length -= scrollphathd.width

    # Now for the scrolling loop...
    while length > 0:
        scrollphathd.scroll(1)  # Scroll the buffer one place to the left
        scrollphathd.show()  # Show the result
        length -= 1
        time.sleep(0.02)  # Delay for each scrolling step

    time.sleep(0.5)  # Delay at the end of scrolling

def main():
    scrollphathd.set_brightness(0.5)
    scrollphathd.rotate(180)
    scrollphathd.clear()

    countdown(datetime.datetime(2018, 12, 16, 18, 0, 0))
    scrollMessage("   KNALLEN!!!   ")
    countdown(datetime.datetime(2018, 12, 18, 18, 0, 0))
    scrollMessage("   STOPPEN!!!   ")

BRIGHTNESS = 0.3
main()
