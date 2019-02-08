import json
import requests
from playsound import playsound

def makeHTTPRequest(url, method, params, headers):
    r = None

    if( method == "GET"):
        r = requests.get(url, headers = headers)
    if( method == "PUT"):
        r = requests.put(url, data = json.dumps(params), headers = headers)

    return r

def main():
	header={"Accept": "application/json, text/plain, */*", "Content-type": "application/json; charset=UTF-8"};
	r= makeHTTPRequest("https://api.coindesk.com/v1/bpi/currentprice.json","GET","NaN",header)
	jsonresp= r.json()
	rate=jsonresp['bpi']['USD']['rate']
	frate = float(rate.replace(',',''))
	if frate > 3400: #change threshold as needed
		playsound('ND_yousuffer.mp3') #Jumpscare here 

if __name__ == '__main__':
    main()
