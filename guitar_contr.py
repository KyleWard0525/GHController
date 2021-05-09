import RPi.GPIO as GPIO
import time

# Buttons on guitar controller
buttonPins = {

    "btnGreen": 5,
    "btnRed": 6,
    "btnYellow": 13,
    "btnBlue": 19,
    "btnOrange": 26,
    "slider": 27,
}

# Validation LEDs
ledPins = {
    
    "ledGreen": 12,
    "ledRed": 16,
    "ledYellow": 20,
    "ledBlue": 21,
    "rgbRed": 18,
    "rgbGreen": 23,
    "rgbBlue": 24,
}

# Listen for and handle button press events
def handleButtonPress():
    while True:
        for button in buttonPins:
            if GPIO.input(buttonPins[button]) == 0:
                
                #Check which led to light up
                
                # Green
                if button == "btnGreen":
                    turnOn(ledPins["ledGreen"])
                    
                # Red 
                elif button == "btnRed":
                    turnOn(ledPins["ledRed"])
                
                # Yellow
                elif button == "btnYellow":
                    turnOn(ledPins["ledYellow"])
                   
                # Blue
                elif button == "btnBlue":
                    turnOn(ledPins["ledBlue"])
                
                # Orange
                else:
                    blinkOrange()
            
            # Disable LED's
            else:
                cleanup()

# Turn on given LED
def turnOn(ledPin):
    GPIO.output(ledPin, GPIO.HIGH)

# Cleanup program resources
def cleanup():
    
    # Set all LEDs to low
    for ledPin in ledPins:
        GPIO.output(ledPins[ledPin], GPIO.LOW)

# Set up controller
def setup():
    GPIO.setmode(GPIO.BCM)

    # Set buttons as input
    for button in buttonPins:
        GPIO.setup(buttonPins[button], GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Set LED's as output
    for ledPin in ledPins:
        GPIO.setup(ledPins[ledPin], GPIO.OUT)

# Blink orange to the RGB led by mixing red and green
def blinkOrange():
    GPIO.output(ledPins["rgbRed"], GPIO.HIGH)
    GPIO.output(ledPins["rgbGreen"], GPIO.HIGH)

# End program
def destroy():
    GPIO.output(ledPin, GPIO.HIGH)
    GPIO.cleanup()

# Main Method
def main():
    handleButtonPress()


# Driver code
if __name__ == "__main__":
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()