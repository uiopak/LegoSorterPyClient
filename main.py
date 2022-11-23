import time
import cv2
import grpc

from generated import LegoAnalysisFast_pb2_grpc as LegoAnalysisFast_pb2_grpc
from generated import LegoAnalysisFast_pb2 as LegoAnalysisFast__pb2


def send_img(img, stub):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
    stub.DetectAndClassifyBricks(
        LegoAnalysisFast__pb2.FastImageRequest(image=cv2.imencode('.jpg', img, encode_param)[1].tobytes(),
                                               rotation=90, session=""))


def test_img(path):
    img_bgr = cv2.imread(path)
    # img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # show image
    cv2.imshow('image', img_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = LegoAnalysisFast_pb2_grpc.LegoAnalysisFastStub(channel)
        send_img(img_bgr, stub)
        print("IMG send")


wait_milliseconds = 500

if __name__ == '__main__':
    # test_img('G:\\LEGO\\noweLego\\LegoSorterServer\\lego_sorter_server\\images\\storage\\stored\\Session_1\\0182bb46-e751-7c0b-8e17-28b28b3583e6.jpg')
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # for windows
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    # ret, frame = cam.read()
    # cv2.imshow('image', frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
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

