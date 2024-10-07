from re import match


def convert_to_seconds(duration: str):
    pattern = r'(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?'
    matches = match(pattern, duration)

    if not matches:
        raise ValueError("Invalid format!")

    [hours, minutes, seconds] = (
        int(matches.group(i) or 0) for i in range(1, 4)
    )

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds
