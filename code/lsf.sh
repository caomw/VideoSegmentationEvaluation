#!/bin/zsh
# Amelio - 16 November 3.50 PM 2011.
# Send jobs to the cluster. One per video

# Get the list of videos
path_to_videos='/n/nssdeep/lichtman_lab/amelio/data/vseg/out/moseg'
array=$(eval l -d $path_to_videos/*/)

# array=(cars1 cars2)
array=(marple7)

path_to_python_scripts='/n/nssdeep/lichtman_lab/amelio/code/share/mike/evaluation_scripts_python/'

# Send the jobs to the cluster:
for x ($array);
do;
rbsub -n 1 -q normal_serial -m wofsy -R "rusage[mem=20000]" -J "brox_2010_run_$x" -e $x"_error.txt" -o $x"_job_summary.txt" python $path_to_python_scripts"brox_eccv_2010_run.py" $x
done

##
# path_to_videos=''
# for x in $path_to_videos/*
# do;
# chmod -R g+rwx $x/asdpofija/asdpofiaj
# done
