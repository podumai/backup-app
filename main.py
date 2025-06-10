import argparse
from backup import Backuper
import logging

logging.basicConfig(
    filename="log.txt",
    filemode="w",
    format="%(asctime)s %(message)s",
    level=logging.ERROR,
    encoding="UTF-8"
)

def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="backup-app",
        formatter_class=argparse.RawTextHelpFormatter,
        description="%(prog)s is the command line utility for monitoring and managing system resources",
        epilog="In case of unseen circumstances, please contact: kirillsm05@gmail.com",
    )
    parser.add_argument(
        "--mode",
        required=True,
        nargs=1,
        type=str,
        choices=["-b", "-o", "-r"],
        help=
        "backuper mode:\n"
        "\t-b -> automatic backup;\n"
        "\t-o -> one-time backup;\n"
        "\t-r -> file recovery."
    )
    parser.add_argument(
      "--path",
      required=True,
      type=str,
      help="path to the source"
    )
    parser.add_argument(
      "--path_to",
      required=False,
      type=str,
      default="",
      help="directory/file path for backup"
    )
    parser.add_argument(
      "--time",
      required=False,
      type=str,
      default="0s",
      help="time delay before backup/restore operation\n"
           "\tformat: <number><time spec>;\n"
           "\ttime specifires: [h, m, s]\n"
           "\texample: 24h60m60s"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0"
    )

    try:
        args: argparse.Namespace = parser.parse_args()
        backuper: Backuper = Backuper()
        backuper.makeBackup(args)
    except Exception as e:
        print(f"[ERROR] {e}")
        logging.error(f"[ERROR] Exception has been thrown: {e}")

if __name__ == "__main__":
    main()