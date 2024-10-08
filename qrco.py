import qrcode

# 网址
url = "https://enanin001.github.io/Yuan_Chen_Resume/"

# 创建 qr 代码生成器
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 添加数据
qr.add_data(url)
qr.make(fit=True)

# 创建一个图像
img = qr.make_image(fill='black', back_color='white')

# 保存图像
img.save("website_qrcode.png")
