#!/usr/bin/env python3
import rospy
import tf2_ros
import geometry_msgs.msg
import math

def handle_planet_pose(planet_radius,star,planet,x):

    br=tf2_ros.TransformBroadcaster()
    t=geometry_msgs.msg.TransformStamped()
    t.header.stamp=rospy.Time.now()
    t.header.frame_id=star
    t.child_frame_id=planet

    t.transform.translation.x=planet_radius*math.sin(x)
    t.transform.translation.y=planet_radius*math.cos(x)
    t.transform.translation.z=0.0
    t.transform.rotation.x=0
    t.transform.rotation.y=0
    t.transform.rotation.z=0
    t.transform.rotation.w=1

    br.sendTransform(t)
    print(t)
    rate.sleep()

if __name__=='__main__':
    rospy.init_node('star_position',anonymous=True)
    rate=rospy.Rate(100)

    astra=rospy.get_param('/celestial_bodies')
    print(astra)

    while not rospy.is_shutdown():
        x=rospy.Time.now().to_sec()
        handle_planet_pose(astra['mars']['radius'],'sun','mars',astra['mars']['vel']*x)
        handle_planet_pose(astra['phobos']['radius'],'mars','phobos',astra['phobos']['vel']*x)
