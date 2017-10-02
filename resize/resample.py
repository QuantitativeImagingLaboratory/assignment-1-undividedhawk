import cv2
import numpy as np
import math



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

        (rows, cols) = image.shape
        rows = int(rows)
        cols = int(cols)
        fx = float(fx)
        fy = float(fy)
        newRows = int(round(rows*fx))
        newCols = int(round(cols*fy))
        image2 = np.zeros((newRows,newCols),np.uint8)
        for i in range(newRows):
            for j in range(newCols):
                r = j/fx
                c = i/fy
                xc = math.ceil(r)
                xf = math.floor(r)
                yc = math.ceil(c)
                yf = math.floor(c)

                wxc = xc - r
                wxf = r - xf
                wyc = yc - c
                wyf = c - yf

                if wxc == 0 or wyc == 0:
                    r0 = image[yf,xf]
                    r1 = 0
                elif wyc == 0 or wyf == 0:
                    r0 = image[yf,xf]
                    r1 = 0
                else:
                    r0 = wxc * (wyc * image[yf, xf] + wyf * image[yc, xf])
                    r1 = wxf * (wyc * image[yf, xc] + wyf * image[yc, xc])
                image2[i, j] = 0 + (r0 + r1)

        return image2




