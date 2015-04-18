import sys, json, httplib
from keys import kAppIdKey, kRestApiKey

def sendPush(receiverId):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', '/1/push', json.dumps({
           "channels": [
             "global"
           ],
           "data": {
             "alert": "This is Azk! Let's Go!.",
             "badge": "1",
             "sound": "applause.mp3",
             "title": "AZK!",
           "p": receiverId
           }
         }), {
           "X-Parse-Application-Id": kAppIdKey,
           "X-Parse-REST-API-Key": kRestApiKey,
           "Content-Type": "application/json"
         })
    result = json.loads(connection.getresponse().read())
    print result

def main(argv):
    print "Sending push to id : "+argv
    sendPush(argv);

if __name__ == "__main__":
    if (len(sys.argv)>2):
        print "Only one argument allowed"
        sys.exit(2)

    main(sys.argv[1])