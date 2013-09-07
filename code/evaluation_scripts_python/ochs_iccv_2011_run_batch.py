import os
import string
import sys
import math

NUM_FILES_PER_BATCH       = 1;
VSEG_ROOT                 = r"/n/nssdeep/lichtman_lab/amelio/data/vseg"
MOSEG_ROOT                = os.path.join( VSEG_ROOT, "out/moseg" )
MIKE_CODE_ROOT            = r"/n/nssdeep/lichtman_lab/amelio/code/share/mike"
OCHS_ICCV_2011_RUN_SCRIPT = os.path.join( MIKE_CODE_ROOT, "evaluation_scripts_python/ochs_iccv_2011_run.py" )
TOUCH_PATH                = r"/n/nssdeep/lichtman_lab/amelio/code/share/mike/ochs_iccv_2011_finished_jobs"

input_original_images_dir = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], r"results/brox_eccv_2010/original_images_ppm" )
output_dir                = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], r"results/ochs_iccv_2011/full_rendering/inpainted_labels" )

files                     = sorted( os.listdir( input_original_images_dir ) )
num_files                 = len( files )
num_batches               = int( math.ceil( num_files / NUM_FILES_PER_BATCH ) )

for batch_index in range( 0, num_batches ):
	file_start_index = ( batch_index * NUM_FILES_PER_BATCH ) + 1
	file_end_index   = file_start_index + NUM_FILES_PER_BATCH - 1
	job_name         = 'ochs_iccv_2011_run_' + sys.argv[ 1 ] + '_' + str( file_start_index ) + '_' + str( file_end_index )
	error_name       = os.path.join( MIKE_CODE_ROOT, 'ochs_iccv_2010_job_output', job_name + '_error.txt' )
	summary_name     = os.path.join( MIKE_CODE_ROOT, 'ochs_iccv_2010_job_output', job_name + '_summary.txt' )
	python_command   = 'python ' + OCHS_ICCV_2011_RUN_SCRIPT + ' ' + sys.argv[ 1 ] + ' ' + str( file_start_index ) + ' ' + str( file_end_index )
	
	output_file = os.path.join( output_dir, ( '%06d' % file_start_index ) + '_dense.ppm' )
	
	if ( not os.path.exists( output_file ) ):
		execute_string = 'rbsub -n 1 -q amelio -R "rusage[mem=10000]" -J ' + job_name + ' -e ' + error_name + ' -o ' + summary_name + ' ' + python_command
		print execute_string
		os.system( execute_string )
	else:
		touch_file     = os.path.join( TOUCH_PATH, 'done_' + sys.argv[ 1 ] + '_' + '%06d' % ( file_start_index ) )
		execute_string = 'touch ' + touch_file
		print execute_string
		os.system( execute_string )
