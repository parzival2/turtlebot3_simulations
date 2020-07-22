#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from ds4_driver.msg import Status
from sensor_msgs.msg import Joy

class DualshockTeleop(object):
    def __init__(self):
        # Initialize node
        rosNode = rospy.init_node("dualshock_keyop")
        # Publisher
        self.twistMsgPublisher = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        # Subscriber
        self.joySub = rospy.Subscriber("joy", Joy, self.onJoyMessageReceived, queue_size=1)
        self.getParameters()
        rospy.spin()

    def getParameters(self):
        # Min and max speed
        self.minSpeed = -1.0
        self.maxSpeed = 1.0

    def onJoyMessageReceived(self, joy):
        self.twistMsg = Twist()
        self.twistMsg.linear.x = joy.axes[3] * self.maxSpeed
        self.twistMsg.angular.z = joy.axes[0]
        self.twistMsgPublisher.publish(self.twistMsg)


if __name__ == '__main__':
    dualShockObject = DualshockTeleop()