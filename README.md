# douyin-sign

douyin sign service

## 安装

1. 本地安装`frida`

    ```bash
    $ pip install frida
    $ pip install frida-tools
    
    $ wget -O frida-server.xz https://github.com/frida/frida/releases/download/12.8.13/frida-server-12.8.13-android-x86.xz
    $ xz -d frida-server.xz
    ```

2. `Android` 安装 `frida-server`

    ```bash
    $ adb push frida-server /data/local/tmp/frida-server
    
    # 进入
    $ adb shell
    $ su
    $ cd /data/local/tmp
    $ chmod +x frida-server
    
    # 启动 server
    $ ./frida-server
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
    # 进入应用
    $ frida -U -f com.ss.android.ugc.aweme
    ```

## 参考链接

- [frida](https://github.com/frida/frida)
- [常用adb命令汇总](http://mumu.163.com/help/func/20190129/30131_797867.html)