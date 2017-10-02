import numpy as np

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""
        (row,col) = image.shape
        hist = [0]*256
        for i in range(row):
            for j in range(col):
                hist[image[i,j]] += 1

        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""
        mu1 =0
        mu1temp = 0
        mu2 = 0
        mu2temp = 0
        totalfirsthistvalues = 0
        totalsecondhistvalues = 0
        for x in range(0, round(len(hist)/2)):
            totalfirsthistvalues += hist[x]
        for x in range(round(len(hist)/2), len(hist)):
            totalsecondhistvalues += hist[x]
        totalhistvalues = totalsecondhistvalues + totalfirsthistvalues
        firsthalfhist = [0]*round(len(hist)/2)
        secondhalfhist = [0]*round(len(hist)/2)
        for x in range(0, (round(len(hist)/2))):
            firsthalfhist[x] = hist[x]
            secondhalfhist[x] = hist[x + (round(len(hist)/2))]
        for x in range(0, round(len(hist)/2)):
            mu1 += (x*(firsthalfhist[x])/totalhistvalues)
            mu2 += ((x+round(len(hist)/2))*(secondhalfhist[x]/totalhistvalues))


        threshold = (mu1 + mu2)/2
        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()
        hist = self.compute_histogram(bin_img)
        t = self.find_optimal_threshold(hist)
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):

                if(image[row,col] >= t):
                    bin_img[row,col] = 0

                if(image[row,col]<t):
                    bin_img[row,col] = 255


        return bin_img


