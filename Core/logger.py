import logging,sys,os
sys.path.append(os.path.dirname(sys.path[0]))
from conf import settings


def logger(log_obj):

    logger= logging.getLogger(log_obj)

    logger.setLevel(logging.DEBUG)


    logfile = "%s/log/%s.log" %(settings.BASE_DIR, log_obj)
    fh=logging.FileHandler(logfile)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger


