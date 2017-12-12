import requests
import sys
from termcolor import colored

def run(action, cookie):
    
    accessed_urls=[]
    denied_urls=[]

    risk_list=["admin", "database", "config","bin"]
    risk_flag=False

    with open('urls.txt', 'r') as urls:
        for url in urls:
            risk_color = "white"
            if (action == 0):
                response = requests.get(url.strip())
            else:
                response = requests.get(url.strip(), cookies=cookie)
            if(len(response.history)>0):
                    response.status_code=response.history[0].status_code
            if response.status_code == 200:
                color="green"
                if any (w in url.strip() for w in risk_list):
                    risk_factor = True;
                    risk_color="red"
                accessed_urls.append(url.strip())
            elif (response.status_code == 401 or response.status_code == 403):  
                color="red"
                denied_urls.append(url.strip())
            else:
                color="white"
            print colored(url.strip(), risk_color) + ' =>> ' + colored(str(response.status_code),color)

    answer= raw_input ('[-] ==== Accessed '+ str(len(accessed_urls))+' urls, would you like to save results? (Y/N) === [-]\n')
    if (answer.lower() == 'y'):
        output_file=raw_input('[-] === Enter Output Filename === [-]\n')
        with open(output_file, 'w') as o:
            for u in accessed_urls:
                o.write(url)
    else:
        sys.exit()

if(len(sys.argv)<2):
    option='0'
else:
    option = sys.argv[1]

if (option == '0'):
        print '[+] ==== Running without cookies ====\n'
        run(0, '')
elif (option == '1'):
        print '[+] ==== Running with cookies enabled ====\n'
        cookie = {}
	cookie_name = raw_input('[-] Enter Cookie Name\n')
	cookie_value = raw_input('[-] Enter Cookie Value\n')
	cookie[cookie_name] = cookie_value;
	run(1,cookie) #run with cookies
