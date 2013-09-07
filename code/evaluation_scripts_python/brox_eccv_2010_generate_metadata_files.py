import os
import sys

VSEG_ROOT  = r"/n/nssdeep/lichtman_lab/amelio/data/vseg"
MOSEG_ROOT = os.path.join( VSEG_ROOT, "out", "moseg" )

input_path          = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], "results/brox_eccv_2010/original_images_ppm" )
input_relative_path = os.path.join( "..", "original_images_ppm" )
output_path         = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], "results/brox_eccv_2010/original_images_metadata" )
output_file_path    = os.path.join( output_path, "original_images_metadata.bmf" )
files               = sorted( os.listdir( input_path ) )

if not os.path.exists( output_path ):
    execute_string = "mkdir -p " + output_path
    print execute_string
    os.system( execute_string )

output_file = open( output_file_path, 'w' )
print output_file_path

output_file.write( str( len( files ) ) + " 1\n" )

for file in files:

    file_path = os.path.join( input_relative_path, file )
    output_file.write( file_path + "\n" )

output_file.close()