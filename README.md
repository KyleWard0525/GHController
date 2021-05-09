## GHController
The goal of this project is to take a broken PlayStation 2 Guitar Hero Controller and fix it so that it can work with a computer.

The idea is to feed the signal from the button on the guitar controller to a Raspberry Pi 4B which will then interpret the signal and convert it into a simulated keypress that can then be used to play Guitar Hero / Clone Hero.

# v0.1
- Controller has been fixed and is now capable of outputing a signal when a button is pressed
- Supports all 5 buttons: Green, Red, Yellow, Blue, Orange
- Signal from button press is fed into the Raspberry Pi through a bread board
- Uses color-coded LEDs to ensure the output signal works correctly
