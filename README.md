# NFT-Vulnerabilty-Analysis
Use Mythril to statically analyze NFT-vulnerabilities
# Installation

 - [Docker Desktop](https://mythril-classic.readthedocs.io/en/master/installation.html#docker)

# Test suite

## Run first test

$ mkdir <foldername>

$ git clone https://github.com/KrishnaKushal/NFT-Vulnerabilty-Analysis.git

$ cd NFT-Vulnerabilty-Analysis/

$ docker run -v %CD%/data:/data mythril/myth -v4 analyze /data/mythx-tests/05222022-25/SelfDestructMultiTxFeasible.sol

$ docker run -v %CD%/data:/data mythril/myth -v4 analyze /data/mythx-tests/05222022-25/PredictTheFutureChallenge_before.sol

$ docker run -v %CD%/data:/data mythril/myth -v4 analyze /data/mythx-tests/05222022-25/FiftyYearsChallenge_before.sol

$ docker run -v %CD%/data:/data mythril/myth -v4 analyze /data/mythx-tests/05222022-25/PredictTheFutureChallenge_before.sol
