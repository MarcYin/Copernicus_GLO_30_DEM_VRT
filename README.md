# Copernicus DEM: 30 meter

 ###   
Feng Yin

### Department of Geography, UCL

### [ucfafyi@ucl.ac.uk](mailto:ucfafyi@ucl.ac.uk)

[The Copernicus DEM](https://spacedata.copernicus.eu/web/cscda/dataset-details?articleId=394198) is a Digital Surface Model (DSM) which represents the surface of the Earth including buildings, infrastructure and vegetation. The Copernicus DEM is provided in 3 different instances named EEA-10, GLO-30 (two sub-datasets) and GLO-90. The Copernicus DEM instances have varying resolution (10 m, 30 m, 90 m), geographical extent (European and global), varying format (INSPIRE, DGED, DTED) and varying access rights (within the GLO-30 coverage, the access to few areas is restricted to some users’ categories).

This is a 30 meters global dem VRT file create from [AWS Open Data registry](https://registry.opendata.aws/copernicus-dem/). [Gaps in the GLO30](https://spacedata.copernicus.eu/documents/20126/0/Non-released-tiles_GLO-30_PUBLIC_Dec.xlsx/bcdd6cef-6379-4890-de8f-788daf41dce8?t=1608549440765) have been filled with GLO90 and resampled with nearest neighour algorithm in gdal.
Acess to the DEM file:
```
gdalinfo
```
