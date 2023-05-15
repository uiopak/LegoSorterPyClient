import os
os.environ['OPENCV_LOG_LEVEL'] = 'silent'

import cv2


def get_available_cameras():
    """Get a list of available cameras"""
    cameras = []
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cameras.append(i)
            cap.release()
    return cameras

def choose_camera(cameras):
    """Choose a camera from the list of available cameras"""
    while True:
        try:
            camera_index = int(input(f"Choose camera index from available cameras: {cameras}: "))
            if camera_index in cameras:
                return camera_index
            else:
                print("Invalid camera index. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def open_camera(camera_index):
    """Open the selected camera"""
    cap = cv2.VideoCapture(camera_index) # default
    # cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW) # DirectShow (Windows)
    # cap = cv2.VideoCapture(camera_index, cv2.CAP_V4L2) # Video for Linux
    return cap

def configure_camera(cap):
    """Configure the camera resolution, frame rate and exposure"""
    # Get current values
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    exposure = cap.get(cv2.CAP_PROP_EXPOSURE)

    # Set new values
    new_width = input(f"Enter desired width (current: {width}) or hit enter to keep current value: ")
    new_height = input(f"Enter desired height (current: {height}) or hit enter to keep current value: ")
    new_fps = input(f"Enter desired FPS (current: {fps}) or hit enter to keep current value: ")
    new_exposure = input(f"Enter desired exposure (current: {exposure}) or hit enter to keep current value: ")

    if new_width:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(new_width))
    if new_height:
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(new_height))
    if new_fps:
        cap.set(cv2.CAP_PROP_FPS, int(new_fps))
    if new_exposure:
        cap.set(cv2.CAP_PROP_EXPOSURE, float(new_exposure))

def display_video(cap):
    """Display a video stream from the camera"""
    while True:
        # Read an image from the camera
        ret, frame = cap.read()

        # Display the image
        cv2.imshow("Camera", frame)

        # Wait for a key press or window close
        key = cv2.waitKey(1)
        if key == ord('q') or cv2.getWindowProperty("Camera", cv2.WND_PROP_VISIBLE) < 1:
            break

def main():
    # Change the way OpenCV displays errors
    # cv2.utils.logging.setLogLevel(cv2.utils.logging.LOG_LEVEL_SILENT)

    # Get a list of available cameras
    cameras = get_available_cameras()

    # Choose a camera
    camera_index = choose_camera(cameras)

    # Open the selected camera
    cap = open_camera(camera_index)

    # Configure the camera resolution and frame rate
    configure_camera(cap)

    display_video(cap)

    # Release the camera resources
    cap.release()

    # Close all windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
   main()
