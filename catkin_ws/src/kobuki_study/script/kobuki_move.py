#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move():
    rospy.init_node('kobuki_move', anonymous=True)
    velocity_publisher = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    vel_msg = Twist()

    while not rospy.is_shutdown():
        vel_msg.linear.x = 0.05

	velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
   
