import os, numpy, PIL
from PIL import Image

# Access all PNG files in directory
#listdir 會列出目標資料夾的所有檔案名稱
allfiles=os.listdir(os.getcwd()) 
#判斷檔案是否為圖片,附檔名四個字
imlist=[filename for filename in allfiles if  filename[-4:] in [".jpg",".JPG"]]


# Assuming all images are the same size, get dimensions of first image
w,h=Image.open(imlist[0]).size #获取图像的宽和高
N=len(imlist)

# Create a numpy array of floats to store the average (assume RGB images)
arr=numpy.zeros((h,w,3),numpy.float)

# Build up average pixel intensities, casting each image as an array of floats
for im in imlist:
    imarr=numpy.array(Image.open(im),dtype=numpy.float)
    arr=arr+imarr/N

# Round values in array and cast as 8-bit integer
arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

# Generate, save and preview final image
out=Image.fromarray(arr,mode="RGB")
out.save("Average.png")
out.show()
