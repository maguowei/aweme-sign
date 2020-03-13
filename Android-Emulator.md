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