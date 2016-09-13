#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from uiautomator import device as d
import time
import commands

class IreaderTest(unittest.TestCase):
    def setUp(self):
        super(IreaderTest, self).setUp()
        d.wakeup()
        d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") \
                             .press.back.home()
        d.press('home')
        
    def testLaunchAndCloseIreaderByBackKey(self):
        '''
        Summary: Test launch and close ireader by back key
        Steps:  1. Launch ireader 
                2. Chech enter ireader successfully
                3. Exit ireader by back key
                4. Repeat steps 1-3 500 times
        '''
        for i in range(1,2):
            #Step 1
            d(text='掌阅iReader',className='android.widget.TextView').click.wait()
            time.sleep(3)
            #Step 2
            assert d(text='书城',className='android.widget.TextView')
            #Step 3
            d.press('back')
            d.press('back') 
            d.press('back')   

    def tearDown(self):
        super(IreaderTest, self).tearDown()
        d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") \
                             .press.back.home()
        d.press('back')
        d.press('home')