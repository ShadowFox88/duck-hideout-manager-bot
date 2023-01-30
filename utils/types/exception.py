from __future__ import annotations

from typing import TYPE_CHECKING, Optional, TypedDict

if TYPE_CHECKING:
    import datetime

    from discord import app_commands
    from discord.ext import commands


class _HideoutTracebackOptional(TypedDict, total=False):
    author: int
    guild: Optional[int]
    channel: int
    command: Optional[commands.Command | app_commands.Command | app_commands.ContextMenu]


class HideoutTraceback(_HideoutTracebackOptional):
    time: datetime.datetime
    exception: Exception
