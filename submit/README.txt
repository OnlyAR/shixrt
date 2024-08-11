    【赛题一】可执行程序及代码

提交时间：2023年5月24日

运行说明:
  可执行程序为 main_glibc217，运行时请确保 GLIBC 版本 >=2.17！
  将名为 data1.csv 的数据文件放置在 main_glibc217 同目录下，执行命令：
    ./main_glibc217
  程序会自动读取 data1.csv 文件，计算结果并输出到 result.csv 文件中。

代码说明:
  代码文件夹是 src/，若因为依赖版本问题可执行文件无法正常运行，可通过执行源代码来运行程序。
  确保名为 data1.csv 的数据文件放置在 src/ 同目录下，运行命令为：
    python3 src/main.py 或 python src/main.py

打包构建环境:
  系统环境:
    - 在 Docker centos:7 官方镜像容器中构建
    - Linux 版本: CentOS Linux 7 (Core)
    - GLIBC 版本: 2.17
  Python 环境:
    - Python 版本：3.9.19
    - Python 包依赖:
      - numpy==1.23.1
      - scipy==1.9.3
    - 打包工具: pyinstaller==6.7.0