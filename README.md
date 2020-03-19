# Aweme-Sign

douyin sign service

## Android Emulator

- [Genymotion](https://www.genymotion.com/)
- [网易MuMu模拟器](https://mumu.163.com/)
- [雷电模拟器](https://www.ldmnq.com/)

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
## 参考链接

- [frida](https://github.com/frida/frida)
- [frida-all-in-one](https://github.com/hookmaster/frida-all-in-one)
- [常用adb命令汇总](http://mumu.163.com/help/func/20190129/30131_797867.html)
