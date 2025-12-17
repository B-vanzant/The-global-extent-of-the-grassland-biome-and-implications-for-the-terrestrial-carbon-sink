import os
from collections import defaultdict as dd

shapefolder = r'E:/Grassland Mapping Files/All Cells/'

#List all shapefiles
mainfolders = dd(list)
for root, folder, files in os.walk(shapefolder):
    for file in files:
        if file.endswith('.geojson'):
            mainfolders[root].append(os.path.join(root, file))

#Reproject shapes
for folders, shapefiles in mainfolders.items():
    for shapefile in shapefiles:
        print(shapefile)
        processing.run("native:reprojectlayer", 
        {'INPUT':shapefile,'TARGET_CRS':'EPSG:3857',
        'OUTPUT':shapefile+".shp"})
