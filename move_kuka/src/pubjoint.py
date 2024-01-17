#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def joint_publisher():
    # Initialize the ROS node
    rospy.init_node('joint_publisher', anonymous=True)

    # Create a publisher for the joint position command
    joint_pub = rospy.Publisher('/kuka_kr4r600/joint_a2_position_controller/command', Float64, queue_size=10)

    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        # Publish a joint position command (replace 0.0 with the desired joint angle)
        joint_position = 30.0
        joint_pub.publish(joint_position)

        rate.sleep()

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass
