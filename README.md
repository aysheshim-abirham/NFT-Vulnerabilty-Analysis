# NFT-Vulnerabilty-Analysis
Created a cutommodule todetect NFT specfic vulnerbailties in Mythril to statically analyze NFT-vulnerabilities. This module checks for nft ownership fraud specifically focused illicit activities during ownership transfer in a transaction.

# Installation

 - [Docker Desktop](https://mythril-classic.readthedocs.io/en/master/installation.html#docker)
 # You can use the following command to install virtualenv:
   $python -m pip install --user virtualenv

##Testing Mythril

#Run first test for before results

$ mkdir <foldername>

$ git clone https://github.com/KrishnaKushal/NFT-Vulnerabilty-Analysis.git

$ cd NFT-Vulnerabilty-Analysis/

$ docker run -v %CD%/data:/data mythril/myth -v4 analyze /data/mythx-tests/05222022-25/SelfDestructMultiTxFeasible.sol

$ docker run -v %CD%/data:/data mythril/myth -v4 analyze /data/mythx-tests/05222022-25/PredictTheFutureChallenge_before.sol

$ docker run -v %CD%/data:/data mythril/myth -v4 analyze /data/mythx-tests/05222022-25/FiftyYearsChallenge_before.sol

$ docker run -v %CD%/data:/data mythril/myth -v4 analyze /data/mythx-tests/05222022-25/PredictTheFutureChallenge_before.sol

##Testing Myhtril for after results pending
 -
