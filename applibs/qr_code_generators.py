import json

import pyqrcode
import qrcode


class GeneratorQRCode:
    def qr_code_with_pyqrcode(self, context):
        qr_code = pyqrcode.create(json.dumps(context))
        with open('whats_app_login/static/qr_codes/code.png', 'wb') as fstream:
            qr_code.png(fstream, scale=5)

    def qr_code_generator(self, context):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=4,
            border=2,
        )

        qr.add_data(json.dumps(context))
        qr.make(fit=True)
        # Create an image from the QR Code instance
        img = qr.make_image()
        img = img.save("image.png")

        # Save it somewhere, change the extension as needed:
        # img.save("image.png")
        # img.save("image.bmp")
        # img.save("image.jpeg")
        # img.save("image1.jpg")

    def qr_code(self):
        code = pyqrcode.create('Are you suggesting coconuts migrate?')
        image_as_str = code.png_as_base64_str(scale=5)
        code.show()


qr_code_generator = GeneratorQRCode()
