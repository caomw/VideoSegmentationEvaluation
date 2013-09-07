function convert_ucm_superpixel_image_to_dense_color_label_image( input_filename, output_filename, threshold, color_map )

    ucm = imread( input_filename );
    ucm_d = im2double(ucm);
    k = threshold;

    i_L = bwlabel(ucm_d <= k);
    i_L = uint32(i_L);

    i_L_zero = i_L == 0;
    [i_D , L] = bwdist(~i_L_zero);

    dist_th = 4;
    i_bw_pixels_to_inpaint = (i_D <= dist_th) & i_L_zero;

    lin_indices_closest = L(i_bw_pixels_to_inpaint);
    i_L_new = i_L;
    i_L_new(i_bw_pixels_to_inpaint) = i_L(lin_indices_closest);

    i_L = i_L_new; clear i_L_new;

    i_lbls_rgb        = ind2rgb(i_L, color_map );   
    i_lbls_rgb_uint   = uint8(i_lbls_rgb);

    imwrite(i_lbls_rgb_uint, output_filename );

end
