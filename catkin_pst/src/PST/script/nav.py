#!/usr/bin/env python
import rospy
#rostopic pub -r 10 mobile_base/commands/velocity geometry_msgs/Twist  '{linear:  {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

def odometryDATA(msg):
    print msg.pose.pose

   
def listener():
    rospy.init_node('get_odom', anonymous=True)
    rospy.Subscriber("/turtle1/cmd_vel",Odometry,odometryDATA)
    rospy.spin()

def talker():
    pub = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10)
    rospy.init_node('Pilot', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(Twist(Vector3(-0.01,0,0),Vector3(0,0,0)))
        rate.sleep()
	#listener() 



if __name__ == '__main__':
    talker()


