from enum import IntEnum

import brownie
import pytest
from brownie import web3

from utils.config import contracts
from utils.evm_script import encode_error
from utils.import_current_votes import is_there_any_vote_scripts, start_and_execute_votes
from utils.test.oracle_report_helpers import oracle_report

DEPOSIT_AMOUNT = 100 * 10 ** 18


@pytest.fixture()
def stopped_lido():
    contracts.lido.stop({"from": contracts.voting})


@pytest.fixture(scope="function", autouse=is_there_any_vote_scripts())
def autoexecute_vote(helpers, vote_ids_from_env, accounts):
    if vote_ids_from_env:
        helpers.execute_votes(accounts, vote_ids_from_env, contracts.voting, topup="0.5 ether")
    else:
        start_and_execute_votes(contracts.voting, helpers)


class StakingModuleStatus(IntEnum):
    Active = 0
    DepositsPaused = 1
    Stopped = 2


class TestEventsEmitted:
    def test_stop_resume_lido_emit_events(self, helpers):
        tx = contracts.lido.stop({"from": contracts.voting})
        helpers.assert_single_event_named("Stopped", tx, {})
        helpers.assert_single_event_named("StakingPaused", tx, {})
        assert contracts.lido.isStopped()
        assert contracts.lido.isStakingPaused()

        tx = contracts.lido.resume({"from": contracts.voting})
        helpers.assert_single_event_named("Resumed", tx, {})

        assert not contracts.lido.isStopped()
        assert not contracts.lido.isStakingPaused()

    def test_stop_resume_staking_lido_emit_events(self, helpers):
        tx = contracts.lido.pauseStaking({"from": contracts.voting})
        helpers.assert_single_event_named("StakingPaused", tx, {})
        helpers.assert_event_not_emitted("Stopped", tx)

        assert contracts.lido.isStakingPaused()
        assert not contracts.lido.isStopped()

        tx = contracts.lido.resumeStaking({"from": contracts.voting})
        helpers.assert_single_event_named("StakingResumed", tx, {})
        helpers.assert_event_not_emitted("Resumed", tx)

        assert not contracts.lido.isStakingPaused()
        assert not contracts.lido.isStopped()

    def test_pause_resume_deposits_staking_module(self, helpers, stranger):
        tx = contracts.staking_router.pauseStakingModule(1, {"from": contracts.deposit_security_module})
        helpers.assert_single_event_named("StakingModuleStatusSet", tx,
                                          {'setBy': contracts.deposit_security_module,
                                           'stakingModuleId': 1,
                                           'status': StakingModuleStatus.DepositsPaused})
        assert contracts.staking_router.getStakingModuleIsDepositsPaused(1)

        contracts.staking_router.grantRole(
            web3.keccak(text="STAKING_MODULE_RESUME_ROLE"),
            stranger,
            {"from": contracts.agent},
        )
        tx = contracts.staking_router.resumeStakingModule(1, {"from": stranger})
        helpers.assert_single_event_named("StakingModuleStatusSet", tx,
                                          {'setBy': stranger,
                                           'stakingModuleId': 1,
                                           'status': StakingModuleStatus.Active})
        assert contracts.staking_router.getStakingModuleIsActive(1)

    def test_stop_staking_module(self, helpers, stranger):
        contracts.staking_router.grantRole(
            web3.keccak(text="STAKING_MODULE_MANAGE_ROLE"),
            stranger,
            {"from": contracts.agent},
        )

        tx = contracts.staking_router.setStakingModuleStatus(1,
                                                             StakingModuleStatus.Stopped,
                                                             {"from": stranger})
        helpers.assert_single_event_named("StakingModuleStatusSet", tx,
                                          {'setBy': stranger,
                                           'stakingModuleId': 1,
                                           'status': StakingModuleStatus.Stopped})

        assert contracts.staking_router.getStakingModuleIsStopped(1)


class TestRevertedSecondCalls:
    def test_revert_second_stop_resume(self):
        contracts.lido.stop({"from": contracts.voting})

        with brownie.reverts("CONTRACT_IS_STOPPED"):
            contracts.lido.stop({"from": contracts.voting})

        contracts.lido.resume({"from": contracts.voting})

        with brownie.reverts("CONTRACT_IS_ACTIVE"):
            contracts.lido.resume({"from": contracts.voting})

    @pytest.mark.skip(reason="Second call of pause/resume staking is not reverted right now."
                             "It maybe should be fixed in the future to be consistent, "
                             "there's not a real problem with it.")
    def test_revert_second_pause_resume_staking(self):
        contracts.lido.pauseStaking({"from": contracts.voting})

        with brownie.reverts(""):
            contracts.lido.pauseStaking({"from": contracts.voting})

        contracts.lido.resumeStaking({"from": contracts.voting})

        with brownie.reverts(""):
            contracts.lido.resumeStaking({"from": contracts.voting})

    def test_revert_second_pause_resume_staking_module(self, stranger):
        contracts.staking_router.pauseStakingModule(1, {"from": contracts.deposit_security_module})

        with brownie.reverts(encode_error('StakingModuleNotActive()')):
            contracts.staking_router.pauseStakingModule(1, {"from": contracts.deposit_security_module})

        contracts.staking_router.grantRole(
            web3.keccak(text="STAKING_MODULE_RESUME_ROLE"),
            stranger,
            {"from": contracts.agent},
        )
        contracts.staking_router.resumeStakingModule(1, {"from": stranger})

        with brownie.reverts(encode_error('StakingModuleNotPaused()')):
            contracts.staking_router.resumeStakingModule(1, {"from": stranger})

    def test_revert_second_stop_staking_module(self, helpers, stranger):
        contracts.staking_router.grantRole(
            web3.keccak(text="STAKING_MODULE_MANAGE_ROLE"),
            stranger,
            {"from": contracts.agent},
        )

        contracts.staking_router.setStakingModuleStatus(1,
                                                        StakingModuleStatus.Stopped,
                                                        {"from": stranger})
        with brownie.reverts(encode_error('StakingModuleStatusTheSame()')):
            contracts.staking_router.setStakingModuleStatus(1,
                                                            StakingModuleStatus.Stopped,
                                                            {"from": stranger})

# Lido contract tests

@pytest.mark.usefixtures("stopped_lido")
def test_stopped_lido_cant_stake(stranger):
    with brownie.reverts("STAKING_PAUSED"):
        stranger.transfer(contracts.lido, DEPOSIT_AMOUNT)


@pytest.mark.usefixtures("stopped_lido")
def test_stopped_lido_cant_deposit():
    with brownie.reverts("CAN_NOT_DEPOSIT"):
        contracts.lido.deposit(1, 1, "0x", {"from": contracts.deposit_security_module}),


@pytest.mark.usefixtures("stopped_lido")
def test_resumed_staking_can_stake(stranger):
    contracts.lido.resumeStaking({"from": contracts.voting})
    stranger.transfer(contracts.lido, DEPOSIT_AMOUNT)


@pytest.mark.usefixtures("stopped_lido")
def test_resumed_staking_cant_deposit():
    contracts.lido.resumeStaking({"from": contracts.voting})

    with brownie.reverts("CAN_NOT_DEPOSIT"):
        contracts.lido.deposit(1, 1, "0x", {"from": contracts.deposit_security_module}),


@pytest.mark.usefixtures("stopped_lido")
def test_resumed_lido_can_stake(stranger):
    contracts.lido.resume({"from": contracts.voting})
    stranger.transfer(contracts.lido, DEPOSIT_AMOUNT)


@pytest.mark.usefixtures("stopped_lido")
def test_resumed_lido_can_deposit(stranger):
    contracts.lido.resume({"from": contracts.voting})
    contracts.lido.deposit(1, 1, "0x", {"from": contracts.deposit_security_module}),


# Staking module tests

def test_paused_staking_module_cant_stake(stranger, helpers):
    contracts.staking_router.pauseStakingModule(1, {"from": contracts.deposit_security_module})
    with brownie.reverts(encode_error('StakingModuleNotActive()')):
        contracts.lido.deposit(1, 1, "0x", {"from": contracts.deposit_security_module}),


def test_paused_staking_module_can_reward(stranger, helpers):
    contracts.staking_router.pauseStakingModule(1, {"from": contracts.deposit_security_module})
    oracle_report()
    _, module_address, *_ = contracts.staking_router.getStakingModule(1)
    assert contracts.lido.sharesOf(module_address) > 0


def test_stopped_staking_module_cant_stake(stranger):
    contracts.staking_router.grantRole(
        web3.keccak(text="STAKING_MODULE_MANAGE_ROLE"),
        stranger,
        {"from": contracts.agent},
    )

    contracts.staking_router.setStakingModuleStatus(1, StakingModuleStatus.Stopped,
                                                    {"from": stranger})
    with brownie.reverts(encode_error('StakingModuleNotActive()')):
        contracts.lido.deposit(1, 1, "0x", {"from": contracts.deposit_security_module}),


def test_stopped_staking_module_cant_reward(stranger):
    contracts.staking_router.grantRole(
        web3.keccak(text="STAKING_MODULE_MANAGE_ROLE"),
        stranger,
        {"from": contracts.agent},
    )
    _, module_address, *_ = contracts.staking_router.getStakingModule(1)
    contracts.staking_router.setStakingModuleStatus(1, StakingModuleStatus.Stopped,
                                                    {"from": stranger})
    oracle_report()
    assert contracts.lido.sharesOf(module_address) == 0
