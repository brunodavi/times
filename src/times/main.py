import time

from times.lib import duration_to_seconds, play, timedelta

import click


def print_message(message: str, current_cycle: int, cycles: int, rest_time: str, bg='red', paused=False):
    pause = '\u23F5' if paused else '\u23F8'

    cycle_message = click.style(f" {current_cycle}/{cycles} ", fg='black', bg='yellow', bold=True)
    time_message = click.style(f" {rest_time} ", fg='white', bg='blue', bold=True)
    task_message = click.style(f' {message} ', fg='black', bg=bg, bold=True)
    paused_message = click.style(f' {pause} ', fg='black', bg='white', bold=True)

    click.echo(f"\r{cycle_message}{time_message}{paused_message}{task_message}", nl=False)


def countdown(duration: str, print_message: callable, paused=False):
    duration_seconds = duration_to_seconds(duration)

    if paused:
        rest_time = str(timedelta(seconds=duration_seconds))
        print_message(rest_time, paused)
        click.pause(info='')

    for rest in range(duration_seconds, 0, -1):
        rest_time = str(timedelta(seconds=rest))
        print_message(rest_time)
        time.sleep(1)

    print_message('0:00:00')

    click.echo()


@click.command(name='t')
@click.option(
    '-m', '--message',
    default='Focus on your task',
    help='Message to display during the task'
)
@click.option(
    '-c', '--cycles',
    default=1,
    type=int,
    help='Number of pomodoro cycles'
)
@click.option(
    '-d', '--duration',
    default='25m',
    help='Task duration'
)
@click.option(
    '-b', '--break-duration',
    default='5m',
    help='Duration of the short break'
)
@click.option(
    '-B', '--break-message',
    default='Give yourself a break',
    help='Message to display during the short break'
)
@click.option(
    '-l', '--long-duration',
    default='10m',
    help='Duration of the long break'
)
@click.option(
    '-L', '--long-message',
    default='Give yourself a long break',
    help='Message to display during the long break'
)
@click.option(
    '-N', '--no-long-break',
    is_flag=True,
    default=False,
    help='Disable the long break at the end of the cycles'
)
@click.option(
    '-p', '--paused',
    is_flag=True, 
    default=False,
    help='Automatically pause each interval'
)
@click.option(
    '-r', '--repeat',
    is_flag=True, 
    help='Automatically repeat the cycles'
)
@click.option(
    '-v', '--verbose',
    is_flag=True, 
    help='Displays notification titles in the terminal'
)
def main(
    message: str,
    cycles: int,
    duration: str,

    break_duration: str,
    break_message: str,

    long_duration: str,
    long_message: str,

    no_long_break: bool,
    paused: bool,
    repeat: bool,
    verbose: bool,
):
    """
    Simple pomodoro CLI on terminal.
    """

    if verbose:
        click.echo(f"Message: {message}")
        click.echo(f"Cycles: {cycles}")
        click.echo(f"Duration: {duration}")

        click.echo(f"Break Duration: {break_duration}")
        click.echo(f"Break Message: {break_message}")

        click.echo(f"Long Duration: {long_duration}")
        click.echo(f"Long Message: {long_message}")

        click.echo(f"No Long Break: {no_long_break}")
        click.echo(f"Paused: {paused}")
        click.echo(f"Repeat: {repeat}")
        click.echo(f"Verbose: {verbose}")
        click.echo()

    for current_cycle in range(1, cycles + 1):
        def print_task_duration(rest_time: str, paused=False):
            print_message(message, current_cycle, cycles, rest_time, paused=paused)

        def print_break_duration(rest_time: str, paused=False):
            print_message(break_message, current_cycle, cycles, rest_time, bg='yellow', paused=paused)

        play('focus.mp3')
        countdown(duration, print_task_duration, paused)

        play('break.mp3')
        countdown(break_duration, print_break_duration, paused)

    def print_long_duration(rest_time: str, paused=False):
        print_message(long_message, cycles, cycles, rest_time, bg='blue', paused=paused)

    if not no_long_break:
        play('long-break.mp3')
        countdown(long_duration, print_long_duration, paused)

    if repeat: main()

if __name__ == "__main__":
    main()
