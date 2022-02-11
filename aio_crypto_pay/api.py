from typing import List, Optional, Union

from aiohttp.client import ClientSession

from .exceptions import Unauthorized
from .types import Hostnames, App, Balance, Currencies, ExchangeRates, Assets, InvoiceStatus


class CryptoPay:
    def __init__(self, token: str, hostname: str = Hostnames.MAIN_NET) -> None:
        """Init CryptoPay api

        Args:
            token (str): [CryptoPay api token from @CryptoBot]
            hostname (str, optional): [api endpoint hostname]. Defaults to Hostnames.MAIN_NET.
        """
        self._token = token
        self._hostname = hostname
        self._client: ClientSession = ClientSession(
            base_url=self._hostname, headers={'Crypto-Pay-API-Token': self._token}
        )
    
    def _raise_errors(self, response: dict) -> Exception:
        """Raise api errors

        Args:
            response (dict): [response dict data]

        Returns:
            Exception: [Exception models]
        """
        if response['ok'] == False:
            if response['error']['code'] == 401:
                raise Unauthorized(response['error']['code'], response['error']['name'])
    
    async def close_client(self) -> None:
        """Close client session"""
        await self._client.close()
    
    async def get_me(self) -> App:
        """Use this method to test your app's authentication token. Requires no parameters.
           On success, returns basic information about an app.

        Returns:
            App: [App model]
        """
        async with self._client.get(url='/api/getMe') as response:
            response_json = await response.json()
            self._raise_errors(response=response_json)
            return App(**response_json['result'])
    
    async def get_balance(self) -> List[Balance]:
        """Use this method to get a balance of your app. Returns array of assets.

        Returns:
            List[Balance]: [Balance list model]
        """
        async with self._client.get(url='/api/getBalance') as response:
            response_json = await response.json()
            self._raise_errors(response=response_json)
            return [Balance(**balance) for balance in response_json['result']]
    
    async def get_currencies(self) -> List[Currencies]:
        """Use this method to get a list of supported currencies. Returns array of currencies.

        Returns:
            List[Currencies]: [Currencies list model]
        """
        async with self._client.get(url='/api/getCurrencies') as response:
            response_json = await response.json()
            self._raise_errors(response=response_json)
            return [Currencies(**currencies) for currencies in response_json['result']]
    
    async def get_exchange_rates(self) -> List[ExchangeRates]:
        """Use this method to get exchange rates of supported currencies. Returns array of currencies.

        Returns:
            List[ExchangeRates]: [ExchangeRates list model]
        """
        async with self._client.get(url='/api/getExchangeRates') as response:
            response_json = await response.json()
            return [ExchangeRates(**exchange_rates) for exchange_rates in response_json['result']]