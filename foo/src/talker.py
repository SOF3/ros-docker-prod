#!/usr/bin/env python3

import rospy
from foo.msg import TheMessage

if __name__ == "__main__":
    rospy.init_node("talker")
    pub = rospy.Publisher("/foo", TheMessage, queue_size=1)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rate.sleep()
        pub.publish(first=True, second=False)
