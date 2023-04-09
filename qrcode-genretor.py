import qrcode
import image

qr = qrcode.QRCode(
    version = 10,
    box_size = 5,
    border = 2.5

)

data = "https://ibb.co/f13PCXt"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_colour = "white")
img.save("Kundan.png")