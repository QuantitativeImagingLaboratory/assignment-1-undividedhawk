import cv2
import numpy as np

def load_display(image):
    cv2.namedWindow("Lenna", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Lenna", image)
    cv2.waitKey(0)
    cv2.destroyWindow("Lenna")


class resample:



    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here
        load_display(image)
        (width, height) = image.shape
        width = int(width)
        height = int(height)
        fx = float(fx)
        fy = float(fy)
        newWid = round(width * fx)
        newHt = round(height * fy)
        image2 = np.zeros((newWid, newHt), np.uint8)

        for x in range(newWid):
            for y in range(newHt):
                srcX = int(round(float(x) / float(newWid) * float(width)))
                srcY = int(round(float(y) / float(newHt) * float(height)))
                srcX = int(min(srcX, width - 1))
                srcY = int(min(srcY, height - 1))
                srcColor = image[srcX][srcY]
                image2[x][y] = srcColor
        image2 = image.copy()
        return image2



    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        (rows,cols) = image.shape
        a = np.zeros((round(rows*fx),round(cols*fy)),np.uint8)

        return image

#lenna = cv2.imread("C:\\Users\\Brad\\Desktop\\UH Fall 2017\\Digital Image Processing\\Assignment_1\\cell2.jpg", 0)
#resample = resample()
#load_display(resample.nearest_neighbor(lenna, 1.5, 1.5))
#load_display(lenna)
