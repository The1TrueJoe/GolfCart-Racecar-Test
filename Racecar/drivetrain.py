from pyvesc import VESC

import logging

# Drive Computer
# Drivetrain
#
# Part of the GSSM Autonomous Golf Cart
# Written by: Joseph Telaak, class of 2022

class Drive:

    def __init__(self, serial_port):
        # Motor
        self.motor = VESC(serial_port=serial_port)

        # Setup the message logging
        self.logger = logging.getLogger("drivetrain")

        # Firmware
        self.logger.info(f"Firmware:  {self.motor.get_firmware_version()}")

        # Servo
        self.servo_pos = .5
        self.setServo(.5)

    # Set the motor duty cycle
    def setMotor(self, duty_cycle):
        self.motor.set_duty_cycle(duty_cycle)
        self.logger.info(f"Setting Duty Cycle: {duty_cycle}")

    # Set the servo position
    def setServo(self, pos):
        self.logger.info(f"Setting Servo Pos: {pos}")
        self.set_servo(pos)
        self.servo_pos = .5


    # Turn Left
    def left(self):
        self.setServo(self.servo_pos - .1)

    # Turn Right
    def right(self):
        self.setServo(self.servo_pos + .1)

    # Forward
    def forward(self, duty_cycle):
        self.setMotor(duty_cycle = duty_cycle)

    # Forward
    def reverse(self, duty_cycle):
        self.setMotor(duty_cycle = -duty_cycle)