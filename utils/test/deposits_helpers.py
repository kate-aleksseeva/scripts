from utils.test.helpers import ETH
from utils.config import contracts
from brownie import ZERO_ADDRESS, accounts


WEI_TOLERANCE = 5  # wei tolerance to avoid rounding issue


def fill_deposit_buffer(deposits_count):
    staking_router, lido, withdrawal_queue = contracts.staking_router, contracts.lido, contracts.withdrawal_queue

    deposit_size = ETH(32)

    buffered_ether_before_submit = lido.getBufferedEther()
    withdrawal_unfinalized_steth = withdrawal_queue.unfinalizedStETH()

    eth_to_deposit = deposits_count * deposit_size
    eth_debt = max(0, withdrawal_unfinalized_steth - buffered_ether_before_submit)
    eth_to_submit = eth_to_deposit + eth_debt + WEI_TOLERANCE

    eth_whale = accounts.at(staking_router.DEPOSIT_CONTRACT(), force=True)
    lido.submit(ZERO_ADDRESS, {"from": eth_whale, "value": eth_to_submit})

    assert lido.getDepositableEther() >= eth_to_deposit
