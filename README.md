# build
* x86平台编译
```shell
mkdir -p build && cd  build 
cmake ..
make
```

* rv1126平台编译
```shell
mkdir -p build && cd  build 
cmake .. -DCHIP=rv1126
make
```

* hi3516平台编译
```shell
mkdir -p build && cd  build 
cmake .. -DCHIP=hi3516
make
```

# example
* producer.cpp 获取音视频数据存放到sring中
```shell
视频sring id 114
音频sring id 115
```

* rtcdc.cpp 将连接IP地址,
```shell
视频sring id 114
音频sring id 115
```


# run
* 在rtc_push/target 目录下生成 producer，在SSH终端运行 ./producer
* 在rtc_push/target 目录下生成 rtcdc，在SSH终端运行 ./rtcdc
