import rospy
from std_msgs import Float32
q = 0.15

def callback(data):
    temp = data.data / q
    pub.publish(temp)
    rate.sleep()
    
def listener():
    global pub
    rospy.init_node('listener', anonymous=False)
    rospy.Subscriber("malhotra", Float32, callback)
    pub = rospy.Publisher('/kthfs/result', Float32)
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
