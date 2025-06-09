class TimeParseError(Exception):
    def __init__(self, errorMessage: str = "TimeParseError") -> None:
        super().__init__(errorMessage)

class TimeParser:
    def __init__(self) -> None:
        pass
    
    def parseTime(self, timeStr: str) -> int:
        totalTime: int = 0
        numericValue: int = 0
        hoursFlag: bool = False
        minutesFlag: bool = False
        secondsFlag: bool = False
        for symbol in timeStr:
            if symbol.isdigit() == True:
                numericValue = numericValue*10 + int(symbol)
            else:
                match symbol:
                    case "h":
                        if numericValue > 24:
                            raise TimeParseError(f"Invalid numeric time value. Expected range: h{{0-24}} but recieved {numericValue}")
                        if hoursFlag == True:
                            raise TimeParseError("Time interval cannot contain more than one 'h' specifier")
                        numericValue *= 3600
                        hoursFlag = True
                    case "m":
                        if numericValue > 60:
                            raise TimeParseError(f"Invalid numeric time value. Expected range: m{{0-60}} but recieved {numericValue}")
                        if minutesFlag == True:
                            raise TimeParseError("Time interval cannot contain more than one 'm' specifier")
                        numericValue *= 60
                        minutesFlag = True
                    case "s":
                        if numericValue > 60:
                            raise TimeParseError(f"Invalid numeric time value. Expected range: s{{0-60}} but recieved {numericValue}")
                        if secondsFlag == True:
                            raise TimeParseError("Time interval cannot contain more than one 's' specifier")
                        secondsFlag = True
                    case _:
                        raise TimeParseError(f"Invalid character in time interval: {symbol}")
                totalTime += numericValue
                numericValue = 0
        return totalTime