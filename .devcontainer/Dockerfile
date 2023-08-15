# Use an official ROS2 base image
FROM ros:humble-ros-base

# Set the working directory to the workspace
ARG WORKSPACE=ros2_ws_1
WORKDIR /root/ros2_ws_1

# Set the locale to avoid potential encoding issues
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Set up the ROS2 environment variables
ENV ROS_DISTRO humble
ENV ROS_VERSION 2
ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics
ENV QT_X11_NO_MITSHM=1
ENV EDITOR=nano
ENV XDG_RUNTIME_DIR=/tmp

# Install any additional dependencies needed for your ROS2 application
RUN apt-get update && apt-get install -y \
    # Add your dependencies here (e.g., build tools, packages, etc.)
    make \
    curl \
    libglu1-mesa-dev \
    nano \
    python3-pip \
    python3-pydantic \
    ruby-dev \
    tmux \
    wget \
    ros-humble-gazebo-ros \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-joint-state-publisher \
    ros-humble-robot-localization \
    ros-humble-plotjuggler-ros \
    ros-humble-robot-state-publisher \
    ros-humble-ros2bag \
    ros-humble-rosbag2-storage-default-plugins \
    ros-humble-rqt-tf-tree \
    ros-humble-rmw-fastrtps-cpp \
    ros-humble-rmw-cyclonedds-cpp \
    ros-humble-slam-toolbox \
    ros-humble-turtlebot3 \
    ros-humble-turtlebot3-msgs \
    ros-humble-twist-mux \
    ros-humble-usb-cam \
    ros-humble-image-transport \
    ros-humble-image-commone \
    ros-humble-xacro \
    libopencv-dev \
    python3-opencv \

    # moduller icin ekleme yapilacak

RUN pip3 install setuptools==58.2.0 \
opencv-python-headless \

# Build the ROS2 packages in the workspace
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build

# Source the workspace setup files in each new terminal
RUN echo "source /ros2_ws_1/install/setup.bash" >> /root/.bashrc

# Start your ROS2 application (replace 'your_ros2_node_executable' with the actual executable)
CMD ["bash", "-c", "source /ros2_ws_1/install/setup.bash && ros2 run ros2_node_deneme"]
