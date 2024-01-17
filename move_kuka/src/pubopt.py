#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def publish_joint_position(pub, position):
    pub.publish(position)
    rospy.sleep(1)  # Sleeps for 1 second

def joint_publisher():
    # Initialize the ROS node
    rospy.init_node('joint_publisher', anonymous=True)

    # Create publishers for the joint position commands
    joint_pubs = [
        rospy.Publisher('/kuka_kr4r600/joint_a1_position_controller/command', Float64, queue_size=10),
        rospy.Publisher('/kuka_kr4r600/joint_a2_position_controller/command', Float64, queue_size=10),
        rospy.Publisher('/kuka_kr4r600/joint_a3_position_controller/command', Float64, queue_size=10),
        rospy.Publisher('/kuka_kr4r600/joint_a4_position_controller/command', Float64, queue_size=10)
    ]

    rate = rospy.Rate(10)  # 10 Hz

    # Define joint positions for movement
    joint_positions = [30.0, -30.0, 50.0, 50.0]

    # Publish joint positions
    for pub, position in zip(joint_pubs, joint_positions):
        publish_joint_position(pub, position)

    # Sleep for 3 seconds
    rospy.sleep(3)

    # Return to the starting position
    starting_positions = [0.0, 0.0, 0.0, 0.0]
    for pub, position in zip(joint_pubs, starting_positions):
        publish_joint_position(pub, position)

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass
