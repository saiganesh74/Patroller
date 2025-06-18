# Campus Patrolling Robot (ROS 2 Project)

This is a modular ROS 2-based project where a mobile robot patrols the college campus, detects students outside authorized zones, and sends alerts to the respective department. The project is designed to be extended daily and is structured like an industry-grade robotic system.

---

## Project Overview

**Main Idea:** A smart mobile robot that navigates autonomously, detects humans/students in real-time using a camera, logs the event, and sends alerts to heads of departments or authorities.

---

## Modules and Packages

### 1. `patrol_navigation`
- Defines robot's patrol route using waypoints
- Sends velocity commands using Nav2

### 2. `student_detector`
- Subscribes to camera feed
- Uses OpenCV or ML models to detect humans

### 3. `incident_logger`
- Logs each student detection event with timestamp and location

### 4. `alert_system`
- Sends alerts (email or API) when unauthorized presence is detected

### 5. `patrol_launch`
- Launch file that brings together all above nodes

---

## Directory Structure

```bash
patroller/
├── src/
│   ├── patrol_navigation/
│   ├── student_detector/
│   ├── incident_logger/
│   ├── alert_system/
│   └── patrol_launch/
└── README.md
```

---

## How to Run (After Code Is Ready)

```bash
cd ~/patroller
colcon build
source install/setup.bash
ros2 launch patrol_launch patrol.launch.py
```

---

## Requirements

- ROS 2 Humble/Foxy/Iron
- OpenCV
- Python 3.8+
- SMTP/HTTP libraries (for alerts)

---


## 🤝 Contributions

This is a personal learning project by me, inspired by real-world robotics solutions for campus monitoring.

---

## Contact
- 📧 ganeshrejeti1@gmail.com
- 🧠 GitHub: [Saiganesh74]

---

Let the patrolling begin! 🚓
