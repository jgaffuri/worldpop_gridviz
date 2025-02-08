from pygridmap import gridtiler_raster




#Dimensions	X: 43200 Y: 18720 Bandes: 1
#Origine	-180.0012492650000127,83.9995831987100132
#Taille du Pixel	0.008333333300000000596,-0.008333333300000000596


gridtiler_raster.tiling_raster(
    {
        "2000": {"file":'/home/juju/geodata/worldpop/ppp_2000_1km_Aggregated.tif', "band":1, 'no_data_values':[0,-3.40282e+38]},
        "2010": {"file":'/home/juju/geodata/worldpop/ppp_2010_1km_Aggregated.tif', "band":1, 'no_data_values':[0,-3.40282e+38]},
        "2020": {"file":'/home/juju/geodata/worldpop/ppp_2020_1km_Aggregated.tif', "band":1, 'no_data_values':[0,-3.40282e+38]},
     },
    "pub/v1/",
    #crs="",
    tile_size_cell=128,
    format="parquet",
    #parquet_compression="snappy",
    num_processors_to_use=8
    )


'''
gridtiler_raster.tiling_raster(
    #input data
    { "2020": {"file":'/home/juju/geodata/worldpop/ppp_2020_1km_Aggregated.tif', "band":1, 'no_data_values':[-3.40282e+38]} },
    #output folder
    "/home/juju/Bureau/worldpop_tiles",
    #resolution
    0.008333333300000000596,
    #extent
    4036900,
    2946000,
    4046740,
    2956380,
    num_processors_to_use = 3
    )
'''
