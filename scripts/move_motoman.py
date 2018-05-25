#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

print "============== Starting tutorial setup"
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("move_motoman", anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("manipulator")
print "============== Reference frame: %s" % group.get_planning_frame()
print "============== Reference frame: %s" % group.get_end_effector_link()
print "============== Robot Groups:"
print robot.get_group_names()

#YOUR CODE

print "random target"
group.set_random_target()
group.go(wait=True)
group.clear_pose_targets()
rospy.sleep(1)

print "home"
group.set_named_target("home")
group.go(wait=True)
group.clear_pose_targets()
rospy.sleep(1)

print "joints"
joint_states={"joint_s":1, "joint_l":1, "joint_e":1, "joint_u":1, "joint_r":1, "joint_b":1, "joint_t":1}
group.set_joint_value_target(joint_states)
group.go(wait=True)
group.clear_pose_targets()
rospy.sleep(1)

print "pose"
pose_target= geometry_msgs.msg.Pose()
pose_target.orientation.x = 1
pose_target.orientation.y = 0
pose_target.orientation.z = 0
pose_target.orientation.w = 0
pose_target.position.x = 0.5
pose_target.position.y = 0
pose_target.position.z = 0.3
group.set_pose_target(pose_target)

group.go(wait=True)
group.clear_pose_targets()
rospy.sleep(1)

moveit_commander.roscpp_shutdown()

