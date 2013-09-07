import os
import sys

VSEG_ROOT                             = r"/n/nssdeep/lichtman_lab/amelio/data/vseg"
MOSEG_ROOT                            = os.path.join( VSEG_ROOT, "out/moseg" )
MIKE_CODE_ROOT                        = r"/n/nssdeep/lichtman_lab/amelio/code/share/mike"
BROX_ECCV_2010_EXECUTABLE             = os.path.join( MIKE_CODE_ROOT, "brox_eccv_2010/motionsegBM" )

original_images_ppm                   = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], "results/brox_eccv_2010/original_images_ppm" )
original_images_metadata              = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], "results/brox_eccv_2010/original_images_metadata" )
original_images_metadata_bmf          = os.path.join( original_images_metadata, "original_images_metadata.bmf" )

brox_eccv_2010_results_path_src       = os.path.join( original_images_metadata, "BroxMalikResults" )
brox_eccv_2010_results_path_dst       = os.path.join( MOSEG_ROOT, sys.argv[ 1 ], "results/brox_eccv_2010/raw_output" )

brox_eccv_2010_results_path_src_files = os.path.join( brox_eccv_2010_results_path_src, "*" )

point_trajectories_dat_relative_path = os.path.join( "../../../../data/vseg/out/moseg", sys.argv[ 1 ], "results/brox_eccv_2010/point_trajectories/point_trajectories.dat" )

num_files = len( os.listdir( original_images_ppm ) )

execute_string = "rm -rf " + brox_eccv_2010_results_path_src
print execute_string
os.system( execute_string )

execute_string = BROX_ECCV_2010_EXECUTABLE + " " + original_images_metadata_bmf + " 0 " + str( num_files ) + " 4\n"
print execute_string
os.system( execute_string )

execute_string = "rm -rf " + brox_eccv_2010_results_path_dst
print execute_string
os.system( execute_string )

execute_string = "mkdir -p " + brox_eccv_2010_results_path_dst
print execute_string
os.system( execute_string )

execute_string = "mv " + brox_eccv_2010_results_path_src_files + " " + brox_eccv_2010_results_path_dst
print execute_string
os.system( execute_string )

execute_string = "rm -rf " + brox_eccv_2010_results_path_src
print execute_string
os.system( execute_string )

tracks_file            = os.path.join( brox_eccv_2010_results_path_dst, "*.dat" )
point_trajectories_dir = os.path.join( brox_eccv_2010_results_path_dst, "../point_trajectories" )
point_trajectories     = os.path.join( point_trajectories_dir, "point_trajectories.dat" )

if not os.path.exists( point_trajectories_dir ):
    execute_string = "mkdir -p " + point_trajectories_dir
    print execute_string
    os.system( execute_string )

execute_string = "cp " + tracks_file + " " + point_trajectories
print execute_string
os.system( execute_string )

point_trajectories_txt      = os.path.join( brox_eccv_2010_results_path_dst, "../point_trajectories/point_trajectories.txt" )
point_trajectories_txt_file = open( point_trajectories_txt, 'w' )

point_trajectories_txt_file.write( point_trajectories_dat_relative_path + "\n" )
point_trajectories_txt_file.close()
