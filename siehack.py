import requests,time
while(True):
    url = "https://zu5efupb7dsf2lrhouum6ylyre0vhmbj.lambda-url.eu-west-1.on.aws/"
    with open("NS_20221201.txt","r") as f:
        x=len(f.readlines())
        payload={}

        headers = {'occupants': str(x)}



        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
    time.sleep(30)
