#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
import geometry_msgs.msg as gsms 
import tf.transformations
#----------------------------------

def retour(msg) : 
	rospy.loginfo("Received a /cmd_vel message!")
	rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
	rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))		

   
def listener():
	rospy.init_node('listen_cmd', anonymous=True)
	rospy.Subscriber("/cmd_vel",gsms.Twist,retour)
	rospy.spin()

if __name__ == '__main__':
	listener()
