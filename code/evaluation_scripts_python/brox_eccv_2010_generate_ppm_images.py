import os
import string
import sys

VSEG_ROOT                  = r"/n/nssdeep/lichtman_lab/amelio/data/vseg"
MOSEG_ROOT                 = os.path.join( VSEG_ROOT, "out/moseg" )
NUMBERED_FILE_STRING_WIDTH = 6

input_path  = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], "box_malik_or" )
output_path = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], "results/brox_eccv_2010/original_images_ppm" )

if not os.path.exists( output_path ):
    execute_string = "mkdir -p " + output_path
    print execute_string
    os.system( execute_string )
    
os.chdir( input_path )

files      = sorted( os.listdir( input_path ) )
file_index = 1

for file in files:
    if ( file.lower().endswith( ".jpg" ) ):

        os.system( "mogrify -format ppm " + file )

        ppm_file      = file[:-3] + "ppm"
        src_file_path = os.path.join( input_path, ppm_file )
        dst_file_path = os.path.join( output_path, str( file_index ).zfill( NUMBERED_FILE_STRING_WIDTH ) + ".ppm" )

        execute_string = "mv " + src_file_path + " " + dst_file_path
        print execute_string
        os.system( execute_string )
		
        file_index = file_index + 1
