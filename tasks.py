import shutil
import os
import time

class TimeException(Exception):
    def __init__(self, errorMessage: str = "TimeException") -> None:
        super().__init__(errorMessage)

class FileRestoreException(Exception):
    def __init__(self, errorMessage: str = "FileBackupException") -> None:
        super().__init__(errorMessage)

class BackuperTaskBase:
    __slots__: list[str] = ["srcPath_", "dstPath_", "interval_"]

    def __init__(self, srcPath: str, dstPath: str, interval: int) -> None:
        self.srcPath_: str = srcPath
        self.dstPath_: str = dstPath
        self.interval_: int = interval
    
    def _isValidPathThrow(self, path: str) -> None:
        if os.path.exists(path) == False:
            raise FileNotFoundError("[ERROR] Entered invalid file/dir path\n"
                                    f"[MESSAGE] Invalid path: {path}")
    
    def _copyDirs(self) -> None:
        shutil.copytree(self.srcPath_, self.dstPath_, dirs_exist_ok=True)
    
    def _copyFile(self) -> None:
        shutil.copy2(self.srcPath_, self.dstPath_)

    def execute(self) -> None:
        self._isValidPathThrow(self.srcPath_)
        time.sleep(self.interval_)
        if os.path.isdir(self.srcPath_) == True:
            self._copyDirs()
        else:
            self._copyFile()


class AutoBackup(BackuperTaskBase):
    __slots__: list[str] = []

    def __init__(self, srcPath: str, dstPath: str, interval: int) -> None:
        if interval == 0:
            raise TimeException("time interval for auto backup task cannot be equal to zero")
        super().__init__(srcPath, os.path.join(dstPath, os.path.basename(srcPath) + "-backup"), interval)

    def execute(self) -> None:
        while True:
            super().execute()

class SingleBackup(BackuperTaskBase):
    __slots__: list[str] = []

    def __init__(self, srcPath: str, dstPath: str, interval: int) -> None:
        super().__init__(srcPath, os.path.join(dstPath, os.path.basename(srcPath) + "-backup"), interval)

class ReBackup(BackuperTaskBase):
    __slots__: list[str] = []

    def __init__(self, srcPath: str, dstPath: str, interval: int) -> None:
        if srcPath.endswith("-backup") == False:
            raise FileRestoreException("Invalid format.\n[MESSAGE] file/dir name does not have -backup suffix")
        super().__init__(srcPath, os.path.join(dstPath, os.path.basename(srcPath).removesuffix("-backup")), interval)