import rclpy
from rclpy.node import Node 
from datetime import datetime 
from std_msgs.msg import String 

class IncidentLogger(Node):
    def __init__(self):
        super().init('incident_logger')
        self.subscription = self.create_subscription(
            String,
            '/student_detected',
            self.listener_callback,
            10
        )
        self.subscription
        self.get_logger().info("Incident logger started")
        
    def listener_callback(self , msg):
        timestamp = datetime.now().strftime()
        log_msg = f"[{timestamp}] INCIDENT : {msg.data}"
        self.get_logger().info(log_msg)
def main():
    rclpy.init()
    node = IncidentLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()