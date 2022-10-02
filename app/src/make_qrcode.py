import os
import qrcode

def make_qrcode(text, file_name):
    img = qrcode.make(text)
    img.save("/app/output/{}.png".format(file_name))

if __name__ == "__main__":
    text = os.environ.get("TEXT", "")
    file_name = os.environ.get("FILE_NAME", "qrcode")
    make_qrcode(text, file_name)