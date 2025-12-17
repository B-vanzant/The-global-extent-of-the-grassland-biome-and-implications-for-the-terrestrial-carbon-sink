from qgis.core import (QgsProject, QgsLayoutExporter, QgsApplication)

folder = r"E:/Grassland Mapping Files/Blank Grids/"
#get a list of all the layer names
root = QgsProject.instance().layerTreeRoot()
mygroup = root.findGroup("All Sites")
layer_list= mygroup.findLayers()
layer_list = [layer.name() for layer in mygroup.children()]

#list the layers
layers = QgsProject.instance().mapLayers()

#looping code making a virtual layer for each layer
i = 0
layer = [layer.name() for layer in  QgsProject.instance().mapLayers().values()]
    
for layer in layers:
    site = layer_list[i]
    print(site)
    print(layer)
    vlayer = QgsVectorLayer(f"?query= select *, char(r+64) || ROW_NUMBER() OVER(PARTITION BY r) as newID from (SELECT *,DENSE_RANK() OVER (ORDER BY round( ST_minY(geometry)/0.000002) desc) as r FROM {layer} ORDER BY round(ST_minY(geometry)/0.000002)  DESC, round( ST_minX(geometry)/0.000002)  ASC)", site, "virtual")
    QgsProject.instance().addMapLayer(vlayer)
    print(i)
    i = i + 1
