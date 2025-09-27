import qrcode
import sys

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "-link":
        print("Usage: python3 generate_qr.py -link <URL>")
        return

    url = sys.argv[2]
    img = qrcode.make(url)
    img.save("qr_cookpit.png")
    print(f"QR généré pour : {url}")

if __name__ == "__main__":
    main()
