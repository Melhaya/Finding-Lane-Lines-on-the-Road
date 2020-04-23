from utilities import *


def detect_lane(image):

	img_shape = image.shape
	gray_img = grayscale(image)
	#plt.imshow(gray_img, cmap='gray')
	#plt.show()

	blur_img = gaussian_blur(gray_img, kernel_size=5)
	#plt.imshow(blur_img, cmap='gray')
	#plt.show()

	canny_img = canny(blur_img, low_threshold=50, high_threshold=150)
	#plt.imshow(canny_img, cmap='Greys_r')
	#plt.show()

	vertices = np.array([[(110,img_shape[0]),(img_shape[1]/2.1, img_shape[0]/1.7), \
				(img_shape[1]/1.9, img_shape[0]/1.7), (img_shape[1]- 70, img_shape[0])]], dtype=np.int32)
	#vertices = np.array([[(0,img_shape[0]),(img_shape[1]/2, img_shape[0]/1.7), \
	#			(img_shape[1]/2, img_shape[0]/1.7), (img_shape[1], img_shape[0])]], dtype=np.int32)
	ROI_img = region_of_interest(canny_img, vertices)
	#plt.imshow(ROI_img)
	#plt.show()

	lines_img = hough_lines(ROI_img, rho=2, theta= np.pi/180, threshold=20, min_line_len=2, max_line_gap=5)

	#plt.imshow(lines_img)
	#plt.show()

	# Draw the lines on the original image
	lanes_in_image = weighted_img(lines_img, image) 
	#plt.imshow(lanes_in_image)
	#plt.show()

	return lanes_in_image


#reading in an image
import os
images = os.listdir("test_images/")
print(images)

for image in images:
	print("\nProcessing ",image,"\n")
	img = mpimg.imread('test_images/' + image)
	#plt.imshow(img)
	#plt.show()
	pImage = detect_lane(img)
	mpimg.imsave("test_images_output/"+image[:-4]+"processed.png", pImage)


#reading in a video
from moviepy.editor import VideoFileClip
from IPython.display import HTML

white_output = 'test_videos_output/solidWhiteRight.mp4'
## To speed up the testing process you may want to try your pipeline on a shorter subclip of the video
## To do so add .subclip(start_second,end_second) to the end of the line below
## Where start_second and end_second are integer values representing the start and end of the subclip
## You may also uncomment the following line for a subclip of the first 5 seconds
##clip1 = VideoFileClip("test_videos/solidWhiteRight.mp4").subclip(0,5)
clip1 = VideoFileClip("test_videos/solidWhiteRight.mp4")
white_clip = clip1.fl_image(detect_lane) #NOTE: this function expects color images!!
white_clip.write_videofile(white_output, audio=False)

HTML("""
<video width="960" height="540" controls>
  <source src="{0}">
</video>
""".format(white_output))

yellow_output = 'test_videos_output/solidYellowLeft.mp4'
## To speed up the testing process you may want to try your pipeline on a shorter subclip of the video
## To do so add .subclip(start_second,end_second) to the end of the line below
## Where start_second and end_second are integer values representing the start and end of the subclip
## You may also uncomment the following line for a subclip of the first 5 seconds
##clip2 = VideoFileClip('test_videos/solidYellowLeft.mp4').subclip(0,5)
clip2 = VideoFileClip('test_videos/solidYellowLeft.mp4')
yellow_clip = clip2.fl_image(detect_lane)
yellow_clip.write_videofile(yellow_output, audio=False)

HTML("""
<video width="960" height="540" controls>
  <source src="{0}">
</video>
""".format(yellow_output))

challenge_output = 'test_videos_output/challenge.mp4'
## To speed up the testing process you may want to try your pipeline on a shorter subclip of the video
## To do so add .subclip(start_second,end_second) to the end of the line below
## Where start_second and end_second are integer values representing the start and end of the subclip
## You may also uncomment the following line for a subclip of the first 5 seconds
##clip3 = VideoFileClip('test_videos/challenge.mp4').subclip(0,5)
clip3 = VideoFileClip('test_videos/challenge.mp4')
challenge_clip = clip3.fl_image(detect_lane)
challenge_clip.write_videofile(challenge_output, audio=False)

HTML("""
<video width="960" height="540" controls>
  <source src="{0}">
</video>
""".format(challenge_output))