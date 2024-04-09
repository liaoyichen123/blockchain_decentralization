# blockchain_decentralization
blockchain decentralization measurement tools

## Context
Proposer-Builder-Separation Model (PBS) in Ethereum Network

**Searchers:** Ethereum users who prioritize privacy and prefer to use a private transaction pool instead of the public mempool. 
Eg. MEV bots, liquidation bots, Ethereum users seeking front-running protection, such as DEX traders. 
Searchers send bundles containing their own transactions and possibly other  transactions from the Ethereum mempool to one or multiple block builders. Searchers bid for block inclusion using either the gas price or direct ETH transfers to the address of the builder.

**Builders:** Users who receive bundles from searchers in the PBS model. Using these bundles along with their private transactions and transactions from the public mempool, builders attempt to create the most profitable block possible. Once a block is constructed, it is sent to one or more relays.

**Relays:** Users responsible for holding blocks from builders for validators. Their role includes accepting blocks from builders, sending the header of the most profitable block to validators and then sending the full block to validators only after receiving a signed header. Importantly, relays keep the contents of the block private until the validator commits to proposing it for inclusion by signing the block’s header

**Validators (Proposer):** Users responsible for proposing blocks to the Ethereum network. They have the option to connect to several relays and then select the most profitable block for themselves to include in the blockchain, by means of receiving bids from relays or subscribe to relays.

The builder’s address is listed in the block’s transaction fee recipient field. Additionally, any direct payments from searchers are sent to the address listed as the block fee recipient, i.e., the builder’s address. 
In the block’s last transaction, the builder address transfers ETH to the proposer’s fee recipient address. 


3. Problem Statement
4. Solution
    1. Key features
    2. How to use it? You can link the demo video here.
    3. For Apps: Identify different types of users and what they can do. Example: someone who sets up the election versus someone who votes. Maybe an admin, depends on your application. 
    4. Provide a link to analytics. Ideally, deploy the dashboard.
    5. Include graphs from benchmarking.
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
