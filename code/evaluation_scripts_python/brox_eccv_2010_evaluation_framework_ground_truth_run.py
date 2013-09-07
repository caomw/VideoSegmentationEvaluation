import os
import sys
import string
from scipy import *
import numpy


VSEG_ROOT                            = r"/n/nssdeep/lichtman_lab/amelio/data/vseg"
MOSEG_ROOT                           = os.path.join( VSEG_ROOT, "out/moseg" )

input_image_path                     = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], "box_malik_or" )
output_image_path                    = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], "results/brox_eccv_2010_evaluation_framework_ground_truth_run/full_rendering/inpainted_labels" )



if not os.path.exists( output_image_path ):
    execute_string = "mkdir -p " + output_image_path
    print execute_string
    os.system( execute_string )



files                   = sorted( os.listdir( input_image_path ) )
global_unique_values    = zeros( 0, int )

for file in files:
    if file.lower().endswith( ".pgm" ):
        image                = misc.imread( os.path.join( input_image_path, file ) )
        global_unique_values = unique( append( global_unique_values, unique( image ) ) )

global_unique_values_to_colormap_indices = dict( zip( global_unique_values, range( size( global_unique_values ) ) ) )



alphabet_size   = len( global_unique_values );
colormap_values = linspace( 0, 255, alphabet_size ).round()

colormap_r = copy( colormap_values )
colormap_g = copy( colormap_values )
colormap_b = copy( colormap_values )

random.shuffle( colormap_r )
random.shuffle( colormap_g )
random.shuffle( colormap_b )



for file in files:
    if file.lower().endswith( ".jpg" ):
        base_name         = file.lower()[:-4]
        pgm_name          = base_name + ".pgm"
        output_image_name = base_name + ".png"

        if os.path.exists( os.path.join( input_image_path, pgm_name ) ):
            input_image  = misc.imread( os.path.join( input_image_path, pgm_name ) )
            output_image = zeros( ( size( input_image, 0 ), size( input_image, 1 ), 3 ) )

            for global_unique_value in global_unique_values:
                colormap_index = global_unique_values_to_colormap_indices[ global_unique_value ]

                matches                 = ( input_image == global_unique_value ).nonzero()
                output_image[ matches ] = [ colormap_r[ colormap_index ], colormap_g[ colormap_index ], colormap_b[ colormap_index ] ]

            misc.imsave( os.path.join( output_image_path, output_image_name ), output_image )

        else:
            input_image = misc.imread( os.path.join( input_image_path, file ) )
            misc.imsave( os.path.join( output_image_path, output_image_name ), input_image )

        print os.path.join( output_image_path, output_image_name )
