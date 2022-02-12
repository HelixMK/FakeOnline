from time import sleep,time
from threading import Thread,Timer
from subprocess import Popen,PIPE
from random import choice
from select import select

freeport=27015

needlog=True

ips=[
['','217.171.147.232','229317671805620', 'vpn',False],
['','91.219.238.56','229317671805620', 'vpn',False],
['','185.65.206.19','229317671805620', 'vpn',False],
['','149.154.154.61','229317671805620', 'vpn',False],
['','93.99.104.14','229317671805620', 'vpn',False],
['','188.241.60.242','229317671805620', 'vpn',False],
['','196.242.244.23','229317671805620', 'vpn',False],
['','207.180.241.143','229317671805620', 'vpn',False],
['','46.249.59.88','229317671805620', 'vpn',False],
['','5.133.179.243','229317671805620', 'vpn',False],
['','45.138.99.3','229317671805620', 'vpn',False],
['','107.175.38.101','229317671805620', 'vpn',False],
['','179.43.174.210','229317671805620', 'vpn',False],
['','104.248.133.59','229317671805620', 'vpn',False],
['','195.123.221.123','229317671805620', 'vpn',False],
['','159.203.78.96','229317671805620', 'vpn',False],
['','139.59.8.131','229317671805620', 'vpn',False],
['','188.208.143.114','229317671805620', 'vpn',False],
['','37.1.215.39','229317671805620', 'vpn',False],
['','110.172.104.227','229317671805620', 'vpn',False],
['','119.59.97.58','229317671805620', 'vpn',False],
['','178.128.51.9','229317671805620', 'vpn',False],
['','209.97.161.129','229317671805620', 'vpn',False],
['','194.38.20.81','229317671805620', 'vpn',False],
['','95.154.199.21','229317671805620', 'vpn',False],
['','89.35.57.15','229317671805620', 'vpn',False],
['','198.50.183.71','229317671805620', 'vpn',False],
['','209.97.133.64','229317671805620', 'vpn',False],
['','89.35.57.17','229317671805620', 'vpn',False],
['','157.230.30.126','229317671805620', 'vpn',False],
['','213.8.166.188','229317671805620', 'vpn',False],
['','151.236.30.50','229317671805620', 'vpn',False],
['','125.212.220.125','229317671805620', 'vpn',False],
]


niki_detey_dombassa=[]
with open('names.txt') as f:
	niki_detey_dombassa = f.readlines()
	for i in range(len(niki_detey_dombassa)):
		niki_detey_dombassa[i]=niki_detey_dombassa[i].strip()
	f.close()

accs=[ # accounts
["pagela93","ramzesramzes123"],
["theyoutubers001","ymt5EmXrdLTo"],
["maitxlol","Ieah9KutAuAs"],
["a_marsinsky","jaxO_ihYl6tU"],
["romamagramov","kMFzKRSF"],
#["carsonpalmer117","Guntherpet1"],
["kmr1yyanxiqvvz0xzjg","owum3yejdb"],
["maxpic1","340756876809701"],
["matthieu27111","Cwacjopsqgrsqh1"],
["kOVaL982","Rwkuhtemyftyoj1"],
["mick2817","45096756343"],
["zbzfizsxyvzavhe","herjvy6y"],
["veeaibwqpouxl","huq5j943"],
["w1z7wbir","0icwwxu1v"],
["arikl4","jmodtkhdtkhdgfh"],

]
'''["theyoutubers001","ymt5EmXrdLTo"],
["maitxlol","Ieah9KutAuAs"],
["a_marsinsky","jaxO_ihYl6tU"],
["romamagramov","kMFzKRSF"],
["carsonpalmer117","Guntherpet1"],
["kmr1yyanxiqvvz0xzjg","owum3yejdb"],
["maxpic1","340756876809701"],
["matthieu27111","Cwacjopsqgrsqh1"],
["kOVaL982","Rwkuhtemyftyoj1"],
["mick2817","45096756343"],
["zbzfizsxyvzavhe","herjvy6y"],
["veeaibwqpouxl","huq5j943"],
["w1z7wbir","0icwwxu1v"],
["arikl4","jmodtkhdtkhdgfh"],'''


servers=[
"92.242.40.127:27015", 
]

threads={}




#logs=open('mlogs.txt','a')
#if not needlog:
#	logs.close()

def PPTPHandler(ip,name,remname):
	global ips
	fname=ip.replace('.','_')
	f=open('/etc/ppp/peers/'+fname,'w')
	f.write('''pty "/usr/sbin/pptp '''+ip+''' --nolaunchpppd"
	lock
	noauth
	nobsdcomp
	nodeflate
	name '''+name+'''
	remotename '''+remname+'''
	ipparam '''+fname+'''
	require-mppe-40
	require-mppe-128
	noipdefault
	persist
	''')
	f.close()
	mynum=0
	for i in ips:
		if i[1]==ip:
			break
		else:
			mynum=mynum+1
	while True:
		p = Popen(["pon",fname,"nodetach"],stdout=PIPE)
		myip=''
		while True:
			if p.poll() is not None:
				print(ip,'closed',"pon"+' '+fname+' '+"nodetach")
				break
			else:
				w=p.stdout.readline()
				if w.find(b'local  IP address') != -1:
					ips[mynum][0]=myip
					print(ip,w)
				if w.find(b'Connect:') != -1:
					myip=w.split(b' ')[1].decode('utf-8').strip()

def SetUpGmod(l,pas,ip,clport):
	#global logs
	global threads
	#global ips
	n=choice(niki_detey_dombassa)
	vsepizdec=False
	while True:
		if vsepizdec:
			print(l,pas,'is lox')
			break
		p = Popen(["node","index.js",l,pas],stdout=PIPE)
		steamid=''
		while True:
			if p.poll() is not None:
				if steamid == '':
					vsepizdec=True
				break
			else:
				w=p.stdout.readline()
				#logs.write(w.decode('utf-8')+'\n')
				if w.find(b'saved!') != -1:
					steamid=w.split(b' ')[0].strip().decode('utf-8')
					p.terminate()
		if vsepizdec:
			print(l,pas,'is lox')
			break
		mynum=0
		threads[clport][2]=time()
		lip='ens192'
		'''while True:
			for j in ips:
				if j[0] != '' and not j[4]:
					ips[mynum][4]=True
					lip=j[0]
					print(steamid,lip)
					break
				else:
					mynum=mynum+1
			if lip == 'eth0':
				mynum=0
				threads[clport][2]=time()
				sleep(1)
			else:
				break'''


		p = Popen(["./gmod",ip,str(clport),n,''.join((choice('abcdxyzpqr') for i in range(5))),steamid,steamid,'ens192'],stdout=PIPE)
		while True:
			if p.poll() is not None:
				break
			else:
				#w = select([p.stdout], [], [], 15.0)
				w=p.stdout.readline()
				#print(threads,clport)
				threads[clport][2]=time()
				print(l,ip,w)

				#logs.write(w.decode('utf-8')+'\n')
				if w.find(b'Client not connected to Steam!') != -1 or w.find(b'canceled') != -1 or w.find(b'errmsg') != -1:
					print(l,ip,w)
					p.terminate()
					break
		#ips[mynum][4]=False
		print(l,ip,'reconnection')

threads_pptp=[]
'''
for i in ips:
	t=Thread(target=PPTPHandler,args=(i[1],i[2],i[3],))
	threads_pptp.append(t)
	t.start()'''

for s in servers:
	for i in accs:
		threads[freeport]=[]
		t=Thread(target=SetUpGmod,args=(i[0],i[1],s,freeport,))
		threads[freeport].append(t)
		threads[freeport].append((i[0],i[1],s,freeport,))
		threads[freeport].append(time())
		t.start()
		sleep(2.3)
		freeport=freeport+1


threads_alive_pptp=[]


while True:

	sleep(10)
	print("Threads: ",len(threads_pptp)+len(threads))
	if len(threads) == 0:
		print('bb')
		break
#if needlog:
	#logs.close()

#"Client not connected to Steam"