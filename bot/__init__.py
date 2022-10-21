#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

""" credentials """

import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from .get_config import get_config

load_dotenv("config.env")

API_HASH = get_config("API_HASH", should_prompt=True)
APP_ID = get_config("APP_ID", should_prompt=True)
TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", should_prompt=True)
AUTH_CHANNEL = int(get_config(
        "AUTH_CHANNEL",
        "-100",
        should_prompt=True
    )
)
SUB_CHANNEL = int(get_config("SUB_CHANNEL", "-100"))
DB_URI = get_config(
    "DATABASE_URL",
    should_prompt=True
)
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
COMMM_AND_PRE_FIX = get_config("COMMM_AND_PRE_FIX", "/")
BAN_COMMAND = get_config("BAN_COMMAND", "ban")
UN_BAN_COMMAND = get_config("UN_BAN_COMMAND", "unban")
START_COMMAND = get_config("START_COMMAND", "start")
BROADCAST_COMMAND = get_config("BROADCAST_COMMAND", "send")
DEFAULT_START_TEXT = (
    "<b>Hi bro... ☺️</b>\n"
    "<b>Tôi có thể giúp gì cho bạn? 😬</b>"
)
START_OTHER_USERS_TEXT = int(get_config(
    "START_OTHER_USERS_TEXT",
    0
))
ONLINE_CHECK_START_TEXT = get_config(
    "ONLINE_CHECK_START_TEXT",
    (
        "✅ <b>Đang hoạt động</b>"
     )
)
DELETED_MESSAGES_NOTIFICATION_TEXT = get_config(
    "DELETED_MESSAGES_NOTIFICATION_TEXT",
    (
        "<b>❌ Tin nhắn đã bị xóa.</b>"
    )
)
DERP_USER_S_TEXT = get_config(
    "DERP_USER_S_TEXT",
    "😐"
)
IS_BLACK_LIST_ED_MESSAGE_TEXT = get_config(
    "IS_BLACK_LIST_ED_MESSAGE_TEXT",
    (
        "❌ Bạn đã bị <b>cấm</b> vĩnh viễn.\n\n"
        "<u>Lý do</u>: <code>{reason}</code>"
    )
)
REASON_DE_LIMIT_ER = get_config(
    "REASON_DE_LIMIT_ER",
    "\n\n"
)
IS_UN_BANED_MESSAGE_TEXT = get_config(
    "IS_UN_BANED_MESSAGE_TEXT",
    (
        "✅ Bạn đã được <b>bỏ cấm</b>.\n\n"
        "<u>Lý do</u>: <code>{reason}</code>"
    )
)
BOT_WS_BLOCKED_BY_USER = get_config(
    "BOT_WS_BLOCKED_BY_USER",
    "Bot đã bị chặn bởi người dùng."
)
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "NoPMsBot.log")

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)
