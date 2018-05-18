CREATE TABLE `T_Tweets` (
  `tweet_id` bigint(20) NOT NULL,
  `user` varchar(512) DEFAULT NULL,
  `text` varchar(4096) DEFAULT NULL,
  `tweet_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`tweet_id`),
  FULLTEXT KEY `idx_mecab_text` (`text`) /*!50100 WITH PARSER `mecab` */ 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci