from sys import argv
import time
import psutil
from multiprocessing import Pool
from multiprocessing import cpu_count

NAME = argv[0]


def cpu_load(x):
    while True:
        x*x


def process_info():

     while True:
        p = psutil.Process()
        it = psutil.process_iter(("name", "cmdline", "cpu_percent", "pid", "memory_percent"))

        for proc in it:
            if "python" in proc.info["name"] and (cl := proc.info["cmdline"]) is not None and len(cl) > 0 and NAME in cl[-1]:
                info = {
                    "PID": f"{proc.info['pid']}",
                    "CPU in use": f"{proc.info['cpu_percent']}%",
                    "Working set": p.memory_info().rss,
                    "Private bytes": p.memory_info().private,
                }

                print("\n".join([f"{key}: {value}" for key, value in info.items()]))

                time.sleep(3)
                save_process(info)


def save_process(info):
    with open('info_process.txt', 'a') as f:
        f.write(str(info))


if __name__ == '__main__':
    processes = cpu_count()
    pool = Pool(processes)
    process_info()
    pool.map(cpu_load, range(processes))

