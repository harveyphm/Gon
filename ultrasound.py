import qwiic_ultrasonic
import time

def main():
    sensor = qwiic_ultrasonic.QwiicUltrasonic()

    if sensor.is_connected() == False:
        print("Sensor not connected. Check wiring.")
        return

    print("Sensor connected!")

    while True:
        distance = sensor.get_distance()
        if distance == None:
            print("Failed to read distance")
        else:
            print(f"Distance: {distance} cm")

        time.sleep(0.5)

if __name__ == '__main__':
    main()
