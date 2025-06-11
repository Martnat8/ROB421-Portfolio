#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class FakeAngle(Node):
    def __init__(self):
        super().__init__('fake_angle')
        self.pub = self.create_publisher(String, '/fake_pose', 10)
        self.timer = self.create_timer(2.0, self.publish_fake_pose)  # every 2 seconds

    def publish_fake_pose(self):
        rsu = {
            "RightChest": 135, "RightShoulder": 120, "RightBicep": 115, "RightElbow": 90,
            "LeftChest": 115, "LeftShoulder": 180, "LeftBicep": 115, "LeftElbow": 105
        }

        msg = String()
        msg.data = json.dumps(rsu)
        self.pub.publish(msg)
        self.get_logger().info(f"Published fake pose: {rsu}")

def main(args=None):
    rclpy.init(args=args)
    node = FakeAngle()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
