import os
import sys

VSEG_ROOT  = r"/n/nssdeep/lichtman_lab/amelio/data/vseg"
MOSEG_ROOT = os.path.join( VSEG_ROOT, "out/moseg" )

output_path                             = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], "ground_truth" )
output_file_path                        = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], output_path, "ground_truth.txt" )
ground_truth_metadata_dat_relative_path = os.path.join( "../../../../data/vseg/out/moseg", sys.argv[ 1 ], "box_malik_or", sys.argv[ 1 ] + "Def.dat" )

if not os.path.exists( output_path ):
    execute_string = "mkdir -p " + output_path
    print execute_string
    os.system( execute_string )

output_file = open( output_file_path, 'w' )
print output_file_path

output_file.write( "1\n" )
output_file.write( ground_truth_metadata_dat_relative_path + "\n" )
output_file.close()
