cmake_minimum_required(VERSION 2.8.3)
project(foo)

find_package(catkin REQUIRED COMPONENTS
	roscpp
	rospy
	message_generation
)

add_message_files(
	FILES
	TheMessage.msg
)

include_directories(${catkin_INCLUDE_DIRS})
