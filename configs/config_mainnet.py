# Ethereum Chain parameters
CHAIN_NETWORK_NAME = "mainnet"
CHAIN_SLOTS_PER_EPOCH = 32
CHAIN_SECONDS_PER_SLOT = 12
CHAIN_GENESIS_TIME = 1606824023
CHAIN_DEPOSIT_CONTRACT = "0x00000000219ab540356cBB839Cbe05303d7705Fa"

# DAO
ARAGON_KERNEL = "0xb8FFC3Cd6e7Cf5a098A1c92F48009765B24088Dc"
LDO_TOKEN = "0x5A98FcBEA516Cf06857215779Fd812CA3beF1B32"
ARAGON_KERNEL_IMPL = "0x2b33CF282f867A7FF693A66e11B0FcC5552e4425"

# Standard (or forked) Aragon apps
ACL = "0x9895F0F17cc1d1891b6f18ee0b483B6f221b37Bb"
AGENT = "0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c"
FINANCE = "0xB9E5CBB9CA5b0d659238807E84D0176930753d86"
VOTING = "0x2e59A20f205bB85a89C53f1936454680651E618e"
TOKEN_MANAGER = "0xf73a1260d222f447210581DDf212D915c09a3249"
ACL_IMPL = "0x9f3b9198911054B122fDb865f8A5Ac516201c339"
VOTING_IMPL = "0x72fb5253AD16307B9E773d2A78CaC58E309d5Ba4"

# Our custom Aragon apps
LIDO = "0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84"
LEGACY_ORACLE = "0x442af784A788A5bd6F42A01Ebe9F287a871243fb"
NODE_OPERATORS_REGISTRY = "0x55032650b14df07b85bF18A3a3eC8E0Af2e028d5"
SIMPLE_DVT = "0xaE7B191A31f627b4eB1d4DaC64eaB9976995b433"

LIDO_IMPL_V1 = "0x47EbaB13B806773ec2A2d16873e2dF770D130b50"
LEGACY_ORACLE_IMPL_V1 = "0x1430194905301504e8830ce4B0b0df7187E84AbD"
NODE_OPERATORS_REGISTRY_IMPL_V1 = "0x5d39ABaa161e622B99D45616afC8B837E9F19a25"

# Aragon APM Repos
REPO_APP_ID = "0xbe49cbb8894efb45c933fd09dc87bdd94909553a9e1f511d7fc10f3dad1564f2"
APM_REGISTRY = "0x0cb113890b04B49455DfE06554e2D784598A29C9"
VOTING_REPO = "0x4Ee3118E3858E8D7164A634825BfE0F73d99C792"
LIDO_REPO = "0xF5Dc67E54FC96F993CD06073f71ca732C1E654B1"
NODE_OPERATORS_REGISTRY_REPO = "0x0D97E876ad14DB2b183CFeEB8aa1A5C788eB1831"
LEGACY_ORACLE_REPO = "0xF9339DE629973c60c4d2b76749c81E6F40960E3A"

## LIDO_ARAGON_REPO_IMPL is common for Lido, NodeOperatorsRegistry, Oracle aragon apps
ARAGON_COMMON_REPO_IMPL = "0xa8A358E9bbB9fF60D4B89CBE5b2FE88f98b51B9D"

# Other Aragon contracts
## For LIDO_EVM_SCRIPT_REGISTRY see Aragon Agent 0x853cc0D5917f49B57B8e9F89e491F5E18919093A
ARAGON_EVMSCRIPT_REGISTRY = "0x853cc0D5917f49B57B8e9F89e491F5E18919093A"
## See getEVMScriptExecutor(0x00000001) of any Aragon App or callsScript of LIDO_EASYTRACK_EVMSCRIPTEXECUTOR
ARAGON_CALLS_SCRIPT = "0x5cEb19e1890f677c3676d5ecDF7c501eBA01A054"

# Other (non-aragon) protocol contracts
WSTETH_TOKEN = "0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0"

EXECUTION_LAYER_REWARDS_VAULT = "0x388C818CA8B9251b393131C08a736A67ccB19297"

DEPOSIT_SECURITY_MODULE_V1 = "0x710B3303fB508a84F10793c1106e32bE873C24cd"
WITHDRAWAL_VAULT = "0xB9D7934878B5FB9610B3fE8A5e441e8fad7E293f"

# EasyTracks
EASYTRACK = "0xF0211b7660680B49De1A7E9f25C65660F0a13Fea"

EASYTRACK_EVMSCRIPT_EXECUTOR = "0xFE5986E06210aC1eCC1aDCafc0cc7f8D63B3F977"
EASYTRACK_INCREASE_NOP_STAKING_LIMIT_FACTORY = "0xFeBd8FAC16De88206d4b18764e826AF38546AfE0"
EASYTRACK_SIMPLE_DVT_TRUSTED_CALLER = "0x08637515E85A4633E23dfc7861e2A9f53af640f7"
EASYTRACK_SIMPLE_DVT_ADD_NODE_OPERATORS_FACTORY = "0xcAa3AF7460E83E665EEFeC73a7a542E5005C9639"
EASYTRACK_SIMPLE_DVT_ACTIVATE_NODE_OPERATORS_FACTORY = "0xCBb418F6f9BFd3525CE6aADe8F74ECFEfe2DB5C8"
EASYTRACK_SIMPLE_DVT_DEACTIVATE_NODE_OPERATORS_FACTORY = "0x8B82C1546D47330335a48406cc3a50Da732672E7"
EASYTRACK_SIMPLE_DVT_SET_VETTED_VALIDATORS_LIMITS_FACTORY = "0xD75778b855886Fc5e1eA7D6bFADA9EB68b35C19D"
EASYTRACK_SIMPLE_DVT_SET_NODE_OPERATOR_NAMES_FACTORY = "0x7d509BFF310d9460b1F613e4e40d342201a83Ae4"
EASYTRACK_SIMPLE_DVT_SET_NODE_OPERATOR_REWARD_ADDRESSES_FACTORY = "0x589e298964b9181D9938B84bB034C3BB9024E2C0"
EASYTRACK_SIMPLE_DVT_UPDATE_TARGET_VALIDATOR_LIMITS_FACTORY = "0x41CF3DbDc939c5115823Fba1432c4EC5E7bD226C"
EASYTRACK_SIMPLE_DVT_CHANGE_NODE_OPERATOR_MANAGERS_FACTORY = "0xE31A0599A6772BCf9b2bFc9e25cf941e793c9a7D"

# Multisigs
FINANCE_MULTISIG = "0x48F300bD3C52c7dA6aAbDE4B683dEB27d38B9ABb"
L1_EMERGENCY_BRAKES_MULTISIG = "0x73b047fe6337183A454c5217241D780a932777bD"

# Other
INSURANCE_FUND = "0x8B3f33234ABD88493c0Cd28De33D583B70beDe35"
RELAY_ALLOWED_LIST = "0xF95f069F9AD107938F6ba802a3da87892298610E"
CURVE_REWARDS_MANAGER = "0x753D5167C31fBEB5b49624314d74A957Eb271709"
BALANCER_REWARDS_MANAGER = "0x1dD909cDdF3dbe61aC08112dC0Fdf2Ab949f79D8"

# Auxiliary addresses
LDO_HOLDER_ADDRESS_FOR_TESTS = "0x820fb25352bb0c5e03e07afc1d86252ffd2f0a18"
LDO_VOTE_EXECUTORS_FOR_TESTS = [
    "0x3e40d73eb977dc6a537af587d48316fee66e9c8c",
    "0xb8d83908aab38a159f3da47a59d84db8e1838712",
    "0xa2dfc431297aee387c05beef507e5335e684fbcd",
]
# General network addresses
DAI_TOKEN = "0x6b175474e89094c44da98b954eedeac495271d0f"
USDT_TOKEN = "0xdac17f958d2ee523a2206206994597c13d831ec7"
USDC_TOKEN = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
WETH_TOKEN = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

#
# Lido V2 upgrade entries
# Grouped the same as in docs
#

# LidoLocator
LIDO_LOCATOR = "0xC1d0b3DE6792Bf6b4b37EccdcC24e45978Cfd2Eb"
LIDO_LOCATOR_IMPL = "0x1D920cc5bACf7eE506a271a5259f2417CaDeCE1d"

# Other upgrade addresses
LIDO_V2_UPGRADE_TEMPLATE = "0xa818fF9EC93122Bf9401ab4340C42De638CD600a"
DUMMY_IMPL = "0x6F6541C2203196fEeDd14CD2C09550dA1CbEDa31"
INITIAL_DEAD_TOKEN_HOLDER = "0x000000000000000000000000000000000000dead"
DEPLOYER_EOA_LOCATOR = "0x2A78076BF797dAC2D25c9568F79b61aFE565B88C"
DEPLOYER_EOA = "0x8Ea83AD72396f1E0cD2f8E72b1461db8Eb6aF7B5"

# 0x01...withdrawal_vault or Lido.getWithdrawalCredentials()
WITHDRAWAL_CREDENTIALS = "0x010000000000000000000000b9d7934878b5fb9610b3fe8a5e441e8fad7e293f"

# Lido
LIDO_IMPL = "0x17144556fd3424EDC8Fc8A4C940B2D04936d17eb"
# see Lido's proxy appId()
LIDO_ARAGON_APP_ID = "0x3ca7c3e38968823ccb4c78ea688df41356f182ae1d159e4ee608d30d68cef320"
LIDO_MAX_STAKE_LIMIT_ETH = 150_000

# LegacyOracle (former LidoOracle)
## address is LIDO_LEGACY_ORACLE
LEGACY_ORACLE_IMPL = "0xa29b819654cE6224A222bb5f586920105E2D7E0E"
## see LidoOracle's proxy appId()
ORACLE_ARAGON_APP_ID = "0x8b47ba2a8454ec799cd91646e7ec47168e91fd139b23f017455f3e5898aaba93"

# NodeOperatorsRegistry aka Curated Staking Module
NODE_OPERATORS_REGISTRY_IMPL = "0x8538930c385C0438A357d2c25CB3eAD95Ab6D8ed"
## see NodeOperatorsRegistry's proxy appId()
NODE_OPERATORS_REGISTRY_ARAGON_APP_ID = "0x7071f283424072341f856ac9e947e7ec0eb68719f757a7e785979b6b8717579d"
CURATED_STAKING_MODULE_STUCK_PENALTY_DELAY = 432000
CURATED_STAKING_MODULE_TARGET_SHARE_BP = 10000
CURATED_STAKING_MODULE_MODULE_FEE_BP = 500
CURATED_STAKING_MODULE_TREASURY_FEE_BP = 500
CURATED_STAKING_MODULE_ID = 1
CURATED_STAKING_MODULE_NAME = "curated-onchain-v1"
CURATED_STAKING_MODULE_TYPE = (
    # bytes32("curated-onchain-v1")
    "0x637572617465642d6f6e636861696e2d76310000000000000000000000000000"
)
CURATED_STAKING_MODULE_OPERATORS_COUNT = 39
CURATED_STAKING_MODULE_OPERATORS_ACTIVE_COUNT = 37

# NodeOperatorsRegistry clone aka SimpleDVT
SIMPLE_DVT_IMPL = "0x8538930c385C0438A357d2c25CB3eAD95Ab6D8ed"
## see SimpleDVT's proxy appId()
SIMPLE_DVT_ARAGON_APP_NAME = "simple-dvt"
SIMPLE_DVT_ARAGON_APP_ID = "0xe1635b63b5f7b5e545f2a637558a4029dea7905361a2f0fc28c66e9136cf86a4"
SIMPLE_DVT_MODULE_STUCK_PENALTY_DELAY = 432000
SIMPLE_DVT_MODULE_TARGET_SHARE_BP = 400
SIMPLE_DVT_MODULE_MODULE_FEE_BP = 800
SIMPLE_DVT_MODULE_TREASURY_FEE_BP = 200
SIMPLE_DVT_MODULE_ID = 2
SIMPLE_DVT_MODULE_NAME = "SimpleDVT"
SIMPLE_DVT_MODULE_TYPE = (
    # bytes32("curated-onchain-v1")
    "0x637572617465642d6f6e636861696e2d76310000000000000000000000000000"
)

# OracleDaemonConfig
ORACLE_DAEMON_CONFIG = "0xbf05A929c3D7885a6aeAd833a992dA6E5ac23b09"
NORMALIZED_CL_REWARD_PER_EPOCH = 64
NORMALIZED_CL_REWARD_MISTAKE_RATE_BP = 1000  # 10%
REBASE_CHECK_NEAREST_EPOCH_DISTANCE = 1
REBASE_CHECK_DISTANT_EPOCH_DISTANCE = 23  # 10% of AO 225 epochs frame
VALIDATOR_DELAYED_TIMEOUT_IN_SLOTS = 7200  # 1 day
VALIDATOR_DELINQUENT_TIMEOUT_IN_SLOTS = 28800  # 4 days
NODE_OPERATOR_NETWORK_PENETRATION_THRESHOLD_BP = 100  # 1%
PREDICTION_DURATION_IN_SLOTS = 50400
FINALIZATION_MAX_NEGATIVE_REBASE_EPOCH_SHIFT = 1350  # 6 days

# OracleReportSanityChecker
ORACLE_REPORT_SANITY_CHECKER = "0x9305c1Dbfe22c12c66339184C0025d7006f0f1cC"
CHURN_VALIDATORS_PER_DAY_LIMIT = 20000
ONE_OFF_CL_BALANCE_DECREASE_BP_LIMIT = 500  # 5%
ANNUAL_BALANCE_INCREASE_BP_LIMIT = 1000  # 10%
SIMULATED_SHARE_RATE_DEVIATION_BP_LIMIT = 50  # 0.5%
MAX_VALIDATOR_EXIT_REQUESTS_PER_REPORT = 600
MAX_ACCOUNTING_EXTRA_DATA_LIST_ITEMS_COUNT = 4
MAX_NODE_OPERATORS_PER_EXTRA_DATA_ITEM_COUNT = 50
REQUEST_TIMESTAMP_MARGIN = 7680  # 2 hours rounded to epoch length
MAX_POSITIVE_TOKEN_REBASE = 750000

# Burner
BURNER = "0xD15a672319Cf0352560eE76d9e89eAB0889046D3"
TOTAL_NON_COVER_SHARES_BURNT = 32145684728326685744
TOTAL_COVER_SHARES_BURNT = 0

# DepositSecurityModule
DEPOSIT_SECURITY_MODULE = "0xC77F8768774E1c9244BEed705C4354f2113CFc09"
DSM_MAX_DEPOSITS_PER_BLOCK = 150
DSM_MIN_DEPOSIT_BLOCK_DISTANCE = 25
DSM_PAUSE_INTENT_VALIDITY_PERIOD_BLOCKS = 6646
## Migrated from LIDO_DEPOSIT_SECURITY_MODULE_V1
DSM_GUARDIANS = [
    "0x5fd0dDbC3351d009eb3f88DE7Cd081a614C519F1",
    "0x7912Fa976BcDe9c2cf728e213e892AD7588E6AaF",
    "0x14D5d5B71E048d2D75a39FfC5B407e3a3AB6F314",
    "0xf82D88217C249297C6037BA77CE34b3d8a90ab43",
    "0xa56b128Ea2Ea237052b0fA2a96a387C0E43157d8",
    "0xd4EF84b638B334699bcf5AF4B0410B8CCD71943f",
]
DSM_GUARDIAN_QUORUM = 4

# AccountingOracle
# and its corresponding HashConsensus
ACCOUNTING_ORACLE = "0x852deD011285fe67063a08005c71a85690503Cee"
ACCOUNTING_ORACLE_IMPL = "0xF3c5E0A67f32CF1dc07a8817590efa102079a1aF"
HASH_CONSENSUS_FOR_AO = "0xD624B08C83bAECF0807Dd2c6880C3154a5F0B288"
AO_EPOCHS_PER_FRAME = 225
AO_FAST_LANE_LENGTH_SLOTS = 100
AO_CONSENSUS_VERSION = 1

# ValidatorsExitBusOracle
VALIDATORS_EXIT_BUS_ORACLE = "0x0De4Ea0184c2ad0BacA7183356Aea5B8d5Bf5c6e"
VALIDATORS_EXIT_BUS_ORACLE_IMPL = "0xA89Ea51FddE660f67d1850e03C9c9862d33Bc42c"
HASH_CONSENSUS_FOR_VEBO = "0x7FaDB6358950c5fAA66Cb5EB8eE5147De3df355a"
VEBO_EPOCHS_PER_FRAME = 75
VEBO_FAST_LANE_LENGTH_SLOTS = 100
VEBO_CONSENSUS_VERSION = 1


# AccountingOracle and ValidatorsExitBusOracle
## Migrated from LidoOracle (LegacyOracle)
ORACLE_QUORUM = 5
ORACLE_COMMITTEE = (
    "0x140Bd8FbDc884f48dA7cb1c09bE8A2fAdfea776E",
    # "0x1d0813bf088BE3047d827D98524fBf779Bc25F00", Excluded from members in vote 2024/01/16
    "0xA7410857ABbf75043d61ea54e07D57A6EB6EF186",
    "0x404335BcE530400a5814375E7Ec1FB55fAff3eA2",
    "0x946D3b081ed19173dC83Cd974fC69e1e760B7d78",
    "0x007DE4a5F7bc37E2F26c0cb2E8A95006EE9B89b5",
    "0xc79F702202E3A6B0B6310B537E786B9ACAA19BAf",  # Added into members in vote 2024/01/16
    # "0xEC4BfbAF681eb505B94E4a7849877DC6c600Ca3A", Excluded from members in vote 2024/08/06
    "0x61c91ECd902EB56e314bB2D5c5C07785444Ea1c8",
    "0x1Ca0fEC59b86F549e1F1184d97cb47794C8Af58d",
    "0xe57B3792aDCc5da47EF4fF588883F0ee0c9835C9"   # Added into members in vote 2024/08/06
)

# WithdrawalQueueERC721
WITHDRAWAL_QUEUE = "0x889edC2eDab5f40e902b864aD4d7AdE8E412F9B1"
WITHDRAWAL_QUEUE_IMPL = "0xE42C659Dc09109566720EA8b2De186c2Be7D94D9"
WQ_ERC721_TOKEN_NAME = "Lido: stETH Withdrawal NFT"
WQ_ERC721_TOKEN_SYMBOL = "unstETH"
WQ_ERC721_TOKEN_BASE_URI = "https://wq-api.lido.fi/v1/nft"

# WithdrawalsVault
WITHDRAWAL_VAULT_IMPL_V1 = "0xe681faB8851484B57F32143FD78548f25fD59980"
WITHDRAWAL_VAULT_IMPL = "0xCC52f17756C04bBa7E377716d7062fC36D7f69Fd"

# EIP712StETH
EIP712_STETH = "0x8F73e4C2A6D852bb4ab2A45E6a9CF5715b3228B7"

# StakingRouter
STAKING_ROUTER = "0xFdDf38947aFB03C621C71b06C9C70bce73f12999"
STAKING_ROUTER_IMPL = "0xD8784e748f59Ba711fB5643191Ec3fAdD50Fb6df"

# Not a precise but still some estimation of the fees. Assume here that both modules are filled
# SR_MODULES_FEE = curated_module_fee * (100% - sdvt_module_share) + sdvt_module_fee * sdvt_module_share

SR_MODULES_FEE_BP = (
    CURATED_STAKING_MODULE_MODULE_FEE_BP * (100_00 - SIMPLE_DVT_MODULE_TARGET_SHARE_BP)
    + SIMPLE_DVT_MODULE_MODULE_FEE_BP * SIMPLE_DVT_MODULE_TARGET_SHARE_BP
) // 100_00

SR_TREASURY_FEE_BP = (
    CURATED_STAKING_MODULE_TREASURY_FEE_BP * (100_00 - SIMPLE_DVT_MODULE_TARGET_SHARE_BP)
    + SIMPLE_DVT_MODULE_TREASURY_FEE_BP * SIMPLE_DVT_MODULE_TARGET_SHARE_BP
) // 100_00

SR_MODULES_FEE_E20 = (
    CURATED_STAKING_MODULE_MODULE_FEE_BP * (100_00 - SIMPLE_DVT_MODULE_TARGET_SHARE_BP)
    + SIMPLE_DVT_MODULE_MODULE_FEE_BP * SIMPLE_DVT_MODULE_TARGET_SHARE_BP
) * 10**12

# same as for SR_MODULES_FEE_E20
SR_TREASURY_FEE_E20 = (
    CURATED_STAKING_MODULE_TREASURY_FEE_BP * (100_00 - SIMPLE_DVT_MODULE_TARGET_SHARE_BP)
    + SIMPLE_DVT_MODULE_TREASURY_FEE_BP * SIMPLE_DVT_MODULE_TARGET_SHARE_BP
) * 10**12

SR_BASE_PRECISION_E20 = 100 * 10**18

# GateSeal
GATE_SEAL_FACTORY = "0x6C82877cAC5a7A739f16Ca0A89c0A328B8764A24"
GATE_SEAL = "0x79243345eDbe01A7E42EDfF5900156700d22611c"
GATE_SEAL_PAUSE_DURATION = 518400  # 6 days
GATE_SEAL_EXPIRY_TIMESTAMP = 1743465600  # 2025-05-01 00:00GMT
GATE_SEAL_COMMITTEE = "0x8772E3a2D86B9347A2688f9bc1808A6d8917760C"

# Aragon Permissions test
ACL_DEPLOY_BLOCK_NUMBER = 11473216

# Obsolete (can be removed after V2 upgrade)
SELF_OWNED_STETH_BURNER = "0xB280E33812c0B09353180e92e27b8AD399B07f26"

# Anchor
ANCHOR_VAULT_PROXY = "0xA2F987A546D4CD1c607Ee8141276876C26b72Bdf"

# 0xSplits
SPLIT_MAIN = "0x2ed6c4B5dA6378c7897AC67Ba9e43102Feb694EE"

# Rewards Wrapper (aka ObolLidoSplit)
OBOL_LIDO_SPLIT_FACTORY = "0xA9d94139A310150Ca1163b5E23f3E1dbb7D9E2A6"
OBOL_LIDO_SPLIT_IMPL = "0x2fB59065F049e0D0E3180C6312FA0FeB5Bbf0FE3"

# L2 common L1 parts
L1_TOKEN_RATE_NOTIFIER = "0xe6793B9e4FbA7DE0ee833F9D02bba7DB5EB27823"

# Optimism L2
L1_OPTIMISM_TOKENS_BRIDGE = "0x76943C0D61395d8F2edF9060e1533529cAe05dE6"
L1_OPTIMISM_CROSS_DOMAIN_MESSENGER = "0x25ace71c97B33Cc4729CF772ae268934F7ab5fA1"
L1_OPTIMISM_TOKEN_RATE_PUSHER = "0xd54c1c6413caac3477AC14b2a80D5398E3c32FfE"
## L2
L2_OPTIMISM_TOKENS_BRIDGE = "0x8E01013243a96601a86eb3153F0d9Fa4fbFb6957"
L2_OPTIMISM_GOVERNANCE_EXECUTOR = "0xefa0db536d2c8089685630fafe88cf7805966fc3"
L2_OPTIMISM_STETH_TOKEN = "0x76A50b8c7349cCDDb7578c6627e79b5d99D24138"
L2_OPTIMISM_TOKEN_RATE_ORACLE = "0x294ED1f214F4e0ecAE31C3Eae4F04EBB3b36C9d0"
L2_OPTIMISM_WSTETH_TOKEN = "0x1F32b1c2345538c0c6f582fCB022739c4A194Ebb"
L2_OPTIMISM_WSTETH_TOKEN_IMPL = "0x92834c37dF982A13bb0f8C3F6608E26F0546538e"


# FOR UPGRADE ONLY: stETH on Optimism
## L1
LIDO_LOCATOR_IMPL_NEW = "0x39aFE23cE59e8Ef196b81F0DCb165E9aD38b9463"
L1_TOKEN_RATE_NOTIFIER_IMPL = "0x2EC2a213cc8086c42856630841CcACb7Bdd29ADf"
L1_OPTIMISM_TOKENS_BRIDGE_IMPL_NEW = "0x168Cfea1Ad879d7032B3936eF3b0E90790b6B6D4"
## L2 Optimism
L2_OPTIMISM_TOKENS_BRIDGE_IMPL_NEW = "0x2734602C0CEbbA68662552CacD5553370B283E2E"
L2_OPTIMISM_WSTETH_IMPL_NEW = "0xFe57042De76c8D6B1DF0E9E2047329fd3e2B7334"
L2_STETH_TOKEN_IMPL = "0xe9b65dA5DcBe92f1b397991C464FF568Dc98D761"
L2_TOKEN_RATE_ORACLE_IMPL = "0x4EB53FaF5B1cf1fCa0339D5E54Cba1C0Af49B97B"

# TRP
TRP_VESTING_ESCROW_FACTORY = "0xDA1DF6442aFD2EC36aBEa91029794B9b2156ADD0"
TRP_FACTORY_DEPLOY_BLOCK_NUMBER = 16540381
