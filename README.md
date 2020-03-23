# Aweme-Sign

douyin sign service

## Android Emulator

- [Genymotion](https://www.genymotion.com/)

    `Genymotion` 基于 `VirtualBox` 可以实现跨平台使用, 加上 `Genymotion_ARM_Translation` 的加持完美支持 `ARM`, 个人版本可免费使用。
    
    - https://www.genymotion.com/download/
    - https://docs.genymotion.com/desktop/3.0/
    - https://github.com/m9rco/Genymotion_ARM_Translation

## Frida

1. 本地安装`frida`

    ```bash
    $ pip install frida
    $ pip install frida-tools
    
    $ wget -O frida-server.xz https://github.com/frida/frida/releases/download/12.8.13/frida-server-12.8.13-android-x86.xz
    $ xz -d frida-server.xz
    ```

2. [`Android` 安装 `frida-server`](https://frida.re/docs/android/)
    
    ```bash
    $ adb root
    $ adb push frida-server /data/local/tmp/
    $ adb shell "chmod 755 /data/local/tmp/frida-server"
    $ nohup adb shell "/data/local/tmp/frida-server" &
    ```
3. 设置端口转发
    ```bash
    $ adb forward tcp:27042 tcp:27042
    $ adb forward tcp:27043 tcp:27043
    ```

4. 测试
    ```bash
    # 列出进程列表
    $ frida-ps -U

    # 只列出应用
    $ frida-ps -Ua

    # 列出所有安装的应用
    $ frida-ps -Uai

    # 进入应用
    $ frida -U -f com.ss.android.ugc.aweme
    ```
5. Run sign server
    ```bash
    gunicorn -w 1 -b 0.0.0.0:5000 app:app
    ```
   
# frp

```bash
# run frida-server
$ adb shell "/data/local/tmp/frida-server -l 0.0.0.0"

# frps
$ docker run --name frps -d --restart always -p 7000:7000 -p 5555:5555 -p 27042:27042 maguowei/frp

# adb
$ docker run --name adb -d --network host --restart always maguowei/frp /frp/frpc tcp -n adb --server_addr ${SERVER_IP}:7000 --local_ip 192.168.56.103 --local_port 5555 --remote_port 5555
$ adb connect ${SERVER_IP}:5555

# frida-server
$ docker run --name frida-server -it --rm --network host maguowei/frp /frp/frpc tcp -n frida-server --server_addr ${SERVER_IP}:7000 --local_ip 192.168.56.103 --local_port 27042 --remote_port 27042
# test
$ frida-ps -H ${SERVER_IP}:27042
```

## 参考链接

- [frida](https://github.com/frida/frida)
- [frida-all-in-one](https://github.com/hookmaster/frida-all-in-one)
- [Android 调试桥 (adb)](https://developer.android.com/studio/command-line/adb)
- [常用adb命令汇总](http://mumu.163.com/help/func/20190129/30131_797867.html)
