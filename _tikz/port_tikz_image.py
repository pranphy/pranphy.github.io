#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2020-07-28 23:34

import os
import sys
from pathlib import Path

md_template =(
"""---
layout: tikzimage
title: {TITLE}
tags: {TAGS}
image: {IMAGENAME}
date: {DATE}
---

{HEADERINFO}

```tex
{CONTENT}
```
"""
)

def copy_image(imagepath):
    cmd = f'view_latex {imagepath} ../static/img/tikz/ >> /dev/null'
    print(f'Running {cmd}')
    op = os.system(cmd)
    print(f'Obtained {op}')


def read_text(path):
    with path.open() as tikf:
        content = tikf.read()
        return content


def create_md(md_path,imagename,content,date='2020-07-14'):
    title = 'This is a test title'
    tags = 'ml tikz'
    with open(md_path,'w') as wf:
        md_string = md_template.replace('{IMAGENAME}',imagename)\
                .replace('{TITLE}',title)\
                .replace('{CONTENT}',content)\
                .replace('{DATE}',date)\
                .replace('{TAGS}',tags)\
                .replace('{HEADERINFO}','header information here')\
                .replace('{%','{ %')

        wf.write(md_string)

    print(f'{md_path} written ')
    return

if __name__ == '__main__':
    path = sys.argv[1]
    write_path = None
    try:
        write_path = sys.argv[2]
    except:
        pass

    tikzpath = Path(path)

    all_images = tikzpath.glob('**/*.tex')
    for imagepath in all_images:
        #copy_image(imagepath)
        fname = imagepath.stem
        #print(f'{imagepath.stem:>20} :: {imagepath.suffix:>5} :: {imagepath.parent}')
        content = read_text(imagepath)
        create_md(f'./{fname}.md',f'{fname}.png',content=content)



