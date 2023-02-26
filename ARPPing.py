import argparse
import scapy.all as scapy

class ARPPing():
	def __init__(self):
		print("ARPPing başlatıldı..")
	
	def get_ip_address(self):
		parser=argparse.ArgumentParser() 
		#argparse kütüphanesi sayesinde terminalden argüman almayı sağladı
		parser.add_argument('-i','--ipaddress',type=str,help="IP Adresinizi girmelisiniz")
		args=parser.parse_args()
		#print(args.ipaddress)
		if args.ipaddress!=None:
			return args #birden fazla argümanı alır
		else:
			print("ip adresini -i argümanıyla giriniz")
		
		
	def arp_request(self,ip):
		#netdiscover gibi ARP Ping atma:
		arp_request_packet=scapy.ARP(pdst=ip) #hangi ip'den istek gelicek paketi
		broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #yayın paketi
		combined_packet=broadcast_packet/arp_request_packet #yayın paketi ve ip istek paketinin birleşmiş hali
			
		(answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
		answered_list.summary() #cevap listesinin özeti
		

	
		
if __name__=="__main__": 
	#program çalışmaya başlayınca ilk ARPPing classın çalışması için
	arp_ping=ARPPing()
	ip_range=arp_ping.get_ip_address() #kullanıcıdan ip girdisini alma 
	arp_ping.arp_request(ip_range.ipaddress) # ip range görme
