import segno

data = "50129201"

qr = segno.make_micro(data, error='M')

qr.save('microqr_50129201.png', scale=10)

# qr.save('microqr_50129201.svg')
print("Micro QR создан и сохранён как microqr_50129201.png")
