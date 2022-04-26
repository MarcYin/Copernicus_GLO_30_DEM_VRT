import requests
from osgeo import gdal 



r = requests.get('https://copernicus-dem-90m.s3.amazonaws.com/tileList.txt')
ret = r.content.decode()
dem_90_list_of_files = ret.split('\n')
dem_90_coords = ['_'.join(i.split('_')[4:8]) for i in dem_90_list_of_files]

r = requests.get('https://copernicus-dem-30m.s3.amazonaws.com/tileList.txt')
ret = r.content.decode()
dem_30_list_of_files = ret.split('\r\n')
dem_30_coords = ['_'.join(i.split('_')[4:8]) for i in dem_30_list_of_files]


#difference between dem_90_coords and dem_30_coords
lost_dem_90_tiles = set(dem_90_coords).difference(dem_30_coords)
dem_90_url_temp = '/vsicurl/https://copernicus-dem-90m.s3.amazonaws.com/Copernicus_DSM_COG_30_%s_DEM/Copernicus_DSM_COG_30_%s_DEM.tif'
lost_dem_90_urls = [dem_90_url_temp%(i, i) for i in lost_dem_90_tiles]

dem_30_url_temp ='/vsicurl/https://copernicus-dem-30m.s3.amazonaws.com/%s/%s.tif'
dem_30_urls = [dem_30_url_temp%(i,i) for i in dem_30_list_of_files]

# filling dem30 gaps with dem90
full_dem_urls = dem_30_urls + lost_dem_90_urls


vrt_options = gdal.BuildVRTOptions(resampleAlg=gdal.GRIORA_NearestNeighbour, resolution='highest')
vrt_file = gdal.BuildVRT('copernicus_GLO_30_dem.vrt', full_dem_urls, options=vrt_options)
vrt_file = None
