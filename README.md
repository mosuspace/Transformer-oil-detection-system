## 基于龙芯教育派的云端互联变压器油检测系统
### 项目概况

项目包含Development-board-side、Server-side、Multi-device-data-display-panel三部分。

Development-board-side目录下是在龙芯教育派上运行的代码部分，是此项目的核心。需要采集数据、处理数据、可视化数据并将数据上传到云服务器中，还会对检测结果进行微信预警，这是我们的一个创新点。

Server-side目录下是在云服务器上运行的代码，它会将龙芯教育派每次采集处理后光谱数据保存在服务器的数据库中。

Multi-device-data-display-panel目录下是在检测端运行的代码，这是我们的创新点，当设备以一定数量被部署在一个区域后，它以一个数据面板的形式可以查看所有设备采集的信息和显示图像。

![image](https://user-images.githubusercontent.com/90094412/176990197-24303de0-ffe5-473b-974c-65b9e5e46ffe.png)

