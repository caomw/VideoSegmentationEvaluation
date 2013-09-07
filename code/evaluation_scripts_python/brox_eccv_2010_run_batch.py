import os
import string
import sys

NUM_FILES_PER_BATCH       = 10;
VSEG_ROOT                 = r"/n/nssdeep/lichtman_lab/amelio/data/vseg"
MOSEG_ROOT                = os.path.join( VSEG_ROOT, "out/moseg" )
BROX_ECCV_2011_RUN_SCRIPT = r"/n/nssdeep/lichtman_lab/amelio/code/share/mike/evaluation_script_python/brox_eccv_2010_run.py"

dirs = sorted( os.listdir( MOSEG_ROOT ) )

for dir in dirs:
	job_name         = 'brox_2010_run_' + dir + '_' + str( file_start_index ) + '_' + str( file_end_index )
	error_name       = job_name + '_error.txt'
	summary_name     = job_name + '_summary.txt'
	python_command   = 'python ' + OCHS_ICCV_2011_RUN_SCRIPT + ' ' + dir
	
	execute_string = 'rbsub -n 1 -q normal_serial -R "rusage[mem=10000]" -J "' + job_name + '" -e "' + error_name + '" -o "' + summary_name + '" ' + command
	print execute_string
	#os.system( execute_string )
