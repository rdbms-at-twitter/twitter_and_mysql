[Purpose of this shell]<br>
Gather data from twitter for Analyzing trend.<br>

Pre-Require:<br>
pip install requests requests_oauthlib <br>
pip install requests-oauthlib <br>
pip install mysql-connector-python <br>


<B>1) Create Table</B> <br>
This script generated on the MySQL8.0.11 (With mecab plugin) <br>
This sample use "APP" as target database.

T_Tweets.sql <br>

<B>2) Create Shell and Modify it.</B><br>

  tweet_import.py <br>

<B>3) Run Shell Periodically.</B><br>

crontab -u root -e
*/10 * * * * /home/user/shell/tweet.sh

That's it.