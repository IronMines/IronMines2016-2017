rosnode list  :  renvoie tous les noeuds qui envoient des messages.
rostopic info : donne le type de messages envoyés

	mkdir works 
	mkdir src 
	cd src 
	catkin_create_pkg PST std_msgs rospy
	cd PST
	mkdir script
	#dans script, creer les programme et faire chmod +x nom.py 
	cd ../..
	source devel/setup.bash
	catkin_make
http://answers.ros.org/question/203575/kobuki-unpredictability/

roslaunch kobuki_node minimal.launch --screen
/diagnostics
/diagnostics_agg
/diagnostics_toplevel_state
/joint_states
/mobile_base/commands/controller_info
/mobile_base/commands/digital_output
/mobile_base/commands/external_power
/mobile_base/commands/led1
/mobile_base/commands/led2
/mobile_base/commands/motor_power              : RENVOIE L ETAT DU MOTEUR (0 EN ARRET 1 SINON)
/mobile_base/commands/reset_odometry
/mobile_base/commands/sound
/mobile_base/commands/velocity                 :
linear: 
  x: 0.0 
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 0.0
						TYPE :   geometry_msgs/Twist
/mobile_base/controller_info
/mobile_base/debug/raw_control_command
/mobile_base/debug/raw_data_command
/mobile_base/debug/raw_data_stream
/mobile_base/events/bumper
/mobile_base/events/button
/mobile_base/events/cliff
/mobile_base/events/digital_input
/mobile_base/events/power_system
/mobile_base/events/robot_state
/mobile_base/events/wheel_drop
/mobile_base/sensors/core
/mobile_base/sensors/dock_ir
/mobile_base/sensors/imu_data
/mobile_base/sensors/imu_data_raw
/mobile_base/version_info
/mobile_base_nodelet_manager/bond
/odom
/rosout
/rosout_agg
/tf


roslaunch kobuki_keyop safe_keyop.launch
rqt_graph



from geometry_msgs import msg 
A =  msg.Twist

