import rospy
from std_msgs import Float32
q = 0.15

def callback(data):
    temp = data / q
    pub = rospy.Publisher('/kthfs/result', Float32, queue_size=1)
    rospy.init_node('talker', anonymous=False)
    rate = rospy.Rate(20)
    msg = Float32();
    msg.data = temp
    pub.publish(msg)
    
def listener():
    rospy.init_node('listener', anonymous=False)
    rospy.Subscriber("malhotra", Float32, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
