def _read_header_tokens(f, n):
    toks = []
    while len(toks) < n:
        line = f.readline()
        if not line:
            raise ValueError("Cabeçalho PPM incompleto.")
        if b"#" in line:
            line = line.split(b"#", 1)[0]
        parts = line.split()
        if parts:
            toks.extend(parts)
    return toks[:n]

def read_ppm(filename):
    with open(filename, "rb") as f:
        magic = f.readline().strip()
        if magic not in (b"P3", b"P6"):
            raise ValueError("Use PPM P3 (ASCII) ou P6 (binário).")
        w_b, h_b, maxv_b = _read_header_tokens(f, 3)
        width = int(w_b); height = int(h_b); max_val = int(maxv_b)
        if max_val != 255:
            raise ValueError("Apenas MaxVal=255 suportado.")
        n_vals = width * height * 3

        if magic == b"P3":
            vals = []
            while len(vals) < n_vals:
                line = f.readline()
                if not line:
                    break
                if b"#" in line:
                    line = line.split(b"#", 1)[0]
                if line.strip():
                    vals.extend(line.split())
            if len(vals) != n_vals:
                raise ValueError("Quantidade de valores P3 inesperada.")
            pixels = [int(x) for x in vals]
            return width, height, pixels
        else:
            raw = f.read(n_vals)
            if len(raw) != n_vals:
                raise ValueError("Quantidade de bytes P6 inesperada.")
            pixels = list(raw)
            return width, height, pixels

def save_bmp(bmp_name, width, height, pixels_rgb):
    # BMP 24-bit, linhas bottom-up, padding de 4 bytes por linha
    import struct

    bpp = 3
    row_bytes = width * bpp
    pad = (4 - (row_bytes % 4)) % 4
    img_size = (row_bytes + pad) * height

    # BITMAPFILEHEADER (14 bytes)
    bfType = b'BM'
    bfSize = 14 + 40 + img_size
    bfReserved1 = 0
    bfReserved2 = 0
    bfOffBits = 14 + 40

    # BITMAPINFOHEADER (40 bytes)
    biSize = 40
    biWidth = width
    biHeight = height  # positivo = bottom-up
    biPlanes = 1
    biBitCount = 24
    biCompression = 0
    biSizeImage = img_size
    biXPelsPerMeter = 2835  # ~72 DPI
    biYPelsPerMeter = 2835
    biClrUsed = 0
    biClrImportant = 0

    with open(bmp_name, "wb") as f:
        # FILE HEADER
        f.write(bfType)
        f.write(struct.pack("<IHHI", bfSize, bfReserved1, bfReserved2, bfOffBits))
        # INFO HEADER
        f.write(struct.pack("<IIIHHIIIIII",
                            biSize, biWidth, biHeight, biPlanes, biBitCount,
                            biCompression, biSizeImage, biXPelsPerMeter,
                            biYPelsPerMeter, biClrUsed, biClrImportant))

        # Dados de imagem (bottom-up): última linha primeiro
        # pixels_rgb está em ordem de varredura top-down RGBRGB...
        for y in range(height - 1, -1, -1):
            row_start = y * width * 3
            row_end = row_start + width * 3
            row = pixels_rgb[row_start:row_end]
            # Converter RGB->BGR
            # row = [R,G,B,R,G,B,...] -> escrever B,G,R por pixel
            for i in range(0, len(row), 3):
                r, g, b = row[i], row[i+1], row[i+2]
                f.write(bytes([b, g, r]))
            # padding
            if pad:
                f.write(b"\x00" * pad)

def ppm_to_bmp(ppm_name, bmp_name):
    w, h, pix = read_ppm(ppm_name)
    save_bmp(bmp_name, w, h, pix)
    print(f"OK: {ppm_name} -> {bmp_name}")

if __name__ == "__main__":
    # Converta seus arquivos gerados:
    try:
        ppm_to_bmp("saida_gray.ppm", "saida_gray.bmp")
    except Exception as e:
        print("Aviso:", e)
    try:
        ppm_to_bmp("saida_binary.ppm", "saida_binary.bmp")
    except Exception as e:
        print("Aviso:", e)