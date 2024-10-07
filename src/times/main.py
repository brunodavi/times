import time

from plyer import notification

from times.cli import get_args
from times.lib import convert_to_seconds


def main(args = None):
    if args is None:
        args = get_args()


    def auto_pause():
        if not args.auto_start:
            input("Press [ Enter ] to continue...")


    def notify(title: str):
        if args.verbose: print(f'{title=}')
        notification.notify(
            title,
            app_name='times',
            timeout=3
        )


    def wait(duration: str):
        time.sleep(
            convert_to_seconds(duration)
        )


    stop_message = args.stop_message.format(stop_duration=args.stop_duration)
    long_message = args.long_message.format(long_duration=args.long_duration)

    while True:
        for current_cycle in range(1, args.cycles + 1):
            message = args.message.format(
                current_cycle=current_cycle,
                cycles=args.cycles,
                short_duration=args.short_duration
            )

            notify(message)
            wait(args.short_duration)
            auto_pause()

            notify(stop_message)
            wait(args.stop_duration)
            auto_pause()

        if args.no_long_break:
            notify(long_message)
            wait(args.long_duration)

        if not args.repeat: break


if __name__ == "__main__":
    main()
