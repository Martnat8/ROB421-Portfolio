# MoveSami Node

This ROS 2 node controls the **SAMI** humanoid robot by sending joint angle commands over a serial connection. It listens to corrected joint angles on `/joint_angles_corrected` and converts them into motor commands using a predefined joint ID map.

---

## Functionality

- **Subscribes**: `/joint_angles_corrected` (`std_msgs/String` in JSON format)
- **Publishes**: Commands to the SAMI robot via serial using the `JamieControl` interface
- **Dependencies**: 
  - `read_json.py` for interfacing with SAMI's motor controller
  - Two configuration files located in `move_sami/config/`: 
    - `Joint_config.json` for joint parameters
    - `Emote.json` for emotion/pose presets

---

## Usage Notes

- Ensure the correct serial port is set in `read_json.py`
- The JSON files used for joint configuration must be installed in the ROS 2 package's `config/` directory
- Joint angles must be passed in as integers in a JSON string

---

## External Files Used

This project includes two files from the [SHARE Research Team's SAMI-Robot GitHub repository](https://github.com/shareresearchteam/SAMI-Robot), used without modification:

- `read_json.py`
- `audio_manager.py`

They remain under their original license and are credited to the original authors.

---

## License

BSD 3-Clause License

