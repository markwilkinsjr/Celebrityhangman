"""Command-line utility for scheduling periodic break reminders."""

import argparse
import importlib
import sys
import time
from typing import Callable, Optional


def get_notifier() -> Optional[Callable[[str, str], None]]:
    """Return a callable that sends notifications or ``None`` if unavailable."""
    spec = importlib.util.find_spec("plyer")
    if spec is None:
        return None

    notification_module = importlib.import_module("plyer.notification")

    def notifier(title: str, message: str) -> None:
        notification_module.notify(title=title, message=message)

    return notifier


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Send desktop notifications reminding you to take breaks."
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=60.0,
        help="Minutes between reminders (default: %(default)s)",
    )
    parser.add_argument(
        "--title",
        default="Break Reminder",
        help="Notification title (default: %(default)s)",
    )
    parser.add_argument(
        "--message",
        default="Time to take a break!",
        help="Notification message (default: %(default)s)",
    )
    return parser.parse_args(argv)


def send_notification(title: str, message: str, notifier: Optional[Callable[[str, str], None]]) -> None:
    if notifier is not None:
        notifier(title, message)
    else:
        print(f"{title}: {message}")


def main(argv: Optional[list[str]] = None) -> None:
    args = parse_args(argv)
    notifier = get_notifier()

    if notifier is None:
        print(
            "plyer is not installed; falling back to console output for reminders.",
            file=sys.stderr,
        )

    if args.interval <= 0:
        print("Interval must be greater than 0 minutes.", file=sys.stderr)
        sys.exit(1)

    delay = args.interval * 60

    print(
        "Starting break reminders every {minutes:.2f} minutes. Press Ctrl+C to stop.".format(
            minutes=args.interval
        )
    )

    try:
        while True:
            send_notification(args.title, args.message, notifier)
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nBreak reminders stopped.")


if __name__ == "__main__":
    main()
