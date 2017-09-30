import cv2
import numpy as np
import math
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
        rows = int(rows)
        cols = int(cols)
        fx = float(fx)
        fy = float(fy)
        newRows = int(round(rows*fx))
        newCols = int(round(cols*fy))
        image2 = np.zeros((newRows,newCols), np.uint8)
        for x in range(newRows):
            for y in range(newCols):
                i = x/fx
                j = y/fy
                r = int(np.floor(i))
                c = int(np.floor(j))
                if r < 0:
                    r = 0
                elif c < 0:
                    c = 0
                if r > rows:
                    r = rows
                elif c > cols:
                    c = cols
                srcColor1 = image[r][c]
                srcColor2 = image[r+1][c]
                srcColor3 = image[r][c+1]
                srcColor4 = image[r+1][c+1]
                r0 = (abs(math.sin(((c+1 - y)/(c+1 - c))))*srcColor2) + (abs(math.sin((y-c)/(c+1-c)))*srcColor4)
                r1 = (abs(math.sin(((c+1-y)/(c+1-c))))*srcColor1) + (abs(math.sin((y-c)/(c+1-c)))*srcColor3)
                image2[x][y] = (abs(math.cos(((r-x)/(r-r+1))))*r0) + (abs(math.cos((x-r+1)/(r-r+1)))*r1)

        return image2
#lenna = cv2.imread("C:\\Users\\Brad\\Desktop\\UH Fall 2017\\Digital Image Processing\\Assignment_1\\cell2.jpg", 0)
#resample = resample()
#load_display(resample.nearest_neighbor(lenna, 1.5, 1.5))
#load_display(lenna)
