import argparse
import os
from imutils import paths
#from PIL import Image

#from resizeimage import resizeimage
testImages="C:/xampp/htdocs/BeefAPI/IMG/AA"
i=1
for imagePath in paths.list_images(testImages):
	dst =testImages+"/"+"AA." + str(i) + ".jpg"
	src =imagePath
	print(src)
       
          
        # rename() function will 
        # rename all the files 
	os.rename(src, dst) 
	i += 1
print ("Complete")
