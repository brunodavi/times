# TIMES
Simple pomodoro cli on terminal


## Install
```
pip install git+https://github.com/brunodavi/times
```

## Usage

```
Usage: t [OPTIONS]

  Simple pomodoro CLI on terminal.

Options:
  -m, --message TEXT         Message to display during the task
  -c, --cycles INTEGER       Number of pomodoro cycles
  -d, --duration TEXT        Task duration
  -b, --break-duration TEXT  Duration of the short break
  -B, --break-message TEXT   Message to display during the short break
  -l, --long-duration TEXT   Duration of the long break
  -L, --long-message TEXT    Message to display during the long break
  -N, --no-long-break        Disable the long break at the end of the cycles
  -r, --repeat               Automatically repeat the cycles
  -v, --verbose              Displays notification titles in the terminal
  --help                     Show this message and exit.
```

### Examples
```sh
$ t --message Work --duration 30m --break-duration 10m --no-long-break
```

OR

```sh
$ t -m Work -d 30m -b 10m -N
```
