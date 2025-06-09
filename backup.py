from timeparser import TimeParser
from tasks import AutoBackup, SingleBackup, ReBackup
import argparse

class Backuper:
    __slots__: list[str] = ["timeParser"]

    def __init__(self) -> None:
        self.timeParser: TimeParser = TimeParser()
    
    def makeBackup(self, args: argparse.Namespace) -> None:
        interval: int = self.timeParser.parseTime(args.time)
        if args.mode[0] == "-b":
            autoBackup: AutoBackup = AutoBackup(args.path, args.path_to, interval)
            autoBackup.execute()
        elif args.mode[0] == "-o":
            singleBackup: SingleBackup = SingleBackup(args.path, args.path_to, interval)
            singleBackup.execute()
        else:
            reBackup: ReBackup = ReBackup(args.path, args.path_to, interval)
            reBackup.execute()