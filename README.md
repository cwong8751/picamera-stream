To run the stream, run this command:
```

./mjpg_streamer -i "./input_uvc.so -d /dev/video0 -r 640x480 -f 30" -o "./output_http.so -p 8080 -w ./www"

```

Then visit 
```
http://carlpi:8080
```

Navigate to the stream section



## below is deprecated
# picamera-stream
Flask server that hosts a real time stream from pi camera.

## what it does
A flask server 

## how to run
1. Open terminal
2. ```cd PATH\TO\FOLDER```
3. Activate the virtual environment ```source /pienv/bin/activate```
4. Run ```python3/python serve.py```
5. Navigate to ```http://ip_to_server/camera```

## what is this for
wurc 2024
