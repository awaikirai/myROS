#!/usr/bin/env python
import rospy
from std_msgs.msg import String

n = 0
hell = 0
time = 0

def cb(message):
    global n
    n = message.data

pub = rospy.Publisher('kaaer', String, queue_size=1)

if __name__ == '__main__':
    rospy.init_node('tuukaa')
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        sub = rospy.Subscriber('tuuer', String, cb)

        if n == "Hello":
            hell = "Shit"
            n = 0
            pub.publish(hell)
            time += 1
            print(time)
        elif n == "What_are_you_doing?":
            hell = "I'm_pooping_now"
            n = 0
            pub.publish(hell)
            time += 1
            print(time)
        elif n == "DIO":
            hell = "THE WORLD!!!!!"
            n = 0
            pub.publish(hell)
            time += 1
            print(time)
        elif n == 0:
            hell = 0
        else:
            hell = "hello"
            n = 0
            pub.publish(hell)
            time += 1
            print(time)
        rate.sleep()
