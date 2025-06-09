#!/usr/bin/env python3

# This node takes in joint angles from the angle publisher and translates them 
# into SAMI Servo frame limiting the output to their min/max given on the github.
# https://github.com/jlruballos/sami_ws
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import json 

class JointAnglesCorrected(Node):
    def __init__(self):
        super().__init__('robot_joint_publisher')

        self.sub = self.create_subscription(String, '/joint_angles', self.callback, 10)
        self.pub = self.create_publisher(String, '/joint_angles_corrected', 10)

        # Unified joint info dictionary
        # Each joint has: servohome, min, max, direction, home_angle
        self.joint_info = {
            "RightChest":     {"servohome": 120, "min": 80,  "max": 150, "direction": 1,  "home_angle": 0},
            "RightShoulder": {"servohome": 85,  "min": 70,  "max": 240, "direction": 1,  "home_angle": 0},
            "RightBicep":    {"servohome": 115, "min": 115, "max": 180, "direction": 1,  "home_angle": 90},
            "RightElbow":    {"servohome": 90,  "min": 10,  "max": 155, "direction": -1, "home_angle": 110},
            "LeftChest":     {"servohome": 90,  "min": 50,  "max": 140, "direction": 1,  "home_angle": 0},
            "LeftShoulder":  {"servohome": 180, "min": 30,  "max": 195, "direction": -1, "home_angle": 0},
            "LeftBicep":     {"servohome": 130, "min": 35,  "max": 195, "direction": 1,  "home_angle": -90},
            "LeftElbow":     {"servohome": 105, "min": 60,  "max": 180, "direction": 1,  "home_angle": 90},

            # Additional joints from dir_map that we aren't using in our current controlling of SAMI
            "LeftGripper":   {"servohome": 'n/a', "min": 'n/a', "max": 'n/a', "direction": 1,  "home_angle": 'n/a'},
            "LeftHip":       {"servohome": 'n/a', "min": 'n/a', "max": 'n/a', "direction": 1,  "home_angle": 'n/a'},
            "LeftKnee":      {"servohome": 'n/a', "min": 'n/a', "max": 'n/a', "direction": 1,  "home_angle": 'n/a'},
            "LeftAnkle":     {"servohome": 'n/a', "min": 'n/a', "max": 'n/a', "direction": 1,  "home_angle": 'n/a'},
            "RightGripper":  {"servohome": 'n/a', "min": 'n/a', "max": 'n/a', "direction": 1,  "home_angle": 'n/a'},
            "RightHip":      {"servohome": 'n/a', "min": 'n/a', "max": 'n/a', "direction": 1,  "home_angle": 'n/a'},
            "RightKnee":     {"servohome": 'n/a', "min": 'n/a', "max": 'n/a', "direction": 1,  "home_angle": 'n/a'},
            "RightAnkle":    {"servohome": 'n/a', "min": 'n/a', "max": 'n/a', "direction": 1,  "home_angle": 'n/a'},
            "HeadNod":       {"servohome": 'n/a', "min": 'n/a', "max": 'n/a', "direction": 1,  "home_angle": 'n/a'},
            "HeadTurn":      {"servohome": 'n/a', "min": 'n/a', "max": 'n/a', "direction": 1,  "home_angle": 'n/a'},
            "HeadTilt":      {"servohome": 'n/a', "min": 'n/a', "max": 'n/a', "direction": 1,  "home_angle": 'n/a'},
            "TorsoBow":      {"servohome": 'n/a', "min": 'n/a', "max": 'n/a', "direction": -1, "home_angle": 'n/a'},
            "TorsoTilt":     {"servohome": 'n/a', "min": 'n/a', "max": 'n/a', "direction": -1, "home_angle": 'n/a'}
        }

    def callback(self, msg: String):

        # Some protection against bad messages
        try:
            angles_in = json.loads(msg.data)
            if not isinstance(angles_in, dict):
                raise ValueError("Expected a dict of joint angles")
            
        except (json.JSONDecodeError, ValueError) as e:
            self.get_logger().error(f"Bad joint_angles message: {e}")
            return

        angles_out = {}

        for joint, angle in angles_in.items():
            if joint not in self.joint_info:
                self.get_logger().warn(f"Unknown joint: {joint}")
                continue
            if not isinstance(angle, (int, float)):
                self.get_logger().warn(f"Non-numeric angle for {joint}: {angle}")
                continue

            info = self.joint_info[joint]
            if 'n/a' in (info['servohome'], info['min'], info['max'], info['home_angle']):
                self.get_logger().warn(f"Missing joint info for {joint}, skipping")
                continue

            delta = info['direction'] * (angle - info['home_angle'])
            raw = info['servohome'] + delta
            corrected = max(info['min'], min(raw, info['max']))
            angles_out[joint] = corrected
        
                
            print(f"{joint}: input={angle}, servohome={info['servohome']}, worldhome={info['home_angle']}, delta={delta}, raw={raw}, corrected={corrected}")

        out_msg = String()
        out_msg.data = json.dumps(angles_out)
        self.pub.publish(out_msg)


def main(args=None):
    rclpy.init(args=args)
    corrected = JointAnglesCorrected()
    rclpy.spin(corrected)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
