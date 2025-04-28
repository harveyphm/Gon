from gpiozero import Servo
import keyboard
import time

# Use PiGPIOFactory backend for better accuracy
# Define Servo object
servo = Servo(18, min_pulse_width=0.001, max_pulse_width=0.002,frame_width=0.02)

try:
    print("Control the motor with UP and DOWN arrows. Press Ctrl+C to quit.")

    while True:
        if keyboard.is_pressed('down'):
            print("Moving Down")
            servo.value = 0.15  # 15% Forward
        elif keyboard.is_pressed('up'):
            print("Moving Up")
            servo.value = -0.20  # 20% Reverse
        else:
            print("Stopping")
            servo.value = 0  # Neutral (Stop)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program stopped by user.")

finally:
    # Detach the servo (stop PWM)
    servo.detach()
