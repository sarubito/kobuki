#!/usr/bin/env python


import rospy
from std_msgs.msg import String


rospy.init_node('talker')
pub = rospy.Publisher('chatter', String, queue_size=10)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
   str = "hello world %s"%rospy.get_time()
   rospy.loginfo(str)
   pub.publish(str)
   rate.sleep()

if __name__ == '__main__':
     try:
         talker()
     except rospy.ROSInterruptException: pass 
