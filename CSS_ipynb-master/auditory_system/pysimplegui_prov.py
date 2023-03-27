import os
import PySimpleGUI as sg
from scipy.io.wavfile import read, write

def get_input_file():
    #cur_dir = os.getcwd()

    absolute_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(absolute_path)
    filename = sg.popup_get_file('', no_window = True, initial_folder = dir_name+"/sounds")
    
    return filename
    
get_input_file()    