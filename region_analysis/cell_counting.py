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

