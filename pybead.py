"""
pyBead: a set of tools to generate brick stitch beading patterns
"""
import sys
from PIL import Image, ImageDraw, ImageFont
from ipywidgets import ColorPicker, VBox

# CIRCLE PATTERN
if __name__ == '__main__':

    pattern = [5, 8, 11, 12, 13, 14, 14, 15, 15, 16, 16, 15, 15, 14, 14, 13, 12, 11, 8, 5]
    
    # Pattern dimensions
    pattern_width = max(pattern)
    pattern_height = len(pattern)

    # Miyuki Delica 11/0, 1.6mm x 1.5mm
    bead_ratio = 1.6/1.3
    bead_height = 50
    bead_width = int(bead_height * bead_ratio) #61

    # Image dimensions
    image_height = bead_height * pattern_height
    image_width = bead_width * pattern_width
    
    # Create image
    image = Image.new(mode='L', size=(image_width, image_height), color=255)
    
    # Draw vertical lines by row
    draw = ImageDraw.Draw(image)

    # Run through rows
    for index, row in enumerate(pattern, start=0):
        y_start = index * bead_height
        y_end = (index+1) * bead_height
        offset = (pattern_width - row) / 2 * bead_width

        # Cycle drawing beads
        for x in range(row):

            # Draw vertical
            line_x1 = ((offset+(x*bead_width), y_start), (offset+(x*bead_width), y_end))
            draw.line(line_x1, fill=128)
            line_x2 = ((offset+((x+1)*bead_width), y_start), (offset+((x+1)*bead_width), y_end))
            draw.line(line_x2, fill=128)

            # Draw horizontal
            line_y1 = ((offset+(x*bead_width), y_start), (offset+((x+1)*bead_width), y_start))
            draw.line(line_y1, fill=128)
            line_y2 = ((offset+(x*bead_width), y_end), (offset+((x+1)*bead_width), y_end))
            draw.line(line_y2, fill=128)

    del draw

    image.show()

#cell 2
main_color = ColorPicker(value="#616161", description="Main color")
a_color = ColorPicker(value="#dcd618", description="Color A")
b_color = ColorPicker(value="#66ccff", description="Color B")
c_color = ColorPicker(value="#db7575", description="Color C")
VBox((main_color, a_color, b_color, c_color))


