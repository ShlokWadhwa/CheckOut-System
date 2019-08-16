# Shlok Wadhwa, Project, CIS345 T/Th 10:30-11:45

# getting required imports
from PIL import Image, ImageFilter

# opening image and adding filter
filename = 'Kitchen_Supply.png'
im = Image.open(filename)
im.show()
sharp = im.filter(ImageFilter.EDGE_ENHANCE)
sharp.show()

# resizing image to fit as icon
small = im.resize((16, 16))
small.show()
im.save("icon.png", "PNG")

# resizing image to use as thumbnail for actual file.
im.thumbnail((128, 128))
im.show()
im.save("logo.png", "PNG")


