#!/usr/bin/env python

import rospy
from kobuki_msgs.msg import BumperEvent

def callback_bamper(bumper):
    if bumper.state == 1:
        print('bumper_touch')
    else:
        print('none')

def main():
    rospy.init_node('kobuki_bumper', anonymous=True)

    #sub = rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, callback_bamper)
    #rospy.spin()
    rospy.wait_for_message('/mobile_base/events/bumper',BumperEvent)
    print('#')
    exit()

if __name__ == '__main__':
#    print('name is main')
    main() #実行してほしい関数

