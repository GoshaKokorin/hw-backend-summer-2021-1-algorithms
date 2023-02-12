__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    second = seconds % 86400 % 3600 % 60
    minute = seconds % 86400 % 3600 // 60
    hour = seconds % 86400 // 3600
    day = seconds // 86400

    if day == 0 and hour == 0 and minute == 0:
        return f"{second:02}s"
    elif day == 0 and hour == 0:
        return f"{minute:02}m{second:02}s"
    elif day == 0:
        return f"{hour:02}h{minute:02}m{second:02}s"
    else:
        return f"{day:02}d{hour:02}h{minute:02}m{second:02}s"
