#!/usr/bin/env python
import rospy

from nav_msgs.msg import Odometry

def odometryDATA(msg):
    print msg.pose.pose

   
def listener():
    rospy.init_node('get_odom', anonymous=True)
    rospy.Subscriber("odom",Odometry,odometryDATA)
    rospy.spin()

if __name__ == '__main__':
    listener()
