1. Resampling:

nearest_neighbor: for my nearest_neighbor method of resample.py I found the dimensions of the original image and the new image. Next I created the output image "image2" 
and resized it to the new dimensions with all elements in the matrix assigned to 0 I then computed the minimum elements between (floor(x/fx), original width-1) and the 
minimum elements between (floor(y/fy), original height-1). then i assigned all the elements in image2 to the values found from the two minimization functions.
The resultant image is the image formed from scaling the original image by fx and fy using the nearest_neighbor interpolation algorithm.


bilinear: for my bilinear method of resample.py I found the dimensions of the original image and the new image then assigned a new image 'image2' to be a zero matrix 
with the new dimensions. Then for every element in image2 if the element x/fx was an integer I assigned the pixel at that location to it's corresponding location in 
the original image. I repeated this process for the elements y/fy aswell. If x/fx and y/fy were not integers then I found the weighted values of x_coordinates ceiling, 
x_coordinates floor, y_coordinates ceiling, and y_coordinates floor; respectively. I then multiplied those weighted values by the corresponding known pixel values 
according to the bilinear interpolation formula and assigned those new pixel values to the cooresponding element in image2. The resultant image is the image formed from
scaling the original image by fx and fy using the bilinear interpolation algorithm.


2. Region Counting:

binarize image: for my binarization method I used a histogram model to generate all the frequencies of pixel values. I then found the threshold of that histogram using the 
given formula and iterated throughout the image assiging a pixel value of 0 if the pixel value was less than the threshold and a pixel value of 255 is the pixel value
was greater than the threshold. The result is a black and white binary image.

Blob coloring: In my blob coloring method I iterated through the binarized image and assigned the i,j element a unique integer value k based on the value to the left
and above the pixel value being inspected. The result is a list of all the unique regions of the binarized image.

