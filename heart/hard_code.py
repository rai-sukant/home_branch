#!/usr/bin/python3

import rospy
import math
from geometry_msgs.msg import Twist

 

def move_turtle():
    rospy.init_node("Turtle_heart", anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    moveitbitch = Twist()
    

    rate = rospy.Rate(600)

    theta = 0.0
    x = 16 * (math.sin(theta)) ** 3
    y = 13 * math.cos(theta) - 5 * math.cos(2 * theta) - 2 * math.cos(3 * theta) - math.cos(4 * theta)

       

    while not rospy.is_shutdown():
        
        dx_dtheta = (48 * (math.sin(theta)) ** 2) * math.cos(theta)
        dy_dtheta = (-13 * math.sin(theta)) + (10 * math.sin(2 * theta)) + (6 * math.sin(3 * theta)) + (4 * math.sin(4 * theta))


        moveitbitch.linear.x = dx_dtheta
        moveitbitch.linear.y = dy_dtheta

        pub.publish(moveitbitch)
        theta += 0.01

        rate.sleep()

if _name_ == '_main_':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass