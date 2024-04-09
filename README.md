# Blockchain Decentralization

blockchain decentralization measurement tools

1. Title of project
2. Context
3. Problem Statement
4. Solution
   1. The source data are pulled from Google Cloud Platform BigQuery (bigquery-public-data.crypto_ethereum.transactions table)
   2. The source data is then processed using pandas
   3. The block number and builder public key are fetched from database and validator address is parsed by parsing the last transaction of the block.
5. How to use?
    1. Instructions for a local setup to host the application
    2. Required libraries for running it - provide installation instructions, links are acceptable. Scripts are preferred wherever possible.
    3. How to run it? - walk through the different features users can use.
    4. If there are different types of users, specify what each can do.
    5. If Metamask is used, indicate which testnet to link to.
6. How to contribute?
    1. Architecture
    2. Local setup instructions
        1. Include required dependencies installation instructions, if any.
        2. Setup for testing, how to run tests.
        3. If a smart contract, how to deploy a new contract?
7. Include an appropriate license for the project.
8. If this repository used components from other projects or is a fork:
    1. Give credits to upstream repositories
    2. Clearly specify what is built on top of them.
