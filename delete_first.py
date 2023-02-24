from jjcli import *

x = glob("camilo_html_md/*.md")

lines = []

for y in x:
  with open(y, 'r') as fp:
    lines = fp.readlines()
    with open(y, 'w') as fp:
        for number, line in enumerate(lines):
            if number not in [0]:
                fp.write(line)