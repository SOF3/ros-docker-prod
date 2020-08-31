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

generate_messages(DEPENDENCIES
)

catkin_package(LIBRARIES ${PROJECT_NAME} CATKIN_DEPENDS message_runtime)

include_directories(${catkin_INCLUDE_DIRS})
