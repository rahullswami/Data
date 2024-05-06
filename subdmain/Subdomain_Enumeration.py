
import requests, sys


user = input("enter site ports : ")
def request(url):
    try:
        result = requests.get("https://"+url)
        if(result):
            print("[+] Subdomain discovered -----> "+url)
    except:
        pass

def main():
    target_url = user
    #open subd list
    with open("/home/jarry/vscode_All_files/first_page/subdmain/subdmainwordlist.txt","r") as wordlist :
        for line in wordlist :
            word = line.strip()
            test_url = word+"."+target_url
            request(test_url)

main()