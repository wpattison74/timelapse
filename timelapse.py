from time import sleep
import picamera

WAIT_TIME = 60

with picamera.PiCamera() as camera:
	camera.resolution = (1920, 1080)
	camera.iso = 800
	#camera.brightness = 50 
	#camera.exposure_mode = 'auto'
	camera.rotation = 180
	for filename in camera.capture_continuous('/mnt/timelapse/img-{timestamp:%y-%m-%d-%H-%M-%S-%f}.jpg'):
		sleep(WAIT_TIME)
