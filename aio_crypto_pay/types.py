from typing import Optional
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
class InvoiceStatus:
    active: str = 'active'
    paid: str = 'paid'


@dataclass
class App:
    app_id: int
    name: str
    payment_processing_bot_username: str


@dataclass
class Balance:
    currency_code: str
    available: float

    def __post_init__(self) -> None:
        self.available = float(self.available)


@dataclass
class Currencies:
    is_blockchain: bool
    is_stablecoin: bool
    is_fiat: bool
    name: str
    code: str
    decimals: int
    url: Optional[str] = None


@dataclass
class ExchangeRates:
    is_valid: bool
    source: str
    target: str
    rate: float

    def __post_init__(self) -> None:
        self.rate = float(self.rate)