import pyotp
import qrcode

# Create a TOTP
totp = pyotp.TOTP("PIPWY5DOEHK3PXP")

auth_str = totp.provisioning_uri(name='testing', issuer_name='ecommerce')

# Generate a QR code
img = qrcode.make(auth_str)
img.save('testQR.jpg')
