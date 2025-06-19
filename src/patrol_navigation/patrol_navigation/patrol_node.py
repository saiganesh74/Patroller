import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist
import time

class PatrolNode(Node):
    def __init__(self):
        super().__init__("Patrol_node")
        self.publisher = self.create_publisher(
            Twist ,
            '/cmd_vel',
            10
        )        
        timer_period = 2.0 
        self.timer = self.create_timer(timer_period, self.patrol_callback)
        self.state = 0 
        self.get_logger().info('Patrol Node Intiated')
        
        
    def patrol_callback(self):
        msg = Twist()
        if self.state == 0 :
            self.get_logger().info('➡️ Moving forward')
            msg.linear.x = 0.3
            msg.angular.z = 0.0
        elif self.state == 1:
            self.get_logger().info('↪️ Turning right')
            msg.linear.x = 0.0
            msg.angular.z = -0.5
        elif self.state == 2:
            self.get_logger().info('⬅️ Turning left')
            msg.linear.x = 0.0
            msg.angular.z = 0.5
        elif self.state == 3:
            self.get_logger().info('⛔ Stopping')
            msg.linear.x = 0.0
            msg.angular.z = 0.0
        self.publisher.publish(msg)
        self.state = (self.state +1) % 4
        
        
        
        
def main():
    rclpy.init()
    node = PatrolNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()