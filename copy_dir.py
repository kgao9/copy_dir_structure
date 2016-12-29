from glob import glob
import os

TOP = <GLOBALPATH>

#copy file structure - not actual files
def copy(dir_name):

    if(dir_name == ''):
        exit(0)

    current_dir = os.getcwd()

    print('here')
    print TOP + dir_name + '/*'
    print(glob(TOP + dir_name + '/*'))

    for path in glob(TOP + dir_name + '/*'):
        if os.path.isdir(path):
            os.mkdir(path.split('/')[-1])
            os.chdir(path.split('/')[-1])

            copy(path.split(TOP)[1])
            os.chdir(current_dir)
            continue

        open(path.split('/')[-1], 'a').close()
        continue

#copy top level file structure
#don't put global path in function - it'll mess everything up
def copyTop(top):
    assert TOP not in top, "top isn't supposed to be a global path, error thrown"
    os.mkdir(top)
    os.chdir(top)

    copy(top)

copyTop(<first dir to copy>)
