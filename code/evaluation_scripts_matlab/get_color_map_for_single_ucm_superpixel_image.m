function color_map = get_color_map_for_single_ucm_superpixel_image( input_filename, threshold )

    ucm = imread( input_filename );
    ucm_d = im2double(ucm);
    k = threshold;

    i_L = bwlabel(ucm_d <= k);
    i_L = uint32(i_L);

    alph_size = ceil(nthroot(double(max(i_L(:))), 3));

    cmap = rand_cmap_alphb_size(alph_size);

    color_map = cmap;
    
end

