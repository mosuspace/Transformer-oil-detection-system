import sys
import json
import os
import sqlite3 as sql
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QHBoxLayout, QVBoxLayout, QGraphicsScene
from PyQt5.QtWidgets import QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QLabel
from PyQt5.QtWidgets import QMessageBox
from boolui import Ui_Form
import paramiko
from stat import S_ISDIR as isdir
from plt import *


# 被测物的光谱
listy = []

# 短路油的光谱
y1 = [23, 28, 64, 93, 125, 130, 129, 133, 135, 130, 131, 118, 124, 124, 124, 132, 124, 130, 128, 126, 133, 138, 121,
      129, 122, 128, 132, 128, 123, 132, 131, 130, 124, 126, 137, 134, 136, 132, 137, 125, 136, 130, 126, 123, 134, 138,
      144, 137, 138, 135, 161, 153, 147, 139, 137, 142, 140, 151, 153, 153, 159, 162, 157, 164, 164, 161, 163, 166, 171,
      169, 175, 188, 192, 194, 198, 207, 222, 221, 234, 238, 227, 229, 232, 231, 244, 233, 232, 244, 242, 259, 256, 265,
      267, 286, 275, 288, 294, 292, 292, 303, 301, 286, 288, 279, 274, 268, 269, 257, 250, 247, 252, 251, 251, 239, 246,
      234, 249, 253, 240, 239, 239, 240, 218, 211, 214, 210, 200, 208, 212, 191, 184, 185, 186, 180, 184, 169, 176, 174,
      182, 177, 171, 178, 167, 179, 178, 176, 171, 162, 167, 168, 165, 163, 159, 167, 162, 161, 154, 151, 156, 153, 152,
      148, 144, 140, 152, 147, 137, 136, 144, 150, 152, 154, 153, 154, 144, 138, 142, 133, 144, 139, 145, 139, 147, 138,
      138, 142, 138, 141, 135, 136, 138, 140, 134, 139, 140, 140, 132, 132, 138, 135, 138, 141, 146, 140, 139, 144, 143,
      136, 134, 141, 134, 140, 132, 141, 142, 141, 144, 137, 134, 144, 137, 133, 131, 139, 132, 131, 136, 150, 132, 129,
      134, 143, 142, 141, 139, 134, 143, 142, 141, 146, 142, 133, 134, 143, 134, 140, 132, 137, 148, 138, 134, 132, 144,
      138, 129, 129, 133, 136, 134, 128, 130, 139, 136, 138, 136, 135, 142, 140, 134, 139, 134, 139, 144, 128, 141, 143,
      136, 134, 146, 140, 138, 134, 140, 142, 134, 132, 150, 138, 133, 136, 139, 140, 140, 134, 146, 137, 140, 139, 134,
      145, 134, 136, 141, 131, 147, 138, 146, 133, 134, 143, 139, 136, 139, 127, 136, 125, 140, 134, 137, 140, 138, 142,
      135, 148, 142, 138, 141, 137, 140, 141, 135, 138, 135, 140, 137, 134, 131, 140, 146, 138, 132]
# 受潮油A型的光谱
y2 = [37, 62, 86, 127, 157, 168, 178, 189, 179, 192, 182, 185, 195, 216, 241, 319, 513, 860, 1299, 1893, 2764, 3824,
      7494, 26100, 30460, 20167, 9057, 6380, 5343, 4204, 3257, 2508, 1990, 1646, 1275, 989, 788, 660, 586, 530, 472,
      444, 415, 401, 377, 355, 346, 312, 290, 265, 257, 252, 244, 241, 236, 234, 237, 241, 250, 262, 257, 258, 257, 262,
      254, 266, 259, 263, 280, 290, 293, 312, 322, 345, 371, 385, 414, 424, 439, 460, 458, 445, 459, 439, 448, 460, 476,
      482, 469, 496, 493, 518, 510, 546, 573, 574, 594, 599, 587, 592, 576, 561, 539, 522, 516, 501, 481, 456, 464, 453,
      457, 442, 445, 437, 441, 428, 438, 424, 432, 420, 413, 394, 379, 369, 354, 347, 338, 332, 316, 317, 301, 286, 288,
      267, 278, 266, 253, 262, 262, 254, 256, 248, 229, 242, 241, 234, 228, 237, 234, 229, 226, 227, 209, 201, 206, 203,
      198, 191, 205, 195, 185, 196, 183, 179, 181, 185, 183, 187, 184, 183, 176, 174, 173, 174, 174, 169, 165, 170, 171,
      167, 173, 169, 178, 164, 164, 172, 171, 169, 176, 174, 156, 166, 159, 165, 167, 169, 168, 155, 161, 164, 164, 166,
      161, 168, 157, 162, 155, 161, 169, 161, 168, 162, 174, 163, 172, 168, 156, 151, 162, 169, 164, 160, 159, 159, 162,
      158, 164, 160, 166, 162, 167, 163, 166, 160, 162, 154, 158, 161, 164, 160, 155, 156, 171, 161, 159, 165, 163, 162,
      152, 161, 167, 158, 168, 165, 169, 162, 166, 163, 160, 164, 161, 166, 169, 153, 163, 163, 155, 165, 165, 161, 158,
      164, 161, 156, 170, 162, 173, 161, 158, 156, 162, 160, 155, 164, 151, 150, 160, 168, 165, 170, 157, 156, 158, 159,
      159, 160, 161, 169, 159, 168, 162, 154, 168, 153, 168, 154, 164, 172, 156, 170, 161, 161, 167, 160, 166, 157, 168,
      166, 165, 166, 164, 159, 159, 166, 175, 163, 163, 158, 166, 182, 155, 156, 166, 168, 162, 158, 158, 166, 157, 156,
      163]
# 受潮油B型的光谱
y3 = [42, 50, 89, 132, 183, 189, 194, 190, 205, 198, 210, 213, 215, 258, 306, 395, 592, 957, 1467, 2267, 3425, 5240,
      10804, 29062, 30910, 29198, 16499, 11330, 9528, 7609, 6062, 4990, 4176, 3518, 2786, 2114, 1597, 1225, 946, 773,
      655, 566, 505, 481, 442, 411, 389, 350, 314, 294, 282, 258, 255, 250, 256, 250, 246, 238, 270, 258, 264, 260, 270,
      276, 270, 268, 268, 272, 275, 292, 297, 311, 329, 338, 359, 378, 409, 417, 433, 452, 449, 449, 452, 462, 463, 474,
      486, 500, 502, 495, 525, 529, 556, 573, 603, 647, 645, 638, 644, 636, 617, 606, 582, 563, 544, 524, 502, 506, 486,
      478, 472, 461, 470, 469, 454, 464, 446, 448, 439, 446, 435, 416, 403, 385, 380, 364, 339, 343, 330, 330, 313, 304,
      301, 280, 280, 274, 274, 269, 260, 265, 259, 262, 246, 256, 246, 243, 240, 235, 226, 226, 220, 222, 220, 223, 205,
      209, 204, 200, 192, 187, 198, 199, 184, 181, 184, 192, 191, 176, 180, 191, 186, 180, 173, 171, 186, 175, 169, 180,
      178, 175, 174, 178, 177, 182, 175, 176, 175, 160, 168, 181, 185, 168, 167, 164, 169, 163, 175, 179, 164, 177, 177,
      167, 170, 170, 167, 171, 170, 172, 166, 175, 168, 178, 172, 180, 163, 168, 162, 161, 170, 173, 166, 174, 170, 162,
      174, 163, 176, 167, 161, 165, 161, 167, 164, 163, 159, 171, 165, 164, 162, 156, 160, 166, 156, 169, 160, 163, 166,
      174, 165, 164, 169, 162, 159, 156, 174, 158, 164, 162, 164, 164, 161, 172, 154, 162, 159, 166, 166, 164, 166, 163,
      149, 159, 153, 162, 171, 159, 161, 157, 162, 157, 165, 170, 168, 161, 160, 168, 179, 166, 167, 164, 164, 163, 164,
      164, 165, 167, 168, 160, 164, 162, 164, 162, 172, 165, 164, 162, 158, 175, 168, 163, 163, 166, 164, 156, 162, 152,
      171, 173, 174, 162, 160, 168, 167, 163, 162, 170, 178, 166, 166, 173, 171, 170, 162, 160, 171, 171, 161, 166, 156,
      167, 164]
# 原油的光谱
y4 = [40, 64, 96, 122, 147, 158, 164, 163, 161, 162, 159, 155, 158, 156, 156, 154, 160, 169, 172, 193, 199, 207, 233,
      432, 493, 309, 237, 225, 204, 192, 190, 182, 167, 164, 171, 167, 176, 169, 162, 170, 178, 189, 198, 204, 206, 213,
      206, 203, 207, 188, 194, 196, 201, 196, 204, 214, 220, 209, 229, 226, 233, 229, 236, 244, 237, 243, 253, 244, 257,
      264, 280, 304, 310, 327, 348, 392, 394, 423, 431, 433, 442, 442, 450, 447, 460, 458, 440, 460, 467, 474, 488, 498,
      514, 552, 554, 587, 584, 596, 590, 602, 585, 565, 547, 526, 510, 496, 489, 478, 487, 454, 452, 442, 448, 444, 442,
      444, 447, 432, 422, 411, 418, 400, 394, 394, 374, 356, 346, 330, 328, 307, 301, 289, 287, 284, 288, 265, 264, 259,
      266, 260, 254, 260, 260, 256, 250, 238, 241, 236, 239, 226, 222, 220, 218, 219, 220, 214, 199, 209, 203, 204, 204,
      195, 188, 189, 183, 191, 190, 185, 193, 184, 185, 186, 187, 189, 182, 179, 177, 182, 184, 178, 186, 176, 170, 188,
      176, 170, 179, 180, 176, 171, 178, 173, 172, 179, 174, 171, 176, 173, 170, 167, 181, 170, 171, 173, 166, 172, 171,
      170, 155, 166, 176, 173, 170, 169, 169, 172, 171, 160, 166, 167, 170, 162, 165, 168, 167, 178, 176, 166, 164, 172,
      162, 171, 174, 172, 172, 174, 177, 168, 162, 176, 176, 170, 168, 169, 164, 167, 172, 174, 174, 173, 178, 166, 172,
      171, 175, 161, 162, 171, 169, 176, 167, 169, 172, 169, 165, 160, 169, 181, 166, 166, 173, 162, 163, 163, 169, 178,
      173, 170, 174, 170, 162, 164, 160, 173, 159, 172, 167, 176, 171, 166, 167, 172, 166, 168, 169, 166, 165, 160, 171,
      169, 159, 171, 165, 178, 175, 172, 171, 170, 170, 166, 172, 173, 178, 170, 174, 170, 168, 173, 171, 169, 167, 176,
      176, 174, 170, 172, 165, 175, 162, 172, 179, 168, 164, 167, 167, 167, 164, 171, 164, 171, 168]


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # # 把父类里面的init功能执行了，代表父类里面有就让它去执行

        self.label_status = None
        self.sftp = None
        self.table_widget = None
        self.child_window = None
        self.setWindowTitle('光谱检测终端')
        self.resize(800, 600)

        # 窗口位置
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        # 创建布局
        layout = QVBoxLayout()
        layout.addLayout(self.init_header())
        layout.addLayout(self.init_table())
        layout.addLayout(self.init_footer())
        # 给窗体设置元素的排列方式
        self.setLayout(layout)

    def show_son(self):
        self.child_window = SonWindow()
        self.child_window.show()

    def init_header(self):
        # 1.创建顶部菜单布局
        head_layout = QHBoxLayout()
        # 1.1 创建标签和按钮，加入head_layout
        label_bool = QLabel("检测油光谱", self)
        head_layout.addWidget(label_bool)

        btn_view = QPushButton('查看')
        btn_view.clicked.connect(self.show_son)
        head_layout.addWidget(btn_view)
        # 弹簧
        head_layout.addStretch()
        return head_layout

    def init_table(self):
        # 2.创建中间的表格
        table_layout = QHBoxLayout()

        # 2.1 创建表格
        table_widget = QTableWidget(0, 3)
        self.table_widget = table_widget
        table_header = [
            {"field": "device", "text": "设备", "width": 120},
            {"field": "time", "text": "检测时间", "width": 260},
            {"field": "data", "text": "数据", "width": 380}
        ]
        for idx, info in enumerate(table_header):
            item = QTableWidgetItem()
            item.setText(info['text'])
            table_widget.setHorizontalHeaderItem(idx, item)
            table_widget.setColumnWidth(idx, info['width'])

        # 2.2 初始化表格数据
        # 读取数据文件

        table_layout.addWidget(table_widget)
        return table_layout

    def init_footer(self):
        # 4.创建底部菜单
        footer_layout = QHBoxLayout()

        label_status = QLabel("未同步", self)
        self.label_status = label_status
        footer_layout.addWidget(label_status)

        footer_layout.addStretch()

        btn_reinit = QPushButton("点击同步")
        btn_reinit.clicked.connect(self.datasyn)
        footer_layout.addWidget(btn_reinit)

        return footer_layout

    def down_from_remote(self, sftp_obj, remote_dir_name, local_dir_name):
        """远程下载文件"""
        remote_file = sftp_obj.stat(remote_dir_name)
        if isdir(remote_file.st_mode):
            # 文件夹，不能直接下载，需要继续循环
            self.check_local_dir(local_dir_name)
            print('开始下载文件夹：' + remote_dir_name)
            for remote_file_name in self.sftp.listdir(remote_dir_name):
                sub_remote = os.path.join(remote_dir_name, remote_file_name)
                sub_remote = sub_remote.replace('\\', '/')
                sub_local = os.path.join(local_dir_name, remote_file_name)
                sub_local = sub_local.replace('\\', '/')
                self.down_from_remote(sftp_obj, sub_remote, sub_local)
        else:
            # 文件，直接下载
            print('开始下载文件：' + remote_dir_name)
            self.sftp.get(remote_dir_name, local_dir_name)

    def check_local_dir(self, local_dir_name):
        """本地文件夹是否存在，不存在则创建"""
        if not os.path.exists(local_dir_name):
            os.makedirs(local_dir_name)

    # 数据库下载
    def datasyn(self):
        # 服务器连接信息
        host_name = '服务器公网ip'
        user_name = '用户名'
        password = '密码'
        port = 22
        # 远程文件路径（需要绝对路径）
        remote_dir = '/home/serve/testdata.db'
        # 本地文件存放路径（绝对路径或者相对路径都可以）
        local_dir = './testdata.db'

        # 连接远程服务器
        t = paramiko.Transport((host_name, port))
        t.connect(username=user_name, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        self.sftp = sftp
        # 远程文件开始下载
        self.down_from_remote(self.sftp, remote_dir, local_dir)

        # 关闭连接
        t.close()
        self.DataSynchronization()
        print("Success")
        self.label_status.setText("同步成功！")


        # 写入表格
    def DataSynchronization(self):
        con = sql.connect("testdata.db")  # 连接数据库
        cur = con.cursor()  # 游标对象
        cur.execute("SELECT J FROM sheet1")  # 选择sheet1表中的id，T，D三列
        list_big = cur.fetchall()  # 大列表,里面是元组

        for i in range(len(list_big)):
            z = len(list_big) - i - 1
            tu = list_big[z]  # 元组数据
            list_json = json.loads(tu[0])  # 还原元组数据原貌，是一个列表
            list_json[2] = json.dumps(list_json[2])  # 列表的第3项是列表，需要格式化，否则放不进去
            # 把数据填入表格
            current_row_count = self.table_widget.rowCount()  # 当前表格有多少行
            self.table_widget.insertRow(current_row_count)
            for m, ele in enumerate(list_json):
                cell = QTableWidgetItem(ele)
                cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                cell.setTextAlignment(Qt.AlignCenter)
                self.table_widget.setItem(current_row_count, m, cell)

        cur.close()


class SonWindow(QWidget, Ui_Form):
    def __init__(self):
        QObject.__init__(self)
        super().__init__()

        self.ui = Ui_Form()  # 使用ui文件导入定义界面类
        self.ui.setupUi(self)  # 初始化界面,执行类中的setupUi函数

        # 数据
        # xaxis坐标
        self.xaxis = [340, 342, 344, 346, 348, 350, 352, 354, 356, 358, 360, 362, 364, 366, 368, 370, 372, 374, 376, 378, 380,
             382,
             384, 386, 388, 390, 392, 394, 396, 398, 400, 402, 404, 406, 408, 410, 412, 414, 416, 418, 420, 422, 424,
             426,
             428, 430, 432, 434, 436, 438, 440, 442, 444, 446, 448, 450, 452, 454, 456, 458, 460, 462, 464, 466, 468,
             470,
             472, 474, 476, 478, 480, 482, 484, 486, 488, 490, 492, 494, 496, 498, 500, 502, 504, 506, 508, 510, 512,
             514,
             516, 518, 520, 522, 524, 526, 528, 530, 532, 534, 536, 538, 540, 542, 544, 546, 548, 550, 552, 554, 556,
             558,
             560, 562, 564, 566, 568, 570, 572, 574, 576, 578, 580, 582, 584, 586, 588, 590, 592, 594, 596, 598, 600,
             602,
             604, 606, 608, 610, 612, 614, 616, 618, 620, 622, 624, 626, 628, 630, 632, 634, 636, 638, 640, 642, 644,
             646,
             648, 650, 652, 654, 656, 658, 660, 662, 664, 666, 668, 670, 672, 674, 676, 678, 680, 682, 684, 686, 688,
             690,
             692, 694, 696, 698, 700, 702, 704, 706, 708, 710, 712, 714, 716, 718, 720, 722, 724, 726, 728, 730, 732,
             734,
             736, 738, 740, 742, 744, 746, 748, 750, 752, 754, 756, 758, 760, 762, 764, 766, 768, 770, 772, 774, 776,
             778,
             780, 782, 784, 786, 788, 790, 792, 794, 796, 798, 800, 802, 804, 806, 808, 810, 812, 814, 816, 818, 820,
             822,
             824, 826, 828, 830, 832, 834, 836, 838, 840, 842, 844, 846, 848, 850, 852, 854, 856, 858, 860, 862, 864,
             866,
             868, 870, 872, 874, 876, 878, 880, 882, 884, 886, 888, 890, 892, 894, 896, 898, 900, 902, 904, 906, 908,
             910,
             912, 914, 916, 918, 920, 922, 924, 926, 928, 930, 932, 934, 936, 938, 940, 942, 944, 946, 948, 950, 952,
             954,
             956, 958, 960, 962, 964, 966, 968, 970, 972, 974, 976, 978, 980, 982, 984, 986, 988, 990, 992, 994, 996,
             998,
             1000, 1002, 1004, 1006, 1008, 1010, 1012, 1014, 1016, 1018, 1020]

        # 初始化 gv_visual_data 的显示
        self.gv_visual_data_content = MyFigureCanvas(width=self.ui.graphicsView.width() / 101,
                                                     height=self.ui.graphicsView.height() / 101,
                                                     xlim=(200, 1100),
                                                     ylim=(0, 1500))  # 实例化一个FigureCanvas

        # 图形初始化
        self.plot_first()
        # 组合选择框响应
        self.ui.comboBox.currentIndexChanged.connect(self.handleSelectionChange)
        # self.plot_last()
        # 开始检测
        self.ui.pushButton.clicked.connect(self.plot_last)

    # 图形初始化
    def plot_first(self):
        self.gv_visual_data_content.axes.set_title('fitting curve')
        # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.graphic_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphic_scene.addWidget(
            self.gv_visual_data_content)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.ui.graphicsView.setScene(self.graphic_scene)  # 把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView.show()  # 调用show方法呈现图形

        # 组合选择框响应

    def handleSelectionChange(self):
        method = self.ui.comboBox.currentText()
        # global x
        if method == "原油":
            global y4
            self.gv_visual_data_content.axes.clear()  # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
            self.gv_visual_data_content.axes.plot(self.xaxis, y4, 'r-')  # 红色
            # x1 = list(range(1, 342))  # 一个包含从200 到682的列表
            self.gv_visual_data_content.axes.plot(self.xaxis, listy)  # 测试物质的图
            self.gv_visual_data_content.draw()  # 刷新画布显示图片，否则不刷新显示

        # 短路油
        if method == "电性故障油":
            global y1
            self.gv_visual_data_content.axes.clear()  # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
            self.gv_visual_data_content.axes.plot(self.xaxis, listy)
            self.gv_visual_data_content.axes.plot(self.xaxis, y1, 'b-')  # 蓝色
            self.gv_visual_data_content.draw()  # 刷新画布显示图片，否则不刷新显示

        if method == "受潮油A型":
            global y2
            self.gv_visual_data_content.axes.clear()  # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
            self.gv_visual_data_content.axes.plot(self.xaxis, listy)
            self.gv_visual_data_content.axes.plot(self.xaxis, y2, 'y-')  # 黄色
            self.gv_visual_data_content.draw()  # 刷新画布显示图片，否则不刷新显示

        if method == "受潮油B型":
            global y3
            self.gv_visual_data_content.axes.clear()  # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
            self.gv_visual_data_content.axes.plot(self.xaxis, listy)
            self.gv_visual_data_content.axes.plot(self.xaxis, y3, 'm-')  # 紫粉色
            self.gv_visual_data_content.draw()  # 刷新画布显示图片，否则不刷新显示

    def plot_last(self):
        global listy
        text = self.ui.lineEdit.text()
        print(text)
        con = sql.connect("testdata.db")  # 连接数据库
        cur = con.cursor()  # 游标对象
        cur.execute("SELECT J FROM sheet1")  # 选择sheet1表中的id，T，D三列
        print("获取列成功")
        list_1 = cur.fetchall()  # 返回一个每一行数据是列表一项的列表
        l = len(list_1)
        print(l)
        i = l - eval(text)
        print(i)
        tu1 = list_1[i]  # 倒序输出
        print(type(tu1))
        print(tu1)
        list_jj = json.loads(tu1[0])  # 需要的数据
        listy = list_jj[2]
        print(listy)
        print(type(listy))
        cur.close()
        # global x
        self.gv_visual_data_content.axes.clear()  # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
        self.gv_visual_data_content.axes.plot(self.xaxis, listy)
        self.gv_visual_data_content.axes.set_title('fitting curve')
        self.gv_visual_data_content.draw()  # 刷新画布显示图片，否则不刷新显示

        return listy


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
