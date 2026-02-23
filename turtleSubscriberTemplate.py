import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseMonitor(Node):
    def __init__(self):
        super().__init__('myTurtleSubscriber')
        # Subscribe to the /turtle1/pose topic
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10)

    def pose_callback(self, msg):
        turtleX = msg.x
        turtleY = msg.y

def main(args=None):
    rclpy.init(args=args)
    node = PoseMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()