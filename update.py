import time, os, json
from datetime import datetime


dirList = os.getcwd().split("\\")
collectionsDir = dirList[0] + "\\" + dirList[1] + "\\" + dirList[2] + "\\radicale\\collections"

while True:
    now = datetime.now()
    if (now.minute % 30) == 0 and now.second == 0:
        print(now.strftime("%H:%M:%S"))
        for r, d, f in os.walk(collectionsDir):
            for file in f:
                if file.endswith(".props"):
                    props = (open(os.path.join(r, file), "r")).read()
                    try:
                        propsDict = json.loads(props)
                        calDesc = propsDict["C:calendar-description"]
                        if (calDesc[:16] == "Importing From: "):
                            print(propsDict["D:displayname"])
                            print(calDesc[16:])
                    except:
                        False

    time.sleep(1)
