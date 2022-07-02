# -*- coding:utf-8 -*-
"""
作者：刘墨苏
"""

import binascii
import serial
import time
import json
import paho.mqtt.client as mqtt     # 导入paho.mqtt模块
from mqttfunction import *      # 导入mqtt的回调函数

class Data(object):
    # 默认初始化
    def __init__(self):
        self.Serial_receive()


    def Serial_receive(self):
        """
        串口数据接收、预处理和保存
        :return:
        """
        t = serial.Serial('/dev/ttyUSB0',9600)
        #t = serial.Serial('com4', 9600)

        try:  # 如果输入不是十六进制数据
            t.write(bytes.fromhex("S"))
        except:  # 则将其作为字符串输出
            t.write(bytes("S", encoding='utf-8'))

        time.sleep(5)  # sleep() 与 inWaiting() 最好配对使用
        num = t.inWaiting()  # inWaiting()：返回接收缓存中的字节数
        data = str(binascii.b2a_hex(t.read(4113)))[2:-1]  # 十六进制显示方法2
        time.sleep(0.1)

        with open('pc_data.txt', 'w') as f:
            f.write(data[2:2742] + '\n')
            f.write(data[2742:5482] + '\n')
            f.write(data[5482:8226])


    def List_fenge(self):
        """
        处理串口接收保存在txt的数据，把数据处理成列表
        :return:
        """
        alist = []
        with open('pc_data.txt', 'r') as f:
            content = f.read()
            # 将文件内容字符串 按换行符 切割 到列表中，每个元素依次对应一行，可以把换行符去掉
            linelist = content.splitlines()  # 所以有三个元素的列表
            # print(linelist)
            for line in linelist:
                # print(line)
                for i in range(0, len(line), 4):
                    alist.append(line[i:i + 4])
        # print(alist)
        return alist


    def Data_conversion(self, strParam):
        """
        把16进制的字符串转换为10进制的字符串
        strParam是一个16进制的字符串，应该仅包含数字0-9和字母ABCDEF。开头可以是0x。
        如果不符合16进制的格式要求，我们将会返回 return False
        """
        if strParam == '' or strParam is None:
            return False
        if strParam[0] == '0' and strParam[1] == 'x':
            strParam = strParam[2:]
        strParam = strParam.upper()
        len_of_hex = strParam.__len__()
        dic_of_hex = {
                "0": 0,
                "1": 1,
                "2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6,
                "7": 7,
                "8": 8,
                "9": 9,
                "A": 10,
                "B": 11,
                "C": 12,
                "D": 13,
                "E": 14,
                "F": 15
            }
        result = 0  # 设置初值
        for elem_of_strParam in strParam:
            if elem_of_strParam in dic_of_hex:
                # 幂运算改为位运算，计算效率更高
                result = result + (dic_of_hex[elem_of_strParam] << (4 * (len_of_hex - 1)))
                len_of_hex -= 1
            else:
                return False
        return result


    def List_zhuanhaun(self, list_1):
        """
        16进制列表转换为10进制列表
        """
        alist1 = []
        for x in list_1:
            hex_changes = self.Data_conversion(x)
            alist1.append(hex_changes)
            # print(m)
        return alist1


    def function(self, the_list):
        """
        处理列表，把列表每6项进行平均简化为新列表的一项，返回一个归一化的341个元素的列表，这个列表就是我最终需要的列表
        """
        alist = []
        i = 0
        for x in range(341):
            blist = the_list[i:i + 6]  # 修改
            # print(blist)
            i += 6  # 修改
            the_sum = sum(blist)
            the_length = len(blist)
            the_average = round(the_sum / the_length)

            alist.append(the_average)
        return alist

    # def mqttcon(self, Str1):
    #     client = mqtt.Client("slave")
    #     client.on_connect = on_connect
    #     client.on_publish = on_publish
    #     client.connect('47.100.193.192', 1883, 60)  # 60为keepalive的时间间隔
    #     client.loop_start()
    #     client.publish(topic='usb2000_data', payload=Str1, qos=0, retain=False)
    #     time.sleep(0.1)
    #     client.loop_stop()

    # 在这个函数里面进行数据的进一步处理

    def main(self):
        time.sleep(0.1)
        list_1 = self.List_fenge()  # 处理好的初始列表 list_1
        list_2 = self.List_zhuanhaun(list_1)  # 转换为10进制的列表 list_2
        del list_2[0:9]     # 删除前面的共同像素
        del list_2[-1]      # 删除后面的结束标志像素
        list_3 = self.function(list_2)
        return list_3


