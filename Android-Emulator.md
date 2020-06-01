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

## Other Tools

- [jadx](https://github.com/skylot/jadx)
- [Apktool](https://github.com/iBotPeaches/Apktool)
- [objection](https://github.com/sensepost/objection)
