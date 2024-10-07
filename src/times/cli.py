import argparse


def get_args():
    parser = argparse.ArgumentParser(
        prog='t',
        description='Simple pomodoro CLI on terminal'
    )
    
    parser.add_argument('-m', '--message',
                        type=str,
                        default='Focus on your task for {short_duration} at {current_cycle}/{cycles}',
                        help='Message to display during the task')

    parser.add_argument('-c', '--cycles',
                        type=int,
                        default=1,
                        help='Number of pomodoro cycles')

    parser.add_argument('-sd', '--short_duration',
                        type=str,
                        default='25m',
                        help='Short duration')

    parser.add_argument('-Sd', '--stop_duration',
                        type=str,
                        default='5m',
                        help='Duration of the short break')

    parser.add_argument('-Sm', '--stop_message',
                        type=str,
                        default='Give yourself {stop_duration}',
                        help='Message to display during the short break')

    parser.add_argument('-ld', '--long_duration',
                        type=str,
                        default='10m',
                        help='Duration of the long break')

    parser.add_argument('-lm', '--long_message',
                        type=str,
                        default='Give yourself {long_duration}',
                        help='Message to display during the long break')

    parser.add_argument('-L', '--no_long_break',
                        action='store_false',
                        default=True,
                        help='Determines if there will be a long break at the end of the cycles')

    parser.add_argument('-r', '--repeat',
                        action='store_true',
                        help='Automatically repeat the cycles')

    parser.add_argument('-a', '--auto_start',
                        action='store_true',
                        help='Automatically starts without pausing at each interval')

    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='Displays notification titles in the terminal')

    return parser.parse_args()
