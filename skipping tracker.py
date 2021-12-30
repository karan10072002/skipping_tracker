import cv2
import numpy
import datetime

frame_height=310
frame_width=600

lower_black=(20,20,20)
upper_black=(51,51,51)

lower_blue=(102,51,0)
upper_blue=(255,253,51)

lowest_point=0
def detect_black(frame,upper_limit,lower_limit):
	global lowest_point
	frame=cv2.resize(frame,(frame_width,frame_height))
	mask=cv2.inRange(frame, lower_limit, upper_limit)
	active=[]
	active_column=[]
	for row in range(0,frame_width,10):
		for column in range(0, frame_height,10):
			if mask[column, row]==255:
				active.append([row,column])
				active_column.append(column)
	try:
		lowest_point=min(active_column)
	except:
		pass
	# print(active)
	return mask

# image_frame=cv2.imread('Screenshot (7).png',1)
# cv2.imshow('mask', detect_black(image_frame,upper_blue,lower_blue))

skips=0

# image_frame=cv2.VideoCapture('http://192.168.43.1:8080/video')
# image_frame=cv2.VideoCapture(0)
image_frame=cv2.VideoCapture('VID_20200614_175548.mp4')

a=1
jump=0
base_line=0
while True:
	if a==31:
		print('..................')
		base_line=lowest_point

	if base_line!=0 and lowest_point-base_line>=18 and a>=32:
		jump=1
	if base_line!=0 and lowest_point<base_line and jump==1 and a>=32:
		skips+=1
		jump=0
	a+=1

	print('lowest_point: ',lowest_point)
	print('base_line: ',base_line)
	print('no. of skips: ',skips)
	ret, frames=image_frame.read()
	k=detect_black(frames,upper_blue,lower_blue)
	font=cv2.FONT_HERSHEY_SIMPLEX
	cv2.line(k, (0,base_line), (1800, base_line), (255,0,0),2)
	cv2.line(k, (0,lowest_point), (1800, lowest_point), (255,0,0),1)
	cv2.putText(k, str(skips), (20,20),font, 1, 	(255,255,255), 1)
	cv2.imshow('mask',k )
	# time=datetime.datetime.now().strftime('%H:%M:%S')
	# frame=cv2.resize(frames,(frame_width,frame_height))
	# cv2.line(frames, (0,base_line), (1800, base_line), (0,255,0),5)
	# cv2.line(frames, (0,base_line), (1800, lowest_point), (255,0,0),3)
	# cv2.putText(frames, 'skips: '+str(skips), (88,190),font, 4, (255,255,255), 9)
	# cv2.putText(frames, 'current datetime: '+time, (88,70),font, 2, (0,0,0), 4)
	cv2.imshow('skipping',frames)
	cv2.waitKey(1)

# cv2.waitKey(0)
cv2.destroyAllWindows()