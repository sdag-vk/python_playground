import json

class Configuration():
    def parseConfig(self):
        f = open("config.json")
        data = json.load(f)
        f.close()

        # Parse configuration and assign default values if JSON has missing keys
        self.listenIP =                 data.get('listenIP', "0.0.0.0")
        self.listenPort =               data.get('listenPort', "80")
        self.databaseFile =             data.get('databaseFile', "recordings.db")
        self.soundFileLocation =        data.get('soundFileLocation', "static/wav")
        self.soundFileSuffix =          data.get('soundFileSuffix', ".wav")
        self.navDashboardTitle =        data.get('locale', {}).get("navDashboardTitle", "dashboard")
        self.navRecordingsTitle =       data.get('locale', {}).get('navRecordingsTitle', "recordings")
        self.outboundIdentification =   data.get('outboundIdentification', "031")
        self.debug =                    data.get('debug', False)
        pass

    def __init__(self) -> None:
        self.parseConfig()
        pass