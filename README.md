# PittRAS 2026 ROS Workshop
Included are python code templates, a sample launch file, and a URDF file for a simple robot arm

Command to launch robot state publisher:

```ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(xacro ./simpleArm.urdf.xacro)"```

For more resources look at:
- [ROS Humble Tutorial](https://docs.ros.org/en/humble/Tutorials.html)
- [Articulated Robotics Youtube](https://www.youtube.com/@ArticulatedRobotics)
