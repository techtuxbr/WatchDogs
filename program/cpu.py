import psutil

def freq():
    return round(psutil.cpu_freq().current/1000,1)
def cores():
    return psutil.cpu_count()
def phyCores():
    return psutil.cpu_count(logical=False)
def percentage():
    return psutil.cpu_times_percent(interval=1)