import qrcode

data = "https://www.google.com"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1, 
    border=1,
)

qr.add_data(data)
qr.make(fit=True)

qr.print_ascii(invert=True) 

print("\n✅ QR Code successfully displayed in terminal!")
