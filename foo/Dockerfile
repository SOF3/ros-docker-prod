FROM ros:noetic-ros-base

ENV ROS_MASTER_URI=http://master:11311

RUN mkdir -p /root/catkin_ws/src
WORKDIR /root/catkin_ws

ADD . /root/catkin_ws/src/pkg

RUN bash -ic "source /opt/ros/noetic/setup.bash && catkin_make"

CMD bash -ic "source /opt/ros/noetic/setup.bash && source devel/setup.bash && rosrun foo talker.py"
