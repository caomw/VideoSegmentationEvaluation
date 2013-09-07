function ochs_iccv_2011_generate_original_and_superpixel_images( directory_name )

	VSEG_ROOT                                 = '/n/nssdeep/lichtman_lab/amelio/data/vseg';
	MOSEG_ROOT                                = strcat( VSEG_ROOT, '/out/moseg' );
	
	input_original_images                     = strcat( MOSEG_ROOT, '/', directory_name, '/results/brox_eccv_2010/original_images_ppm/*.ppm' );
	input_ucm_images_dir                      = strcat( MOSEG_ROOT, '/', directory_name, '/ucm_img' );
	input_ucm_images                          = strcat( input_ucm_images_dir, '/*.png' );
	output_original_and_superpixel_images_dir = strcat( MOSEG_ROOT, '/', directory_name, '/results/ochs_iccv_2011/original_and_superpixel_and_sparse_label_images' );
		
	execute_string         = char( strcat( 'rm -rf', {' '}, output_original_and_superpixel_images_dir ) );
	execute_string_display = char( strcat( execute_string, '\n' ) );
	fprintf( execute_string_display );
	system( execute_string );

	execute_string         = char( strcat( 'mkdir -p', {' '}, output_original_and_superpixel_images_dir ) );
	execute_string_display = char( strcat( execute_string, '\n' ) );
	fprintf( execute_string_display );
	system( execute_string );
	
	execute_string         = char( strcat( 'cp', {' '}, input_original_images, {' '}, output_original_and_superpixel_images_dir ) );
	execute_string_display = char( strcat( execute_string, '\n' ) );
	fprintf( execute_string_display );
	system( execute_string );
	
	
	files = dir( input_ucm_images );
	
	for file_index = 1:numel( files )
		
		[ input_file_path, input_file_base_name, input_file_extension ] = fileparts( files( file_index ).name );
		input_file_full_name = strcat( input_ucm_images_dir, '/', input_file_base_name, input_file_extension );
		
		threshold        = 0.05;
		output_file_path = strcat( output_original_and_superpixel_images_dir, '/', input_file_base_name, '_seg0.ppm' );
		color_map        = get_color_map_for_single_ucm_superpixel_image( input_file_full_name, threshold );
		
		convert_ucm_superpixel_image_to_dense_color_label_image( input_file_full_name, output_file_path, threshold, color_map );
		fprintf( strcat( output_file_path, '\n' ) );

		threshold        = 0.1;
		output_file_path = strcat( output_original_and_superpixel_images_dir, '/', input_file_base_name, '_seg1.ppm' );
		color_map        = get_color_map_for_single_ucm_superpixel_image( input_file_full_name, threshold );
		
		convert_ucm_superpixel_image_to_dense_color_label_image( input_file_full_name, output_file_path, threshold, color_map );
		fprintf( strcat( output_file_path, '\n' ) );

		threshold        = 0.15;
		output_file_path = strcat( output_original_and_superpixel_images_dir, '/', input_file_base_name, '_seg2.ppm' );
		color_map        = get_color_map_for_single_ucm_superpixel_image( input_file_full_name, threshold );
		
		convert_ucm_superpixel_image_to_dense_color_label_image( input_file_full_name, output_file_path, threshold, color_map );
		fprintf( strcat( output_file_path, '\n' ) );
		
	end

end