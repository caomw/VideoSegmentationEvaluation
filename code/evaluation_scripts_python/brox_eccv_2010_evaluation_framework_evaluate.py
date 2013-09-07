import os
import sys

VSEG_ROOT                                          = r"/n/nssdeep/lichtman_lab/amelio/data/vseg"
MOSEG_ROOT                                         = os.path.join( VSEG_ROOT, "out/moseg" )
MIKE_CODE_ROOT                                     = r"/n/nssdeep/lichtman_lab/amelio/code/share/mike"
BROX_ECCV_2010_EVALUATION_FRAMEWORK_EXECUTABLE_DIR = os.path.join( MIKE_CODE_ROOT, "brox_eccv_2010_evaluation_framework" )
BROX_ECCV_2010_EVALUATION_FRAMEWORK_EXECUTABLE     = os.path.join( BROX_ECCV_2010_EVALUATION_FRAMEWORK_EXECUTABLE_DIR, "MoSegEvalAll" )

ground_truth_metadata_txt_relative_path        = os.path.join( "../../../../data/vseg/out/moseg/", sys.argv[ 2 ], "ground_truth/ground_truth.txt" )
point_trajectories_txt_relative_path           = os.path.join( "../../../../data/vseg/out/moseg/", sys.argv[ 2 ], "results", sys.argv[ 1 ], "point_trajectories/point_trajectories.txt" )

input_path       = os.path.join( MOSEG_ROOT, sys.argv[ 2 ], "results", sys.argv[ 1 ], "point_trajectories/point_trajectoriesNumbers.txt" )
output_path      = os.path.join( MOSEG_ROOT, sys.argv[ 2 ], "results", sys.argv[ 1 ], "brox_eccv_2010_evaluation_framework_results" )
output_file_path = os.path.join( output_path, "brox_eccv_2010_evaluation_framework_results.txt" )

os.chdir( BROX_ECCV_2010_EVALUATION_FRAMEWORK_EXECUTABLE_DIR )

execute_string = BROX_ECCV_2010_EVALUATION_FRAMEWORK_EXECUTABLE + " " + ground_truth_metadata_txt_relative_path + " all " + point_trajectories_txt_relative_path
print execute_string
os.system( execute_string )

if not os.path.exists( output_path ):
    execute_string = "mkdir -p " + output_path
    print execute_string
    os.system( execute_string )

execute_string = "mv " + input_path + " " + output_file_path
print execute_string
os.system( execute_string )

execute_string = "cat " + output_file_path
print execute_string
os.system( execute_string )
