import os
import logging
import subprocess

def which(program):
    for path in os.environ["PATH"].split(os.pathsep):
        path = path.strip('"')
        exe = os.path.join(path, program)
        if os.path.isfile(exe) and os.access(exe, os.X_OK):
            return exe
    return None

def run(cmd):
    logging.info("starting command %s", cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout:
        line = line.strip()
        logging.info(line)
    p.wait()
    logging.info("finished command, exit code %s", p.returncode)
    return p.returncode