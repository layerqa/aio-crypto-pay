from dataclasses import dataclass


@dataclass
class Assets:
    BTC: str = 'BTC'
    TON: str = 'TON'
    ETH: str = 'ETH'
    USDT: str = 'USDT'
    USDC: str = 'USDC'
    BUSD: str = 'BUSD'


@dataclass
class PaidButtonNames:
    VIEW_ITEM: str = 'viewItem',
    OPEN_CHANNEL: str = 'openChannel',
    OPEN_BOT: str = 'openBot',
    CALLBACK: str = 'callback'


@dataclass
class Hostnames:
    MAIN_NET: str = 'https://pay.crypt.bot'
    TEST_NET: str = 'https://testnet-pay.crypt.bot'


@dataclass
class App:
    app_id: int
    name: str
    payment_processing_bot_username: str