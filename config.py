#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiAFKBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiAFKBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("24779895"))
API_HASH = getenv("24ca02336ac39cb748e2946de19814e3")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("7651069480:AAEJOhBH1RxoCUl-L4HH9NhNdl8INxuKwQY")

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("mongodb+srv://ztx1430:<db_password>@cluster0.pagia.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("7757912959", "").split())
)  # Input type must be interger
