import time
import cv2
import grpc

from generated import LegoAnalysisFast_pb2_grpc as LegoAnalysisFast_pb2_grpc
from generated import LegoAnalysisFast_pb2 as LegoAnalysisFast__pb2

wait_milliseconds = 500
camera_index = 2
width = 1920
height = 1080
fps = 30
# exposure = 384 # tested camera was not changing

rotation = 90 # 90 or 270


def send_img(img, stub):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 95]
    stub.DetectAndClassifyBricks(
        LegoAnalysisFast__pb2.FastImageRequest(image=cv2.imencode('.jpg', img, encode_param)[1].tobytes(),
                                               rotation=rotation, session=""))


if __name__ == '__main__':
    cam = cv2.VideoCapture(camera_index) # default
    # cam = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW) # DirectShow (Windows)
    # cam = cv2.VideoCapture(camera_index, cv2.CAP_V4L2) # Video for Linux
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cam.set(cv2.CAP_PROP_FPS, fps)
    # cam.set(cv2.CAP_PROP_EXPOSURE, float(exposure))
    ret, frame = cam.read()

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = LegoAnalysisFast_pb2_grpc.LegoAnalysisFastStub(channel)
        while(True):
            start_time = time.time()
            # get image from web camera
            ret, frame = cam.read()
            send_img(frame, stub)
            elapsed_milliseconds = int((time.time() - start_time) * 1000)
            diff = wait_milliseconds - elapsed_milliseconds
            if diff > 0:
                time.sleep(diff/1000)
