# Copyright (c) 2010 Diogo Becker
# Distributed under the MIT License
# See accompanying file LICENSE

""" """
import core
import shutil
import os

def clean_experiments(cfg, experiments):
    for run,experiment in experiments:
        folder = core.get_folder(cfg, experiment, run)
        print "Cleaning", folder
        shutil.rmtree(folder)

def clean_experiment(folder):
    print "Cleaning", folder
    os.remove(folder+'/dude.status')
