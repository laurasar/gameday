import requests , base64, os, string, secrets, hashlib 
from dotenv import load_dotenv



url='https://accounts.spotify.com/api/token'
grant_type='client_credentials'
 
 ### privatizes client info 
def makeCodeVerifier():
    length = 64; 
    codeSource= string.ascii_letters + string.digits + '-._~'
    separate = ''

    code= ''.join(secrets.choice(codeSource) for i in range(length))

    return code 

codeVer= makeCodeVerifier()
### encodes client info 
def generateCodeChallenge(codeVerifier): 
    encodedCode = base64.b64encode((codeVerifier))
    

    

def getClientCredentials() :
    load_dotenv()
    clientID = os.getenv("CLIENT_ID")
    clientSecret = os.getenv("CLIENT_SECRET")

    preclientInfo = (clientID + ":" + clientSecret).encode("ascii")

    clientInfo = (base64.b64encode((preclientInfo))).decode('utf-8')

    return clientInfo


def getAccess():
    authOptions = {
    'url': 'https://accounts.spotify.com/api/token',

    'headers': {
        'Authorization': 'Basic ' + getClientCredentials() 
    },
    'data': {
        'grant_type': 'client_credentials'
    }
    }
    response = requests.post(authOptions['url'], headers=authOptions['headers'], data=authOptions['data'])

    return response

def getTokenHeaders():

    if getAccess().status_code == 200:
        body = getAccess().json()
        token = body['access_token']
        type = body['token_type']
        #print("Is working")

    headers = {
    "Authorization": f"{type} {token}"
    }
    #print(headers)
    return headers

x = getTokenHeaders()

print(x)
url = "https://api.spotify.com/v1/me/shows?offset=0&limit=20"
response = requests.get(url, params= x)
print(response.status_code)