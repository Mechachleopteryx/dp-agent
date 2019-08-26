import asyncio
from typing import Awaitable

from core.transport.base import ChannelConnectorBase


class CmdConnector(ChannelConnectorBase):
    _loop: asyncio.AbstractEventLoop
    _user_id: str

    def __init__(self, config: dict, on_channel_callback: Awaitable) -> None:
        super(CmdConnector, self).__init__(config=config, on_channel_callback=on_channel_callback)
        self._loop = asyncio.get_event_loop()
        self._user_id = self._config['channel']['instance_id'] or 'cmd_client'

        utterance = input('>> ')
        self._loop.create_task(self._on_channel_callback(utterance=utterance,
                                                         channel_id=self._channel_id,
                                                         user_id=self._user_id,
                                                         reset_dialog=True))

    async def send_to_channel(self, user_id: str, response: str) -> None:
        print(f'<< {response}')
        utterance = input('>> ')
        self._loop.create_task(self._on_channel_callback(utterance=utterance,
                                                         channel_id=self._channel_id,
                                                         user_id=self._user_id,
                                                         reset_dialog=False))