# -*- coding:utf-8 -*-
"""
作者：刘墨苏
"""

import paho.mqtt.client as mqtt
import json
import sqlite3 as sql
import time


def aqlsave(a):
    con = sql.connect("testdata.db")  # 连接数据库
    cur = con.cursor()  # 游标对象
    # 数据库初始化,运行一次之后注释
    # cur.execute("CREATE TABLE sheet1(id TEXT PRIMARY KEY NOT NULL,J TEXT)")  # 创建一个有2列的表
    # con.commit()  # 提交一次
    t = time.gmtime()
    T1 = time.strftime("%Y-%m-%d %H:%M:%S", t)  # 当前的时间
    cur.execute("INSERT INTO sheet1(id,J) VALUES(?,?)", (T1, a))  # ?是占位符，写入数据
    print(T1)
    con.commit()  # 提交一次
    con.close()

#	链接回调
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


#	消息信息回调
def on_message(client, userdata, msg):
    get_data = msg.payload  # bytes b'[s]
    string = get_data.decode()  # string ，还原格式
    # sqljson= json.loads(string)
    aqlsave(string)     # 存入数据库
    # print(string)
    # print(type(string))
    # print(msg.topic + " " + str(msg.payload))


#   订阅回调
def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)
    pass


#   取消订阅回调
def on_unsubscribe(client, userdata, mid):
    print("取消订阅")
    print("On unSubscribed: qos = %d" % mid)
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


if __name__ == '__main__':

    client = mqtt.Client("rev")
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.on_disconnect = on_disconnect
    client.on_unsubscribe = on_unsubscribe
    client.on_subscribe = on_subscribe

    client.connect('服务器公网IP', 1883, 60)  # 60为keepalive的时间间隔
    # 当 qos>0 时，发送消息队列的最大值，默认是 0 ，表示无限制。当队列满时，旧消息会丢弃。
    client.subscribe('usb2000_data', qos=0)

    # loop_forever()  =>  该函数是保持永久连接, 阻塞式,可结合多线程或多进程的方式使用
    client.loop_forever()  # 保持连接
