import argparse
import os
import re
import shutil
import json

def get_user_hfs(force=False):
    
    hdirs = [ hdir for hdir in os.listdir(os.environ["HOME"])
                    if os.path.isdir(hdir) and
                    if re.match("^houdini[0-9]+.[0-9]+$", hdir) ]
    
    if len(hdirs) < 1:
        print "No houdini preferences found in user folder."
        return None

    if len(hdirs == 1):
        return hdirs[0]

    if force:
        return max([hdir for hdir in hdirs],
                    key=lambda hdir: float(hdir.replace("houdini", "")))
    
    print "\nHOUDINI PREFS FOLDERS:\n\n"
    for i, hdir in enumerate(hdirs):
        print "[{0}] {1}\n".format(i, hdir)
    print "\nChoose a Houdini version\n\n"
    
    valid_input = False
    
    while True:
        selection = raw_input("Number between {0}-{1}, or q to quit: "
                              .format(0, len(dirs) - 1))
        if selection == "q":
            return None
        
        try:
            num = int(selection)
            if num < 0 or num >= len(houdinidirs):
                print "Not in range.\n"
                continue
            return hdirs[num]
        
        except ValueError:
            print "Not a valid number.\n"
            continue

parser = argparse.ArgumentParser(description="Install or update HOPs")
parser.add_argument("--fromuser", "-u", action="store_true",
                    help="Pull changes from user's folder")
parser.add_argument("--hdadir", "-d", action="store",
                    help="Install to a specific hda directory")
parser.add_argument("--force", "-f", action="store_true",
                    help="Ask for no user input, chooses defaults where it can")
args = parser.parse_args()

hdadir = os.hdadir

if not hdadir:
    hfs = get_user_hfs(force=bool(args.force))
    if not hfs:
        quit()
    hdadir = os.path.join(hfs, "otls")

src_hdadir = os.path.join(os.path.dirname(__file__), "hdas")

history = {}
if args.fromuser:
    history_file = os.path.join(src_hdadir, "hops_data", "history.json")
else:
    history_file = os.path.join(hdadir, "hops_data", "history.json")

with open(history_file, "r") as f:
    history = json.loads(f)

version = 0
about_file = os.path.join(src_hdadir, "hops_data", "about.json")
with open(about_file, "r") as f:
    about = json.loads(f)
    if args.fromuser:
        about["version"] += 1

    version = about["version"]

# shutil.copytree(src_hdadir, hdadir)

with open(about_file, "w") as f:
    f.write(json.dumps(version))

import getpass, socket, datetime
user = getpass.getuser()
hostname = socket.gethostname()
time = datetime.datetime.now().isoformat()

history.update({"type" : "development" if args.fromuser else "deployment",
                "version" : version,
                "user" : user,
                "host" : hostname,
                "time" : time })

with open(history_file, "w") as f:
    f.write(json.dumps(history))
