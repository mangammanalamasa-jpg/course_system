import qrcode

url = "http://192.168.1.5:5000/s3"

img = qrcode.make(url)

img.save("stage3_qr.png")

print("QR generated successfully")