import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:8888/")

notice =  """
Pilih nomor data yang akan di-ambil dari server:
1. aviation_observation
2. cuaca_indo_1
3. gempaterkini
4. Klimat_Potensi_Banjir
5. Maritim_Tinggi_Gelombang_12jam

Pilihan: """

def aviation_observation():
	print server.aviation_observation()

def cuaca_indo_1 ():
	print server.cuaca_indo_1()

def gempaterkini():
	print server.gempaterkini()

def Klimat_Potensi_Banjir():
	print server.Klimat_Potensi_Banjir()

def Maritim_Tinggi_Gelombang_12jam():
	print server.Maritim_Tinggi_Gelombang_12jam()

case = {
	"1" : aviation_observation,
	"2" : cuaca_indo_1,
	"3" : gempaterkini,
	"4" : Klimat_Potensi_Banjir,
	"5" : Maritim_Tinggi_Gelombang_12jam	
}


while True:
	print notice
	inp = raw_input()
	case[inp]()


