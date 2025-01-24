import qrcode


def main():
    src = input("Enter the text to convert to QR code: ")

    box_size = int(input("Enter the box size (default is 10): ") or "10")
    border = int(input("Enter the border size (default is 4): ") or "4")

    fill_color = input("Enter the fill color (default is black): ") or "black"
    back_color = input("Enter the background color (default is white): ") or "white"

    qr = qrcode.QRCode(version=1, box_size=box_size, border=border)
    qr.add_data(src)

    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    save = input("Do you want to save the QR code? (y/n): ")

    if save.lower() == "y" or len(save) == 0:
        img.save("./dotutils/media/qrcode.png")
        print("QR code saved as qrcode.png")


if __name__ == "__main__":
    main()
