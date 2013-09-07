import os
import string
import sys

VSEG_ROOT                                              = r"/n/nssdeep/lichtman_lab/amelio/data/vseg"
MOSEG_ROOT                                             = os.path.join( VSEG_ROOT, "out/moseg" )
OCHS_ICCV_2011_GENERATE_SPARSE_LABEL_IMAGES_EXECUTABLE = r"/n/nssdeep/lichtman_lab/amelio/code/share/mike/ochs_iccv_2011/conv_Track2Img"

input_original_images_dir                     = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], r"results/brox_eccv_2010/original_images_ppm" )
input_original_images                         = os.path.join( input_original_images_dir, r"*.ppm" )
input_original_images_dir_sparse_label_images = os.path.join( input_original_images_dir, r"*_labels*.ppm" )
input_point_trajectories                      = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], r"results/brox_eccv_2010/point_trajectories/point_trajectories.dat" )
output_sparse_label_images_dir                = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], r"results/ochs_iccv_2011/original_and_superpixel_and_sparse_label_images" )

files       = sorted( os.listdir( input_original_images_dir ) )
frame_index = 0

for file in files:
    if ( file.lower().endswith( ".ppm" ) ):

		input_file_full_name = os.path.join( input_original_images_dir, file );

		execute_string = OCHS_ICCV_2011_GENERATE_SPARSE_LABEL_IMAGES_EXECUTABLE + " " + input_file_full_name + " " + input_point_trajectories + " " + str( frame_index )
		print execute_string
		os.system( execute_string )
		
		frame_index = frame_index + 1

execute_string = "mv " + " " + input_original_images_dir_sparse_label_images + " " + output_sparse_label_images_dir
print execute_string
os.system( execute_string )
