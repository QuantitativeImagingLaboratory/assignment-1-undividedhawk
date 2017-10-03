import sys
class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""

        regions = dict()
        k = 1
        (rows,cols) = image.shape
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    if image[i][j] == 0:
                        regions[i,j] = k
                        k+=1
                elif i == 0 and j != 0:
                    if image[i][j] == 0 and image[i][j-1] == 0:
                        regions[i][j] = regions[i][j-1]
                elif j == 0 and i !=0:
                    if image[i][j] == 0 and image[i-1][j] == 0:
                        regions[i][j] = regions[i-1][j]
                elif image[i][j] == 0 and image[i][j-1] == 255 and image[i-1][j] == 255:
                    regions[i,j] = k
                    k += 1
                elif image[i][j] == 0 and image[i][j-1] == 255 and image[i-1][j] == 0:
                    regions[i,j] = regions[i-1,j]

                elif image[i][j] == 0 and image[i][j-1] == 0 and image[i-1][j] == 255:
                    regions[i,j] = regions[i,j-1]

                elif image[i][j] == 0 and image[i][j-1] == 0 and image[i-1][j] == 0:
                    regions[i,j] = regions[i-1,j]
                    if regions[i,j-1] != regions[i-1,j]:
                        regions[i,j-1] = regions[i-1,j]



        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""

        b = {}
        x_coord=[]
        y_coord=[]
        i = 0
        l = []
        for k,v in region.items():

            if not v in b:
                l.insert(i,v)
                b[v] = 1
                x_coord.insert(i,k[0])
                y_coord.insert(i,k[1])
                i += 1

            else:
                b[v] +=1
                u = x_coord.pop()
                v = y_coord.pop()
                x_coord.insert(i,u+k[0])
                y_coord.insert(i,v+k[1])

        centroid = len(x_coord)*[0]



        for z in range(len(x_coord)):
            centroid_x = round((x_coord[z]/len(x_coord)))
            centroid_y = round((y_coord[z]/len(y_coord)))
            centroid[z] = (centroid_x, centroid_y)

        q = dict(zip(l[:len(centroid)],centroid[:len(x_coord)]))
        i = 0
        for k,v in b.items():
            if b[k] >= 15:
                sys.stdout.write('Region: ' + str(k) + ', Area: ' + str(b[k]) + ', Centroid: ' + str(q[k]))

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return 0

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        return image

