[Purpose of this shell]
Gather data from twitter for Analyzing trend.<br>

Pre-Require:<br>
pip install requests requests_oauthlib <br>
pip install requests-oauthlib <br>
pip install mysql-connector-python <br>


1) Create Table
This script generated on the MySQL8.0.11 (With mecab plugin)

CREATE TABLE `T_Tweets` (
  `tweet_id` bigint(20) NOT NULL,
  `user` varchar(512) DEFAULT NULL,
  `text` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`tweet_id`),
  FULLTEXT KEY `idx_mecab_text` (`text`) /*!50100 WITH PARSER `mecab` */ 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


2) Create Shell and Modify it.


3) Run Shell Periodically.

crontab -u root -e
*/10 * * * * /home/user/shell/tweet.sh

That's it.