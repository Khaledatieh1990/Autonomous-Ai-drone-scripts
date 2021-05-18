import jetson.utils
import 

cams = []

def create_camera(csi_port): 
    cams.append(jetson.utils.videoSource("csi://" + str(csi_port)))

def get_image_size(camera_id):
	return cams[camera_id].GetWidth(), camera.GetHeight()

def get_video(camera_id):
    return cams[camera_id].Capture()

def close_cameras():
    for cam in cams:
        cam.Close()