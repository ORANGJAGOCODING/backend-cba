data_toko = {
    "Jakarta": [500, -100, 300, 200],
    "Bandung": [-50, 400, 150],
    "Surabaya": [100, 250, -200, 50]
}

def hitung_pendapatan(data_toko):
    total = 0
    for kota in data_toko:
        for value in data_toko[kota]:
            if value >= 0:
                total += value
    
    return total

print("Total Pendapatan:", hitung_pendapatan(data_toko))