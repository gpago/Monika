import asyncio
import json
import aiohttp
import rule34
from pybooru import Danbooru


class Gelbooru:

    def accessAPI(self):

        print("meow")

class Realbooru:

    def accessAPI(self):

        print("nya")

class Danbooru:

    def accessAPI(self):

        print("mew")

class Rule34:

    def __init__(self):
        self.api = rule34.Rule34(asyncio.get_event_loop())

    async def randomImage(self):
        url = await self.api.getImageURLS(tags='*', randomPID=1)[0]


class Boorus:

    def __init__(self):
        self.Gelbooru = Gelbooru
        self.Realbooru = Realbooru
        self.Rule34 = Rule34
