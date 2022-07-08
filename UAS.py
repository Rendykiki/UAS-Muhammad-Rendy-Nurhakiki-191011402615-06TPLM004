def down(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)

def up(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)

class B_Pakaian():
    s_dikit = 20
    sedikit = 40
    banyak = 60

    def s_sedikit(self, x):
        if x >= self.sedikit:
            return 0
        elif x<= self.s_dikit:
            return 1
        else:
            return down(x, self.s_dikit, self.sedikit)

    def sedikit(self, x):
        if x >= self.banyak:
            return 0
        elif x<= self.sedikit:
            return 1
        else:
            return down(x, self.sedikit, self.banyak)

    def Banyak(self, x):
        if x >= self.banyak:
            return 1
        elif x<= self.sedikit:
            return 0
        else:
            return up(x, self.sedikit, self.banyak)

class K_pakaian():
    rendah = 40
    sedang = 50
    tinggi = 60
    s_tinngi= 80


    
    def rendah(self, x):
        if x >= self.sedang:
            return 0
        elif x<= self.rendah:
            return 1
        else:
            return down(x, self.sedang,self.rendah)

    def sedang(self, x):
        if x >= self.tinggi:
            return 0
        elif x<= self.sedang:
            return 1
        else:
            return down(x, self.sedang, self.tinggi)

    def tinggi(self, x):
        if x >= self.s_tinngi:
            return 0
        elif x<= self.tinggi:
            return 1
        else:
            return up(x, self.tinggi, self.s_tinngi)

    def s_tinggi(self, x):
        if x >= self.s_tinngi:
            return 1
        elif x<= self.tinggi:
            return 0
        else:
            return up(x, self.tinggi, self.s_tinngi)

class kecepatan():
    cepat = 1500
    lambat = 5000
    banyak = 0
    kotor = 0

    def _lambat(self, a):
        return self.cepat - a*(self.cepat - self.lambat)

    def _cepat(self, a):
        return a*(self.cepat - self.lambat) + self.lambat

    def _inferensi(self, byk=B_Pakaian(), ktr=K_pakaian()):
        result = []
        
        a1 = min(byk.s_sedikit (self.banyak), ktr.rendah (self.kotor))
        z1 = self._cepat(a1)
        result.append((a1, z1))
        
        a2 = min(byk.s_sedikit (self.banyak), ktr.sedang (self.kotor))
        z2 = self._cepat(a1)
        result.append((a2, z2))
        
        a3 = min(byk.s_sedikit (self.banyak), ktr.tinggi (self.kotor))
        z3 = self.cepat(a3)
        result.append((a3, z3))

        a4 = min(byk.s_sedikit (self.banyak), ktr.tinggi (self.kotor))
        z4 = self._cepat(a4)
        result.append((a4, z4))
        
        a5 = min(byk.sedikit (self.banyak), ktr.rendah (self.kotor))
        z5 = self._cepat(a4)
        result.append((a5, z5))

        a6 = min(byk.sedikit (self.banyak), ktr.sedang (self.kotor))
        z6 = self._lambat(a6)
        result.append((a6, z6))

        a7 = min(byk.sedikit (self.banyak), ktr.tinggi (self.kotor))
        z7= self._cepat(a7)
        result.append((a7, z7))

        a8 = min(byk.sedikit (self.banyak), ktr.s_tinggi (self.kotor))
        z8 = self._lambat(a8)
        result.append((a8,z8))

        a9 = min(byk.Banyak (self.banyak), ktr.rendah (self.kotor))
        z9 = self._lambat(a8)
        result.append ((a9,z9))

        a10 = min(byk.Banyak (self.banyak), ktr.sedang (self.kotor))
        z10 = self._cepat (a10)
        result.append((a10,z10))

        a11 = min(byk.Banyak (self.banyak), ktr.tinggi (self.kotor))
        z11 = self._cepat(a11)
        result.append((a11,z11))
        
        a12 = min(byk.Banyak (self.banyak), ktr.s_tinggi (self.kotor))
        z12 = self._cepat(a12)
        result.append((a12,z12))
        return result
    
    def defuzifikasi(self, data_inferensi=[]):
        # (α1∗z1+α2∗z2+α3∗z3+α4∗z4) / (α1+α2+α3+α4)
        data_inferensi = data_inferensi if data_inferensi else self._inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            # data[0] = a 
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        return res_a_z/res_a