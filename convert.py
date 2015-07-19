#!/usr/bin/python3

import os

import pngs_from_svg as pfs

if __name__ == "__main__":

    print("Converting SVG files to PNG")

    # input directory with svgs in subdirectories
    svgdir = 'svgs'
    # output directory with png files
    pngdir = 'pngs'

    # go through all subdirectories of the input directory
    dirs = os.listdir(svgdir)
    for dirname in dirs:

        # find corresponding png subdir for the svg subdir
        svg_subdir = os.path.join(svgdir, dirname)
        png_subdir = os.path.join(pngdir, dirname)

        # create corresponding png subdir
        os.makedirs(png_subdir, exist_ok=True)

        # iterate svgs
        files = os.listdir(svg_subdir)
        for file in files:

            # figure out name and extension
            svg = os.path.join(svg_subdir, file)
            name, extension = os.path.splitext(file)

            # only take 48px svgs to save some time
            if not "48px" in name:
                continue

            # do the actual conversion
            pfs.create_images(svg, png_subdir, name,
                              "_simple", 48, None, None, nopngcrush=True)
            pfs.create_images(svg, png_subdir, name,
                              "_opacity", 48, "#f00", 0.7, nopngcrush=True)
