# Inspiration for Webot E-puck robot 
# Maze solver exercise.
# 
# Template code for Wall following algorithm.
# Inspiration for Maze solver exercise
#
# Wall Following Logic:
#
#    If there's an obstacle straight ahead, the robot turns left to avoid it.
#    If there's a wall detected on the right, the robot follows it by slowing down its right wheel.
#    If no wall is detected on the right, the robot turns slightly right to search for the wall.


from controller import Robot, DistanceSensor, Motor, GPS, Compass

# time in [ms] of a simulation step
TIME_STEP = 64

MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()

# initialize devices
ps = []
psNames = [
    'ps0', 'ps1', 'ps2', 'ps3',
    'ps4', 'ps5', 'ps6', 'ps7'
]

for i in range(8):
    ps.append(robot.getDevice(psNames[i]))
    ps[i].enable(TIME_STEP)

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

gps = robot.getDevice("gps")
gps.enable(TIME_STEP)

# Get the compass device
compass = robot.getDevice("compass")
compass.enable(TIME_STEP)  

def wall_following():
    """Wall following behavior."""
    while robot.step(TIME_STEP) != -1:
        # read sensors outputs
        psValues = [ps[i].getValue() for i in range(8)]

        # Detect obstacles
        right_obstacle = psValues[1] > 80.0 or psValues[2] > 80.0
        left_obstacle = psValues[5] > 80.0 or psValues[6] > 80.0
        straight_ahead_obstacle = psValues[7] > 80.0 or psValues[0] > 80.0

        # Wall following logic
        left_speed = MAX_SPEED
        right_speed = MAX_SPEED

        if straight_ahead_obstacle:
            # Obstacle ahead, turn left
            print("Obstacle ahead, turning left")
            left_speed = -0.5 * MAX_SPEED
            right_speed = 0.5 * MAX_SPEED
        elif right_obstacle:
            # Follow the wall on the right
            print("Following wall on the right")
            left_speed = MAX_SPEED
            right_speed = 0.5 * MAX_SPEED
        elif not right_obstacle:
            # Move closer to the wall on the right
            print("Searching for wall on the right")
            left_speed = 0.5 * MAX_SPEED
            right_speed = MAX_SPEED

        # Set the motor speeds
        leftMotor.setVelocity(left_speed)
        rightMotor.setVelocity(right_speed)

if __name__ == "__main__":
    print("Starting wall-following behavior")
    wall_following()