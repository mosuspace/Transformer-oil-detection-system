#  连接回调
def on_connect(client, userdata, flags, rc):
    print ("连接")
    print("Connected with result code: " + str(rc))

#  消息内容回调
def on_message(client, userdata, msg):
    print("消息内容")
    print(msg.topic + " " + str(msg.payload))


#   订阅回调
def on_subscribe(client, userdata, mid, granted_qos):
    print("订阅")
    print("On Subscribed: qos = %d" % granted_qos)
    pass


#   取消订阅回调
def on_unsubscribe(client, userdata, mid, granted_qos):
    print("取消订阅")
    print("On unSubscribed: qos = %d" % granted_qos)
    pass


#   发布消息回调
def on_publish(client, userdata, mid):
    print("发布消息")
    print("On onPublish: qos = %d" % mid)
    pass


#   断开链接回调
def on_disconnect(client, userdata, rc):
    print("断开链接")
    print("Unexpected disconnection rc = " + str(rc))
    pass
