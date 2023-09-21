import geopandas as gpd
import pickle

import pandas as pd

cond_shp = r'test_data/03_Net_Cond_Calib2022V0_776_SM_latlong.shp'

# Read in shapefile read the first 1000 rows
gdf = gpd.read_file(cond_shp)

# creat UFID column
gdf['UFID'] = gdf['us_node_id'].astype(str) + '.' + gdf['link_suffi'].astype(str)

# only keep the columns ufid and geometry
csv = gdf.copy()
gdf = gdf[['UFID', 'geometry']]
gdf['layer_Name'] = 'ICM_Cond'


# CONVERT TO WKT
gdf['geometry'] = gdf['geometry'].apply(lambda x: x.wkt)

# save to csv
gdf.to_csv('test_data/ICM_Cond.csv', index=False)



node_shp = r'test_data/03_Net_Node_Calib2022V0_776_SM_latlong.shp'
# Read in shapefile
gdf_node = gpd.read_file(node_shp)



gdf_node['UFID'] = gdf_node['node_id'].astype(str)
csv_node = gdf_node.copy()
gdf_node['layer_Name'] = 'ICM_Node'
gdf_node = gdf_node[['UFID', 'geometry', 'layer_Name']]
gdf_node['geometry'] = gdf_node['geometry'].apply(lambda x: x.wkt)

gdf_node.to_csv('test_data/ICM_Node.csv', index=False)



boundary_shp = r'test_data/LS_Boundaries.shp'
# Read in shapefile
gdf_boundary = gpd.read_file(boundary_shp)

#convert ot wgs84
gdf_boundary = gdf_boundary.to_crs(epsg=4326)
gdf_boundary['UFID'] = gdf_boundary['LS_name'].astype(str)
csv_boundary = gdf_boundary.copy()

gdf_boundary['geometry'] = gdf_boundary['geometry'].apply(lambda x: x.wkt)
gdf_boundary['layer_Name'] = 'ICM_Boundary'
gdf_boundary = gdf_boundary[['UFID', 'geometry', 'layer_Name']]
#COMBINE NODE AND COND and BOUNDARY
gdf_node_cond_boundary = pd.concat([gdf_node, gdf,gdf_boundary ], axis=0)
gdf_node_cond_boundary.to_csv('test_data/ICM_Node_Cond_Boundary.csv', index=False)

#export all csv files
csv.to_csv('test_data/ICM_Cond.csv', index=False)
csv_node.to_csv('test_data/ICM_Node.csv', index=False)
csv_boundary.to_csv('test_data/ICM_Boundary.csv', index=False)