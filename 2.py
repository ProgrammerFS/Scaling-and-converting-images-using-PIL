import os
from PIL import Image
for i in os.listdir("./images"):
    im = Image.open("./images/"+i)
    new_im = im.rotate(90).resize((128,128))
    new_im.save("./opt/icons/"+i, "jpeg")