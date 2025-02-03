import airsim
import time

# Connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()

# Arm and take off the drone
client.armDisarm(True)
client.takeoffAsync().join()

# Move the drone
client.moveToPositionAsync(10, 10, -10, 5).join()

# Land the drone
client.landAsync().join()
client.armDisarm(False)


