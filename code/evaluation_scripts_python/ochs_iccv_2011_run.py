import os
import string
import sys

VSEG_ROOT                 = r"/n/nssdeep/lichtman_lab/amelio/data/vseg"
MOSEG_ROOT                = os.path.join( VSEG_ROOT, "out/moseg" )
OCHS_ICCV_2011_EXECUTABLE = r"/n/nssdeep/lichtman_lab/amelio/code/share/mike/ochs_iccv_2011/dens100"
TOUCH_PATH                = r"/n/nssdeep/lichtman_lab/amelio/code/share/mike/ochs_iccv_2011_finished_jobs"

input_original_images_dir                = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], r"results/brox_eccv_2010/original_images_ppm" )
input_original_and_superpixel_images_dir = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], r"results/ochs_iccv_2011/original_and_superpixel_and_sparse_label_images" )
intermediate_output_dir                  = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], r"results/ochs_iccv_2011/original_and_superpixel_and_sparse_label_images/OchsBroxResults" )
output_dir                               = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], r"results/ochs_iccv_2011/full_rendering/inpainted_labels" )

files           = sorted( os.listdir( input_original_images_dir ) )
num_input_files = len( files )
frame_index     = 0

execute_string = "mkdir -p " + output_dir
print execute_string
os.system( execute_string )

for file in files:
    if ( file.lower().endswith( ".ppm" ) ):
		if ( frame_index in range( int( sys.argv[ 2 ] ) - 1, int( sys.argv[ 3 ] ) ) ):
		
			input_file_base_name          = file[:-4]
			input_file_full_name          = os.path.join( input_original_and_superpixel_images_dir, file );
			input_sparse_label_image_name = input_file_base_name + "_labels%04d.ppm" % frame_index;
			
			execute_string = OCHS_ICCV_2011_EXECUTABLE + " " + input_file_full_name + " 3 " + input_sparse_label_image_name
			print execute_string
			os.system( execute_string )

			intermediate_output = os.path.join( intermediate_output_dir, ( '%06d' % ( frame_index + 1 ) ) + '_dense.ppm' )
			
			execute_string = "mv " + intermediate_output + " " + output_dir
			print execute_string
			os.system( execute_string )

			touch_file     = os.path.join( TOUCH_PATH, 'done_' + sys.argv[ 1 ] + '_' + '%06d' % ( frame_index + 1 ) )
			execute_string = 'touch ' + touch_file
			print execute_string
			os.system( execute_string )
			
		frame_index = frame_index + 1
