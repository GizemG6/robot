import cv2

def FaceDetect():

	face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')

	# capture frames from a camera
	cap = cv2.VideoCapture(0)

	# reads frames from a camera
	ret, img = cap.read()

	# convert to gray scale of each frames
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Detects faces of different sizes in the input image
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	if faces.all():
		print("yuz var")
		return 1
	else:
		print("yuz yok")
		return 0

FaceDetect()



