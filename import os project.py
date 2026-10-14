import os
import time


def shutdown_computer():
    # The "-s" flag means "shutdown"
    # The "-f" flag forces running applications to close
    # The "/t 5" delay waits 5 seconds before shutting down
    command = "shutdown /s /f /t 5"
    os.system(command)

# Call this function only when you truly want to power off the PC.
shutdown_computer()

# If you want a delay message before shutdown:
print("Your computer will shut down in 5 seconds.")
time.sleep(5)
print("Shutting down now...")
