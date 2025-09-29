# Celebrity Hangman Utilities

This repository contains a simple celebrity-themed Hangman game along with
supporting utilities.

## Break Reminder Tool

A lightweight reminder loop is available in `tools/break_reminder.py`. The
utility sends periodic notifications encouraging you to step away from the
keyboard.

### Installation

The reminder only requires the Python standard library. For desktop
notifications, install the optional [plyer](https://github.com/kivy/plyer)
dependency:

```bash
pip install plyer
```

Without `plyer`, the script falls back to printing reminders to the console.

### Usage

Run the reminder from the repository root:

```bash
python tools/break_reminder.py --interval 30
```

Key options:

- `--interval`: Minutes between reminders (default: `60`).
- `--title`: Notification title text.
- `--message`: Notification message body.

Use `Ctrl+C` to stop the reminder loop when you are done.
