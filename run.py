import beadPattern as bp
import pumpkin

pumpkinCircle = bp.BeadPattern(pumpkin.pattern, pumpkin.palette)
pumpkinCircle.renderPattern(transparent=True)
pumpkinCircle.renderPattern(withPalette=True)