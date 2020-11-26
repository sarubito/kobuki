#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent

rospy.init_node('kobuki_move_stop', anonymous=True)
pub_vel = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
pub_bumper = rospy.Publisher('/mobile_base/events/bumper', BumperEvent, queue_size=10)
stop_flg = 0

def callback_stop(bumper):
    global stop_flg
    if bumper.state != 0:
        stop_flg = 1
    
   

def main():
    global stop_flg
    bump = BumperEvent()
    bump.state = 0

    sub = rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, callback_stop)

    vel = Twist()


    while not rospy.is_shutdown():
        pub_bumper.publish(bump)
        print(bump.state, stop_flg)

        vel.linear.x = 0.5
        pub_vel.publish(vel)
        
        if stop_flg == 1:
            vel.linear.x = 0.0
            bump.state = 1
            pub_vel.publish(vel)
            pub_bumper.publish(bump)
        elif stop_flg == 0:
            vel.linear.x = 0.5
            pub_vel.publish(vel)
        rospy.sleep(0.5)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass