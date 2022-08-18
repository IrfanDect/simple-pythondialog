#!/usr/bin/python3 
# Author : irfanoid as irfanDect
# version : tahap pengembangan

import os
import time
from dialog import Dialog as irfanoid
import dialog
import sys
from googlesearch import search


class MyApp:
    def __init__(self,white,**kwargs):
        """ simple create colors """
        self.white = white
        self.red = kwargs.get('red')
        self.blue = kwargs.get('blue')
        self.cyan = kwargs.get('cyan')
        self.green = kwargs.get('green')
        self.yellow = kwargs.get('yellow')
        self.reset = kwargs.get('reset')
        self.default_title = kwargs.get('default_title')

        """ simple create dialog """
        self.aplication = irfanoid(
                dialog='dialog',
                autowidgetsize=True,
                use_stdout=None
            )
        self.yn = self.aplication.yesno
        self.msg = self.aplication.msgbox
        self.inf = self.aplication.infobox
        self.inp = self.aplication.inputbox
        self.ok = self.aplication.OK
        self.cancel = self.aplication.CANCEL
        self.help = self.aplication.HELP
        self.edit = self.aplication.editbox
        self.text = self.aplication.textbox

        return self.aplication.set_background_title('{}'.format(self.default_title))

""" simple create menu """
class MyIrfanoid(MyApp):
    """ simple create yn """
    def _irfanoid_yn_(self,title='',**kwargs):
        try:
            self.title = title
            self.back_title = kwargs.get('back_title')

            self.msd = self.yn('\n{} yes{} == quit from tool\n\n {}cancel{} == back to frist_menu tool\n'.format(
                self.red,
                self.reset,
                self.red,
                self.reset
                ),
                    colors=True,
                    height=9,
                    width=40,
                    backtitle=self.back_title,
                    title=self.title
                )
            if self.msd == self.aplication.OK:
                sys.exit(1)
            elif self.msd == self.aplication.CANCEL:
                self.aplication.msgbox('{} cancel = back to frist_menu tool '.format(self.cyan),
                        colors=True,
                        height=8,
                        width=40,
                        title=self.title,
                        backtitle=self.back_title
                    )
        except KeyboardInterrupt:
            sys.exit(1)

    def _irfanoid_mn_(self,title,**kwargs):
        self.back_title = kwargs.get('back_title')
        x , self.mw = self.aplication.menu('title',
                choices=[
                    ('search','search links'),
                    ('result','show results ')
                    ],
                title="{}".format(title),
                menu_height=4)

        if x == self.aplication.OK:
            fields = open('links.txt','w')
            if self.mw in ['search']:
                query = self.aplication.inputbox('>_ ')
                for parserd in query:
                    pass
                for d in search(query=parserd,tld='com',num=10000,stop=10000,pause=0.1):
                    time.sleep(0.1)
                    fields.write(d + '\n')
                    self.inf(f'{d}')

            elif self.mw in ['result']:
                self.text('.links.txt',height=13,width=80)
        elif x == self.cancel:
            self.inf('\tExiting...',height=7,width=40) 


# --*-- Examples colors --*--
#
#ap = MyIrfanoid(white,red,yellow,cyan,green,black,blue,magenta , **kwargs)

# --*-- Examples menu --*--
#
#_irfanoid_mn_(title, **kwargs)
