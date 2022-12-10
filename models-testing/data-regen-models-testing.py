import random
import numpy as np
import pandas as pd
import os
import time
from sklearn import preprocessing
from keras.models import load_model

curr_dir = os.path.dirname(__file__)
output_dir = os.path.join(curr_dir, '..', '..', '..', 'Matlab/Edge/')
step = 200
model = load_model(curr_dir + '/models/model1.h5')
# means_arr = np.load(curr_dir + "/npy/means.npy")
# stds_arr = np.load(curr_dir + "/npy/stds.npy")

def data_gen_test():
    # timeline_list = []
    mega_net_state_arr = np.array([])
    net_state_arr = np.array([])
    pred_drop_rate_arr = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    attack_state_list = [[0, 0, 0]]

    a111_slist = []; a211_slist = []; a221_slist = []
    a111_plist = []; a211_plist = []; a221_plist = []
    a111_s311_total = 0; a111_s312_total = 0; a111_s322_total = 0; a111_s331_total = 0
    a211_s311_total = 0; a211_s312_total = 0; a211_s322_total = 0; a211_s331_total = 0
    a221_s311_total = 0; a221_s312_total = 0; a221_s322_total = 0; a221_s331_total = 0
    a111_a211_total = 0; a111_a221_total = 0
    a211_a111_total = 0; a211_a221_total = 0
    a221_a111_total = 0; a221_a211_total = 0

    h112_list = []; h121_list = []; h122_list = []
    h212_list = []; h221_list = []; h222_list = []
    h112_total = 0; h121_total = 0; h122_total = 0
    h212_total = 0; h221_total = 0; h222_total = 0

    sw34_dr_list = []; sw31_dr_list = []; sw32_dr_list = []; sw33_dr_list = []
    sw23_dr_list = []; sw21_dr_list = []; sw22_dr_list = []
    sw13_dr_list = []; sw11_dr_list = []; sw12_dr_list = []
    sw34_dr_total = 0; sw31_dr_total = 0; sw32_dr_total = 0; sw33_dr_total = 0
    sw23_dr_total = 0; sw21_dr_total = 0; sw22_dr_total = 0
    sw13_dr_total = 0; sw11_dr_total = 0; sw12_dr_total = 0

    sw34_fb_list = []; sw31_fb_list = []; sw32_fb_list = []; sw33_fb_list = []
    sw23_fb_list = []; sw21_fb_list = []; sw22_fb_list = []
    sw13_fb_list = []; sw11_fb_list = []; sw12_fb_list = []
    sw34_fb_total = 0; sw31_fb_total = 0; sw32_fb_total = 0; sw33_fb_total = 0
    sw23_fb_total = 0; sw21_fb_total = 0; sw22_fb_total = 0
    sw13_fb_total = 0; sw11_fb_total = 0; sw12_fb_total = 0

    s13s34_list = []; s13s34_total = 0   # 1 attacker
    s23s34_list = []; s23s34_total = 0   # 2 attackers
    sv311_list = []; sv312_list = []; sv322_list = []; sv331_list = []
    sv311_total = 0; sv312_total = 0; sv322_total = 0; sv331_total = 0


    a111_mod_slist = []; a211_mod_slist = []; a221_mod_slist = []
    a111_mod_plist = []; a211_mod_plist = []; a221_mod_plist = []
    a111_s311_mod_total = 0; a111_s312_mod_total = 0; a111_s322_mod_total = 0; a111_s331_mod_total = 0
    a211_s311_mod_total = 0; a211_s312_mod_total = 0; a211_s322_mod_total = 0; a211_s331_mod_total = 0
    a221_s311_mod_total = 0; a221_s312_mod_total = 0; a221_s322_mod_total = 0; a221_s331_mod_total = 0
    a111_a211_mod_total = 0; a111_a221_mod_total = 0
    a211_a111_mod_total = 0; a211_a221_mod_total = 0
    a221_a111_mod_total = 0; a221_a211_mod_total = 0

    h112_mod_list = []; h121_mod_list = []; h122_mod_list = []
    h212_mod_list = []; h221_mod_list = []; h222_mod_list = []
    h112_mod_total = 0; h121_mod_total = 0; h122_mod_total = 0
    h212_mod_total = 0; h221_mod_total = 0; h222_mod_total = 0

    sw34_dr_mod_list = []; sw31_dr_mod_list = []; sw32_dr_mod_list = []; sw33_dr_mod_list = []
    sw23_dr_mod_list = []; sw21_dr_mod_list = []; sw22_dr_mod_list = []
    sw13_dr_mod_list = []; sw11_dr_mod_list = []; sw12_dr_mod_list = []
    sw34_dr_mod_total = 0; sw31_dr_mod_total = 0; sw32_dr_mod_total = 0; sw33_dr_mod_total = 0
    sw23_dr_mod_total = 0; sw21_dr_mod_total = 0; sw22_dr_mod_total = 0
    sw13_dr_mod_total = 0; sw11_dr_mod_total = 0; sw12_dr_mod_total = 0

    att_rate_list = [0, 0, 0]
    att_rate = 0
    for i in range(47400):
        # attackers to server [server31-1, server31-2, server32-2, server33-1]
        a111_s311 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_s311_total += a111_s311
        a111_s312 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_s312_total += a111_s312
        a111_s322 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_s322_total += a111_s322
        a111_s331 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_s331_total += a111_s331

        a211_s311 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_s311_total += a211_s311
        a211_s312 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_s312_total += a211_s312
        a211_s322 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_s322_total += a211_s322
        a211_s331 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_s331_total += a211_s331

        a221_s311 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a221_s311_total += a221_s311
        a221_s312 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a221_s312_total += a221_s312
        a221_s322 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a221_s322_total += a221_s322
        a221_s331 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a221_s331_total += a221_s331

        a111_a211 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_a221 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_a221 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))

        a111_a211_total += a111_a211; a111_a221_total += a111_a221
        a211_a111_total += a111_a211; a211_a221_total += a211_a221
        a221_a111_total += a111_a221; a221_a211_total += a211_a221

        if i%step == 0:
            a111_slist = [[a111_s311_total/step, a111_s312_total/step, a111_s322_total/step, a111_s331_total/step]]
            a211_slist = [[a211_s311_total/step, a211_s312_total/step, a211_s322_total/step, a211_s331_total/step]]
            a221_slist = [[a221_s311_total/step, a221_s312_total/step, a221_s322_total/step, a221_s331_total/step]]
            a111_plist = [[a111_a211_total/step, a111_a221_total/step]]
            a211_plist = [[a111_a211_total/step, a211_a221_total/step]]
            a221_plist = [[a111_a221_total/step, a211_a221_total/step]]
            a111_s311_total = 0; a111_s312_total = 0; a111_s322_total = 0; a111_s331_total = 0
            a211_s311_total = 0; a211_s312_total = 0; a211_s322_total = 0; a211_s331_total = 0
            a221_s311_total = 0; a221_s312_total = 0; a221_s322_total = 0; a221_s331_total = 0
            a111_a211_total = 0; a111_a221_total = 0
            a211_a111_total = 0; a211_a221_total = 0
            a221_a111_total = 0; a221_a211_total = 0

        # host11-2: time diff between two successive frames (ms)
        delay = 0
        if 6000 < i <= 8400 or 12600 < i <= 16200 or 17400 < i <= 24000 or 28200 < i <= 34800 or 36600 < i <= 43800:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif i <= 6000 or 10200 < i <= 12600 or 16800 < i <= 17400 or 24000 < i <= 25200 or 34800 < i <= 36000 or 36000 < i <= 36600:
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
        h112_total += delay

        # [server31-1, server31-2, server32-2, server33-1]
        if i%step == 0:
            if i <= 8400:
                h112_list = [[h112_total/step, 0, 0, 0]]
            elif 16800 < i <= 25200 or 36000 < i <= 43800:
                h112_list = [[0, h112_total/step, 0, 0]]
            elif 10200 < i <= 16200 or 28200 < i <= 36000:
                h112_list = [[0, 0, h112_total/step, 0]]
            else:
                h112_list = [[0, 0, 0, 0]]
            h112_total = 0

        # host12-1: time diff between two successive frames (ms)
        delay = 0
        if i <= 9000 or 16200 < i <= 18600 or 24000 < i <= 28200 or 31800 < i <= 36000:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif 12000 < i <= 16200 or 18600 < i <= 21000 or 22200 < i <= 24000 or 30600 < i <= 31800 or 36000 < i <= 36600:
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
        h121_total += delay

        # [server31-1, server31-2, server32-2, server33-1]
        if i%step == 0:
            if 12000 < i <= 21000 or 38400 < i <= 47400:
                h121_list = [[h121_total/step, 0, 0, 0]]
            elif i <= 9000 or 30600 < i <= 36600:
                h121_list = [[0, h121_total/step, 0, 0]]
            elif 22200 < i <= 28200:
                h121_list = [[0, 0, h121_total/step, 0]]
            else:
                h121_list = [[0, 0, 0, 0]]
            h121_total = 0

        # host12-2: time diff between two successive frames (ms)
        delay = 0
        if i <= 7800 or 10200 < i <= 16800 or 22200 < i <= 27000 or 32400 < i <= 35400 or 36000 < i <= 38400:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif 16800 < i <= 17400 or 19800 < i <= 22200 or 27000 < i <= 28800 or 28800 < i <= 32400 or 38400 < i <= 42000:
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
        h122_total += delay
        
        # [server31-1, server31-2, server32-2, server33-1]
        if i%step == 0:
            if 28800 < i <= 35400 or 36000 < i <= 42000:
                h122_list = [[h122_total/step, 0, 0, 0]]
            elif 10200 < i <= 17400:
                h122_list = [[0, h122_total/step, 0, 0]]
            elif i <= 7800:
                h122_list = [[0, 0, h122_total/step, 0]]
            elif 19800 < i <= 28800:
                h122_list = [[0, 0, 0, h122_total/step]]
            else:
                h122_list = [[0, 0, 0, 0]]
            h122_total = 0

        # host21-2: time diff between two successive frames (ms)
        delay = 0
        if 6600 < i <= 7200 or 12000 < i <= 16200 or 16200 < i <= 22200 or 25200 < i <= 30600 or 35400 < i <= 36600:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif i <= 6600 or 8400 < i <= 12000 or 22200 < i <= 24000 or 24600 < i <= 25200 or 30600 < i <= 31800 or 34800 < i <= 35400 or 36600 < i <= 41400:
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
        h212_total += delay

        # [server31-1, server31-2, server32-2, server33-1]
        if i%step == 0:
            if 8400 < i <= 16200:
                h212_list = [[h212_total/step, 0, 0, 0]]
            elif 24600 < i <= 31800:
                h212_list = [[0, h212_total/step, 0, 0]]
            elif 16200 < i <= 24000:
                h212_list = [[0, 0, h212_total/step, 0]]
            elif i <= 7200 or 34800 < i <= 41400:
                h212_list = [[0, 0, 0, h212_total/step]]
            else:
                h212_list = [[0, 0, 0, 0]]
            h212_total = 0

        # host22-1: time diff between two successive frames (ms)
        delay = 0
        if 7200 < i <= 14400 or 21000 < i <= 23400 or 28800 < i <= 34800 or 41400 < i <= 43800:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif i < 6600 or 14400 < i <= 15600 or 18600 < i <= 21000 or 23400 < i <= 25200 or 27000 < i <= 28800 or 34800 < i <= 35400 or 36600 < i <= 41400:
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
        h221_total += delay

        # [server31-1, server31-2, server32-2, server33-1]
        if i%step == 0:
            if 18600 < i <= 25200:
                h221_list = [[h221_total/step, 0, 0, 0]]
            elif i <= 6600 or 7200 < i <= 15600 or 27000 < i <= 35400 or 36600 < i <= 43800:
                h221_list = [[0, 0, 0, h221_total/step]]
            else:
                h221_list = [[0, 0, 0, 0]]
            h221_total = 0

        # host22-2: time diff between two successive frames (ms)
        delay = 0
        if 7800 < i <= 10200 or 15600 < i <= 19800 or 25200 < i <= 28800 or 36000 < i <= 43200:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif i < 6000 or 6000 < i <= 7800 or 10200 < i <= 12600 or 14400 < i <= 15600 or 19800 < i <= 22200 or 23400 < i <= 25200 or 28800 < i <= 32400 or 34800 < i <= 36000:
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
        h222_total += delay

        # [server31-1, server31-2, server32-2, server33-1]
        if i%step == 0:
            if i <= 6000 or 23400 < i <= 32400:
                h222_list = [[h222_total/step, 0, 0, 0]]
            elif 6000 < i <= 12600 or 34800 < i <= 43200:
                h222_list = [[0, 0, h222_total/step, 0]]
            elif 14400 < i <= 22200:
                h222_list = [[0, 0, 0, h222_total/step]]
            else:
                h222_list = [[0, 0, 0, 0]]
            h222_total = 0






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
        sw34_dr_total += drop_rate
        if i%step == 0:
            sw34_dr_list = [sw34_dr_total/step]
            sw34_dr_total = 0

        # switch34: flow table size
        flow_table = 150
        if att_rate > 2.7:
            flow_table = 1000
        elif 2.4 < att_rate <= 2.7:
            flow_table = 1000
        elif 2.1 < att_rate <= 2.4:
            flow_table = 1000
        elif 1.8 < att_rate <= 2.1:
            flow_table = 1000
        elif 1.5 < att_rate <= 1.8:
            flow_table = 1000
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        if flow_table > 1000:
            flow_table = 1000
        sw34_fb_total += flow_table
        if i%step == 0:
            sw34_fb_list = [sw34_fb_total/step]
            sw34_fb_total = 0

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
        sw31_dr_total += drop_rate
        if i%step == 0:
            sw31_dr_list = [sw31_dr_total/step]
            sw31_dr_total = 0
            
        # switch31: flow table size
        flow_table = 90
        if att_rate > 2.7:
            flow_table = 1000
        elif 2.4 < att_rate <= 2.7:
            flow_table = 1000
        elif 2.1 < att_rate <= 2.4:
            flow_table = 1000
        elif 1.8 < att_rate <= 2.1:
            flow_table = 1000
        elif 1.5 < att_rate <= 1.8:
            flow_table = 1000
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        if flow_table > 1000:
            flow_table = 1000
        sw31_fb_total += flow_table
        if i%step == 0:
            sw31_fb_list = [sw31_fb_total/step]
            sw31_fb_total = 0

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
        sw32_dr_total += drop_rate
        if i%step == 0:
            sw32_dr_list = [sw32_dr_total/step]
            sw32_dr_total = 0
            
        # switch32: flow table size
        flow_table = 90
        if att_rate > 2.7:
            flow_table = 1000
        elif 2.4 < att_rate <= 2.7:
            flow_table = 1000
        elif 2.1 < att_rate <= 2.4:
            flow_table = 1000
        elif 1.8 < att_rate <= 2.1:
            flow_table = 1000
        elif 1.5 < att_rate <= 1.8:
            flow_table = 1000
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        if flow_table > 1000:
            flow_table = 1000
        sw32_fb_total += flow_table
        if i%step == 0:
            sw32_fb_list = [sw32_fb_total/step]
            sw32_fb_total = 0

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
        sw33_dr_total += drop_rate
        if i%step == 0:
            sw33_dr_list = [sw33_dr_total/step]
            sw33_dr_total = 0
            
        # switch33: flow table size
        flow_table = 90
        if att_rate > 2.7:
            flow_table = 1000
        elif 2.4 < att_rate <= 2.7:
            flow_table = 1000
        elif 2.1 < att_rate <= 2.4:
            flow_table = 1000
        elif 1.8 < att_rate <= 2.1:
            flow_table = 1000
        elif 1.5 < att_rate <= 1.8:
            flow_table = 1000
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        if flow_table > 1000:
            flow_table = 1000
        sw33_fb_total += flow_table
        if i%step == 0:
            sw33_fb_list = [sw33_fb_total/step]
            sw33_fb_total = 0

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
        sw23_dr_total += drop_rate
        if i%step == 0:
            sw23_dr_list = [sw23_dr_total/step]
            sw23_dr_total = 0
            
        # switch23: flow table size
        flow_table = 40
        if att_rate > 2.7:
            flow_table = 1000
        elif 2.4 < att_rate <= 2.7:
            flow_table = 1000
        elif 2.1 < att_rate <= 2.4:
            flow_table = 1000
        elif 1.8 < att_rate <= 2.1:
            flow_table = 1000
        elif 1.5 < att_rate <= 1.8:
            flow_table = 1000
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        if flow_table > 1000:
            flow_table = 1000
        sw23_fb_total += flow_table
        if i%step == 0:
            sw23_fb_list = [sw23_fb_total/step]
            sw23_fb_total = 0

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
        sw21_dr_total += drop_rate
        if i%step == 0:
            sw21_dr_list = [sw21_dr_total/step]
            sw21_dr_total = 0
            
        # switch21: flow table size
        flow_table = 40
        if att_rate > 2.7:
            flow_table = 1000
        elif 2.4 < att_rate <= 2.7:
            flow_table = 1000
        elif 2.1 < att_rate <= 2.4:
            flow_table = 1000
        elif 1.8 < att_rate <= 2.1:
            flow_table = 1000
        elif 1.5 < att_rate <= 1.8:
            flow_table = 1000
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        if flow_table > 1000:
            flow_table = 1000
        sw21_fb_total += flow_table
        if i%step == 0:
            sw21_fb_list = [sw21_fb_total/step]
            sw21_fb_total = 0

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
        sw22_dr_total += drop_rate
        if i%step == 0:
            sw22_dr_list = [sw22_dr_total/step]
            sw22_dr_total = 0
            
        # switch22: flow table size
        flow_table = 40
        if att_rate > 2.7:
            flow_table = 1000
        elif 2.4 < att_rate <= 2.7:
            flow_table = 1000
        elif 2.1 < att_rate <= 2.4:
            flow_table = 1000
        elif 1.8 < att_rate <= 2.1:
            flow_table = 1000
        elif 1.5 < att_rate <= 1.8:
            flow_table = 1000
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        if flow_table > 1000:
            flow_table = 1000
        sw22_fb_total += flow_table
        if i%step == 0:
            sw22_fb_list = [sw22_fb_total/step]
            sw22_fb_total = 0

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
        sw13_dr_total += drop_rate
        if i%step == 0:
            sw13_dr_list = [sw13_dr_total/step]
            sw13_dr_total = 0
            
        # switch13: flow table size
        flow_table = 40
        if att_rate > 2.7:
            flow_table = 1000
        elif 2.4 < att_rate <= 2.7:
            flow_table = 1000
        elif 2.1 < att_rate <= 2.4:
            flow_table = 1000
        elif 1.8 < att_rate <= 2.1:
            flow_table = 1000
        elif 1.5 < att_rate <= 1.8:
            flow_table = 1000
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        if flow_table > 1000:
            flow_table = 1000
        sw13_fb_total += flow_table
        if i%step == 0:
            sw13_fb_list = [sw13_fb_total/step]
            sw13_fb_total = 0

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
        sw11_dr_total += drop_rate
        if i%step == 0:
            sw11_dr_list = [sw11_dr_total/step]
            sw11_dr_total = 0
            
        # switch11: flow table size
        flow_table = 40
        if att_rate > 2.7:
            flow_table = 1000
        elif 2.4 < att_rate <= 2.7:
            flow_table = 1000
        elif 2.1 < att_rate <= 2.4:
            flow_table = 1000
        elif 1.8 < att_rate <= 2.1:
            flow_table = 1000
        elif 1.5 < att_rate <= 1.8:
            flow_table = 1000
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        if flow_table > 1000:
            flow_table = 1000
        sw11_fb_total += flow_table
        if i%step == 0:
            sw11_fb_list = [sw11_fb_total/step]
            sw11_fb_total = 0

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
        sw12_dr_total += drop_rate
        if i%step == 0:
            sw12_dr_list = [sw12_dr_total/step]
            sw12_dr_total = 0
            
        # switch12: flow table size
        flow_table = 40
        if att_rate > 2.7:
            flow_table = 1000
        elif 2.4 < att_rate <= 2.7:
            flow_table = 1000
        elif 2.1 < att_rate <= 2.4:
            flow_table = 1000
        elif 1.8 < att_rate <= 2.1:
            flow_table = 1000
        elif 1.5 < att_rate <= 1.8:
            flow_table = 1000
        elif 1.2 < att_rate <= 1.5:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 1 <= att_rate <= 1.2:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.7 <= att_rate < 1:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        elif 0.4 <= att_rate < 0.7:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        else:
            flow_table += round(att_rate * random.randrange(random.randrange(700, 750), random.randrange(750, 800)))
        if flow_table > 1000:
            flow_table = 1000
        sw12_fb_total += flow_table
        if i%step == 0:
            sw12_fb_list = [sw12_fb_total/step]
            sw12_fb_total = 0







        # link s13-s34: bandwidth utilization (%)
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
        s13s34_total += bw
        if i%step == 0:
            s13s34_list = [s13s34_total/step]
            s13s34_total = 0

        # link s23-s34: bandwidth utilization (%)
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
        s23s34_total += bw
        if i%step == 0:
            s23s34_list = [s23s34_total/step]
            s23s34_total = 0






        # server31-1: no. of waiting frames
        frames = 0
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
        frames = random.choices(waiting, weights, k = 1)[0]
        sv311_total += frames
        if i%step == 0:
            sv311_list = [sv311_total/step]
            sv311_total = 0

        # server31-2: no. of waiting frames
        frames = 0
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
        frames = random.choices(waiting, weights, k = 1)[0] 
        sv312_total += frames
        if i%step == 0:
            sv312_list = [sv312_total/step]
            sv312_total = 0

        # server32-2: no. of waiting frames
        frames = 0
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
        frames = random.choices(waiting, weights, k = 1)[0]
        sv322_total += frames
        if i%step == 0:
            sv322_list = [sv322_total/step]
            sv322_total = 0

        # server33-1: no. of waiting frames
        frames = 0
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
        frames = random.choices(waiting, weights, k = 1)[0]       
        sv331_total += frames
        if i%step == 0:
            sv331_list = [sv331_total/step]
            sv331_total = 0
        # timeline_list.append(i/10)












        if i%step == 0:
            # gather collected data
            # temp_net_state_arr = np.column_stack((h112_list, h121_list, h122_list, h212_list, h221_list, h222_list, sw34_dr_list, sw34_fb_list, sw31_dr_list, sw31_fb_list, sw32_dr_list, sw32_fb_list, sw33_dr_list, sw33_fb_list, sw23_dr_list, sw23_fb_list, sw21_dr_list, sw21_fb_list, sw22_dr_list, sw22_fb_list, sw13_dr_list, sw13_fb_list, sw11_dr_list, sw11_fb_list, sw12_dr_list, sw12_fb_list, s13s34_list, s23s34_list, sv311_list, sv312_list, sv322_list, sv331_list))
            # temp_net_state_arr = np.column_stack((h112_list, h121_list, h122_list, h212_list, h221_list, h222_list))
            # temp_net_state_arr = np.column_stack((sw21_dr_list, sw22_dr_list, sw11_dr_list, sw21_fb_list, sw22_fb_list, sw11_fb_list, s13s34_list, s23s34_list))
            # temp_net_state_arr = np.column_stack((sw21_dr_list, sw22_dr_list, sw11_dr_list))
            # temp_net_state_arr = np.column_stack((sw21_fb_list, sw22_fb_list, sw11_fb_list))
            # temp_net_state_arr = np.column_stack((s13s34_list, s23s34_list))


            temp_net_state_arr = np.column_stack((sw34_fb_list, sw31_fb_list, sw32_fb_list, sw33_fb_list, sw23_fb_list, sw21_fb_list, sw22_fb_list, sw13_fb_list, sw11_fb_list, sw12_fb_list, sw34_dr_list, sw31_dr_list, sw32_dr_list, sw33_dr_list, sw23_dr_list, sw21_dr_list, sw22_dr_list, sw13_dr_list, sw11_dr_list, sw12_dr_list, a111_slist, a211_slist, a221_slist, a111_plist, a211_plist, a221_plist))
            print(temp_net_state_arr)
            # temp_net_state_arr = np.column_stack((a111_slist, a211_slist, a221_slist))

            # This is for mega file output purpose only
            # temp_tmp_net_state_arr = np.column_stack((attack_state_list, temp_net_state_arr))
            # if len(mega_net_state_arr) == 0:
            #     mega_net_state_arr = temp_tmp_net_state_arr
            # else:
            #     mega_net_state_arr = np.row_stack((mega_net_state_arr, temp_tmp_net_state_arr))

            # change attack rates based on the last prediction
            # att_rate = sum(att_rate_list)
            att_rate = random.randrange(0, 2) + random.uniform(0, 1)
            att_rate_list[0] = att_rate/3
            att_rate_list[1] = att_rate/3
            att_rate_list[2] = att_rate/3

            # Append adjusted attack rates to current network state array
            attack_state_list = [[att_rate_list[0], att_rate_list[1], att_rate_list[2]]]
            temp_net_state_arr = np.column_stack((attack_state_list, temp_net_state_arr))
            if len(net_state_arr) == 0:
                net_state_arr = temp_net_state_arr
            else:
                net_state_arr = np.row_stack((net_state_arr, temp_net_state_arr))

            # Normalization
            scaler = preprocessing.StandardScaler().fit(net_state_arr)
            norm = scaler.transform(net_state_arr)
            # norm = []
            # for j in range(len(net_state_arr[-1])):
            #     norm.append( (net_state_arr[-1][j] - means_arr[j])/stds_arr[j] )

            # Calculate neural network prediction
            pred = model.predict(np.array([norm[-1]]))
            # Append the latest prediction to to an array for comparision with actual drop rate later
            if (pred_drop_rate_arr == np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])).all():
                pred_drop_rate_arr = pred
            else:
                pred_drop_rate_arr = np.row_stack((pred_drop_rate_arr, pred))


        






        # collect new packet drop rates of each switch here, after 5 minutes under new attack
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
        sw34_dr_mod_total += drop_rate
        if i%step == 0:
            sw34_dr_mod_list.append(sw34_dr_mod_total/step)
            sw34_dr_mod_total = 0

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
        sw31_dr_mod_total += drop_rate
        if i%step == 0:
            sw31_dr_mod_list.append(sw31_dr_mod_total/step)
            sw31_dr_mod_total = 0

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
        sw32_dr_mod_total += drop_rate
        if i%step == 0:
            sw32_dr_mod_list.append(sw32_dr_mod_total/step)
            sw32_dr_mod_total = 0

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
        sw33_dr_mod_total += drop_rate
        if i%step == 0:
            sw33_dr_mod_list.append(sw33_dr_mod_total/step)
            sw33_dr_mod_total = 0

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
        sw23_dr_mod_total += drop_rate 
        if i%step == 0:
            sw23_dr_mod_list.append(sw23_dr_mod_total/step)
            sw23_dr_mod_total = 0

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
        sw21_dr_mod_total += drop_rate
        if i%step == 0:
            sw21_dr_mod_list.append(sw21_dr_mod_total/step)
            sw21_dr_mod_total = 0

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
        sw22_dr_mod_total += drop_rate
        if i%step == 0:
            sw22_dr_mod_list.append(sw22_dr_mod_total/step)
            sw22_dr_mod_total = 0

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
        sw13_dr_mod_total += drop_rate
        if i%step == 0:
            sw13_dr_mod_list.append(sw13_dr_mod_total/step)
            sw13_dr_mod_total = 0

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
        sw11_dr_mod_total += drop_rate
        if i%step == 0:
            sw11_dr_mod_list.append(sw11_dr_mod_total/step)
            sw11_dr_mod_total = 0

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
        sw12_dr_mod_total += drop_rate
        if i%step == 0:
            sw12_dr_mod_list.append(sw12_dr_mod_total/step)
            sw12_dr_mod_total = 0











        # observe new cols
        # attackers to server [server31-1, server31-2, server32-2, server33-1]
        a111_s311 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_s311_mod_total += a111_s311
        a111_s312 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_s312_mod_total += a111_s312
        a111_s322 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_s322_mod_total += a111_s322
        a111_s331 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_s331_mod_total += a111_s331

        a211_s311 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_s311_mod_total += a211_s311
        a211_s312 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_s312_mod_total += a211_s312
        a211_s322 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_s322_mod_total += a211_s322
        a211_s331 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_s331_mod_total += a211_s331

        a221_s311 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a221_s311_mod_total += a221_s311
        a221_s312 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a221_s312_mod_total += a221_s312
        a221_s322 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a221_s322_mod_total += a221_s322
        a221_s331 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a221_s331_mod_total += a221_s331

        a111_a211 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a111_a221 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))
        a211_a221 = att_rate * random.uniform(random.randrange(88, 90), random.randrange(90, 92))

        a111_a211_mod_total += a111_a211; a111_a221_mod_total += a111_a221
        a211_a111_mod_total += a111_a211; a211_a221_mod_total += a211_a221
        a221_a111_mod_total += a111_a221; a221_a211_mod_total += a211_a221

        if i%step == 0:
            a111_mod_slist.append([a111_s311_mod_total/step, a111_s312_mod_total/step, a111_s322_mod_total/step, a111_s331_mod_total/step])
            a211_mod_slist.append([a211_s311_mod_total/step, a211_s312_mod_total/step, a211_s322_mod_total/step, a211_s331_mod_total/step])
            a221_mod_slist.append([a221_s311_mod_total/step, a221_s312_mod_total/step, a221_s322_mod_total/step, a221_s331_mod_total/step])
            a111_mod_plist.append([a111_a211_mod_total/step, a111_a221_mod_total/step])
            a211_mod_plist.append([a111_a211_mod_total/step, a211_a221_mod_total/step])
            a221_mod_plist.append([a111_a221_mod_total/step, a211_a221_mod_total/step])
            a111_s311_mod_total = 0; a111_s312_mod_total = 0; a111_s322_mod_total = 0; a111_s331_mod_total = 0
            a211_s311_mod_total = 0; a211_s312_mod_total = 0; a211_s322_mod_total = 0; a211_s331_mod_total = 0
            a221_s311_mod_total = 0; a221_s312_mod_total = 0; a221_s322_mod_total = 0; a221_s331_mod_total = 0
            a111_a211_mod_total = 0; a111_a221_mod_total = 0
            a211_a111_mod_total = 0; a211_a221_mod_total = 0
            a221_a111_mod_total = 0; a221_a211_mod_total = 0




        # observe new time difference between frames
        # host11-2: time diff between two successive frames (ms)
        delay = 0
        if 6000 < i <= 8400 or 12600 < i <= 16200 or 17400 < i <= 24000 or 28200 < i <= 34800 or 36600 < i <= 43800:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif i <= 6000 or 10200 < i <= 12600 or 16800 < i <= 17400 or 24000 < i <= 25200 or 34800 < i <= 36000 or 36000 < i <= 36600:
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
        h112_mod_total += delay

        # [server31-1, server31-2, server32-2, server33-1]
        if i%step == 0:
            if i <= 8400:
                h112_mod_list.append([h112_mod_total/step, 0, 0, 0])
            elif 16800 < i <= 25200 or 36000 < i <= 43800:
                h112_mod_list.append([0, h112_mod_total/step, 0, 0])
            elif 10200 < i <= 16200 or 28200 < i <= 36000:
                h112_mod_list.append([0, 0, h112_mod_total/step, 0])
            else:
                h112_mod_list.append([0, 0, 0, 0])
            h112_mod_total = 0

        # host12-1: time diff between two successive frames (ms)
        delay = 0
        if i <= 9000 or 16200 < i <= 18600 or 24000 < i <= 28200 or 31800 < i <= 36000:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif 12000 < i <= 16200 or 18600 < i <= 21000 or 22200 < i <= 24000 or 30600 < i <= 31800 or 36000 < i <= 36600:
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
        h121_mod_total += delay

        # [server31-1, server31-2, server32-2, server33-1]
        if i%step == 0:
            if 12000 < i <= 21000 or 38400 < i <= 47400:
                h121_mod_list.append([h121_mod_total/step, 0, 0, 0])
            elif i <= 9000 or 30600 < i <= 36600:
                h121_mod_list.append([0, h121_mod_total/step, 0, 0])
            elif 22200 < i <= 28200:
                h121_mod_list.append([0, 0, h121_mod_total/step, 0])
            else:
                h121_mod_list.append([0, 0, 0, 0])
            h121_mod_total = 0

        # host12-2: time diff between two successive frames (ms)
        delay = 0
        if i <= 7800 or 10200 < i <= 16800 or 22200 < i <= 27000 or 32400 < i <= 35400 or 36000 < i <= 38400:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif 16800 < i <= 17400 or 19800 < i <= 22200 or 27000 < i <= 28800 or 28800 < i <= 32400 or 38400 < i <= 42000:
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
        h122_mod_total += delay
        
        # [server31-1, server31-2, server32-2, server33-1]
        if i%step == 0:
            if 28800 < i <= 35400 or 36000 < i <= 42000:
                h122_mod_list.append([h122_mod_total/step, 0, 0, 0])
            elif 10200 < i <= 17400:
                h122_mod_list.append([0, h122_mod_total/step, 0, 0])
            elif i <= 7800:
                h122_mod_list.append([0, 0, h122_mod_total/step, 0])
            elif 19800 < i <= 28800:
                h122_mod_list.append([0, 0, 0, h122_mod_total/step])
            else:
                h122_mod_list.append([0, 0, 0, 0])
            h122_mod_total = 0

        # host21-2: time diff between two successive frames (ms)
        delay = 0
        if 6600 < i <= 7200 or 12000 < i <= 16200 or 16200 < i <= 22200 or 25200 < i <= 30600 or 35400 < i <= 36600:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif i <= 6600 or 8400 < i <= 12000 or 22200 < i <= 24000 or 24600 < i <= 25200 or 30600 < i <= 31800 or 34800 < i <= 35400 or 36600 < i <= 41400:
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
        h212_mod_total += delay

        # [server31-1, server31-2, server32-2, server33-1]
        if i%step == 0:
            if 8400 < i <= 16200:
                h212_mod_list.append([h212_mod_total/step, 0, 0, 0])
            elif 24600 < i <= 31800:
                h212_mod_list.append([0, h212_mod_total/step, 0, 0])
            elif 16200 < i <= 24000:
                h212_mod_list.append([0, 0, h212_mod_total/step, 0])
            elif i <= 7200 or 34800 < i <= 41400:
                h212_mod_list.append([0, 0, 0, h212_mod_total/step])
            else:
                h212_mod_list.append([0, 0, 0, 0])
            h212_mod_total = 0

        # host22-1: time diff between two successive frames (ms)
        delay = 0
        if 7200 < i <= 14400 or 21000 < i <= 23400 or 28800 < i <= 34800 or 41400 < i <= 43800:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif i < 6600 or 14400 < i <= 15600 or 18600 < i <= 21000 or 23400 < i <= 25200 or 27000 < i <= 28800 or 34800 < i <= 35400 or 36600 < i <= 41400:
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
        h221_mod_total += delay

        # [server31-1, server31-2, server32-2, server33-1]
        if i%step == 0:
            if 18600 < i <= 25200:
                h221_mod_list.append([h221_mod_total/step, 0, 0, 0])
            elif i <= 6600 or 7200 < i <= 15600 or 27000 < i <= 35400 or 36600 < i <= 43800:
                h221_mod_list.append([0, 0, 0, h221_mod_total/step])
            else:
                h221_mod_list.append([0, 0, 0, 0])
            h221_mod_total = 0

        # host22-2: time diff between two successive frames (ms)
        delay = 0
        if 7800 < i <= 10200 or 15600 < i <= 19800 or 25200 < i <= 28800 or 36000 < i <= 43200:
            delay = random.randrange(random.randrange(60, 63), random.randrange(63, 65)) + random.uniform(0.1, 0.9)
        elif i < 6000 or 6000 < i <= 7800 or 10200 < i <= 12600 or 14400 < i <= 15600 or 19800 < i <= 22200 or 23400 < i <= 25200 or 28800 < i <= 32400 or 34800 < i <= 36000:
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
        h222_mod_total += delay

        # [server31-1, server31-2, server32-2, server33-1]
        if i%step == 0:
            if i < 6000 or 23400 < i <= 32400:
                h222_mod_list.append([h222_mod_total/step, 0, 0, 0])
            elif 6000 < i <= 12600 or 34800 < i <= 43200:
                h222_mod_list.append([0, 0, h222_mod_total/step, 0])
            elif 14400 < i <= 22200:
                h222_mod_list.append([0, 0, 0, h222_mod_total/step])
            else:
                h222_mod_list.append([0, 0, 0, 0])
            h222_mod_total = 0













    # calculate difference between predicted and actual rates here
    actual_drop_rate_arr = np.column_stack((sw34_dr_mod_list, sw31_dr_mod_list, sw32_dr_mod_list, sw33_dr_mod_list, sw23_dr_mod_list, sw21_dr_mod_list, sw22_dr_mod_list, sw13_dr_mod_list, sw11_dr_mod_list, sw12_dr_mod_list))
    scaler = preprocessing.StandardScaler().fit(actual_drop_rate_arr)
    norm_actual_drop_rate_arr = scaler.transform(actual_drop_rate_arr)

    # norm_actual_drop_rate_arr = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    # for row in range(len(actual_drop_rate_arr)):
    #     mega_col = 27
    #     temp_arr = np.array([])
    #     for col in range(len(actual_drop_rate_arr[row])):
    #         temp_arr = np.append(temp_arr, (actual_drop_rate_arr[row][col] - means_arr[mega_col])/stds_arr[mega_col])
    #         mega_col += 2
    #     if (norm_actual_drop_rate_arr == np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])).all():
    #         norm_actual_drop_rate_arr = temp_arr
    #     else:
    #         norm_actual_drop_rate_arr = np.row_stack((norm_actual_drop_rate_arr, temp_arr))
    error_drop_rate_arr = np.abs(pred_drop_rate_arr - norm_actual_drop_rate_arr)

    # observe the time diff between 2 consecutive frames
    frames_time_diff_arr = np.column_stack((h112_mod_list, h121_mod_list, h122_mod_list, h212_mod_list, h221_mod_list, h222_mod_list))
    attacker_cols_arr = np.column_stack((a111_mod_slist, a211_mod_slist, a221_mod_slist, a111_mod_plist, a211_mod_plist, a221_mod_plist))
    
    frames_time_diff_df = pd.DataFrame(frames_time_diff_arr)
    frames_time_diff_df.drop(index = frames_time_diff_df.index[:137], axis = 0, inplace = True)
    attacker_cols_arr_df = pd.DataFrame(attacker_cols_arr)
    attacker_cols_arr_df.drop(index = attacker_cols_arr_df.index[:137], axis = 0, inplace = True)
    pred_drop_rate_df = pd.DataFrame(pred_drop_rate_arr)
    pred_drop_rate_df.drop(index = pred_drop_rate_df.index[:137], axis = 0, inplace = True)
    actual_drop_rate_df = pd.DataFrame(actual_drop_rate_arr)
    actual_drop_rate_df.drop(index = actual_drop_rate_df.index[:137], axis = 0, inplace = True)
    norm_actual_drop_rate_df = pd.DataFrame(norm_actual_drop_rate_arr)
    norm_actual_drop_rate_df.drop(index = norm_actual_drop_rate_df.index[:137], axis = 0, inplace = True)
    error_drop_rate_df = pd.DataFrame(error_drop_rate_arr)
    error_drop_rate_df.drop(index = error_drop_rate_df.index[:137], axis = 0, inplace = True)

    '''
    mega_net_state_df = pd.DataFrame(mega_net_state_arr)
    # mega_net_state_df = pd.concat([pd.DataFrame(timeline_list), mega_net_state_df])
    mega_net_state_df.drop(index = mega_net_state_df.index[:137], axis = 0, inplace = True)
    mega_net_state_df.columns = ['1. Attacker1 rate', '2. Attacker2 rate', '3. Attacker3 rate',
        '4. h112 to s311', '5. h112 to s312', '6. h112 to s322', '7. h112 to s331',
        '8. h121 to s311', '9. h121 to s312', '10. h121 to s322', '11. h121 to s331',
        '12. h122 to s311', '13. h122 to s312', '14. h122 to s322', '15. h122 to s331',
        '16. h212 to s311', '17. h212 to s312', '18. h212 to s322', '19. h212 to s331',
        '20. h221 to s311', '21. h221 to s312', '22. h221 to s322', '23. h221 to s331',
        '24. h222 to s311', '25. h222 to s312', '26. h222 to s322', '27. h222 to s331',
        '28. s34 packet drop rate', '29. s34 flow table size',
        '30. s31 packet drop rate', '31. s31 flow table size',
        '32. s32 packet drop rate', '33. s32 flow table size',
        '34. s33 packet drop rate', '35. s33 flow table size',
        '36. s23 packet drop rate', '37. s23 flow table size',
        '38. s21 packet drop rate', '39. s21 flow table size',
        '40. s22 packet drop rate', '41. s22 flow table size',
        '42. s13 packet drop rate', '43. s13 flow table size',
        '44. s11 packet drop rate', '45. s11 flow table size',
        '46. s12 packet drop rate', '47. s12 flow table size',
        '48. s13s34 bw utilization', '49. s23s34 bw utilization',
        '50. sv311 no. of waiting frames', '51. sv312 no. of waiting frames',
        '52. sv322 no. of waiting frames', '53. sv331 no. of waiting frames']

    mega_net_state_output = output_dir + 'xmega_net_state.csv'
    mega_net_state_local_output = curr_dir + '/xmega_net_state.csv'
    mega_net_state_df.to_csv(mega_net_state_output, mode = 'w', header = True, index = False)
    # mega_net_state_df.to_csv(mega_net_state_local_output, mode = 'w', header = True, index = False)
    '''

    attacker_cols_arr_ouput = output_dir + 'attacker_cols.csv'
    attacker_cols_arr_df.to_csv(attacker_cols_arr_ouput, mode = 'w', header = True, index = False)

    frames_time_diff_ouput = output_dir + 'frames_time_diff.csv'
    # frames_time_diff_local_ouput = curr_dir + '/frames_time_diff1.csv'
    frames_time_diff_df.to_csv(frames_time_diff_ouput, mode = 'w', header = True, index = False)
    # frames_time_diff_df.to_csv(frames_time_diff_local_ouput, mode = 'w', header = True, index = False)
    
    pred_drop_rate_output = output_dir + 'norm_predicted_drop_rate.csv'
    # pred_drop_rate_local_output = curr_dir + '/predicted_drop_rate2.csv'
    pred_drop_rate_df.to_csv(pred_drop_rate_output, mode = 'w', header = True, index = False)
    # pred_drop_rate_df.to_csv(pred_drop_rate_local_output, mode = 'w', header = True, index = False)

    norm_actual_drop_rate_output = output_dir + 'norm_actual_drop_rate.csv'
    # actual_norm_drop_rate_local_output = curr_dir + '/actual_norm_drop_rate2.csv'
    norm_actual_drop_rate_df.to_csv(norm_actual_drop_rate_output, mode = 'w', header = True, index = False)
    # actual_norm_drop_rate_df.to_csv(actual_norm_drop_rate_local_output, mode = 'w', header = True, index = False)

    actual_drop_rate_output = output_dir + 'actual_drop_rate.csv'
    # actual_drop_rate_local_output = curr_dir + '/actual_drop_rate2.csv'
    actual_drop_rate_df.to_csv(actual_drop_rate_output, mode = 'w', header = True, index = False)
    # actual_drop_rate_df.to_csv(actual_drop_rate_local_output, mode = 'w', header = True, index = False)

    drop_rate_error_output = output_dir + 'drop_rate_error.csv'
    # drop_rate_error_local_output = curr_dir + '/drop_rate_error1.csv'
    error_drop_rate_df.to_csv(drop_rate_error_output, mode = 'w', header = True, index = False)
    # error_drop_rate_df.to_csv(drop_rate_error_local_output, mode = 'w', header = True, index = False)

if __name__ == "__main__":
    start_time = time.time()
    data_gen_test()
    print('Took', round(time.time()-start_time, 2), 'seconds')