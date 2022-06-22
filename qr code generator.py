#pip install qrcode use this command to download the qrcode module
import qrcode as qr
link=input("enter link\n")
name=input("what should be the name of the file\n")
image=qr.make(f"{link}")
image.save(f"{name}.png")
