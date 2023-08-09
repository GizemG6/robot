# Use an official ROS2 base image
FROM ros:foxy

# Set the locale to avoid potential encoding issues
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Set up the ROS2 environment variables
ENV ROS_DISTRO foxy
ENV ROS_VERSION 2

# Install any additional dependencies needed for your ROS2 application
RUN apt-get update && apt-get install -y \
    # Add your dependencies here (e.g., build tools, packages, etc.)

# Create a workspace directory
RUN mkdir -p /ros2_ws/src

# Set the working directory to the workspace
WORKDIR /ros2_ws

# Copy your ROS2 application code into the workspace
COPY ./path/to/your/ros2_app /ros2_ws/src

# Build the ROS2 packages in the workspace
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build

# Source the workspace setup files in each new terminal
RUN echo "source /ros2_ws/install/setup.bash" >> /root/.bashrc

# Start your ROS2 application (replace 'your_ros2_node_executable' with the actual executable)
CMD ["bash", "-c", "source /ros2_ws/install/setup.bash && ros2 run your_ros2_node_executable"]
