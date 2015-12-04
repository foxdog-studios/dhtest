#!/usr/bin/env python

import subprocess
import time
from argparse import ArgumentParser
from pathlib import Path


def main():
    parser = ArgumentParser()
    parser.add_argument('-i', '--interval', default=0.25, type=float)
    parser.add_argument('-s', '--start', default=0, type=int)
    parser.add_argument('-S', '--stop', default=256, type=int)
    args = parser.parse_args()

    dhtest_path = (Path(__file__).parent / 'dhtest').resolve()

    for index in range(args.start, args.stop):
        suffix = '%02x:%02x' % ((index & 0xff00) >> 8, index & 0x00ff)

        print()
        print(index)

        subprocess.check_call([
            '/usr/bin/sudo',
            str(dhtest_path),
            '--interface', 'enp3s0',
            '-m', '00:00:11:22:' + suffix
        ])
        time.sleep(args.interval)


if __name__ == '__main__':
    main()

