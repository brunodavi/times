from re import match
from datetime import timedelta
from pathlib import Path

from playsound3 import playsound


assets_dir = Path(__file__).resolve().parent.parent.parent / 'assets'


def play(sound: str):
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
