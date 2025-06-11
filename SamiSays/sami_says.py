#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import random
from math import isclose

class SamiSays(Node):
    def __init__(self):
        super().__init__('sami_says')

        #subscribes to joint angles
        self.sub = self.create_subscription(
            String, '/joint_angles_corrected', self.callback, 10)
        
        # in nathans Move sami node it will subscribe to this
        self.pub = self.create_publisher(String, '/new_pose', 10)

        #how we adjust our tolerance
        self.match_count = 0
        self.required_matches   = 5
        self.tolerance = 5.0  # degrees tolerance

        # pick the first target
        self.current_pose = self.pose_select(random.randint(1, 5))
        self.publish_target_pose()

    # sending a new pose to sami
    def publish_target_pose(self):
        msg = String()
        msg.data = json.dumps(self.current_pose)
        self.pub.publish(msg)
        self.get_logger().info(f"New target pose: {self.current_pose}")

    def callback(self, msg: String):
        # making sure we havve data from corrected angles and make it into a dictionary
        try:
            angles_in = json.loads(msg.data)
            if not isinstance(angles_in, dict):
                raise ValueError("expected dict")
        except (json.JSONDecodeError, ValueError) as e:
            self.get_logger().error(f"Bad message: {e}")
            return

        # check each joint in the target
        for joint, target_angle in self.current_pose.items():

            actual = angles_in.get(joint)

            #some more debugging checks
            if actual is None:
                self.get_logger().warn(f"Missing joint in incoming data: {joint}")
                return
            
            if not isclose(actual, target_angle, abs_tol=self.tolerance):
                # not close enough → bail out
                return

        # if we get here, all joints are within tolerance!
        self.match_count += 1
        self.get_logger().info(f"Pose matched ({self.match_count}/{self.required_matches})")

        if self.match_count >= self.required_matches:
            self.get_logger().info("🎉 All poses matched. Shutting down.")
            rclpy.shutdown()
            return

        # otherwise, pick a new target and publish it
        next_pose_number = (self.match_count % 5) + 1  # Cycle through 1-5
        self.current_pose = self.pose_select(next_pose_number)
        self.publish_target_pose()


    def pose_select(self, number):

        self.RSU = {
            "RightChest": 135, "RightShoulder": 120, "RightBicep": 115, "RightElbow": 90,
             "LeftChest": 115, "LeftShoulder": 180, "LeftBicep": 115,"LeftElbow": 105
        }
        self.LSU = {
             "RightChest": 135, "RightShoulder": 85, "RightBicep": 115, "RightElbow": 90,
             "LeftChest": 115, "LeftShoulder": 120, "LeftBicep": 115,"LeftElbow": 105
        }
        self.BSU = {
             "RightChest": 135, "RightShoulder": 120, "RightBicep": 115, "RightElbow": 90,
             "LeftChest": 115, "LeftShoulder": 120, "LeftBicep": 115,"LeftElbow": 105
        }
        self.RFlex = {
            "RightChest": 135, "RightShoulder": 120, "RightBicep": 145, "RightElbow": 90,
             "LeftChest": 115, "LeftShoulder": 180, "LeftBicep": 115,"LeftElbow": 105
        }
        self.LFlex = {
            "RightChest": 135, "RightShoulder": 85, "RightBicep": 115, "RightElbow": 90,
            "LeftChest": 115, "LeftShoulder": 120, "LeftBicep": 85,"LeftElbow": 105
        }

        if number == 1:
          return self.RSU
        elif number == 2:
          return self.LSU
        elif number == 3:
          return self.BSU
        elif number == 4:
          return self.RFlex
        elif number == 5:
          return self.LFlex
        else:
          self.get_logger().error(f"Invalid pose number: {number}")
          return {}


def main(args=None):
    rclpy.init(args=args)
    node = SamiSays()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

#Jacob's function is now hooked up and should work

