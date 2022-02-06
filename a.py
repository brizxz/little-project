from ensurepip import version
import qrcode
import image
qr=qrcode.QRCode(
    version = 15,
    box_size = 15,
    border=8
)
data="https://youtu.be/kYhh1PpsOg4"

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black", back_color="white")
img.save("test.png")
