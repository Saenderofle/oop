import turtle
import time
from dial import Dial
from hand import Hand

def update_time(hour_hand, minute_hand, second_hand):
    while True:
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        second_angle = seconds * 6
        minute_angle = minutes * 6 + seconds * 0.1
        hour_angle = hours * 30 + minutes * 0.5

        second_hand.update(second_angle)
        minute_hand.update(minute_angle)
        hour_hand.update(hour_angle)

        time.sleep(1)

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    screen.title("Analog Clock")

    dial = Dial()
    dial.draw()

    hour_hand = Hand(length=7, width=0.3, color="black")
    minute_hand = Hand(length=10, width=0.2, color="blue")
    second_hand = Hand(length=12, width=0.1, color="red")

    update_time(hour_hand, minute_hand, second_hand)

    screen.mainloop()
