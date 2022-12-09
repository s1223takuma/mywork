import qrcode
import pyotp
import time

# ユーザーに渡す乱数を作成
random_base32 = pyotp.random_base32()
# uriを作成
uri = pyotp.totp.TOTP(random_base32).provisioning_uri(name="marsquai@google.com",issuer_name="サンプルアプリ")
# QRコードを作成
img = qrcode.make(uri)
img.save('qr_code.png')

# 1000秒間OneTimePasswordを表示
totp = pyotp.TOTP(random_base32)
for i in range(1000):
    print(totp.now())
    time.sleep(1)