from re import match
from datetime import timedelta
from functools import cache
from pathlib import Path

from playsound3 import playsound


@cache
def get_assets():
    this_path = Path(__file__).resolve().parent
    assets_dir = this_path / 'assets'

    while not assets_dir.exists():
        assets_dir = assets_dir.parent.parent
        assets_dir = assets_dir / 'assets'

    return assets_dir


def play(sound: str):
    assets_dir = get_assets()
    sound_path = str(assets_dir / sound)
    playsound(sound_path)


def duration_to_timedelta(duration: str):
    pattern = r'(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?'
    matches = match(pattern, duration)

    if not matches:
        raise ValueError("Invalid format!")

    [hours, minutes, seconds] = (
        int(matches.group(i) or 0) for i in range(1, 4)
    )

    return timedelta(hours=hours, minutes=minutes, seconds=seconds)


def duration_to_seconds(duration: str):
    return int(
        duration_to_timedelta(duration).total_seconds()
    )
