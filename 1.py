from PIL import Image

im = Image.open("./bluecamaro.jpeg")
# new_im = im.resize((640,480))
new_im = im.rotate(180).resize((640,480))
new_im.save("./files/camaro_resized.jpg")
