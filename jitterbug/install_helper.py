import subprocess
import jitterbug


class BabiliSetupException(Exception):
    pass


class BabelSetupException(Exception):
    pass


def run_npm_install():
    verify_babel()
    verify_babili()

    run_install_commands()


def get_install_commands():
    for key in jitterbug.preset_map.keys():
        yield "npm install babel-plugin-{} --save-dev -g".format(key)


def run_install_commands():
    for command in get_install_commands():
        p = subprocess.Popen(command.split(' '))
        result, err = p.communicate()
        if err:
            print(err)


def verify_babili():
    p = subprocess.Popen(['babili', '--version'])
    result, err = p.communicate()
    if err:
        raise BabiliSetupException("babili did not respond to version check. Did you install it globally?")


def verify_babel():
    p = subprocess.Popen(['babel', '--version'])
    result, err = p.communicate()
    if err:
        raise BabelSetupException("babel did not respond to version check. Did you install it globally?")
