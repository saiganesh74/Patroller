from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='patrol_navigation',
            executable='patrol_node',
            name='patrol_node'
        ),
        Node(
            package='student_detector',
            executable='student_detector',
            name='student_detector'
        ), 
        # Node(
        #     package='incident_logger',
        #     executable='incident_logger',
        #     name='incident_logger'
        # ),
        # Node(
        #     package='alert_system',
        #     executable='alert_api',
        #     name='alert_api'
        # ),
    ])
