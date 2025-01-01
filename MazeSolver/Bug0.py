# Inspiration for Webot E-puck robot 
# Maze solver exercise.
# 
# Template code for Bug0 algorithm.
# Inspiration for Maze solver exercise
#
# Bug0 algorithm
# Explanation of the Bug0 Algorithm Implementation:
#
#    Goal Position:
#        The goal position is set in the goal_position variable as [x, y] coordinates.
#
#    Obstacle Detection:
#        The proximity sensors (ps) are used to detect obstacles in the robot's path.
#
#    Wall Following:
#        When an obstacle is detected, the robot turns left or adjusts its trajectory to follow the wall until it #        can move directly toward the goal again.
#
#    Direct Movement:
#        If no obstacle is detected, the robot moves directly toward the goal position.
#
#    Goal Check:
#        The robot checks its distance to the goal using GPS and stops when it is within 0.1 units of the goal.

from controller import Robot, DistanceSensor, Motor, GPS, Compass
import math

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

compass = robot.getDevice("compass")
compass.enable(TIME_STEP)

def get_bearing_in_degrees():
    compass_values = compass.getValues()
    rad = math.atan2(compass_values[0], compass_values[1])
    bearing = (rad - 1.5708) / math.pi * 180.0
    if bearing < 0.0:
        bearing += 360.0
    return bearing

def distance_to_goal(current_pos, goal_pos):
    return math.sqrt((goal_pos[0] - current_pos[0])**2 + (goal_pos[1] - current_pos[1])**2)

def wall_following():
    """Wall following behavior."""
    while robot.step(TIME_STEP) != -1:
        psValues = [ps[i].getValue() for i in range(8)]
        right_obstacle = psValues[1] > 80.0 or psValues[2] > 80.0
        straight_ahead_obstacle = psValues[7] > 80.0 or psValues[0] > 80.0

        if straight_ahead_obstacle:
            print("Obstacle ahead, turning left")
            leftMotor.setVelocity(-0.5 * MAX_SPEED)
            rightMotor.setVelocity(0.5 * MAX_SPEED)
        elif right_obstacle:
            print("Following wall on the right")
            leftMotor.setVelocity(MAX_SPEED)
            rightMotor.setVelocity(0.5 * MAX_SPEED)
        else:
            print("Moving along the wall")
            leftMotor.setVelocity(0.5 * MAX_SPEED)
            rightMotor.setVelocity(MAX_SPEED)
        
        # Exit wall following if no obstacle ahead and robot is not blocked
        if not straight_ahead_obstacle and not right_obstacle:
            break

def bug0_algorithm(goal_pos):
    while robot.step(TIME_STEP) != -1:
        # Read sensor values
        psValues = [ps[i].getValue() for i in range(8)]

        # Read GPS for current position
        current_pos = gps.getValues()
        
        # Check if goal is reached
        if distance_to_goal(current_pos, goal_pos) < 0.1:
            print("Goal reached!")
            leftMotor.setVelocity(0)
            rightMotor.setVelocity(0)
            break

        # Obstacle detection
        right_obstacle = psValues[1] > 80.0 or psValues[2] > 80.0
        left_obstacle = psValues[5] > 80.0 or psValues[6] > 80.0
        straight_ahead_obstacle = psValues[7] > 80.0 or psValues[0] > 80.0

        if straight_ahead_obstacle:
            # Call wall-following behavior
            print("Obstacle detected, switching to wall-following mode")
            wall_following()
        else:
            # Move towards the goal
            print("Heading towards the goal")
            leftMotor.setVelocity(MAX_SPEED)
            rightMotor.setVelocity(MAX_SPEED)

if __name__ == "__main__":
    goal_position = [1.0, 1.0]  # Change to your desired goal coordinates
    print("Starting Bug0 algorithm towards goal:", goal_position)
    bug0_algorithm(goal_position)