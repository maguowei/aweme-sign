# Android Emulator

- [google/android-emulator-container-scripts](https://github.com/google/android-emulator-container-scripts)
- docker image
  - [android4docker/q-google-x86](https://hub.docker.com/r/android4docker/q-google-x86)
  - [android4docker/n-google-a32](https://hub.docker.com/r/android4docker/n-google-a32)

## Run
```bash
# for x86
docker run --device /dev/kvm --publish 8554:8554/tcp --publish 5555:5555/tcp android4docker/q-google-x86:30.0.0
```

## adb usage

1. 系统文件获取读写权限
    ```bash
    `/android/sdk/launch-emulator.sh`
    
    # https://developer.android.com/studio/run/emulator-commandline
    `-writable-system`
    
    # example
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