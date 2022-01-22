# Generate QR code for your Url and save your QR to local as png file.

import qrcode           # module for qr generation 

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
data = "google.com"                  # url of website whose qr you want
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("imageQR.png")
