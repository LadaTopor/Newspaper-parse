﻿# SDK Pullenti Unitext, version 4.19, may 2023. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter UniSharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

from enum import IntEnum

class FormattingLevel(IntEnum):
    CHARACTER = 0
    CHARACTERSTYLE = 1
    PARAGRAPH = 2
    PARAGRAPHSTYLE = 3
    PART = 4
    GLOBAL = 5
    ALL = 6
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)