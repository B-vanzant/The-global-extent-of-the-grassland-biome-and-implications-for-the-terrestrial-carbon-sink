from os.path import join
import sys
root = QgsProject.instance().layerTreeRoot()
project = QgsProject().instance()
canvas = iface.mapCanvas()
layers = root.layerOrder()

layout = project.layoutManager().layoutByName('map') #name of the layout
title_item = layout.itemById('Label 1') #ID of the title item
folder = r"E:/Grassland Mapping Files/Data Visualization/" #Where you want to save the images to

j = 0
for j in range (1): # number in brackets is number of sites you go through
    #zoom to different layers 
    canvas.setExtent(layers[j].extent())
    canvas.zoomScale(1900)
    
    map_item = [i for i in layout.items() if isinstance(i, QgsLayoutItemMap)][0]
    map_item.zoomToExtent(canvas.extent())
    

    file_name = join(folder, layers[j].name()+".png") #names each png file the exacat same thing as the layer name
    title = layers[j].name() #makes the title of each image same as the layer name
    print(file_name)
    print(title)
    
    title_item.setText(title) #sets the title
    
    exporter = QgsLayoutExporter(layout)
    settings = QgsLayoutExporter.ImageExportSettings()
    settings.dpi = 300

    result = exporter.exportToImage(file_name, settings)
    print(result)#0 = Export was successful!
    j = j+1
