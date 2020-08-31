FROM ros:noetic-ros-base AS master

EXPOSE 11311/tcp

ENTRYPOINT ["bash", "-ic", "source /opt/ros/noetic/setup.bash && roscore"]

FROM ubuntu:latest AS cloner
RUN apt-get update && apt-get install -y git openssh-client
ADD id_rsa /root/.ssh/id_rsa
RUN ssh-keyscan -t rsa github.com > ~/.ssh/known_hosts

RUN mkdir -p /root/src
WORKDIR /root/src
RUN git clone git@github.com:m2robocon/m2_ps4.git m2_ps4

FROM master

ENV ROS_MASTER_URI=http://master:11311

RUN apt-get update && apt-get install -y curl python2.7 python3.8
RUN ln -s /usr/bin/python2.7 /usr/bin/python
RUN ln -s /usr/bin/python2.7 /usr/bin/python2
RUN curl https://bootstrap.pypa.io/get-pip.py | python2
RUN pip install future pyyaml rospkg

COPY --from=cloner /root/src /root/catkin_ws/src

WORKDIR /root/catkin_ws
RUN bash -ic "source /opt/ros/noetic/setup.bash && catkin_make"

RUN echo "source /opt/ros/noetic/setup.bash" >> /root/.bashrc && \
	echo "source devel/setup.bash" >> /root/.bashrc

ENTRYPOINT ["bash", "-ic", "rosrun $0 $1"]