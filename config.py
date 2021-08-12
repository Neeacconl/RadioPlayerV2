"""
RadioPlayerV2, Telegram Voice Chat Bot
Copyright (C) 2021  Asm Safone <https://t.me/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", "1573980407")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 7022149))
    CHAT = int(os.environ.get("CHAT", ""))
    LOG_GROUP = os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "https://radioindia.net/radio/hungamanow/icecast.audio")
    API_HASH = os.environ.get("32345d9f632af9ffba9cbb9767030b6a", "")
    BOT_TOKEN = os.environ.get("1912545340:AAH3MEmKb0sM2iVsBcdxrmwUD5Jh-J9wJ9E", "") 
    SESSION = os.environ.get("BQCWGgACn5PhENiGbaQg8HksynkGz0OUvDvBKA6aB7bpQ4Dz08EFTPlMt6Cw3emigkTePBQjPdnrLGbHeZnM4YsEzBHPQt5X4vo38opbyWSPeZ9dwtSrotQZ78M_HoRhd499MW22H27OTB2SwnJBbDksCvhBUDBFMFEo9wCVTPPRdb7x0B8egViub5a90HMTycRM0xghJzYVlV3Dzps3ltkaxW-d3AREBSYzTJZol3SRxIILpa4q8yz-lZmJnX-mpXqGGoeSiOBAmt1ISQ22HiWDDcqdx-3459xcUMWbx8ceM_sUWxQOpCG-B7MGo4oBbXJ8PNS_fIg5x1zzdZb8Lm7tXdEI9wA", "")

