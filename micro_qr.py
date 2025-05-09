import segno

data = "50129201"

qr = segno.make_micro(data, error='M')

qr.save('microqr.png', scale=10)

# qr.save('microqr.svg')
print("保存した　microqr.png")
