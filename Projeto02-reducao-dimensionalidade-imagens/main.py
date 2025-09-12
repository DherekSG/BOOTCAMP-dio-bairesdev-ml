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
            raise ValueError("Formato não suportado. Use PPM P3 (ASCII) ou P6 (binário).")

        # lê largura, altura, max_val (ignorando comentários e quebras)
        w_b, h_b, maxv_b = _read_header_tokens(f, 3)
        width = int(w_b); height = int(h_b); max_val = int(maxv_b)
        if max_val != 255:
            raise ValueError("Apenas MaxVal=255 suportado.")

        n_pix_vals = width * height * 3

        if magic == b"P3":
            # ASCII: coletar todos os números restantes
            vals = []
            while len(vals) < n_pix_vals:
                line = f.readline()
                if not line:
                    break
                if b"#" in line:
                    line = line.split(b"#", 1)[0]
                if line.strip():
                    vals.extend(line.split())
            if len(vals) != n_pix_vals:
                raise ValueError("Quantidade de valores P3 inesperada.")
            pixels = [int(x) for x in vals]
            return width, height, max_val, pixels

        else:  # P6 binário
            # Há um único byte de whitespace após o max_val; garantimos que estamos
            # no início dos dados binários (como usamos readline, já estamos).
            raw = f.read(n_pix_vals)
            if len(raw) != n_pix_vals:
                raise ValueError("Quantidade de bytes P6 inesperada.")
            pixels = list(raw)  # lista de ints 0..255
            return width, height, max_val, pixels

def save_ppm(filename, width, height, max_val, pixels):
    # salva em P3 ASCII para ficar legível/compatível com o enunciado
    with open(filename, "w", encoding="ascii") as f:
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_val}\n")
        for i in range(0, len(pixels), 3):
            f.write(f"{pixels[i]} {pixels[i+1]} {pixels[i+2]}\n")

def to_grayscale(width, height, pixels):
    gray = []
    for i in range(0, len(pixels), 3):
        r, g, b = pixels[i], pixels[i+1], pixels[i+2]
        gval = int(0.299*r + 0.587*g + 0.114*b + 0.5)
        gray.extend([gval, gval, gval])
    return gray

def to_binary(width, height, gray_pixels, threshold=128):
    binpix = []
    for i in range(0, len(gray_pixels), 3):
        v = 255 if gray_pixels[i] >= threshold else 0
        binpix.extend([v, v, v])
    return binpix

if __name__ == "__main__":
    # troque aqui o nome do seu arquivo .ppm (P3 ou P6)
    in_name = "./imagens/lena.ppm"        # <— ajuste se o nome for outro
    w, h, maxv, pix = read_ppm(in_name)

    gray = to_grayscale(w, h, pix)
    save_ppm("saida_gray.ppm", w, h, maxv, gray)

    binary = to_binary(w, h, gray, threshold=128)
    save_ppm("saida_binary.ppm", w, h, maxv, binary)

    print("OK: gerados saida_gray.ppm e saida_binary.ppm")
