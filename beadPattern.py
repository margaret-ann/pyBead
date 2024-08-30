"""
pyBead: a set of tools to generate brick stitch beading patterns
"""
import sys
import colors
from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageFont
from ipywidgets import ColorPicker, VBox

# Render Centered Pattern
class BeadPattern:

    def __init__(self, pattern, palette):
        self.pattern = pattern
        self.palette = palette

        # Miyuki Delica 11/0, 1.6mm x 1.5mm
        self.bead_ratio = 1.6/1.3
        self.bead_height = 50
        self.bead_width = int(self.bead_height * self.bead_ratio) #61

        # Shape-only Pattern
        self.pattern_shape = [len(x) for x in self.pattern]
        self.pattern_width = max(self.pattern_shape)
        self.pattern_height = len(self.pattern_shape)

        # Image dimensions
        self.image_height = self.bead_height * self.pattern_height
        self.image_width = self.bead_width * self.pattern_width

        self.renderPattern()
    
    def renderPattern(self, withGrid=False, withPalette=False, transparent=False):
    
        # Create image
        if transparent:
            if withPalette:
                image = Image.new(mode='RGBA', size=(self.image_width+500, self.image_height), color=(255, 255, 255, 0))
            else:
                image = Image.new(mode='RGBA', size=(self.image_width, self.image_height), color=(255, 255, 255, 0))
        else:
            if withPalette:
                image = Image.new(mode='RGB', size=(self.image_width+500, self.image_height), color=(255, 255, 255))
            else:
                image = Image.new(mode='RGB', size=(self.image_width, self.image_height), color=(255, 255, 255))

        # Create drawing on image
        draw = ImageDraw.Draw(image)

        # Write palette onto image
        if withPalette:
            font = ImageFont.truetype("PTSerif-Regular.ttf", 60)
            text_height = 100
            for key, value in self.palette.items():
                p1 = (self.image_width+100, text_height+15)
                p2 = (self.image_width+150, text_height+15)
                p3 = (self.image_width+150, text_height+65)
                p4 = (self.image_width+100, text_height+65)
                draw.polygon([p1, p2, p3, p4], fill=value[0])
                draw.text((self.image_width+165, text_height), value[1], font=font, fill=0)
                text_height += 80

        # Run through rows
        for index, row in enumerate(self.pattern, start=0):
            y_start = index * self.bead_height
            y_end = (index+1) * self.bead_height
            offset = (self.pattern_width - len(row)) / 2 * self.bead_width

            # Cycle drawing beads
            for x in range(len(row)):

                # Calculate points
                p1 = (offset+((x+1)*self.bead_width), y_start)
                p2 = (offset+(x*self.bead_width), y_start)
                p3 = (offset+(x*self.bead_width), y_end)
                p4 = (offset+((x+1)*self.bead_width), y_end)

                if withGrid:
                    draw.polygon([p1, p2, p3, p4], fill=self.palette[row[x]][0], outline=0, width=3)
                else:
                    draw.polygon([p1, p2, p3, p4], fill=self.palette[row[x]][0])

        del draw

        image.show()


