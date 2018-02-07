import sys
from PIL import Image
import os.path

import sys
firstarg=sys.argv[1]

def compareImage(userRoll):

	images = map(Image.open, [userRoll+'User1.jpg', userRoll+'User2.jpg',userRoll+'User3.jpg',userRoll+'User4.jpg',userRoll+'User5.jpg',userRoll+'User6.jpg',userRoll+'User7.jpg',userRoll+'User8.jpg',userRoll+'User9.jpg',userRoll+'User10.jpg',userRoll+'User11.jpg', userRoll+'User12.jpg',userRoll+'User13.jpg',userRoll+'User14.jpg',userRoll+'User15.jpg',userRoll+'User16.jpg',userRoll+'User17.jpg',userRoll+'User18.jpg',userRoll+'User19.jpg',userRoll+'User20.jpg'])
	widths, heights = zip(*(i.size for i in images))
	total_width = sum(widths)
	max_height = max(heights)
	new_im = Image.new('RGB', (total_width, max_height))
	x_offset = 0
	for im in images:
		new_im.paste(im, (x_offset,0))
  		x_offset += im.size[0]
	
	new_im.save('test.jpg')
	

compareImage(firstarg)

