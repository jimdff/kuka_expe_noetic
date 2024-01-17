#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def joint_publisher():
    # Initialize the ROS node
    rospy.init_node('joint_publisher', anonymous=True)

    # Create publishers for the joint position commands
    joint_pub1 = rospy.Publisher('/kuka_kr4r600/joint_a1_position_controller/command', Float64, queue_size=10)
    joint_pub2 = rospy.Publisher('/kuka_kr4r600/joint_a2_position_controller/command', Float64, queue_size=10)
    joint_pub3 = rospy.Publisher('/kuka_kr4r600/joint_a3_position_controller/command', Float64, queue_size=10)
    joint_pub4 = rospy.Publisher('/kuka_kr4r600/joint_a4_position_controller/command', Float64, queue_size=10)

    rate = rospy.Rate(10)  # 10 Hz

    # Publish a joint position command (replace 0.0 with the desired joint angle)
    joint_position1 = 30.0
    joint_pub1.publish(joint_position1)

    rospy.sleep(1) # Sleeps for 1 sec

    # Publish a joint position command (replace 0.0 with the desired joint angle)
    joint_position2 = -30.0
    joint_pub2.publish(joint_position2)

    rospy.sleep(1) # Sleeps for 1 sec

    # Publish a joint position command (replace 0.0 with the desired joint angle)
    joint_position3 = 50.0
    joint_pub3.publish(joint_position3)

    rospy.sleep(1) # Sleeps for 1 sec

    # Publish a joint position command (replace 0.0 with the desired joint angle)
    joint_position4 = 50.0
    joint_pub4.publish(joint_position4)

    rospy.sleep(3) # Sleeps for 1 sec

    # Publish a joint position command (replace 0.0 with the desired joint angle)
    joint_position1 = 0.0
    joint_pub1.publish(joint_position1)

    rospy.sleep(1) # Sleeps for 1 sec

    # Publish a joint position command (replace 0.0 with the desired joint angle)
    joint_position2 = 0.0
    joint_pub2.publish(joint_position2)

    rospy.sleep(1) # Sleeps for 1 sec

    # Publish a joint position command (replace 0.0 with the desired joint angle)
    joint_position3 = 0.0
    joint_pub3.publish(joint_position3)

    rospy.sleep(1) # Sleeps for 1 sec

    # Publish a joint position command (replace 0.0 with the desired joint angle)
    joint_position4 = 0.0
    joint_pub4.publish(joint_position4)

    rospy.sleep(1) # Sleeps for 1 sec

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass
