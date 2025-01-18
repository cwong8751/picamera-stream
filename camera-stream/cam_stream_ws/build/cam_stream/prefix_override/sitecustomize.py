import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/drone/camera-stream/cam_stream_ws/install/cam_stream'
