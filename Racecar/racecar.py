import logging
import sys
import threading

from Racecar.drivetrain import Drive
from Racecar.teleop.teleop import Teleop

# Drive Computer
# Racecar main
#
# Part of the GSSM Autonomous Golf Cart
# Written by: Joseph Telaak, class of 2022

def main():
    # Setup the message logging
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Print to file
    file_handler = logging.FileHandler("logs/main.log")
    logging_format = logging.Formatter("%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(logging_format)
    logger.addHandler(file_handler)

    # Print to console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging_format)
    logger.addHandler(console_handler)

    # Teleop
    logger.info("Initializing Drive System")
    run_state = Teleop(drivetrain=Drive(serial_port=""))
    run = threading.Thread(target=run_state.perodic, name="teleop-drive-thread", daemon=True)
    logger.info("Drive System Setup")

    # Run
    logger.info("Starting")
    run_state.initialize()
    run.start()

