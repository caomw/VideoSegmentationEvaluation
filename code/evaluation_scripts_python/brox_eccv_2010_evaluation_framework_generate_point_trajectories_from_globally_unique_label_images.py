import os
import sys
import string
from scipy import *
import numpy

VSEG_ROOT                            = r"/n/nssdeep/lichtman_lab/amelio/data/vseg"
MOSEG_ROOT                           = os.path.join( VSEG_ROOT, "out/moseg" )

original_image_path                  = os.path.join( MOSEG_ROOT, sys.argv[ 2 ], "box_malik_or" )
input_image_path                     = os.path.join( MOSEG_ROOT, sys.argv[ 2 ], "results", sys.argv[ 1 ], "full_rendering/inpainted_labels" )
output_path                          = os.path.join( MOSEG_ROOT, sys.argv[ 2 ], "results", sys.argv[ 1 ], "point_trajectories" )
output_image_path                    = os.path.join( MOSEG_ROOT, sys.argv[ 2 ], "results", sys.argv[ 1 ], "point_trajectory_rendering" )
output_dat_path                      = os.path.join( output_path, "point_trajectories.dat" )
output_txt_path                      = os.path.join( output_path, "point_trajectories.txt" )
output_dat_relative_path             = os.path.join( "../../../../data/vseg/out/moseg", sys.argv[ 2 ], "results", sys.argv[ 1 ], "point_trajectories/point_trajectories.dat" )

if not os.path.exists( output_path ):
    execute_string = "mkdir -p " + output_path
    print execute_string
    os.system( execute_string )

if not os.path.exists( output_image_path ):
    execute_string = "mkdir -p " + output_image_path
    print execute_string
    os.system( execute_string )



original_image_files          = sorted( os.listdir( original_image_path ) )
input_image_files             = sorted( os.listdir( input_image_path ) )
original_image_file_map       = {}
ground_truth_indices          = []
total_num_ground_truth_pixels = 0
total_num_original_files      = 0
original_image_file_index     = 0

for file in original_image_files:
    if file.lower().endswith( ".jpg" ):
        original_image_file_map[ file.lower()[:-4] ] = original_image_file_index
        original_image_file_index = original_image_file_index + 1
        total_num_original_files  = total_num_original_files  + 1

for file in original_image_files:
    if file.lower().endswith( ".pgm" ):
        original_image_index = original_image_file_map[ file.lower()[:-4] ]
        ground_truth_indices.append( original_image_index )
        image = misc.imread( os.path.join( original_image_path, file ) )
        total_num_ground_truth_pixels = total_num_ground_truth_pixels + ( size( image, 0 ) * size( image, 1 ) )



global_unique_colors = zeros( 0, "u1, u1, u1" )
input_image_index    = 0

for file in input_image_files:
    if string.lower( file ).endswith( ".png" ) or string.lower( file ).endswith( ".ppm" ):
        if input_image_index in ground_truth_indices:
            image                = misc.imread( os.path.join( input_image_path, file ) )
            image_view           = image.view( dtype="u1, u1, u1" )
            global_unique_colors = unique( append( global_unique_colors, unique( image_view ) ) )
            
        input_image_index    = input_image_index + 1



dat_file = open( output_dat_path, 'w' )
dat_file.write( "%d\n" % total_num_original_files )
dat_file.write( "%d\n" % total_num_ground_truth_pixels )

input_image_index = 0

for file in input_image_files:
    if string.lower( file ).endswith( ".png" ) or string.lower( file ).endswith( ".ppm" ):
        if input_image_index in ground_truth_indices:

            image      = misc.imread( os.path.join( input_image_path, file ) )
            image_view = image.view( dtype="u1, u1, u1" )

            for global_unique_color_index in range( size( global_unique_colors ) ):

                global_unique_color  = global_unique_colors[ global_unique_color_index ]
                matches              = ( image_view == global_unique_color ).reshape( size( image, 0 ), size( image, 1 ) )

                misc.imsave( os.path.join( output_image_path, file[:-4] + "." + str( global_unique_color_index ) + ".png" ), matches )

                matching_coordinates   = matches.nonzero()
                matching_coordinates_y = matching_coordinates[ 0 ]
                matching_coordinates_x = matching_coordinates[ 1 ]

                num_matching_coordinates = size( matching_coordinates_y )

                for coordinate_index in range( num_matching_coordinates ):
                    dat_file.write( "%d 1\n"     % global_unique_color_index )
                    dat_file.write( "%d %d %d\n" % ( matching_coordinates_x[ coordinate_index ], matching_coordinates_y[ coordinate_index ], input_image_index ) )

        input_image_index = input_image_index + 1

dat_file.close()



txt_file = open( output_txt_path, 'w' )
txt_file.write( "%s" % output_dat_relative_path )
txt_file.close()