import praw
import pandas as pd
import datetime as dt
import sys
from notify_run import Notify

notify = Notify()

#use https://www.reddit.com/prefs/apps/ to get info below if you dont have it already
reddit =praw.Reddit(client_id='id goes here',
                    client_secret='secret goes here',
                    user_agent='user goes here')

search_term='all' #searches all subreddits 
keyword=['moderna']

if (len(sys.argv)>1):
    search_term=(sys.argv[1])
if (len(sys.argv)>2):
    keyword=(sys.argv[2])

print("Subreddit: ",search_term)
print("Keyword: ",keyword)
print

subreddit = reddit.subreddit(search_term)

resp = subreddit.search(keyword, limit=1000)

headlines = []
for submission in resp:
    headlines.append(submission.title)

words = ['Phase 2', 'Approved'] # returns any word that contains our keyword (finds plurals as well) 
words1 = ['phase 2', 'Rejected']

def check(headlines, words):
    res = [all([w in h for w in words]) for h in headlines]
    return [headlines[i] for i in range(0, len(res)) if res[i]] #gathers headlines containing 'Phase 3'

while len(check(headlines, words))>=1:
    print(check(headlines, words))
    print('--Keywords "Phase 3 + Approved" found!')
    notify.send('Approval for MRNA buy needed')
    answer = input("Approve buy, enter yes or no: ")
    if answer == "yes":
        print('Buying...')
        import robin_stocks
        login=robin_stocks.login('robinhood user','robinhood pass') #you will have to 2FA verify when this is first used
        robin_stocks.orders.order_sell_market('MRNA', 2, timeInForce='gtc', extendedHours=False)       
        
    elif answer =="no":
            print('trade aborted')
    else:
            print('yes or no in lowercase pls!')
    break

if len(check(headlines, words))==0:
        print('Not yet, keywords "Phase 3 + Approved" not found')

else:
    def check(headlines, words1):
        res1 = [all([w in h for w in words1]) for h in headlines]
        return [headlines[i] for i in range(0, len(res1)) if res1[i]] #if 'Approved' not found then it searches
                                                                      #for the keyword 'Rejected'
if len(check(headlines, words1))==0:
    print('--Keywords "Phase 3 + Rejected" not found')
    notify.send('Undefined MRNA news found go look')

else:
    while len(check(headlines, words1))>=1:
        print('--Keywords "Phase 3 + Rejected" found')
        print(check(headlines, words2))
        notify.send('Approval for MRNA sell needed')
        answer = input("Approve sell, enter yes or no: ")
        if answer == "yes":
            print('Selling...')
            import robin_stocks
            login=robin_stocks.login('robinhood user','robinhood pass')
            robin_stocks.orders.order_sell_market('MRNA', 2, timeInForce='gtc', extendedHours=False) 
        elif answer =="no":
            print('trade aborted')
        else:
            print('yes or no in lowercase pls!')
        break
    


    
