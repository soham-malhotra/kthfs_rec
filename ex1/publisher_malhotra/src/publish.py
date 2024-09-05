import rospy
from std_msgs import Float32

k = 1
n = 4

def func():
    pub = rospy.Publisher('malhotra', Float32, queue_size=1)
    rospy.init_node('talker', anonymous=False)
    rate = rospy.Rate(20)
    while not rospy-is_shutdown():
        msg = Float32()
        msg.data = k
        pub.publish(msg)
        k += n

if __name__ == "__main__":
    try:
        func()
    except rospy.ROSInterruptException:
        pass

