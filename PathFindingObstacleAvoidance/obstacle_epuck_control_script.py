"""my_obstacle avoidance controller."""
"""use with the world obstacle_avoidance.wbt """
# https://www.cyberbotics.com/doc/guide/epuck?version=cyberbotics:R2019a

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
    
    device = robot.getDevice(psNames[i])
    print("Device name is : ",psNames[i])
    print(device)

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

print("all good")

right_obstacle = False
left_obstacle = False
straight_ahead_obstacle = False

# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:
    # read sensors outputs
    psValues = []
    for i in range(8):
        psValues.append(ps[i].getValue())

    # detect obstacles
    #right_obstacle = psValues[0] > 80.0 or psValues[1] > 80.0 or psValues[2] > 80.0
    #left_obstacle = psValues[5] > 80.0 or psValues[6] > 80.0 or psValues[7] > 80.0
    #straight_ahead_obstacle = psValues[3] > 80.0 or psValues[4] > 80.0
    
    right_obstacle = psValues[1] > 80.0 or psValues[2] > 80.0
    left_obstacle = psValues[5] > 80.0 or psValues[6] > 80.0 
    straight_ahead_obstacle = psValues[7] > 80.0 or psValues[0] > 80.0
    
    
    if (right_obstacle):
       print("There is something on the right")
    
    if (left_obstacle):
       print("There is something on the left")  
       
    if (straight_ahead_obstacle):       
        print("There is something straight ahead") 
        
    gps_values = gps.getValues()
    print(f"GPS Position: X: {gps_values[0]:.2f}, Y: {gps_values[1]:.2f}")
   
    #Read compass values
    compass_values = compass.getValues()
    print(f"Compass values: {compass_values}")
   
    # initialize motor speeds at 50% of MAX_SPEED.
    leftSpeed  = 0.5 * MAX_SPEED
    rightSpeed = 0.5 * MAX_SPEED
    # modify speeds according to obstacles
    if left_obstacle:
        # turn right
        leftSpeed  = 0.5 * MAX_SPEED
        rightSpeed = -0.5 * MAX_SPEED
    elif right_obstacle:
        # turn left
        leftSpeed  = -0.5 * MAX_SPEED
        rightSpeed = 0.5 * MAX_SPEED
    # write actuators inputs
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)
