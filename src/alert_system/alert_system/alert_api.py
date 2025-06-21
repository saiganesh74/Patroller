import rclpy
from rclpy.node import Node 
from std_msgs.msg import String
from datetime import datetime
from collections import deque

class AlertSystem(Node):
    def __init__(self):
        super().__init__('alert_api')
        self.subscription = self.create_subscription(
            String,
            '/student_detected',
            self.callback,
            10
        )
        self.get_logger().info("Alert System Started")
        self.detections = deque()
    def callback(self,msg):
        now = datetime.now()
        self.detections.append(now)
        while self.detections and self.detections[0] < now - timedelta(seconds=15):
            self.detections.popleft()
        self.get_logger().info(f"📦 Detections in last 15s: {len(self.detections)}")

        if len(self.detections) > 3:
            self.send_alert(len(self.detections))

    def send_alert(self, count):
        self.get_logger().warn(f"⚠️ ALERT: {count} student(s) detected in 15 seconds!")

def main(args=None):
    rclpy.init(args=args)
    node = AlertSystem()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()