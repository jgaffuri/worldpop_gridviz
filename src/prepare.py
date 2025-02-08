from pygridmap import gridtiler_raster




#Dimensions	X: 43200 Y: 18720 Bandes: 1
#Origine	-180.0012492650000127,83.9995831987100132
#Taille du Pixel	0.008333333300000000596,-0.008333333300000000596



gridtiler_raster.tiling_raster(
    #input data
    { "height": {"file":'assets/LU001_LUXEMBOURG_UA2012_DHM_V020.tif', "band":1, 'no_data_values':[255,0]} },
    #output folder
    "assets/lux_height/",
    #resolution
    10,
    #extent
    4036900,
    2946000,
    4046740,
    2956380,
    num_processors_to_use = 3
    )
