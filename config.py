import configparser
import sys
import os.path


class Config(configparser.ConfigParser):
    def __init__(self, filename="config.ini"):
        super().__init__()
        self.fn = filename

        if not os.path.isfile(filename):
            self._create()
            sys.exit(f"Need to configure {filename} file.")

        self.read(filename)

    def _create(self):
        self["TgBot"] = {"token": "bot123123:123"}
        self["user"] = {"uid": "123123123"}
        self["admin"] = {"uid": "123123123"}

        with open(self.fn, "w") as cf:
            self.write(cf)
