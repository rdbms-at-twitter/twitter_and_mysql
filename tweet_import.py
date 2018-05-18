# coding: utf-8

print ("======================================================")
print ("Import Tweets from Twitter Search API to MySQL")
print ("Created: 2018-05-18")
print ("======================================================")

from requests_oauthlib import OAuth1Session
import datetime
import json
import mysql.connector

##### Batch Start #####
start_time = (datetime.datetime.now())

##############################################################
#    This section is just used for my private account.
##############################################################

api_key      = "Your API Key"
api_secret   = "Your Secret Key"
token        = "Your Token"
token_secret = "Your Secret Token"

##############################################################
#    This section is API and Auth.
##############################################################

url = "https://api.twitter.com/1.1/search/tweets.json?"
params = {
     "q": "ANY-WORD-Y-WANT-TO-CHECK",
     "lang": "ja",
     "result_type": "recent",
     #"result_type": "mixed",
     "count": "100"
      }

auth = OAuth1Session(api_key, api_secret, token, token_secret)
res = auth.get(url, params = params)

##############################################################
#     Connect Session to the MySQL Instance.
##############################################################

if res.status_code == 200: # 成功した場合

### Insert documents ###

   timeline = json.loads(res.text)
   for tweet in timeline["statuses"]:
   #for tweet in timeline:
      tid = tweet['id']
      tuser= tweet['user']['name']
      ttext= tweet['text']

      connect = mysql.connector.connect(host='localhost', port=3306, user='user-name', password='password', db='database-name', charset='utf8mb4')
      cursor = connect.cursor()

      sql_statement = "insert ignore into T_Tweets(tweet_id,user,text) values(%s,%s,%s)"
      cursor.execute(sql_statement,(tid,tuser,ttext))
      #print (sql_statement,(tid,tuser,ttext))
      #JSONがMySQLのJSONにINSERTエラーになるのでまた次回調整してINSERTする。Bug88995
      connect.commit()
      cursor.close()
      connect.close()
 
####################################################
###         Drop the collection(Table)
####################################################
# mySession.dropCollection('NEW57','dbts2016')

else: # 失敗した場合
        print ("Error: %d" % res.status_code)

##### Batch End #####
end_time = (datetime.datetime.now())
print ('DATA LOAD TIME:')
print (end_time - start_time)
print ("======================================================")