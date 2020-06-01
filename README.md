# Aweme-Sign

douyin sign service

## Android Emulator

- [Genymotion](https://www.genymotion.com/)

    `Genymotion` 基于 `VirtualBox` 可以实现跨平台使用, 加上 `Genymotion_ARM_Translation` 的加持完美支持 `ARM`, 个人版本可免费使用。
    
    - https://www.genymotion.com/download/
    - https://docs.genymotion.com/desktop/3.0/
    - https://github.com/m9rco/Genymotion_ARM_Translation

## Frida 

- [`Emulator` 安装 `frida-server`](https://frida.re/docs/android/)

    ```bash
    $ wget -O frida-server.xz https://github.com/frida/frida/releases/download/12.8.13/frida-server-12.8.13-android-x86.xz
    $ xz -d frida-server.xz

    $ adb root
    $ adb push frida-server /data/local/tmp/
    $ adb shell "chmod 755 /data/local/tmp/frida-server"
    $ adb shell "/data/local/tmp/frida-server -l 0.0.0.0"
    ```

## frp

```bash
# frps
$ docker run --name frps -d --restart always -p 7000:7000 -p 5555:5555 -p 27042:27042 maguowei/frp

# 将模拟器注册为远程设备
$ export SERVER_IP=xxx.xxx.xxx.xxx   # frps server ip
$ export LOCAL_IP=192.168.56.103    # device ip
# adb
$ docker run --name adb -d --network host --restart always maguowei/frp /frp/frpc tcp -n adb --server_addr ${SERVER_IP}:7000 --local_ip ${LOCAL_IP} --local_port 5555 --remote_port 5555

# test 使用下面的命令连接上面注册的设备
$ adb connect ${SERVER_IP}:5555
```

## Run

```bash
$ cp .env.tpl .env
$ make run
```

## 参考链接

- [frida](https://github.com/frida/frida)
- [frida-all-in-one](https://github.com/hookmaster/frida-all-in-one)
- [Android 调试桥 (adb)](https://developer.android.com/studio/command-line/adb)
- [awesome-adb](https://github.com/mzlogin/awesome-adb)
