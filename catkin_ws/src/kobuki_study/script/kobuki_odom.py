import rospy
from nav_msgs.msg import Odometry
#from geometry_msgs.msg import Twist
 

def odom_callback(vel):
   rospy.loginfo(vel.pose.pose.position.x)

def main():
    rospy.init_node('kobuki_odom',anonymous=True)
    sub = rospy.Subscriber('/odom',Odometry,odom_callback)
    rospy.spin()

if __name__ == '__main__':
    main()
