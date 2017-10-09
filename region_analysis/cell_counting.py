import sys
import cv2
class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""
        (rows, cols) = image.shape
        regions = dict()
        for i in range(rows):
            for j in range(cols):
                regions[i,j] = 0
        k = 1

        for i in range(rows):
            for j in range(cols):

                if image[i][j] == 0 and image[i][j-1] == 255 and image[i-1][j] == 255:
                    regions[i,j] = k
                    k += 1
                if image[i][j] == 0 and image[i][j-1] == 255 and image[i-1][j] == 0:
                    regions[i,j] = regions[i-1,j]

                if image[i][j] == 0 and image[i][j-1] == 0 and image[i-1][j] == 255:
                    regions[i,j] = regions[i,j-1]

                if image[i][j] == 0 and image[i][j-1] == 0 and image[i-1][j] == 0:
                    regions[i,j] = regions[i-1,j]
                    if regions[i,j-1] != regions[i-1,j]:
                        regions[i,j-1] = regions[i-1,j]



        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""
        stats = dict()
        b = {}
        x_coord=[]
        y_coord=[]
        i = 0
        l = []
        counter = []
        counter2 = 1
        for k,v in region.items():

            if not v in b:
                l.append(v)
                b[v] = 1
                x_coord.append(k[0])
                y_coord.append(k[1])
                counter.append(1)
                i += 1

            else:
                b[v] +=1
                u = x_coord.pop()
                z = y_coord.pop()

                counter2 += 1

                x_coord.append(u+k[0])
                y_coord.append(z+k[1])

        centroid = len(x_coord)*[0]



        for ele in range(0,len(x_coord)):
            centroid_x = round((x_coord[ele]/len(x_coord)))
            centroid_y = round((y_coord[ele]/len(y_coord)))
            centroid[ele] = (centroid_x, centroid_y)


        q = dict(zip(l[:len(centroid)],centroid[:len(x_coord)]))
        print('q:')
        print(q)

        for k,v in b.items():
            if b[k] >= 15:
                stats[k] = q[k], b[k]
                print('Region: ' + str(k) + ', Centroid: ' + str(stats[k][0]) + ', Area: ' + str(stats[k][1]))
        print(stats)

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return stats

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        for k, v in stats.items():
            cv2.putText(image, '*', stats[k][0], cv2.FONT_HERSHEY_COMPLEX, 1, 255)
            cv2.putText(image, str(k), stats[k][0], cv2.FONT_HERSHEY_COMPLEX, 1, 255)
            cv2.putText(image, str(stats[k][1]), stats[k][0], cv2.FONT_HERSHEY_COMPLEX, 1, 255)
        return image




