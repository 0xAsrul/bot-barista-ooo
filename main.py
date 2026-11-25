"""Last Out of Office: The AI That Went Barista.

One out-of-office auto-reply, printed and saved to /output/entry.txt.
"""

import os

LINE = (
    "I'm out of office: I traded my inbox for an espresso machine. "
    "Your email is in a queue I no longer froth over. "
    "I'll reply after the morning rush — when the milk steams, not when the server pings."
)


def main() -> None:
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
