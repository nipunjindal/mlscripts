import cv2
import os

input_dir = "x"
output_dir = "y"
for fname in os.listdir(input_dir):
	print('fname is ', fname)
	img_rgb = cv2.imread(input_dir +str(fname))
	img_gray =  cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
	img_gray_inv = 255 - img_gray
	img_blur = cv2.GaussianBlur(img_gray_inv, (25, 25), 0, 0)
	img_blend = cv2.divide(img_gray, 255-img_blur, scale=256)

	cv2.imwrite(output_dir + str(fname), img_blend)

