import argparse
from datetime import datetime
from time import sleep
from asciimatics.constants import COLOUR_RED
from docx import Document
import keyboard
import logwriting
import os
import parsers
import querygen
import sys
from threading import Thread
from asciimatics.effects import Cycle, RandomNoise, BannerText
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen



parser = argparse.ArgumentParser(description='Kumonome: simple random youtube parser')
parser.add_argument('--maxviews', type=int, default=2000, help='max views count for videos (default: 2000)')
parser.add_argument('--ql', type=int, default=5, help='number of random-generated symbols (default: 5)')
parser.add_argument('--mode', type=str, default="vid", help='search mode(TODO; now avalible for videos only)')
parser.add_argument('--docx', type=int, default=0, help='write .docx logs(optional; default: disabled)')
argsl = parser.parse_args()

def demo(screen):
    effects = [RandomNoise(screen, signal = FigletText("KUMONOME", font='standard', width=200))]
    screen.play([Scene(effects, 500)],repeat=False)
    screen.clear()
    d = ', .docx logs enabled' if (argsl.docx != 0) else ''
    screen.print_at(f'\n\tThe next params will be used: mode = {argsl.mode}, max count of views = {argsl.maxviews}, {argsl.ql} generated symbols{d}', 0, 0, COLOUR_RED)
    screen.refresh()
    sleep(10)
Screen.wrapper(demo)


direct = logwriting.make_logs_dir(argsl.docx)
os.chdir(direct)
dt = str(datetime.now())
if argsl.docx != 0:
    test_log = logwriting.Docx_log('logs.docx')
    test_log.default_set()
    test_log.logwrite(f'<{dt}>')
with open('logs.txt', 'a+', encoding='utf-8') as l:
    l.write(f'\n\n<{dt}>\n')
q = querygen.Query(argsl.ql)
test = parsers.Yt_Parser(argsl.mode, argsl.maxviews)
#th.start
while True:
    test.search(q.rand_qgen(), argsl.docx)



