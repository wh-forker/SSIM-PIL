# https://en.wikipedia.org/wiki/Standard_deviation#Population_standard_deviation_of_grades_of_eight_students
# https: // en.wikipedia.org / wiki / Structural_similarity  # Algorithm

def compare_ssim(image_0, image_1, tile_size: int = 7, GPU: bool = False) -> float:
    """
    Compute the structural similarity between the two images.
    :param image_0: PIL Image object
    :param image_1: PIL Image object
    :param tile_size: Height and width of the image's sub-sections used
    :param GPU: If true, try to compute on GPU
    :return: Structural similarity value
    """
    # constants
    dynamic_range = 255
    c_1 = (dynamic_range * 0.01) ** 2
    c_2 = (dynamic_range * 0.03) ** 2
    pixel_len = tile_size * tile_size
    width, height = image_0.size
    width = width // tile_size * tile_size
    height = height // tile_size * tile_size

    # Verify input parameters
    if image_0.size != image_1.size:
        raise AttributeError('The images do not have the same resolution')
    # no else
    if image_0.mode != image_1.mode:
        raise AttributeError('The images have different color channels')
    # no else
    if width < tile_size or height < tile_size:
        raise AttributeError('The images are smaller than the window_size')
    # no else

    if GPU:
        try:
            from ._gpu_strategy import get_ssim_sum
        except Exception as e:
            print(e.replace("No module named 'pyopencl' ", "No module named 'pyopencl' "
                                                           "cl12 version by Christoph Gohlke for windows is recommended: "
                                                           "https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopencl"))
            from ._cpu_strategy import get_ssim_sum
    else:
        from ._cpu_strategy import get_ssim_sum

    # Calculate mean
    return get_ssim_sum(image_0, image_1, tile_size, pixel_len, width, height, c_1, c_2) * pixel_len / (
                len(image_0.mode) * width * height)
