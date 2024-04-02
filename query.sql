-- SELECT DISTINCT(COUNT(MINER)) CNT, MINER
-- FROM `bigquery-public-data.crypto_ethereum.blocks`
-- WHERE TIMESTAMP_TRUNC(timestamp, DAY) BETWEEN TIMESTAMP ("2024-01-01") AND TIMESTAMP ("2024-01-31")
-- GROUP BY MINER
-- ORDER BY CNT DESC LIMIT 1000;
--
-- SELECT COUNT(DISTINCT(MINER)) CNT
-- FROM `bigquery-public-data.crypto_ethereum.blocks`
-- WHERE TIMESTAMP_TRUNC(timestamp, DAY) BETWEEN TIMESTAMP ("2024-01-01") AND TIMESTAMP ("2024-01-31") LIMIT 1000;
--
-- SELECT COUNT(MINER)
-- FROM `bigquery-public-data.crypto_ethereum.blocks`
-- WHERE TIMESTAMP_TRUNC(timestamp, DAY) BETWEEN TIMESTAMP ("2024-01-01") AND TIMESTAMP ("2024-01-31") LIMIT 1000;

SELECT A.*
FROM `bigquery-public-data.crypto_ethereum.transactions` A
JOIN (
 SELECT MAX(T.transaction_index) AS ma, T.block_number
 FROM `bigquery-public-data.crypto_ethereum.transactions` T
 WHERE DATE(T.block_timestamp) between '2024-01-01' and '2024-01-31'
 GROUP BY T.block_number
) AS I ON A.block_number = I.block_number AND A.transaction_index = I.ma;
