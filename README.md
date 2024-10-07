# TIMES
Simple pomodoro cli on terminal


## Install
```
pip install git+https://github.com/brunodavi/times
```

## Usage

```
usage: t [-h] [-m MESSAGE] [-c CYCLES] [-sd SHORT_DURATION]
         [-Sd STOP_DURATION] [-Sm STOP_MESSAGE] [-ld LONG_DURATION]
         [-lm LONG_MESSAGE] [-L] [-r] [-a] [-v]

Simple pomodoro CLI on terminal

options:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        Message to display during the task
  -c CYCLES, --cycles CYCLES
                        Number of pomodoro cycles
  -sd SHORT_DURATION, --short_duration SHORT_DURATION
                        Short duration
  -Sd STOP_DURATION, --stop_duration STOP_DURATION
                        Duration of the short break
  -Sm STOP_MESSAGE, --stop_message STOP_MESSAGE
                        Message to display during the short break
  -ld LONG_DURATION, --long_duration LONG_DURATION
                        Duration of the long break
  -lm LONG_MESSAGE, --long_message LONG_MESSAGE
                        Message to display during the long break
  -L, --no_long_break   Determines if there will be a long break at the end of
                        the cycles
  -r, --repeat          Automatically repeat the cycles
  -a, --auto_start      Automatically starts without pausing at each interval
  -v, --verbose         Displays notification titles in the terminal

```

### Examples
```sh
$ t --message Work --short_duration 30m --stop_duration 10m --no_long_break
```

OR

```sh
$ t -m Work -sd 30m -Sd 10m -L
```
