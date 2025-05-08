import qrcode
from qrcode.constants import ERROR_CORRECT_M
import binascii
import os

# HEX
hex_data = "50966FAF0342E957DCE6ED8E6AC23609504F4B454D4F4E3131DD"
binary_data = binascii.unhexlify(hex_data)

# QRの設定
qr = qrcode.QRCode(
    version=2,
    error_correction=ERROR_CORRECT_M,
    box_size=10,
    border=4,
    mask_pattern=2  
)

qr.add_data(binary_data)
qr.make(fit=False)

# 作成
img = qr.make_image(fill_color="black", back_color="white")

# 保存
output_path = os.path.join(os.path.dirname(__file__), "qr.png")
img.save(output_path)
print(f"{output_path}に保存された")
