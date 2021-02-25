import tweepy
consumerkey="UNLSdFebZG7gGuY1NERHcb5O8"
consumersecret="XYqh5ohxy3CUGRgYbL5ylnToTpXzjQozcpTYXjzjml94vbPEhQ"
access_token ="1353998710930354176-wzaBL2XT37w9Qf7VTppGCNRU8cLoSl"
access_token_secret ="McKhNczDDTnmB360WKXIG9rJz9Ky6r9zUMkLZ7khSMK85"

auth=tweepy.OAuthHandle(consumerkey,consumersecret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

userID=input("Give twitter account: ")
tweets=api.user_timeline(screen_name=userID,count=10,include_rts=False,tweet_mode="extended")
all_tweets=[]
for info in tweets[:10]:
    x=info.full_text
    all_tweets.append(x.split())

maxlength=0
minlength=100
maximums=[]
minimums=[]
words1=[]
words2=[]
for i in range(0,5,1):
    maximums.append(0)
    minimums.append(100)
for tweet in all_tweets:
    for word in tweet:
        if len(word)>maxlength:
            maxlength=len(word)
            for i in range(0,5,1):
                if maximums[i]<maxlength:
                    maximums.append(maxlength)
                    words1.append(word)
        if len(word)<minlength:
            minlength=len(word)
            for i in range(0,5,1):
                if minimums[i]>minlength:
                    minimums.append(minlength)
                    words2.append(word)
print("Οι5 μεγαλύτερες λέξεις του χρήστη που δώσατε είναι οι :")
for i in range(0,5,1):
    print(words1[i])
print("Οι5 μικρότερες λέξεις του χρήστη που δώσατε είναι οι :")
for i in range(0,5,1):
    print(words2[i])
