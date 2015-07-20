#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 truong-d <truong-d@ahclab08>
#
# Distributed under terms of the MIT license.

"""

"""
import glob
import sys
import py_io
import itertools
import os
from random import shuffle

# nutt-set: number of utterance per set
opts, args = py_io.easy_option(['nutt-set'])

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def main():
    fn_text = py_io.read_scp(args[0])
    list_audio_dir = args[1:]
    
    wav_info = {}
    for audio_dir in list_audio_dir:
        method = os.path.basename(audio_dir)
        wav_info[method] = {}

        for filename in glob.glob(audio_dir + "/*.wav"):
            base = os.path.basename(filename).replace(".wav", "")
            wav_info[method][base] = filename
    
    # Find intersection between methods
    intersec = set(wav_info[wav_info.keys()[0]].keys())
    for method, method_data in wav_info.items():
        filelist = set(method_data.keys())
        intersec = intersec & filelist

    # Remove some elements
    keys = sorted(list(intersec))
    for method, method_data in wav_info.items():
        for k in method_data.keys():
            if k not in keys:
                method_data.pop(k, None)
    
    utt_id = 1
    for setidx, utt_list in enumerate(list(chunks(keys, int(opts.nutt_set)))):
        set_name = 'set-' + str(setidx + 1)
        for k in utt_list:
            method_list = wav_info.keys()
            method_combines = itertools.combinations(method_list, 2)
            for method1, method2 in method_combines:
                text = "%s|%s|%s" % (k + "-" + str(utt_id), set_name, fn_text[k])
                winfo = wav_info[method1]
                text += "|%s|%s" % (winfo[k], method1)
                winfo = wav_info[method2]
                text += "|%s|%s" % (winfo[k], method2)
                utt_id += 1
                print text

    exit(1)
    for k in keys[start1:end1]:
        text = "%s|set1|%s" % (k, fn_text[k])
        
        methods = wav_info.keys()
        shuffle(methods)

    for k in keys[start2:end2]:
        text = "%s|set2|%s" % (k, fn_text[k])
        methods = wav_info.keys()
        shuffle(methods)
        for method in methods:
            winfo = wav_info[method]
            text += "|%s|%s" % (winfo[k], method)
        print text

    for k in keys[start3:end3]:
        text = "%s|set3|%s" % (k, fn_text[k])
        methods = wav_info.keys()
        shuffle(methods)
        for method in methods:
            winfo = wav_info[method]
            text += "|%s|%s" % (winfo[k], method)
        print text

if __name__ == '__main__':
    main()
