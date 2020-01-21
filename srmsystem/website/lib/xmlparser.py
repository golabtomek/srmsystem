from xml.dom import minidom

def parse_race_results(xmlfile):
    xmldoc = minidom.parse(xmlfile)
    race = xmldoc.getElementsByTagName('Race')
    raceInfo = RaceInfo()
    raceInfo.mostLaps = race[0].getElementsByTagName('MostLapsCompleted')[0].firstChild.nodeValue
    drivers = race[0].getElementsByTagName('Driver')
    driversRaceResults = []

    def getTiresData(laps):
        tires = []
        previousLap = Lap()
        for lap in laps:
            newTires = TireChange()
            if lap.num == 1:
                newTires.lap = 1
                newTires.fcompound = lap.fcompound
                newTires.rcompound = lap.rcompound
                tires.append(newTires)
            else:
                if (lap.twrr > previousLap.twrr or lap.twrl > previousLap.twrl or lap.twfl > previousLap.twfl or lap.twfr > previousLap.twfr):
                    newTires.fcompound = lap.fcompound
                    newTires.rcompound = lap.rcompound
                    newTires.lap = lap.num
                    tires.append(newTires)
            
            previousLap = lap

        return tires

    for driver in drivers:
        driverRaceResult = DriverRaceResult()
        driverRaceResult.name = driver.getElementsByTagName('Name')[0].firstChild.nodeValue
        driverRaceResult.carType = driver.getElementsByTagName('CarType')[0].firstChild.nodeValue
        driverRaceResult.gridPos = int(driver.getElementsByTagName('GridPos')[0].firstChild.nodeValue)
        driverRaceResult.position = int(driver.getElementsByTagName('Position')[0].firstChild.nodeValue)
        try:
            driverRaceResult.lapRank = int(driver.getElementsByTagName('LapRankIncludingDiscos')[0].firstChild.nodeValue)
        except:
            driverRaceResult.lapRank = 0
        try:
            driverRaceResult.bestLapTime = float(driver.getElementsByTagName('BestLapTime')[0].firstChild.nodeValue)
        except:
            driverRaceResult.bestLapTime = 0
        try:
            driverRaceResult.finishTime = float(driver.getElementsByTagName('FinishTime')[0].firstChild.nodeValue)
        except:
            driverRaceResult.finishTime = 0
        driverRaceResult.lapsNr = int(driver.getElementsByTagName('Laps')[0].firstChild.nodeValue)
        driverRaceResult.pitStops = int(driver.getElementsByTagName('Pitstops')[0].firstChild.nodeValue)
        driverRaceResult.finishStatus = driver.getElementsByTagName('FinishStatus')[0].firstChild.nodeValue
        try:
            driverRaceResult.aids = driver.getElementsByTagName('ControlAndAids')[0].firstChild.nodeValue
        except:
            driverRaceResult.aids = 0
        laps = []
        for lap in driver.getElementsByTagName('Lap'):
            single_lap = Lap()
            single_lap.num = lap.attributes['num'].value
            single_lap.rcompound = lap.attributes['rcompound'].value
            single_lap.fcompound = lap.attributes['fcompound'].value
            single_lap.twrr = float(lap.attributes['twrr'].value)
            single_lap.twrl = float(lap.attributes['twrl'].value)
            single_lap.twfr = float(lap.attributes['twfr'].value)
            single_lap.twfl = float(lap.attributes['twfl'].value)
            single_lap.fuel = float(lap.attributes['fuel'].value)
            try:
                single_lap.s1 = float(lap.attributes['s1'].value)
            except:
                single_lap.s1 = 0
            try:
                single_lap.s2 = float(lap.attributes['s2'].value)
            except:
                single_lap.s2 = 0
            try:
                single_lap.s3 = float(lap.attributes['s3'].value)
            except:
                single_lap.s2 = 0
            try:
                single_lap.lapTime = float(lap.firstChild.nodeValue)
            except:
                single_lap.lapTime = 0
            laps.append(single_lap)
        driverRaceResult.laps = laps
        driverRaceResult.tires = getTiresData(driverRaceResult.laps)
        driversRaceResults.append(driverRaceResult)
    raceResults = RaceResult()
    raceResults.raceInfo = raceInfo
    raceResults.driversRaceResults = driversRaceResults
    return raceResults


def parse_qual_results(xmlfile):
    xmldoc = minidom.parse(xmlfile)
    qual = xmldoc.getElementsByTagName('Qualify')

    drivers = qual[0].getElementsByTagName('Driver')
    driversQualResults = []
    for driver in drivers:
        driverQualResult = DriverQualResult()
        driverQualResult.name = driver.getElementsByTagName('Name')[0].firstChild.nodeValue
        driverQualResult.carType = driver.getElementsByTagName('CarType')[0].firstChild.nodeValue
        driverQualResult.position = int(driver.getElementsByTagName('Position')[0].firstChild.nodeValue)
        try:
            driverQualResult.bestLapTime = float(driver.getElementsByTagName('BestLapTime')[0].firstChild.nodeValue)
        except:
            driverQualResult.bestLapTime = 0
        try:
            driverQualResult.aids = driver.getElementsByTagName('ControlAndAids')[0].firstChild.nodeValue
        except:
            driverQualResult.aids = 0
        try:
            driverQualResult.lapsNr = int(driver.getElementsByTagName('Laps')[0].firstChild.nodeValue)
        except:
            driverQualResult.lapsNr = 0
        laps = []
        best_lap_time = 0
        best_lap_ftires_compound = ""
        best_lap_rtires_compound = ""
        for lap in driver.getElementsByTagName('Lap'):
            single_lap = Lap()
            single_lap.rcompound = lap.attributes['rcompound'].value
            single_lap.fcompound = lap.attributes['fcompound'].value
            single_lap.twrr = float(lap.attributes['twrr'].value)
            single_lap.twrl = float(lap.attributes['twrl'].value)
            single_lap.twfr = float(lap.attributes['twfr'].value)
            single_lap.twfl = float(lap.attributes['twfl'].value)
            single_lap.fuel = float(lap.attributes['fuel'].value)
            try:
                single_lap.s1 = float(lap.attributes['s1'].value)
            except:
                single_lap.s1 = 0
            try:
                single_lap.s2 = float(lap.attributes['s2'].value)
            except:
                single_lap.s2 = 0
            try:
                single_lap.s3 = float(lap.attributes['s3'].value)
            except:
                single_lap.s2 = 0
            try:
                single_lap.lapTime = float(lap.firstChild.nodeValue)
                if single_lap.lapTime < best_lap_time:
                    best_lap_time = single_lap.lapTime
                    best_lap_ftires_compound = single_lap.fcompound
                    best_lap_rtires_compound = single_lap.rcompound
                if best_lap_time == 0:
                    best_lap_time = single_lap.lapTime
                    best_lap_ftires_compound = single_lap.fcompound
                    best_lap_rtires_compound = single_lap.rcompound
            except:
                single_lap.lapTime = 0
            laps.append(single_lap)
        driverQualResult.fcompound = best_lap_ftires_compound
        driverQualResult.rcompound = best_lap_rtires_compound
        driverQualResult.laps = laps
        driversQualResults.append(driverQualResult)
    qualResults = QualResult()
    qualResults.driversQualResults = driversQualResults
    return qualResults

class Lap():
    rcompound = ""
    fcompound = ""
    twrr = 0
    twrl = 0
    twfr = 0
    twfl = 0
    fuel = 0
    s3 = 0
    s2 = 0
    s1 = 0
    p = 0
    num = 0
    pit = False
    lapTime = 0

class TireChange():
    lap = 0
    fcompound = ""
    rcompound = ""

class DriverRaceResult():
    name = ""
    carType = ""
    gridPos = 0
    position = 0
    lapRank = 0
    laps = []
    bestLapTime = 0
    finishTime = 0
    lapsNr = 0
    pitStops = 0
    finishStatus = 0
    aids = ""
    tires = []


class RaceInfo():
    mostLaps = 0

class RaceResult():
    raceInfo = RaceInfo()
    driversRaceResults = []

class DriverQualResult():
    name = ""
    carType = ""
    position = 0
    laps = []
    bestLapTime = 0
    lapsNr = 0
    aids = ""
    fcompound = ""
    rcompound = ""
    
class QualResult():
    driversQualResults = []