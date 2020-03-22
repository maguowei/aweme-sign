# Android Emulator

- [google/android-emulator-container-scripts](https://github.com/google/android-emulator-container-scripts)
- docker image
  - [android4docker/q-google-x86](https://hub.docker.com/r/android4docker/q-google-x86)
  - [android4docker/n-google-a32](https://hub.docker.com/r/android4docker/n-google-a32)

## Run
```bash
# for x86
docker run -d --device /dev/kvm -p 8554:8554 -p 5555:5555 android4docker/q-google-x86:30.0.0
```

## adb usage

1. 系统文件获取读写权限
    ```bash
    docker run -d --device /dev/kvm -p 8554:8554 -p 5555:5555 -v $PWD/launch-emulator.sh:/android/sdk/launch-emulator.sh android4docker/o-google-x86:30.0.0
    
    # https://developer.android.com/studio/run/emulator-commandline
    `-writable-system`
    
    # launch-emulator.sh
    exec emulator/emulator @Pixel2 -no-audio -verbose -wipe-data \
      -ports 5556,5557 \
      -writable-system \
      -grpc 8554 -no-window -skip-adb-auth \
      -no-snapshot \
      -shell-serial file:/tmp/android-unknown/kernel.log \
      -logcat-output /tmp/android-unknown/logcat.log \
      -feature  AllowSnapshotMigration \
      -gpu swiftshader_indirect \
      -metrics-collection -shell-serial file:/tmp/android-unknown/kernel.log -logcat-output /tmp/android-unknown/logcat.log ${EMULATOR_PARAMS} -qemu -append panic=1
    
    
    adb root
    adb remount
    ```
2. busybox install
    
    - [dowoload busybox](https://busybox.net/downloads/binaries/)
    ```bash
    adb push busybox /system/xbin
    adb shell
       cd /system/xbin
       chmod +x busybox
       busybox --install .
    ```
   
3. arm libhoudini
    ```bash
    # Genymotion /system/bin/flash-archive.sh
    # Genymotion /system/etc/init.genymotion.sh
    armabi() {
        _abilist=x86
        is_genymotion_cloud_product && _abilist=x86_64,x86
    
        # ARM applications
        if [ -f /system/lib/libhoudini.so ]; then
            # Allow installation of ARM apps
            setprop ro.product.cpu.abi2 armeabi-v7a
            setprop ro.product.cpu.abilist $_abilist,armeabi-v7a,armeabi
            setprop ro.product.cpu.abilist32 x86,armeabi-v7a,armeabi
            # Enable native bridge for ARM apps
            setprop ro.dalvik.vm.isa.arm x86
            setprop ro.dalvik.vm.native.bridge libhoudini.so
        else
            setprop ro.dalvik.vm.native.bridge 0
            setprop ro.product.cpu.abilist $_abilist
            setprop ro.product.cpu.abilist32 x86
        fi
    
        # ARM executables
        if [ -f /system/bin/houdini ]; then
            # Enable execution of ARM executables
            setprop ro.enable.native.bridge.exec 1
            mount -t binfmt_misc binfmt_misc /proc/sys/fs/binfmt_misc
            cp /system/etc/binfmt_misc/arm_exe /proc/sys/fs/binfmt_misc/register
            cp /system/etc/binfmt_misc/arm_dyn /proc/sys/fs/binfmt_misc/register
        fi
    }
    ```
