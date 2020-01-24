#!/usr/bin/env python
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('tuu')
    pub = rospy.Publisher('tuuer', String, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hell = input("->")
        pub.publish(hell)
        rate.sleep()
