# Ultralytics

## Running Ultralytics container with camera support
```
docker run -it --ipc=host --runtime=nvidia --device=/dev/video0 --device=/dev/i2c-9 --env DISPLAY:$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/argus_socket:/tmp/argus_socket --cap-add SYS_PTRACE -v $PWD/:/scripts ultralytics/ultralytics:latest-jetson-jetpack6
```


**For some reason, this has stopped working**