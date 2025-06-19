import rclpy
from rclpy.node import Node 
import cv2
from std_msgs.msg import String

class StudentDetector(Node):
    def __init__(self):
        super().__init__('Student_detector')
        self.publisher = self.create_publisher(
            String ,
            '/student_detected',
            10
        )
        self.get_logger().info('Student Detector Node Started')
        self.timer = self.create_timer(1.0 , self.detect_callback)
        self.human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
        self.cap = cv2.VideoCapture(0)

    def detect_callback(self):
        ret , frame = self.cap.read()
        if not ret:
            self.get_logger().warn('Failed to read from camera')
            return
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bodies = self.human_cascade.detectMultiScale(gray, 1.1, 4)
        
        if len(bodies)> 0 :
            self.get_logger().info(f"{len(bodies)} persons detected")
            msg = String()
            self.publisher.publish(msg)
        
        cv2.imshow('Student Detection', frame)
        cv2.waitKey(1)
        
    def destroy_node(self):
        self.cap.release()
        cv2.destroyAllWindows()
        super().destroy_node()
        
def main():
    rclpy.init()
    node = StudentDetector()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
if __name__ == "__main__":
    main()