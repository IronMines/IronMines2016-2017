#!/usr/bin/env python
from kobuki_msgs.msg import SensorState
from kobuki_msgs.msg import ButtonEvent
import rospy

def SensorStateCallback(data):
	sens_1 = data.analog_input[0] 
	sens_2 = data.analog_input[1]
	sens_3 = data.analog_input[2]
	print sens_1
	print sens_2
	print sens_3

def main()  : 
	rospy.init_node('get_sensors_value', anonymous=True)
	rospy.Subscriber("/mobile_base/sensors/core", SensorState, SensorStateCallback )
	rospy.spin()	

if __name__ == "__main__" : 
	main()
