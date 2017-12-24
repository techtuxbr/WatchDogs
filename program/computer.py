import platform

def os():
    return platform.uname().system
def osVersion():
    return platform.uname().version
def name():
    return platform.uname().node
def arc():
    return platform.uname().machine
def cpu():
    return platform.uname().processor
def distro():
    if os() == "Linux":
        return platform.linux_distribution()
    else:
        return os()