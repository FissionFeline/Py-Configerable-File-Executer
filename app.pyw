import json
import subprocess
import time

def main():
    try:
        with open("config.json","r") as File:
            try:
                JsonTmpVar = json.loads(File.read())
                Run_File(JsonTmpVar["File"])
                time.sleep(int(JsonTmpVar["Time_Int"]))
                Run_File(JsonTmpVar["File1"])
            except Exception as e:
                pass
    except FileExistsError:
        pass
    except FileNotFoundError:
        pass

def Run_File(Path):
    try:
        subprocess.Popen(Path)
    except Exception as e:
        print(e)

if __name__ == "__main__":#tf do you think this does ?
    main()
#furious F
