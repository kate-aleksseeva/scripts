<div style="display: flex;" align="center">
  <h1 align="center">Voting scripts</h1>
  <img src="assets/voting.png" width="60" height="60" align="left" style="padding: 20px"/>
</div>

![python ~3.10](https://img.shields.io/badge/python->=3.10,<3.11-blue)
![poetry 1.8.2](https://img.shields.io/badge/poetry-1.8.2-blue)
![eth_brownie 1.20.2](https://img.shields.io/badge/eth__brownie-1.20.2-brown)
![AVotesParser 0.5.6](https://img.shields.io/badge/AVotesParser-0.5.6-brown)
![Ganache ~7.9.2-lido](https://img.shields.io/badge/ganache-7.9.2--lido-orange)
![license MIT](https://img.shields.io/badge/license-MIT-brightgreen)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Lido DAO Support Scripts.

There is a script that collects a list of transactions for gas compensation to Oracle members and saves it to a file for upload to the on-chain den.

Instructions for running the script:

1. Navigate to your project directory, clone the repository, switch to the feature branch
```shell
cd <YOUR_PROJECT_REPO>
git clone git@github.com:lidofinance/scripts.git
cd scripts
git checkout feat/oracle-comp
```

2. Install Poetry, install the dependencies, import the network configuration, activate the Poetry shell

```shell
pip install --user poetry==1.8.2
pipx install poetry==1.8.2
poetry install
yarn
poetry run brownie networks import network-config.yaml True
poetry shell
```

3. Set your environment variables

```shell
export WEB3_INFURA_PROJECT_ID=<your_infura_api_key>
export ETHERSCAN_TOKEN=<your_etherscan_api_key>
```

4. Run and follow the script

```shell
brownie run comp_file --network mainnet-fork
```

5. Review the preview of the recipient list. Enter yes to proceed (if you make a mistake, you’ll need to rerun the script).

6. Find the file at the provided link.
7. Upload the file to onchainden.

**Done!**

The script has two modes:
- Accrual to a specific amount
- Accrual until a specific balance is reached

In Block I, set the following variables
- threshold_balance = "1 ether"  # the Ether threshold value that triggers a decision to charge the user
- target_balance = "1 ether"  # the Ether amount up to which the accrual will be made
- target_accrual = "1 ether"  # the Ether amount for which the accrual will be made

In Block II, set the mode of operation.
1. To add a specific amount to the balance:
- members_info = get_oracle_members_info(members_list, threshold_balance=threshold_balance, target_accrual=target_accrual)
2. To fill the balance until a specific amount:
- members_info = get_oracle_members_info(members_list, threshold_balance=threshold_balance, target_balance=target_balance)
