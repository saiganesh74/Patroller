import rclpy
from rclpy.node import Node 

class PatrolNode(Node):
    def __init__(self):
        super().__init__("Patrol_node")
        self.get_logger().info('Patrol Node is running')
def main():
    rclpy.init()
    node = PatrolNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()