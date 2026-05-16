import qrcode

# The exact working link to your student system
url = "https://course-system-mg00.onrender.com/s3"

img = qrcode.make(url)

img.save("stage3_qr.png")

print("QR generated successfully")