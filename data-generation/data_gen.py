import pandas as pd
import numpy as np
import random
import os

step = 500

def data_gen():
    mega_list = []
    a111_slist = []; a211_slist = []; a221_slist = []
    a111_plist = []; a211_plist = []; a221_plist = []
    h112_list = []; h121_list = []; h122_list = []; h212_list = []; h221_list = []; h222_list = []
    sw34_list = []; sw31_list = []; sw32_list = []; sw33_list = []
    sw11_list = []; sw12_list = []; sw13_list = []
    sw21_list = []; sw22_list = []; sw23_list = []
    s13s34_list = []    # 1 attacker
    s23s34_list = []    # 2 attackers
    sv311_list = []; sv312_list = []; sv322_list = []; sv331_list = []

    for i in range(58800): # every 10 ms
        if i%50 == 0:
            att_rate_list = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]
        att_rate = sum(att_rate_list)
        mega_list.append([i/10, att_rate_list[0], att_rate_list[1], att_rate_list[2]])

        # attackers to server [server31-1, server31-2, server32-2, server33-1]
        a111_s311 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_s312 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_s322 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_s331 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))

        a211_s311 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_s312 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_s322 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_s331 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))

        a221_s311 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a221_s312 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a221_s322 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a221_s331 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))

        a111_a211 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_a221 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_a221 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))

        # [server31-1, server31-2, server32-2, server33-1]
        a111_slist.append([a111_s311, a111_s312, a111_s322, a111_s331])
        a211_slist.append([a211_s311, a211_s312, a211_s322, a211_s331])
        a221_slist.append([a221_s311, a221_s312, a221_s322, a221_s331])
        a111_plist.append([a111_a211, a111_a221])
        a211_plist.append([a111_a211, a211_a221])
        a221_plist.append([a111_a221, a211_a221])

        # host11-2: time diff between two successive frames (ms)
        delay = 0
        if i <= 7200 or 7200 < i <= 13200 or 16200 <= i < 19800 or 25200 < i <= 28200 or 36000 < i <= 39600 or 45000 < i <= 51000:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif 19800 < i <= 24000 or 28200 < i <= 33600 or 39600 < i <= 43800:
            # delay = random.randrange(random.randrange(49, 52), random.randrange(70, 74)) + random.uniform(0.1, 3.9) + random.randrange(34, 56) + random.uniform(0.1, 3.9)
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        else: # idle
            delay = 0
        
        if delay != 0: # attack
            if att_rate > 2.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 2.4 < att_rate <= 2.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 2.1 < att_rate <= 2.4:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.8 < att_rate <= 2.1:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.5 < att_rate <= 1.8:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.2 < att_rate <= 1.5:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1 <= att_rate <= 1.2:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 0.7 <= att_rate < 1:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 0.4 <= att_rate < 0.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            else:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))

        # [server31-1, server31-2, server32-2, server33-1]
        if i <= 13200 or 25200 < i <= 33600:
            h112_list.append([delay, 0, 0, 0])
        elif 16200 < i <= 24000 or 36000 < i <= 43800:
            h112_list.append([0, 0, 0, delay])
        elif 45000 < i <= 51000:
            h112_list.append([0, 0, delay, 0])
        else:
            h112_list.append([0, 0, 0, 0])

        # host12-1: time diff between two successive frames (ms)
        delay = 0
        if i <= 7200 or 7200 < i <= 13200 or 16200 <= i < 19800 or 25200 < i <= 28200 or 36000 < i <= 39600 or 45000 < i <= 51000:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif 19800 < i <= 24000 or 28200 < i <= 33600 or 39600 < i <= 43800:
            # delay = random.randrange(random.randrange(49, 52), random.randrange(70, 74)) + random.uniform(0.1, 3.9) + random.randrange(34, 56) + random.uniform(0.1, 3.9)
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        else: # idle
            delay = 0
        
        if delay != 0: # attack
            if att_rate > 2.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 2.4 < att_rate <= 2.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 2.1 < att_rate <= 2.4:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.8 < att_rate <= 2.1:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.5 < att_rate <= 1.8:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.2 < att_rate <= 1.5:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1 <= att_rate <= 1.2:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 0.7 <= att_rate < 1:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 0.4 <= att_rate < 0.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            else:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))

        # [server31-1, server31-2, server32-2, server33-1]
        if i <= 6000 or 7800 < i <= 16800 or 30600 < i <= 37800 or 50400 < i <= 58800:
            h121_list.append([0, delay, 0, 0])
        elif 18600 < i <= 27600:
            h121_list.append([0, 0, delay, 0])
        elif 39600 < i <= 48000:
            h121_list.append([0, 0, 0, delay])
        else:
            h121_list.append([0, 0, 0, 0])

        # host12-2: time diff between two successive frames (ms)
        delay = 0
        if i <= 7200 or 7200 < i <= 13200 or 16200 <= i < 19800 or 25200 < i <= 28200 or 36000 < i <= 39600 or 45000 < i <= 51000:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif 19800 < i <= 24000 or 28200 < i <= 33600 or 39600 < i <= 43800:
            # delay = random.randrange(random.randrange(49, 52), random.randrange(70, 74)) + random.uniform(0.1, 3.9) + random.randrange(34, 56) + random.uniform(0.1, 3.9)
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        else: # idle
            delay = 0
        
        if delay != 0: # attack
            if att_rate > 2.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 2.4 < att_rate <= 2.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 2.1 < att_rate <= 2.4:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.8 < att_rate <= 2.1:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.5 < att_rate <= 1.8:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.2 < att_rate <= 1.5:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1 <= att_rate <= 1.2:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 0.7 <= att_rate < 1:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 0.4 <= att_rate < 0.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            else:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))

        # [server31-1, server31-2, server32-2, server33-1]
        if i <= 7800 or 35400 < i <= 44400:
            h122_list.append([0, 0, delay, 0])
        elif 8400 < i <= 15600:
            h122_list.append([0, 0, 0, delay])
        elif 15600 < i <= 23400:
            h122_list.append([delay, 0, 0, 0])
        elif 25800 < i <= 34800:
            h122_list.append([0, delay, 0, 0])
        else:
            h122_list.append([0, 0, 0, 0])

        # host21-2: time diff between two successive frames (ms)
        delay = 0
        if i <= 7200 or 7200 < i <= 13200 or 16200 <= i < 19800 or 25200 < i <= 28200 or 36000 < i <= 39600 or 45000 < i <= 51000:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif 19800 < i <= 24000 or 28200 < i <= 33600 or 39600 < i <= 43800:
            # delay = random.randrange(random.randrange(49, 52), random.randrange(70, 74)) + random.uniform(0.1, 3.9) + random.randrange(34, 56) + random.uniform(0.1, 3.9)
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        else: # idle
            delay = 0
        
        if delay != 0: # attack
            if att_rate > 2.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 2.4 < att_rate <= 2.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 2.1 < att_rate <= 2.4:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.8 < att_rate <= 2.1:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.5 < att_rate <= 1.8:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.2 < att_rate <= 1.5:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1 <= att_rate <= 1.2:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 0.7 <= att_rate < 1:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 0.4 <= att_rate < 0.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            else:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))

        # [server31-1, server31-2, server32-2, server33-1]
        if i < 9000 or 19800 < i <= 27000:
            h212_list.append([0, 0, 0, delay])
        elif 10800 < i <= 18600:
            h212_list.append([0, 0, delay, 0])
        elif 28200 < i <= 37200:
            h212_list.append([delay, 0, 0, 0])
        elif 37200 < i <= 43800:
            h212_list.append([0, delay, 0, 0])
        else:
            h212_list.append([0, 0, 0, 0])

        # host22-1 time diff between two successive frames (ms)
        delay = 0
        if i <= 7200 or 7200 < i <= 13200 or 16200 <= i < 19800 or 25200 < i <= 28200 or 36000 < i <= 39600 or 45000 < i <= 51000:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif 19800 < i <= 24000 or 28200 < i <= 33600 or 39600 < i <= 43800:
            # delay = random.randrange(random.randrange(49, 52), random.randrange(70, 74)) + random.uniform(0.1, 3.9) + random.randrange(34, 56) + random.uniform(0.1, 3.9)
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        else: # idle
            delay = 0
        
        if delay != 0: # attack
            if att_rate > 2.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 2.4 < att_rate <= 2.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 2.1 < att_rate <= 2.4:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.8 < att_rate <= 2.1:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.5 < att_rate <= 1.8:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.2 < att_rate <= 1.5:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1 <= att_rate <= 1.2:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 0.7 <= att_rate < 1:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 0.4 <= att_rate < 0.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            else:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))

        # [server31-1, server31-2, server32-2, server33-1]
        if i <= 8400 or 9000 < i <= 16200:
            h221_list.append([0, 0, 0, delay])
        elif 19200 < i <= 25800 or 27600 < i <= 34200 or 37200 < i <= 43200:
            h221_list.append([0, 0, delay, 0])
        else:
            h221_list.append([0, 0, 0, 0])

        # host22-2: time diff between two successive frames (ms)
        delay = 0
        if i <= 7200 or 7200 < i <= 13200 or 16200 <= i < 19800 or 25200 < i <= 28200 or 36000 < i <= 39600 or 45000 < i <= 51000:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif 19800 < i <= 24000 or 28200 < i <= 33600 or 39600 < i <= 43800:
            # delay = random.randrange(random.randrange(49, 52), random.randrange(70, 74)) + random.uniform(0.1, 3.9) + random.randrange(34, 56) + random.uniform(0.1, 3.9)
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        else: # idle
            delay = 0
        
        if delay != 0: # attack
            if att_rate > 2.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 2.4 < att_rate <= 2.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 2.1 < att_rate <= 2.4:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.8 < att_rate <= 2.1:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.5 < att_rate <= 1.8:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1.2 < att_rate <= 1.5:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 1 <= att_rate <= 1.2:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 0.7 <= att_rate < 1:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            elif 0.4 <= att_rate < 0.7:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
            else:
                delay += att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))

        # [server31-1, server31-2, server32-2, server33-1]
        if i <= 16200:
            h222_list.append([0, 0, delay, 0])
        elif 18000 < i <= 26400:
            h222_list.append([0, delay, 0, 0])
        elif 27000 < i <= 34800:
            h222_list.append([0, 0, 0, delay])
        elif 36000 < i <= 42000:
            h222_list.append([delay, 0, 0, 0])
        else:
            h222_list.append([0, 0, 0, 0])






        
        # switch34: packet drop rate (%)
        drop_rate = 3.5
        if att_rate > 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 2.4 < att_rate <= 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 2.1 < att_rate <= 2.4:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1.8 < att_rate <= 2.1:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1.5 < att_rate <= 1.8:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1.2 < att_rate <= 1.5:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1 <= att_rate <= 1.2:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 0.7 <= att_rate < 1:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 0.4 <= att_rate < 0.7:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        else:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        if drop_rate > 100:
            drop_rate = 100

        # switch34: flow table size
        max_size = 1000
        flow_table = 150
        if att_rate > 2.7:
            flow_table = max_size
        elif 2.4 < att_rate <= 2.7:
            flow_table = max_size
        elif 2.1 < att_rate <= 2.4:
            flow_table = max_size
        elif 1.8 < att_rate <= 2.1:
            flow_table = max_size
        elif 1.5 < att_rate <= 1.8:
            flow_table = max_size
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        if flow_table > max_size:
            flow_table = max_size
        sw34_list.append([drop_rate, flow_table])

        # switch31: packet drop rate (%)
        drop_rate = 2
        if att_rate > 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 2.4 < att_rate <= 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 2.1 < att_rate <= 2.4:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1.8 < att_rate <= 2.1:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1.5 < att_rate <= 1.8:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1.2 < att_rate <= 1.5:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1 <= att_rate <= 1.2:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 0.7 <= att_rate < 1:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 0.4 <= att_rate < 0.7:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        else:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        if drop_rate > 100:
            drop_rate = 100
            
        # switch31: flow table size
        max_size = 750
        flow_table = 90
        if att_rate > 2.7:
            flow_table = max_size 
        elif 2.4 < att_rate <= 2.7:
            flow_table = max_size 
        elif 2.1 < att_rate <= 2.4:
            flow_table = max_size 
        elif 1.8 < att_rate <= 2.1:
            flow_table = max_size 
        elif 1.5 < att_rate <= 1.8:
            flow_table = max_size 
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        if flow_table > max_size:
            flow_table = max_size
        sw31_list.append([drop_rate, flow_table])

        # switch32: packet drop rate (%)
        drop_rate = 2
        if att_rate > 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 2.4 < att_rate <= 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 2.1 < att_rate <= 2.4:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1.8 < att_rate <= 2.1:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1.5 < att_rate <= 1.8:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1.2 < att_rate <= 1.5:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1 <= att_rate <= 1.2:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 0.7 <= att_rate < 1:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 0.4 <= att_rate < 0.7:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        else:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        if drop_rate > 100:
            drop_rate = 100
            
        # switch32: flow table size
        max_size = 500
        flow_table = 90
        if att_rate > 2.7:
            flow_table = max_size
        elif 2.4 < att_rate <= 2.7:
            flow_table = max_size
        elif 2.1 < att_rate <= 2.4:
            flow_table = max_size
        elif 1.8 < att_rate <= 2.1:
            flow_table = max_size
        elif 1.5 < att_rate <= 1.8:
            flow_table = max_size
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        if flow_table > max_size:
            flow_table = max_size
        sw32_list.append([drop_rate, flow_table])

        # switch33: packet drop rate (%)
        drop_rate = 2
        if att_rate > 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 2.4 < att_rate <= 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 2.1 < att_rate <= 2.4:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1.8 < att_rate <= 2.1:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1.5 < att_rate <= 1.8:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1.2 < att_rate <= 1.5:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 1 <= att_rate <= 1.2:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 0.7 <= att_rate < 1:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        elif 0.4 <= att_rate < 0.7:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        else:
            drop_rate += att_rate * random.uniform(random.randrange(2, 3), random.randrange(4, 5))
        if drop_rate > 100:
            drop_rate = 100
            
        # switch33: flow table size
        max_size = 500
        flow_table = 90
        if att_rate > 2.7:
            flow_table = max_size
        elif 2.4 < att_rate <= 2.7:
            flow_table = max_size
        elif 2.1 < att_rate <= 2.4:
            flow_table = max_size
        elif 1.8 < att_rate <= 2.1:
            flow_table = max_size
        elif 1.5 < att_rate <= 1.8:
            flow_table = max_size
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        if flow_table > max_size:
            flow_table = max_size
        sw33_list.append([drop_rate, flow_table])

        # switch23: packet drop rate (%)
        drop_rate = 0.5
        if att_rate > 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 2.4 < att_rate <= 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 2.1 < att_rate <= 2.4:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.8 < att_rate <= 2.1:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.5 < att_rate <= 1.8:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.2 < att_rate <= 1.5:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1 <= att_rate <= 1.2:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 0.7 <= att_rate < 1:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 0.4 <= att_rate < 0.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        else:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        if drop_rate > 100:
            drop_rate = 100
            
        # switch23: flow table size
        max_size = 750
        flow_table = 40
        if att_rate > 2.7:
            flow_table = max_size
        elif 2.4 < att_rate <= 2.7:
            flow_table = max_size
        elif 2.1 < att_rate <= 2.4:
            flow_table = max_size
        elif 1.8 < att_rate <= 2.1:
            flow_table = max_size
        elif 1.5 < att_rate <= 1.8:
            flow_table = max_size
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        if flow_table > max_size:
            flow_table = max_size
        sw23_list.append([drop_rate, flow_table])

        # switch21: packet drop rate (%)
        drop_rate = 0.5
        if att_rate > 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 2.4 < att_rate <= 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 2.1 < att_rate <= 2.4:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.8 < att_rate <= 2.1:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.5 < att_rate <= 1.8:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.2 < att_rate <= 1.5:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1 <= att_rate <= 1.2:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 0.7 <= att_rate < 1:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 0.4 <= att_rate < 0.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        else:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        if drop_rate > 100:
            drop_rate = 100
            
        # switch21: flow table size
        max_size = 500
        flow_table = 40
        if att_rate > 2.7:
            flow_table = max_size
        elif 2.4 < att_rate <= 2.7:
            flow_table = max_size
        elif 2.1 < att_rate <= 2.4:
            flow_table = max_size
        elif 1.8 < att_rate <= 2.1:
            flow_table = max_size
        elif 1.5 < att_rate <= 1.8:
            flow_table = max_size
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        if flow_table > max_size:
            flow_table = max_size
        sw21_list.append([drop_rate, flow_table])

        # switch22: packet drop rate (%)
        drop_rate = 0.5
        if att_rate > 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 2.4 < att_rate <= 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 2.1 < att_rate <= 2.4:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.8 < att_rate <= 2.1:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.5 < att_rate <= 1.8:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.2 < att_rate <= 1.5:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1 <= att_rate <= 1.2:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 0.7 <= att_rate < 1:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 0.4 <= att_rate < 0.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        else:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        if drop_rate > 100:
            drop_rate = 100
            
        # switch22: flow table size
        max_size = 500
        flow_table = 40
        if att_rate > 2.7:
            flow_table = max_size
        elif 2.4 < att_rate <= 2.7:
            flow_table = max_size
        elif 2.1 < att_rate <= 2.4:
            flow_table = max_size
        elif 1.8 < att_rate <= 2.1:
            flow_table = max_size
        elif 1.5 < att_rate <= 1.8:
            flow_table = max_size
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        if flow_table > max_size:
            flow_table = max_size
        sw22_list.append([drop_rate, flow_table])

        # switch13: packet drop rate (%)
        drop_rate = 0.5
        if att_rate > 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 2.4 < att_rate <= 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 2.1 < att_rate <= 2.4:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.8 < att_rate <= 2.1:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.5 < att_rate <= 1.8:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.2 < att_rate <= 1.5:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1 <= att_rate <= 1.2:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 0.7 <= att_rate < 1:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 0.4 <= att_rate < 0.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        else:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        if drop_rate > 100:
            drop_rate = 100
            
        # switch13: flow table size
        max_size = 1000
        flow_table = 40
        if att_rate > 2.7:
            flow_table = max_size
        elif 2.4 < att_rate <= 2.7:
            flow_table = max_size
        elif 2.1 < att_rate <= 2.4:
            flow_table = max_size
        elif 1.8 < att_rate <= 2.1:
            flow_table = max_size
        elif 1.5 < att_rate <= 1.8:
            flow_table = max_size
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        if flow_table > max_size:
            flow_table = max_size
        sw13_list.append([drop_rate, flow_table])

        # switch11: packet drop rate (%)
        drop_rate = 0.5
        if att_rate > 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 2.4 < att_rate <= 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 2.1 < att_rate <= 2.4:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.8 < att_rate <= 2.1:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.5 < att_rate <= 1.8:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.2 < att_rate <= 1.5:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1 <= att_rate <= 1.2:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 0.7 <= att_rate < 1:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 0.4 <= att_rate < 0.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        else:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        if drop_rate > 100:
            drop_rate = 100
            
        # switch11: flow table size
        max_size = 750
        flow_table = 40
        if att_rate > 2.7:
            flow_table = max_size
        elif 2.4 < att_rate <= 2.7:
            flow_table = max_size
        elif 2.1 < att_rate <= 2.4:
            flow_table = max_size
        elif 1.8 < att_rate <= 2.1:
            flow_table = max_size
        elif 1.5 < att_rate <= 1.8:
            flow_table = max_size
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        if flow_table > max_size:
            flow_table = max_size
        sw11_list.append([drop_rate, flow_table])

        # switch12: packet drop rate (%)
        drop_rate = 0.5
        if att_rate > 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 2.4 < att_rate <= 2.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 2.1 < att_rate <= 2.4:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.8 < att_rate <= 2.1:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.5 < att_rate <= 1.8:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1.2 < att_rate <= 1.5:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 1 <= att_rate <= 1.2:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 0.7 <= att_rate < 1:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        elif 0.4 <= att_rate < 0.7:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        else:
            drop_rate += att_rate * random.uniform(random.randrange(1, 2), random.randrange(3, 4))
        if drop_rate > 100:
            drop_rate = 100
            
        # switch12: flow table size
        max_size = 500
        flow_table = 40
        if att_rate > 2.7:
            flow_table = max_size
        elif 2.4 < att_rate <= 2.7:
            flow_table = max_size
        elif 2.1 < att_rate <= 2.4:
            flow_table = max_size
        elif 1.8 < att_rate <= 2.1:
            flow_table = max_size
        elif 1.5 < att_rate <= 1.8:
            flow_table = max_size
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(round(max_size/1.4), round(max_size/1.33)), random.randrange(round(max_size/1.33), round(max_size/1.25))))
        if flow_table > max_size:
            flow_table = max_size
        sw12_list.append([drop_rate, flow_table])





        # link s13-s34: bandwidth utilization (%) - 1 attacker
        # bw = random.randrange(13, 20) + random.uniform(0.1, 0.3)
        bw = random.randrange(0, 2)
        if att_rate > 2.7:
            bw += random.uniform(0.1, 0.9) + random.randrange(19, 22)
        elif 2.4 < att_rate <= 2.7:
            bw += random.uniform(0.1, 0.9) + random.randrange(17, 20)
        elif 2.1 < att_rate <= 2.4:
            bw += random.uniform(0.1, 0.9) + random.randrange(15, 18)
        elif 1.8 < att_rate <= 2.1:
            bw += random.uniform(0.1, 0.9) + random.randrange(13, 16)
        elif 1.5 < att_rate <= 1.8:
            bw += random.uniform(0.1, 0.9) + random.randrange(11, 14)
        elif 1.2 < att_rate <= 1.5:
            bw += random.uniform(0.1, 0.9) + random.randrange(9, 12)
        elif 1 <= att_rate <= 1.2:
            bw += random.uniform(0.1, 0.9) + random.randrange(7, 10)
        elif 0.7 <= att_rate < 1:
            bw += random.uniform(0.1, 0.9) + random.randrange(5, 8)
        elif 0.4 <= att_rate < 0.7:
            bw += random.uniform(0.1, 0.9) + random.randrange(3, 6)
        else:
            bw += random.uniform(0.1, 0.9) + random.randrange(1, 4)
        if bw > 100:
            bw = 100
        s13s34_list.append(bw)

        # link s23-s34: bandwidth utilization (%) - 2 attackers
        # bw = random.randrange(14, 21) + random.uniform(0.1, 0.3)
        bw = random.randrange(3, 5)
        if att_rate > 2.7:
            bw += random.uniform(0.1, 0.9) + random.randrange(25, 28)
        elif 2.4 < att_rate <= 2.7:
            bw += random.uniform(0.1, 0.9) + random.randrange(23, 26)
        elif 2.1 < att_rate <= 2.4:
            bw += random.uniform(0.1, 0.9) + random.randrange(21, 24)
        elif 1.8 < att_rate <= 2.1:
            bw += random.uniform(0.1, 0.3) + random.randrange(19, 22)
        elif 1.5 < att_rate <= 1.8:
            bw += random.uniform(0.1, 0.3) + random.randrange(17, 20)
        elif 1.2 < att_rate <= 1.5:
            bw += random.uniform(0.1, 0.3) + random.randrange(15, 18)
        elif 1 <= att_rate <= 1.2:
            bw += random.uniform(0.1, 0.3) + random.randrange(13, 16)
        elif 0.7 <= att_rate < 1:
            bw += random.uniform(0.1, 0.3) + random.randrange(11, 14)
        elif 0.4 <= att_rate < 0.7:
            bw += random.uniform(0.1, 0.3) + random.randrange(9, 12)
        else:
            bw += random.uniform(0.1, 0.3) + random.randrange(7, 10)
        if bw > 100:
            bw = 100
        s23s34_list.append(bw)







        # server31-1: no. of waiting frames
        waiting = [0, 1, 2]
        weights = []
        if att_rate >= 2.7:
            weights = [0.95, 0.05, 0]
        elif 2.3 <= att_rate < 2.7:
            weights = [0.9, 0.07, 0.03]
        elif 1.8 <= att_rate < 2.3:
            weights = [0.8, 0.15, 0.05]
        elif 1.3 <= att_rate < 1.8:
            weights = [0.69, 0.2, 0.11]
        elif 0.8 <= att_rate < 1.3:
            weights = [0.56, 0.29, 0.15]
        elif 0.3 <= att_rate < 0.8:
            weights = [0.55, 0.3, 0.15]
        else:
            weights = [0.4, 0.4, 0.2]    
        sv311_list.append(random.choices(waiting, weights, k = 1)[0])

        # server31-2: no. of waiting frames
        waiting = [0, 1, 2]
        weights = []
        if att_rate >= 2.7:
            weights = [0.95, 0.05, 0]
        elif 2.3 <= att_rate < 2.7:
            weights = [0.9, 0.07, 0.03]
        elif 1.8 <= att_rate < 2.3:
            weights = [0.8, 0.15, 0.05]
        elif 1.3 <= att_rate < 1.8:
            weights = [0.69, 0.2, 0.11]
        elif 0.8 <= att_rate < 1.3:
            weights = [0.56, 0.29, 0.15]
        elif 0.3 <= att_rate < 0.8:
            weights = [0.55, 0.3, 0.15]
        else:
            weights = [0.4, 0.4, 0.2]          
        sv312_list.append(random.choices(waiting, weights, k = 1)[0])

        # server32-2: no. of waiting frames
        waiting = [0, 1, 2]
        weights = []
        if att_rate >= 2.7:
            weights = [0.95, 0.05, 0]
        elif 2.3 <= att_rate < 2.7:
            weights = [0.9, 0.07, 0.03]
        elif 1.8 <= att_rate < 2.3:
            weights = [0.8, 0.15, 0.05]
        elif 1.3 <= att_rate < 1.8:
            weights = [0.69, 0.2, 0.11]
        elif 0.8 <= att_rate < 1.3:
            weights = [0.56, 0.29, 0.15]
        elif 0.3 <= att_rate < 0.8:
            weights = [0.55, 0.3, 0.15]
        else:
            weights = [0.4, 0.4, 0.2]          
        sv322_list.append(random.choices(waiting, weights, k = 1)[0])

        # server33-1: no. of waiting frames
        waiting = [0, 1, 2]
        weights = []
        if att_rate >= 2.7:
            weights = [0.95, 0.05, 0]
        elif 2.3 <= att_rate < 2.7:
            weights = [0.9, 0.07, 0.03]
        elif 1.8 <= att_rate < 2.3:
            weights = [0.8, 0.15, 0.05]
        elif 1.3 <= att_rate < 1.8:
            weights = [0.69, 0.2, 0.11]
        elif 0.8 <= att_rate < 1.3:
            weights = [0.56, 0.29, 0.15]
        elif 0.3 <= att_rate < 0.8:
            weights = [0.55, 0.3, 0.15]
        else:
            weights = [0.4, 0.4, 0.2]          
        sv331_list.append(random.choices(waiting, weights, k = 1)[0])







    
    output_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Matlab/Edge/')
    mega_output = output_dir + 'mega_output.csv'
    mega_plot_output = output_dir + 'mega_plot_output.csv'
    
    mega_df = pd.DataFrame(mega_list)
    mega_df.columns = ['1. Timeline (s)', '2. Attacker1 rate', '3. Attacker2 rate', '4. Attacker3 rate']

    h112_df = pd.DataFrame(h112_list)
    h112_df.columns = ['5. h112 to sv311', '6. h112 to sv312', '7. h112 to sv322', '8. h112 to sv331']

    h121_df = pd.DataFrame(h121_list)
    h121_df.columns = ['9. h121 to sv311', '10. h121 to sv312', '11. h121 to sv322', '12. h121 to sv331']

    h122_df = pd.DataFrame(h122_list)
    h122_df.columns = ['13. h122 to sv311', '14. h122 to sv312', '15. h122 to sv322', '16. h122 to sv331']

    h212_df = pd.DataFrame(h212_list)
    h212_df.columns = ['17. h212 to sv311', '18. h212 to sv312', '19. h212 to sv322', '20. h212 to sv331']

    h221_df = pd.DataFrame(h221_list)
    h221_df.columns = ['21. h221 to sv311', '22. h221 to sv312', '23. h221 to sv322', '24. h221 to sv331']

    h222_df = pd.DataFrame(h222_list)
    h222_df.columns = ['25. h222 to sv311', '26. h222 to sv312', '27. h222 to sv322', '28. h222 to sv331']

    sw34_df = pd.DataFrame(sw34_list)
    sw34_df.columns = ['29. sw34 packet drop rate', '30. sw34 flow table size']

    sw31_df = pd.DataFrame(sw31_list)
    sw31_df.columns = ['31. sw31 packet drop rate', '32. sw31 flow table size']

    sw32_df = pd.DataFrame(sw32_list)
    sw32_df.columns = ['33. sw32 packet drop rate', '34. sw32 flow table size']

    sw33_df = pd.DataFrame(sw33_list)
    sw33_df.columns = ['35. sw33 packet drop rate', '36. sw33 flow table size']

    sw23_df = pd.DataFrame(sw23_list)
    sw23_df.columns = ['37. sw23 packet drop rate', '38. sw23 flow table size']

    sw21_df = pd.DataFrame(sw21_list)
    sw21_df.columns = ['39. sw21 packet drop rate', '40. sw21 flow table size']

    sw22_df = pd.DataFrame(sw22_list)
    sw22_df.columns = ['41. sw22 packet drop rate', '42. sw22 flow table size']

    sw13_df = pd.DataFrame(sw13_list)
    sw13_df.columns = ['43. sw13 packet drop rate', '44. sw13 flow table size']

    sw11_df = pd.DataFrame(sw11_list)
    sw11_df.columns = ['45. sw11 packet drop rate', '46. sw11 flow table size']

    sw12_df = pd.DataFrame(sw12_list)
    sw12_df.columns = ['47. sw12 packet drop rate', '48. sw12 flow table size']

    s13s34_df = pd.DataFrame(s13s34_list)
    s13s34_df.columns = ['49. sw13sw34 bw utilization']
    
    s23s34_df = pd.DataFrame(s23s34_list)
    s23s34_df.columns = ['50. sw23sw34 bw utilization']

    sv311_df = pd.DataFrame(sv311_list)
    sv311_df.columns = ['51. sv311 no. of waiting frames']

    sv312_df = pd.DataFrame(sv312_list)
    sv312_df.columns = ['52. sv312 no. of waiting frames']

    sv322_df = pd.DataFrame(sv322_list)
    sv322_df.columns = ['53. sv322 no. of waiting frames']

    sv331_df = pd.DataFrame(sv331_list)
    sv331_df.columns = ['54. sv331 no. of waiting frames']




    # sv311, sv312, sv322, sv331
    a111_sdf = pd.DataFrame(a111_slist)
    a111_sdf.columns = ['55. a111 to sv311', '56. a111 to sv312', '57. a111 to sv322', '58. a111 to sv331']

    a211_sdf = pd.DataFrame(a211_slist)
    a211_sdf.columns = ['59. a211 to sv311', '60. a211 to sv312', '61. a211 to sv322', '62. a211 to sv331']

    a221_sdf = pd.DataFrame(a221_slist)
    a221_sdf.columns = ['63. a221 to sv311', '64. a221 to sv312', '65. a221 to sv322', '66. a221 to sv331'] 

    a111_pdf = pd.DataFrame(a111_plist)
    a111_pdf.columns = ['67. a111 to a211', '68. a111 to a221']

    a211_pdf = pd.DataFrame(a211_plist)
    a211_pdf.columns = ['69. a211 to a111', '70. a211 to a221']

    a221_pdf = pd.DataFrame(a221_plist)
    a221_pdf.columns = ['71. a221 to a111', '72. a221 to a211']

    mega_df = pd.concat([mega_df, h112_df, h121_df, h122_df, h212_df, h221_df, h222_df, sw34_df, sw31_df, sw32_df, sw33_df, sw23_df, sw21_df, sw22_df, sw13_df, sw11_df, sw12_df, s13s34_df, s23s34_df, sv311_df, sv312_df, sv322_df, sv331_df, a111_sdf, a211_sdf, a221_sdf, a111_pdf, a211_pdf, a221_pdf], axis = 1)
    mega_df.to_csv(mega_output, mode = 'w', header = True, index = False)



    # Plot
    mega_plot_arr = [np.array(mega_list).T[0][0:-1:step], np.array(mega_list).T[1][0:-1:step], np.array(mega_list).T[2][0:-1:step], np.array(mega_list[3]).T[0:-1:step]]
    a111_plot_sarr = [np.array(a111_slist).T[0][0:-1:step], np.array(a111_slist).T[1][0:-1:step], np.array(a111_slist).T[2][0:-1:step], np.array(a111_slist[3]).T[0:-1:step]]
    a211_plot_sarr = [np.array(a211_slist).T[0][0:-1:step], np.array(a211_slist).T[1][0:-1:step], np.array(a211_slist).T[2][0:-1:step], np.array(a211_slist[3]).T[0:-1:step]]
    a221_plot_sarr = [np.array(a221_slist).T[0][0:-1:step], np.array(a221_slist).T[1][0:-1:step], np.array(a221_slist).T[2][0:-1:step], np.array(a221_slist[3]).T[0:-1:step]]
    a111_plot_parr = [np.array(a111_plist).T[0][0:-1:step], np.array(a111_plist).T[1][0:-1:step]]
    a211_plot_parr = [np.array(a211_plist).T[0][0:-1:step], np.array(a211_plist).T[1][0:-1:step]]
    a221_plot_parr = [np.array(a221_plist).T[0][0:-1:step], np.array(a221_plist).T[1][0:-1:step]]

    sw34_plot_list = [np.array(sw34_list).T[0][0:-1:step], np.array(sw34_list).T[1][0:-1:step]]
    sw31_plot_list = [np.array(sw31_list).T[0][0:-1:step], np.array(sw31_list).T[1][0:-1:step]]
    sw32_plot_list = [np.array(sw32_list).T[0][0:-1:step], np.array(sw32_list).T[1][0:-1:step]]
    sw33_plot_list = [np.array(sw33_list).T[0][0:-1:step], np.array(sw33_list).T[1][0:-1:step]]

    sw23_plot_list = [np.array(sw23_list).T[0][0:-1:step], np.array(sw23_list).T[1][0:-1:step]]
    sw21_plot_list = [np.array(sw21_list).T[0][0:-1:step], np.array(sw21_list).T[1][0:-1:step]]
    sw22_plot_list = [np.array(sw22_list).T[0][0:-1:step], np.array(sw22_list).T[1][0:-1:step]]
    
    sw13_plot_list = [np.array(sw13_list).T[0][0:-1:step], np.array(sw13_list).T[1][0:-1:step]]
    sw11_plot_list = [np.array(sw11_list).T[0][0:-1:step], np.array(sw11_list).T[1][0:-1:step]]
    sw12_plot_list = [np.array(sw12_list).T[0][0:-1:step], np.array(sw12_list).T[1][0:-1:step]]
    

    sw34_plot_df = pd.DataFrame(sw34_plot_list).T
    sw34_plot_df.columns = ['29. sw34 packet drop rate', '30. sw34 flow table size']

    sw31_plot_df = pd.DataFrame(sw31_plot_list).T
    sw31_plot_df.columns = ['31. sw31 packet drop rate', '32. sw31 flow table size']

    sw32_plot_df = pd.DataFrame(sw32_plot_list).T
    sw32_plot_df.columns = ['33. sw32 packet drop rate', '34. sw32 flow table size']

    sw33_plot_df = pd.DataFrame(sw33_plot_list).T
    sw33_plot_df.columns = ['35. sw33 packet drop rate', '36. sw33 flow table size']

    sw23_plot_df = pd.DataFrame(sw23_plot_list).T
    sw23_plot_df.columns = ['37. sw23 packet drop rate', '38. sw23 flow table size']

    sw21_plot_df = pd.DataFrame(sw21_plot_list).T
    sw21_plot_df.columns = ['39. sw21 packet drop rate', '40. sw21 flow table size']

    sw22_plot_df = pd.DataFrame(sw22_plot_list).T
    sw22_plot_df.columns = ['41. sw22 packet drop rate', '42. sw22 flow table size']

    sw13_plot_df = pd.DataFrame(sw13_plot_list).T
    sw13_plot_df.columns = ['43. sw13 packet drop rate', '44. sw13 flow table size']

    sw11_plot_df = pd.DataFrame(sw11_plot_list).T
    sw11_plot_df.columns = ['45. sw11 packet drop rate', '46. sw11 flow table size']

    sw12_plot_df = pd.DataFrame(sw12_plot_list).T
    sw12_plot_df.columns = ['47. sw12 packet drop rate', '48. sw12 flow table size']


    mega_plot_df = pd.DataFrame(mega_plot_arr).T
    mega_plot_df.columns = ['1. Timeline (s)', '2. Attacker1 rate', '3. Attacker2 rate', '4. Attacker3 rate']
    
    a111_plot_sdf = pd.DataFrame(a111_plot_sarr).T
    a111_plot_sdf.columns = ['55. a111 to sv311', '56. a111 to sv312', '57. a111 to sv322', '58. a111 to sv331']

    a211_plot_sdf = pd.DataFrame(a211_plot_sarr).T
    a211_plot_sdf.columns = ['59. a211 to sv311', '60. a211 to sv312', '61. a211 to sv322', '62. a211 to sv331']

    a221_plot_sdf = pd.DataFrame(a221_plot_sarr).T
    a221_plot_sdf.columns = ['63. a221 to sv311', '64. a221 to sv312', '65. a221 to sv322', '66. a221 to sv331'] 

    a111_plot_pdf = pd.DataFrame(a111_plot_parr).T
    a111_plot_pdf.columns = ['67. a111 to a211', '68. a111 to a221']

    a211_plot_pdf = pd.DataFrame(a211_plot_parr).T
    a211_plot_pdf.columns = ['69. a211 to a111', '70. a211 to a221']

    a221_plot_pdf = pd.DataFrame(a221_plot_parr).T
    a221_plot_pdf.columns = ['71. a221 to a111', '72. a221 to a211']

    mega_plot_df = pd.concat([mega_plot_df, sw34_plot_df, sw33_plot_df, sw32_plot_df, sw31_plot_df, sw23_plot_df, sw21_plot_df, sw22_plot_df, sw13_plot_df, sw11_plot_df, sw12_plot_df, a111_plot_sdf, a211_plot_sdf, a221_plot_sdf, a111_plot_pdf, a211_plot_pdf, a221_plot_pdf], axis = 1)
    mega_plot_df.to_csv(mega_plot_output, mode = 'w', header = True, index = False)

if __name__ == "__main__":
    data_gen()