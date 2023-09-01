# __init__.py

__version__ = '1.0.0'
__name__ = "tge"
__author__ = "Miner3D"

__doc__ = """
    tge - Text Game Engine
    Originally made for displaying and creating console-based games but has evolved into a general-purpose library.

    This library provides a wide range of functions and utilities for text-based game development, console operations,
    data manipulation, conversions, math calculations, user interfaces, file operations, and more.

    With a collection of 490 functions, tge tries to simplify the development process and offers capabilities for
    building text-based games, console applications, file manipulation, and various quality of life functions.
    """





#   Import modules from "manipulation"
from .manipulation import string_utils
from .manipulation import list_utils
from .manipulation import dictionary_utils as dict_utils

#   Import modules from "compatibility"
from .compatibility import tge_pygame 
from .compatibility import tge_tkinter



#   Import modules from "conversion"
from .conversion import convert_binary as binary
from .conversion import convert_temperature as temperature
from .conversion import convert_time as time
from .conversion import convert_units as units
from .conversion import data_conversion as data


#   Import modules from "math_functions"
from .math_functions import financial_calculations 
from .math_functions import geometry_calculations
from .math_functions import math_functions
from .math_functions import statistics_calculations


#   Import modules from "user_interface"
from .user_interface import keyboard_operations
from .user_interface import cursor_operations


#   Import modules from root directory
from . import alternatives
from . import audio
from . import clipboard
from . import codec
from . import console_utils as console
from . import file_operations
from . import formatting_utils as formatting
from . import image_processing
from . import random_generators as tge_random
from . import tbe
from . import time_utils
from . import validation
from . import user_interface as interface
from . import bool_operations
from . import bitwise
from . import steam_scrapper








