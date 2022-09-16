import os
from PIL import Image
def image_operator(image_dir, degrees, new_size, target_dir):
    for i in os.listdir(image_dir):
        im = Image.open(f"{image_dir}/"+i)
        new_im = im.rotate(degrees).resize(new_size).convert("RGB")
        new_im.save(f"{target_dir}/"+i, "jpeg")

image_operator("./images", 90, (128,128), "./opt/icons")