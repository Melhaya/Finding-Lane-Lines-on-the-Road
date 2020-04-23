# **Finding Lane Lines on the Road** 


**Finding Lane Lines on the Road**

The goal of this project is the following:
* Make a pipeline that finds lane lines on the road



[//]: # (Image References)

[image1]: ./test_images_output/solidWhiteCurveprocessed.png "Detected lanes"

---

### Reflection

### 1. Pipeline Description.

My pipeline consisted of 5 steps. First, I converted the images to grayscale, then a gaussian blur is done to the image with a kernel size of 5. Canny function is then used on the image with a low threshold of 50 and high threshold of 150. Furthermore, A ROI is then extracted from that image and inputted to the hough_lines function to detect and highlight the lines/lanes in the image.

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by first calculating the slope to identify if the it is the left or right lane. Once that is done, I then extract from the detected lines the minimum and maximum x and y positions in a given set of lines. Once that is obtained, I make sure first there are no outliers and misdetected lines and then I connect the points together to make a single line for each lane. 

The output of the pipeline is as follows: 

![alt text][image1]


### 2. Potential shortcomings with my current pipeline


One potential shortcoming would be what would happen when the lanes start to take a curve, it becomes more challenging to detect and accurately draw the lines 


### 3. Possible improvements to my pipeline

A possible improvement would be to using a more complex function to detect curves and thus detecting the lanes with a polynomial function instead of using a straight line. The performance would definetly be enhanced.
