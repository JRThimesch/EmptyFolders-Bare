import os
import shutil

try:
    for root, directories, files in os.walk("."):
        for file in files:
            if not os.path.isfile(os.path.join(".", file)):
            	shutil.move(os.path.join(root, file), ".")
                print(file + " in " + root + " moved to ./")
except IOError as err:
    print("I/O error: {0}".format(err))
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
