# Generated from ANTLRv4Lexer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


if "." in __name__:
    from .LexerAdaptor import LexerAdaptor
else:
    from LexerAdaptor import LexerAdaptor

def serializedATN():
    return [
        4,0,63,814,6,-1,6,-1,6,-1,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,
        4,7,4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,
        2,12,7,12,2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,
        7,18,2,19,7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,
        2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,
        7,31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,
        2,38,7,38,2,39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,
        7,44,2,45,7,45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,
        2,51,7,51,2,52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,
        7,57,2,58,7,58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,
        2,64,7,64,2,65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,
        7,70,2,71,7,71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,
        2,77,7,77,2,78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,
        7,83,2,84,7,84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,
        2,90,7,90,2,91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,
        7,96,2,97,7,97,2,98,7,98,2,99,7,99,2,100,7,100,2,101,7,101,2,102,
        7,102,2,103,7,103,2,104,7,104,2,105,7,105,2,106,7,106,2,107,7,107,
        2,108,7,108,2,109,7,109,2,110,7,110,2,111,7,111,2,112,7,112,2,113,
        7,113,2,114,7,114,2,115,7,115,2,116,7,116,2,117,7,117,2,118,7,118,
        2,119,7,119,2,120,7,120,2,121,7,121,2,122,7,122,2,123,7,123,2,124,
        7,124,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,
        4,1,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,5,8,289,8,8,10,8,12,8,292,9,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,5,9,304,8,9,10,9,12,9,307,9,9,1,9,1,9,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,321,8,10,10,10,12,
        10,324,9,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,
        14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,
        24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        26,1,26,1,26,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,
        31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,1,36,1,36,1,37,1,
        37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,
        44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,
        50,1,51,4,51,494,8,51,11,51,12,51,495,1,51,1,51,1,52,1,52,1,52,1,
        52,1,53,1,53,3,53,506,8,53,1,54,1,54,1,55,1,55,1,56,1,56,1,56,1,
        56,5,56,516,8,56,10,56,12,56,519,9,56,1,56,1,56,1,56,3,56,524,8,
        56,1,57,1,57,1,57,1,57,1,57,5,57,531,8,57,10,57,12,57,534,9,57,1,
        57,1,57,1,57,3,57,539,8,57,1,58,1,58,1,58,1,58,5,58,545,8,58,10,
        58,12,58,548,9,58,1,59,1,59,1,59,1,59,1,59,3,59,555,8,59,1,60,1,
        60,1,60,1,61,1,61,1,61,1,61,1,61,3,61,565,8,61,3,61,567,8,61,3,61,
        569,8,61,3,61,571,8,61,1,62,1,62,1,62,5,62,576,8,62,10,62,12,62,
        579,9,62,3,62,581,8,62,1,63,1,63,1,64,1,64,1,65,1,65,1,65,1,65,1,
        65,1,65,1,65,1,65,1,65,3,65,596,8,65,1,66,1,66,1,66,3,66,601,8,66,
        1,66,1,66,1,67,1,67,1,67,5,67,608,8,67,10,67,12,67,611,9,67,1,67,
        1,67,1,68,1,68,1,68,5,68,618,8,68,10,68,12,68,621,9,68,1,68,1,68,
        1,69,1,69,1,69,5,69,628,8,69,10,69,12,69,631,9,69,1,70,1,70,1,70,
        1,70,1,70,3,70,638,8,70,1,71,1,71,1,72,1,72,1,72,1,72,1,73,1,73,
        1,74,1,74,1,75,1,75,1,75,1,76,1,76,1,77,1,77,1,78,1,78,1,79,1,79,
        1,80,1,80,1,81,1,81,1,82,1,82,1,83,1,83,1,84,1,84,1,84,1,85,1,85,
        1,86,1,86,1,87,1,87,1,88,1,88,1,89,1,89,1,90,1,90,1,91,1,91,1,91,
        1,92,1,92,1,93,1,93,1,94,1,94,1,95,1,95,1,96,1,96,1,97,1,97,1,98,
        1,98,1,99,1,99,1,99,1,100,1,100,1,101,1,101,1,102,1,102,1,103,1,
        103,1,103,1,103,1,103,1,104,1,104,1,104,1,104,1,105,1,105,1,105,
        1,105,1,106,1,106,1,106,1,106,1,107,1,107,1,107,1,108,1,108,1,108,
        1,108,1,109,1,109,1,110,1,110,1,110,1,110,1,110,1,111,1,111,1,111,
        1,111,1,112,1,112,1,112,1,112,1,113,1,113,1,113,1,113,1,114,1,114,
        1,114,1,114,1,115,1,115,1,115,1,115,1,116,1,116,1,116,1,116,1,117,
        1,117,1,117,1,118,1,118,1,118,1,118,1,119,1,119,1,120,1,120,4,120,
        776,8,120,11,120,12,120,777,1,120,1,120,1,121,1,121,1,121,1,121,
        1,122,1,122,1,122,1,122,1,123,1,123,5,123,792,8,123,10,123,12,123,
        795,9,123,1,124,1,124,5,124,799,8,124,10,124,12,124,802,9,124,1,
        124,1,124,1,124,5,124,807,8,124,10,124,12,124,810,9,124,1,124,3,
        124,813,8,124,2,517,532,0,125,4,4,6,5,8,6,10,7,12,8,14,9,16,10,18,
        11,20,12,22,13,24,14,26,0,28,15,30,16,32,17,34,18,36,19,38,20,40,
        21,42,22,44,23,46,24,48,25,50,26,52,27,54,28,56,29,58,30,60,31,62,
        32,64,33,66,34,68,35,70,36,72,37,74,38,76,39,78,40,80,41,82,42,84,
        43,86,44,88,45,90,46,92,47,94,48,96,49,98,50,100,51,102,52,104,53,
        106,54,108,55,110,0,112,0,114,0,116,0,118,0,120,0,122,0,124,0,126,
        0,128,0,130,0,132,0,134,0,136,0,138,0,140,0,142,0,144,0,146,0,148,
        0,150,0,152,0,154,0,156,0,158,0,160,0,162,0,164,0,166,0,168,0,170,
        0,172,0,174,0,176,0,178,0,180,0,182,0,184,0,186,0,188,0,190,0,192,
        0,194,0,196,0,198,0,200,0,202,0,204,0,206,0,208,0,210,0,212,0,214,
        0,216,0,218,56,220,57,222,58,224,0,226,0,228,0,230,0,232,0,234,0,
        236,0,238,59,240,60,242,61,244,0,246,3,248,62,250,0,252,63,4,0,1,
        2,3,15,3,0,9,10,12,13,32,32,2,0,9,9,32,32,2,0,10,10,12,13,2,0,10,
        10,13,13,8,0,34,34,39,39,92,92,98,98,102,102,110,110,114,114,116,
        116,1,0,49,57,3,0,48,57,65,70,97,102,1,0,48,57,4,0,10,10,13,13,39,
        39,92,92,4,0,10,10,13,13,34,34,92,92,3,0,183,183,768,879,8255,8256,
        13,0,65,90,97,122,192,214,216,246,248,767,880,893,895,8191,8204,
        8205,8304,8591,11264,12271,12289,55295,63744,64975,65008,65533,1,
        0,92,93,1,0,34,34,1,0,39,39,795,0,4,1,0,0,0,0,6,1,0,0,0,0,8,1,0,
        0,0,0,10,1,0,0,0,0,12,1,0,0,0,0,14,1,0,0,0,0,16,1,0,0,0,0,18,1,0,
        0,0,0,20,1,0,0,0,0,22,1,0,0,0,0,24,1,0,0,0,0,28,1,0,0,0,0,30,1,0,
        0,0,0,32,1,0,0,0,0,34,1,0,0,0,0,36,1,0,0,0,0,38,1,0,0,0,0,40,1,0,
        0,0,0,42,1,0,0,0,0,44,1,0,0,0,0,46,1,0,0,0,0,48,1,0,0,0,0,50,1,0,
        0,0,0,52,1,0,0,0,0,54,1,0,0,0,0,56,1,0,0,0,0,58,1,0,0,0,0,60,1,0,
        0,0,0,62,1,0,0,0,0,64,1,0,0,0,0,66,1,0,0,0,0,68,1,0,0,0,0,70,1,0,
        0,0,0,72,1,0,0,0,0,74,1,0,0,0,0,76,1,0,0,0,0,78,1,0,0,0,0,80,1,0,
        0,0,0,82,1,0,0,0,0,84,1,0,0,0,0,86,1,0,0,0,0,88,1,0,0,0,0,90,1,0,
        0,0,0,92,1,0,0,0,0,94,1,0,0,0,0,96,1,0,0,0,0,98,1,0,0,0,0,100,1,
        0,0,0,0,102,1,0,0,0,0,104,1,0,0,0,0,106,1,0,0,0,0,108,1,0,0,0,1,
        210,1,0,0,0,1,212,1,0,0,0,1,214,1,0,0,0,1,216,1,0,0,0,1,218,1,0,
        0,0,1,220,1,0,0,0,1,222,1,0,0,0,2,224,1,0,0,0,2,226,1,0,0,0,2,228,
        1,0,0,0,2,230,1,0,0,0,2,232,1,0,0,0,2,234,1,0,0,0,2,236,1,0,0,0,
        2,238,1,0,0,0,2,240,1,0,0,0,2,242,1,0,0,0,3,244,1,0,0,0,3,246,1,
        0,0,0,3,248,1,0,0,0,3,252,1,0,0,0,4,254,1,0,0,0,6,258,1,0,0,0,8,
        262,1,0,0,0,10,266,1,0,0,0,12,268,1,0,0,0,14,270,1,0,0,0,16,272,
        1,0,0,0,18,275,1,0,0,0,20,279,1,0,0,0,22,295,1,0,0,0,24,310,1,0,
        0,0,26,327,1,0,0,0,28,329,1,0,0,0,30,336,1,0,0,0,32,345,1,0,0,0,
        34,351,1,0,0,0,36,358,1,0,0,0,38,366,1,0,0,0,40,376,1,0,0,0,42,383,
        1,0,0,0,44,391,1,0,0,0,46,399,1,0,0,0,48,406,1,0,0,0,50,413,1,0,
        0,0,52,419,1,0,0,0,54,427,1,0,0,0,56,439,1,0,0,0,58,444,1,0,0,0,
        60,446,1,0,0,0,62,448,1,0,0,0,64,450,1,0,0,0,66,452,1,0,0,0,68,454,
        1,0,0,0,70,456,1,0,0,0,72,458,1,0,0,0,74,460,1,0,0,0,76,462,1,0,
        0,0,78,464,1,0,0,0,80,466,1,0,0,0,82,468,1,0,0,0,84,470,1,0,0,0,
        86,472,1,0,0,0,88,474,1,0,0,0,90,476,1,0,0,0,92,478,1,0,0,0,94,480,
        1,0,0,0,96,482,1,0,0,0,98,484,1,0,0,0,100,486,1,0,0,0,102,488,1,
        0,0,0,104,490,1,0,0,0,106,493,1,0,0,0,108,499,1,0,0,0,110,505,1,
        0,0,0,112,507,1,0,0,0,114,509,1,0,0,0,116,511,1,0,0,0,118,525,1,
        0,0,0,120,540,1,0,0,0,122,549,1,0,0,0,124,556,1,0,0,0,126,559,1,
        0,0,0,128,580,1,0,0,0,130,582,1,0,0,0,132,584,1,0,0,0,134,595,1,
        0,0,0,136,597,1,0,0,0,138,604,1,0,0,0,140,614,1,0,0,0,142,624,1,
        0,0,0,144,637,1,0,0,0,146,639,1,0,0,0,148,641,1,0,0,0,150,645,1,
        0,0,0,152,647,1,0,0,0,154,649,1,0,0,0,156,652,1,0,0,0,158,654,1,
        0,0,0,160,656,1,0,0,0,162,658,1,0,0,0,164,660,1,0,0,0,166,662,1,
        0,0,0,168,664,1,0,0,0,170,666,1,0,0,0,172,668,1,0,0,0,174,671,1,
        0,0,0,176,673,1,0,0,0,178,675,1,0,0,0,180,677,1,0,0,0,182,679,1,
        0,0,0,184,681,1,0,0,0,186,683,1,0,0,0,188,686,1,0,0,0,190,688,1,
        0,0,0,192,690,1,0,0,0,194,692,1,0,0,0,196,694,1,0,0,0,198,696,1,
        0,0,0,200,698,1,0,0,0,202,700,1,0,0,0,204,703,1,0,0,0,206,705,1,
        0,0,0,208,707,1,0,0,0,210,709,1,0,0,0,212,714,1,0,0,0,214,718,1,
        0,0,0,216,722,1,0,0,0,218,726,1,0,0,0,220,729,1,0,0,0,222,733,1,
        0,0,0,224,735,1,0,0,0,226,740,1,0,0,0,228,744,1,0,0,0,230,748,1,
        0,0,0,232,752,1,0,0,0,234,756,1,0,0,0,236,760,1,0,0,0,238,764,1,
        0,0,0,240,767,1,0,0,0,242,771,1,0,0,0,244,775,1,0,0,0,246,781,1,
        0,0,0,248,785,1,0,0,0,250,789,1,0,0,0,252,812,1,0,0,0,254,255,3,
        118,57,0,255,256,1,0,0,0,256,257,6,0,0,0,257,5,1,0,0,0,258,259,3,
        116,56,0,259,260,1,0,0,0,260,261,6,1,0,0,261,7,1,0,0,0,262,263,3,
        120,58,0,263,264,1,0,0,0,264,265,6,2,0,0,265,9,1,0,0,0,266,267,3,
        128,62,0,267,11,1,0,0,0,268,269,3,138,67,0,269,13,1,0,0,0,270,271,
        3,142,69,0,271,15,1,0,0,0,272,273,3,168,82,0,273,274,6,6,1,0,274,
        17,1,0,0,0,275,276,3,164,80,0,276,277,1,0,0,0,277,278,6,7,2,0,278,
        19,1,0,0,0,279,280,5,111,0,0,280,281,5,112,0,0,281,282,5,116,0,0,
        282,283,5,105,0,0,283,284,5,111,0,0,284,285,5,110,0,0,285,286,5,
        115,0,0,286,290,1,0,0,0,287,289,3,26,11,0,288,287,1,0,0,0,289,292,
        1,0,0,0,290,288,1,0,0,0,290,291,1,0,0,0,291,293,1,0,0,0,292,290,
        1,0,0,0,293,294,5,123,0,0,294,21,1,0,0,0,295,296,5,116,0,0,296,297,
        5,111,0,0,297,298,5,107,0,0,298,299,5,101,0,0,299,300,5,110,0,0,
        300,301,5,115,0,0,301,305,1,0,0,0,302,304,3,26,11,0,303,302,1,0,
        0,0,304,307,1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,308,1,0,
        0,0,307,305,1,0,0,0,308,309,5,123,0,0,309,23,1,0,0,0,310,311,5,99,
        0,0,311,312,5,104,0,0,312,313,5,97,0,0,313,314,5,110,0,0,314,315,
        5,110,0,0,315,316,5,101,0,0,316,317,5,108,0,0,317,318,5,115,0,0,
        318,322,1,0,0,0,319,321,3,26,11,0,320,319,1,0,0,0,321,324,1,0,0,
        0,322,320,1,0,0,0,322,323,1,0,0,0,323,325,1,0,0,0,324,322,1,0,0,
        0,325,326,5,123,0,0,326,25,1,0,0,0,327,328,7,0,0,0,328,27,1,0,0,
        0,329,330,5,105,0,0,330,331,5,109,0,0,331,332,5,112,0,0,332,333,
        5,111,0,0,333,334,5,114,0,0,334,335,5,116,0,0,335,29,1,0,0,0,336,
        337,5,102,0,0,337,338,5,114,0,0,338,339,5,97,0,0,339,340,5,103,0,
        0,340,341,5,109,0,0,341,342,5,101,0,0,342,343,5,110,0,0,343,344,
        5,116,0,0,344,31,1,0,0,0,345,346,5,108,0,0,346,347,5,101,0,0,347,
        348,5,120,0,0,348,349,5,101,0,0,349,350,5,114,0,0,350,33,1,0,0,0,
        351,352,5,112,0,0,352,353,5,97,0,0,353,354,5,114,0,0,354,355,5,115,
        0,0,355,356,5,101,0,0,356,357,5,114,0,0,357,35,1,0,0,0,358,359,5,
        103,0,0,359,360,5,114,0,0,360,361,5,97,0,0,361,362,5,109,0,0,362,
        363,5,109,0,0,363,364,5,97,0,0,364,365,5,114,0,0,365,37,1,0,0,0,
        366,367,5,112,0,0,367,368,5,114,0,0,368,369,5,111,0,0,369,370,5,
        116,0,0,370,371,5,101,0,0,371,372,5,99,0,0,372,373,5,116,0,0,373,
        374,5,101,0,0,374,375,5,100,0,0,375,39,1,0,0,0,376,377,5,112,0,0,
        377,378,5,117,0,0,378,379,5,98,0,0,379,380,5,108,0,0,380,381,5,105,
        0,0,381,382,5,99,0,0,382,41,1,0,0,0,383,384,5,112,0,0,384,385,5,
        114,0,0,385,386,5,105,0,0,386,387,5,118,0,0,387,388,5,97,0,0,388,
        389,5,116,0,0,389,390,5,101,0,0,390,43,1,0,0,0,391,392,5,114,0,0,
        392,393,5,101,0,0,393,394,5,116,0,0,394,395,5,117,0,0,395,396,5,
        114,0,0,396,397,5,110,0,0,397,398,5,115,0,0,398,45,1,0,0,0,399,400,
        5,108,0,0,400,401,5,111,0,0,401,402,5,99,0,0,402,403,5,97,0,0,403,
        404,5,108,0,0,404,405,5,115,0,0,405,47,1,0,0,0,406,407,5,116,0,0,
        407,408,5,104,0,0,408,409,5,114,0,0,409,410,5,111,0,0,410,411,5,
        119,0,0,411,412,5,115,0,0,412,49,1,0,0,0,413,414,5,99,0,0,414,415,
        5,97,0,0,415,416,5,116,0,0,416,417,5,99,0,0,417,418,5,104,0,0,418,
        51,1,0,0,0,419,420,5,102,0,0,420,421,5,105,0,0,421,422,5,110,0,0,
        422,423,5,97,0,0,423,424,5,108,0,0,424,425,5,108,0,0,425,426,5,121,
        0,0,426,53,1,0,0,0,427,428,5,97,0,0,428,429,5,110,0,0,429,430,5,
        110,0,0,430,431,5,111,0,0,431,432,5,116,0,0,432,433,5,97,0,0,433,
        434,5,116,0,0,434,435,5,105,0,0,435,436,5,111,0,0,436,437,5,110,
        0,0,437,438,5,115,0,0,438,55,1,0,0,0,439,440,5,109,0,0,440,441,5,
        111,0,0,441,442,5,100,0,0,442,443,5,101,0,0,443,57,1,0,0,0,444,445,
        3,152,74,0,445,59,1,0,0,0,446,447,3,154,75,0,447,61,1,0,0,0,448,
        449,3,196,96,0,449,63,1,0,0,0,450,451,3,198,97,0,451,65,1,0,0,0,
        452,453,3,160,78,0,453,67,1,0,0,0,454,455,3,162,79,0,455,69,1,0,
        0,0,456,457,3,164,80,0,457,71,1,0,0,0,458,459,3,166,81,0,459,73,
        1,0,0,0,460,461,3,172,84,0,461,75,1,0,0,0,462,463,3,174,85,0,463,
        77,1,0,0,0,464,465,3,176,86,0,465,79,1,0,0,0,466,467,3,178,87,0,
        467,81,1,0,0,0,468,469,3,180,88,0,469,83,1,0,0,0,470,471,3,182,89,
        0,471,85,1,0,0,0,472,473,3,186,91,0,473,87,1,0,0,0,474,475,3,184,
        90,0,475,89,1,0,0,0,476,477,3,192,94,0,477,91,1,0,0,0,478,479,3,
        194,95,0,479,93,1,0,0,0,480,481,3,202,99,0,481,95,1,0,0,0,482,483,
        3,200,98,0,483,97,1,0,0,0,484,485,3,204,100,0,485,99,1,0,0,0,486,
        487,3,206,101,0,487,101,1,0,0,0,488,489,3,208,102,0,489,103,1,0,
        0,0,490,491,3,250,123,0,491,105,1,0,0,0,492,494,3,110,53,0,493,492,
        1,0,0,0,494,495,1,0,0,0,495,493,1,0,0,0,495,496,1,0,0,0,496,497,
        1,0,0,0,497,498,6,51,3,0,498,107,1,0,0,0,499,500,9,0,0,0,500,501,
        1,0,0,0,501,502,6,52,4,0,502,109,1,0,0,0,503,506,3,112,54,0,504,
        506,3,114,55,0,505,503,1,0,0,0,505,504,1,0,0,0,506,111,1,0,0,0,507,
        508,7,1,0,0,508,113,1,0,0,0,509,510,7,2,0,0,510,115,1,0,0,0,511,
        512,5,47,0,0,512,513,5,42,0,0,513,517,1,0,0,0,514,516,9,0,0,0,515,
        514,1,0,0,0,516,519,1,0,0,0,517,518,1,0,0,0,517,515,1,0,0,0,518,
        523,1,0,0,0,519,517,1,0,0,0,520,521,5,42,0,0,521,524,5,47,0,0,522,
        524,5,0,0,1,523,520,1,0,0,0,523,522,1,0,0,0,524,117,1,0,0,0,525,
        526,5,47,0,0,526,527,5,42,0,0,527,528,5,42,0,0,528,532,1,0,0,0,529,
        531,9,0,0,0,530,529,1,0,0,0,531,534,1,0,0,0,532,533,1,0,0,0,532,
        530,1,0,0,0,533,538,1,0,0,0,534,532,1,0,0,0,535,536,5,42,0,0,536,
        539,5,47,0,0,537,539,5,0,0,1,538,535,1,0,0,0,538,537,1,0,0,0,539,
        119,1,0,0,0,540,541,5,47,0,0,541,542,5,47,0,0,542,546,1,0,0,0,543,
        545,8,3,0,0,544,543,1,0,0,0,545,548,1,0,0,0,546,544,1,0,0,0,546,
        547,1,0,0,0,547,121,1,0,0,0,548,546,1,0,0,0,549,554,3,150,73,0,550,
        555,7,4,0,0,551,555,3,126,61,0,552,555,9,0,0,0,553,555,5,0,0,1,554,
        550,1,0,0,0,554,551,1,0,0,0,554,552,1,0,0,0,554,553,1,0,0,0,555,
        123,1,0,0,0,556,557,3,150,73,0,557,558,9,0,0,0,558,125,1,0,0,0,559,
        570,5,117,0,0,560,568,3,130,63,0,561,566,3,130,63,0,562,564,3,130,
        63,0,563,565,3,130,63,0,564,563,1,0,0,0,564,565,1,0,0,0,565,567,
        1,0,0,0,566,562,1,0,0,0,566,567,1,0,0,0,567,569,1,0,0,0,568,561,
        1,0,0,0,568,569,1,0,0,0,569,571,1,0,0,0,570,560,1,0,0,0,570,571,
        1,0,0,0,571,127,1,0,0,0,572,581,5,48,0,0,573,577,7,5,0,0,574,576,
        3,132,64,0,575,574,1,0,0,0,576,579,1,0,0,0,577,575,1,0,0,0,577,578,
        1,0,0,0,578,581,1,0,0,0,579,577,1,0,0,0,580,572,1,0,0,0,580,573,
        1,0,0,0,581,129,1,0,0,0,582,583,7,6,0,0,583,131,1,0,0,0,584,585,
        7,7,0,0,585,133,1,0,0,0,586,587,5,116,0,0,587,588,5,114,0,0,588,
        589,5,117,0,0,589,596,5,101,0,0,590,591,5,102,0,0,591,592,5,97,0,
        0,592,593,5,108,0,0,593,594,5,115,0,0,594,596,5,101,0,0,595,586,
        1,0,0,0,595,590,1,0,0,0,596,135,1,0,0,0,597,600,3,156,76,0,598,601,
        3,122,59,0,599,601,8,8,0,0,600,598,1,0,0,0,600,599,1,0,0,0,601,602,
        1,0,0,0,602,603,3,156,76,0,603,137,1,0,0,0,604,609,3,156,76,0,605,
        608,3,122,59,0,606,608,8,8,0,0,607,605,1,0,0,0,607,606,1,0,0,0,608,
        611,1,0,0,0,609,607,1,0,0,0,609,610,1,0,0,0,610,612,1,0,0,0,611,
        609,1,0,0,0,612,613,3,156,76,0,613,139,1,0,0,0,614,619,3,158,77,
        0,615,618,3,122,59,0,616,618,8,9,0,0,617,615,1,0,0,0,617,616,1,0,
        0,0,618,621,1,0,0,0,619,617,1,0,0,0,619,620,1,0,0,0,620,622,1,0,
        0,0,621,619,1,0,0,0,622,623,3,158,77,0,623,141,1,0,0,0,624,629,3,
        156,76,0,625,628,3,122,59,0,626,628,8,8,0,0,627,625,1,0,0,0,627,
        626,1,0,0,0,628,631,1,0,0,0,629,627,1,0,0,0,629,630,1,0,0,0,630,
        143,1,0,0,0,631,629,1,0,0,0,632,638,3,146,71,0,633,638,2,48,57,0,
        634,638,3,188,92,0,635,638,3,190,93,0,636,638,7,10,0,0,637,632,1,
        0,0,0,637,633,1,0,0,0,637,634,1,0,0,0,637,635,1,0,0,0,637,636,1,
        0,0,0,638,145,1,0,0,0,639,640,7,11,0,0,640,147,1,0,0,0,641,642,5,
        105,0,0,642,643,5,110,0,0,643,644,5,116,0,0,644,149,1,0,0,0,645,
        646,5,92,0,0,646,151,1,0,0,0,647,648,5,58,0,0,648,153,1,0,0,0,649,
        650,5,58,0,0,650,651,5,58,0,0,651,155,1,0,0,0,652,653,5,39,0,0,653,
        157,1,0,0,0,654,655,5,34,0,0,655,159,1,0,0,0,656,657,5,40,0,0,657,
        161,1,0,0,0,658,659,5,41,0,0,659,163,1,0,0,0,660,661,5,123,0,0,661,
        165,1,0,0,0,662,663,5,125,0,0,663,167,1,0,0,0,664,665,5,91,0,0,665,
        169,1,0,0,0,666,667,5,93,0,0,667,171,1,0,0,0,668,669,5,45,0,0,669,
        670,5,62,0,0,670,173,1,0,0,0,671,672,5,60,0,0,672,175,1,0,0,0,673,
        674,5,62,0,0,674,177,1,0,0,0,675,676,5,61,0,0,676,179,1,0,0,0,677,
        678,5,63,0,0,678,181,1,0,0,0,679,680,5,42,0,0,680,183,1,0,0,0,681,
        682,5,43,0,0,682,185,1,0,0,0,683,684,5,43,0,0,684,685,5,61,0,0,685,
        187,1,0,0,0,686,687,5,95,0,0,687,189,1,0,0,0,688,689,5,45,0,0,689,
        191,1,0,0,0,690,691,5,124,0,0,691,193,1,0,0,0,692,693,5,36,0,0,693,
        195,1,0,0,0,694,695,5,44,0,0,695,197,1,0,0,0,696,697,5,59,0,0,697,
        199,1,0,0,0,698,699,5,46,0,0,699,201,1,0,0,0,700,701,5,46,0,0,701,
        702,5,46,0,0,702,203,1,0,0,0,703,704,5,64,0,0,704,205,1,0,0,0,705,
        706,5,35,0,0,706,207,1,0,0,0,707,708,5,126,0,0,708,209,1,0,0,0,709,
        710,3,168,82,0,710,711,1,0,0,0,711,712,6,103,5,0,712,713,6,103,6,
        0,713,211,1,0,0,0,714,715,3,124,60,0,715,716,1,0,0,0,716,717,6,104,
        5,0,717,213,1,0,0,0,718,719,3,140,68,0,719,720,1,0,0,0,720,721,6,
        105,5,0,721,215,1,0,0,0,722,723,3,138,67,0,723,724,1,0,0,0,724,725,
        6,106,5,0,725,217,1,0,0,0,726,727,3,170,83,0,727,728,6,107,7,0,728,
        219,1,0,0,0,729,730,5,0,0,1,730,731,1,0,0,0,731,732,6,108,8,0,732,
        221,1,0,0,0,733,734,9,0,0,0,734,223,1,0,0,0,735,736,3,164,80,0,736,
        737,1,0,0,0,737,738,6,110,9,0,738,739,6,110,2,0,739,225,1,0,0,0,
        740,741,3,124,60,0,741,742,1,0,0,0,742,743,6,111,9,0,743,227,1,0,
        0,0,744,745,3,140,68,0,745,746,1,0,0,0,746,747,6,112,9,0,747,229,
        1,0,0,0,748,749,3,138,67,0,749,750,1,0,0,0,750,751,6,113,9,0,751,
        231,1,0,0,0,752,753,3,118,57,0,753,754,1,0,0,0,754,755,6,114,9,0,
        755,233,1,0,0,0,756,757,3,116,56,0,757,758,1,0,0,0,758,759,6,115,
        9,0,759,235,1,0,0,0,760,761,3,120,58,0,761,762,1,0,0,0,762,763,6,
        116,9,0,763,237,1,0,0,0,764,765,3,166,81,0,765,766,6,117,10,0,766,
        239,1,0,0,0,767,768,5,0,0,1,768,769,1,0,0,0,769,770,6,118,8,0,770,
        241,1,0,0,0,771,772,9,0,0,0,772,243,1,0,0,0,773,776,8,12,0,0,774,
        776,3,124,60,0,775,773,1,0,0,0,775,774,1,0,0,0,776,777,1,0,0,0,777,
        775,1,0,0,0,777,778,1,0,0,0,778,779,1,0,0,0,779,780,6,120,11,0,780,
        245,1,0,0,0,781,782,3,170,83,0,782,783,1,0,0,0,783,784,6,121,8,0,
        784,247,1,0,0,0,785,786,5,0,0,1,786,787,1,0,0,0,787,788,6,122,8,
        0,788,249,1,0,0,0,789,793,3,146,71,0,790,792,3,144,70,0,791,790,
        1,0,0,0,792,795,1,0,0,0,793,791,1,0,0,0,793,794,1,0,0,0,794,251,
        1,0,0,0,795,793,1,0,0,0,796,800,5,34,0,0,797,799,8,13,0,0,798,797,
        1,0,0,0,799,802,1,0,0,0,800,798,1,0,0,0,800,801,1,0,0,0,801,803,
        1,0,0,0,802,800,1,0,0,0,803,813,5,34,0,0,804,808,5,39,0,0,805,807,
        8,14,0,0,806,805,1,0,0,0,807,810,1,0,0,0,808,806,1,0,0,0,808,809,
        1,0,0,0,809,811,1,0,0,0,810,808,1,0,0,0,811,813,5,39,0,0,812,796,
        1,0,0,0,812,804,1,0,0,0,813,253,1,0,0,0,36,0,1,2,3,290,305,322,495,
        505,517,523,532,538,546,554,564,566,568,570,577,580,595,600,607,
        609,617,619,627,629,637,775,777,793,800,808,812,12,0,3,0,1,6,0,5,
        2,0,0,2,0,0,1,0,7,58,0,5,1,0,1,107,1,4,0,0,7,61,0,1,117,2,3,0,0
    ]

class ANTLRv4Lexer(LexerAdaptor):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OFF_CHANNEL = 2
    COMMENT = 3

    Argument = 1
    TargetLanguageAction = 2
    LexerCharSet = 3

    TOKEN_REF = 1
    RULE_REF = 2
    LEXER_CHAR_SET = 3
    DOC_COMMENT = 4
    BLOCK_COMMENT = 5
    LINE_COMMENT = 6
    INT = 7
    STRING_LITERAL = 8
    UNTERMINATED_STRING_LITERAL = 9
    BEGIN_ARGUMENT = 10
    BEGIN_ACTION = 11
    OPTIONS = 12
    TOKENS = 13
    CHANNELS = 14
    IMPORT = 15
    FRAGMENT = 16
    LEXER = 17
    PARSER = 18
    GRAMMAR = 19
    PROTECTED = 20
    PUBLIC = 21
    PRIVATE = 22
    RETURNS = 23
    LOCALS = 24
    THROWS = 25
    CATCH = 26
    FINALLY = 27
    ANNOTATIONS = 28
    MODE = 29
    COLON = 30
    COLONCOLON = 31
    COMMA = 32
    SEMI = 33
    LPAREN = 34
    RPAREN = 35
    LBRACE = 36
    RBRACE = 37
    RARROW = 38
    LT = 39
    GT = 40
    ASSIGN = 41
    QUESTION = 42
    STAR = 43
    PLUS_ASSIGN = 44
    PLUS = 45
    OR = 46
    DOLLAR = 47
    RANGE = 48
    DOT = 49
    AT = 50
    POUND = 51
    NOT = 52
    ID = 53
    WS = 54
    ERRCHAR = 55
    END_ARGUMENT = 56
    UNTERMINATED_ARGUMENT = 57
    ARGUMENT_CONTENT = 58
    END_ACTION = 59
    UNTERMINATED_ACTION = 60
    ACTION_CONTENT = 61
    UNTERMINATED_CHAR_SET = 62
    ANNOTATION_VALUE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"OFF_CHANNEL", 
                                                          u"COMMENT" ]

    modeNames = [ "DEFAULT_MODE", "Argument", "TargetLanguageAction", "LexerCharSet" ]

    literalNames = [ "<INVALID>",
            "'import'", "'fragment'", "'lexer'", "'parser'", "'grammar'", 
            "'protected'", "'public'", "'private'", "'returns'", "'locals'", 
            "'throws'", "'catch'", "'finally'", "'annotations'", "'mode'" ]

    symbolicNames = [ "<INVALID>",
            "TOKEN_REF", "RULE_REF", "LEXER_CHAR_SET", "DOC_COMMENT", "BLOCK_COMMENT", 
            "LINE_COMMENT", "INT", "STRING_LITERAL", "UNTERMINATED_STRING_LITERAL", 
            "BEGIN_ARGUMENT", "BEGIN_ACTION", "OPTIONS", "TOKENS", "CHANNELS", 
            "IMPORT", "FRAGMENT", "LEXER", "PARSER", "GRAMMAR", "PROTECTED", 
            "PUBLIC", "PRIVATE", "RETURNS", "LOCALS", "THROWS", "CATCH", 
            "FINALLY", "ANNOTATIONS", "MODE", "COLON", "COLONCOLON", "COMMA", 
            "SEMI", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "RARROW", "LT", 
            "GT", "ASSIGN", "QUESTION", "STAR", "PLUS_ASSIGN", "PLUS", "OR", 
            "DOLLAR", "RANGE", "DOT", "AT", "POUND", "NOT", "ID", "WS", 
            "ERRCHAR", "END_ARGUMENT", "UNTERMINATED_ARGUMENT", "ARGUMENT_CONTENT", 
            "END_ACTION", "UNTERMINATED_ACTION", "ACTION_CONTENT", "UNTERMINATED_CHAR_SET", 
            "ANNOTATION_VALUE" ]

    ruleNames = [ "DOC_COMMENT", "BLOCK_COMMENT", "LINE_COMMENT", "INT", 
                  "STRING_LITERAL", "UNTERMINATED_STRING_LITERAL", "BEGIN_ARGUMENT", 
                  "BEGIN_ACTION", "OPTIONS", "TOKENS", "CHANNELS", "WSNLCHARS", 
                  "IMPORT", "FRAGMENT", "LEXER", "PARSER", "GRAMMAR", "PROTECTED", 
                  "PUBLIC", "PRIVATE", "RETURNS", "LOCALS", "THROWS", "CATCH", 
                  "FINALLY", "ANNOTATIONS", "MODE", "COLON", "COLONCOLON", 
                  "COMMA", "SEMI", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "RARROW", "LT", "GT", "ASSIGN", "QUESTION", "STAR", "PLUS_ASSIGN", 
                  "PLUS", "OR", "DOLLAR", "RANGE", "DOT", "AT", "POUND", 
                  "NOT", "ID", "WS", "ERRCHAR", "Ws", "Hws", "Vws", "BlockComment", 
                  "DocComment", "LineComment", "EscSeq", "EscAny", "UnicodeEsc", 
                  "DecimalNumeral", "HexDigit", "DecDigit", "BoolLiteral", 
                  "CharLiteral", "SQuoteLiteral", "DQuoteLiteral", "USQuoteLiteral", 
                  "NameChar", "NameStartChar", "Int", "Esc", "Colon", "DColon", 
                  "SQuote", "DQuote", "LParen", "RParen", "LBrace", "RBrace", 
                  "LBrack", "RBrack", "RArrow", "Lt", "Gt", "Equal", "Question", 
                  "Star", "Plus", "PlusAssign", "Underscore", "Dash", "Pipe", 
                  "Dollar", "Comma", "Semi", "Dot", "Range", "At", "Pound", 
                  "Tilde", "NESTED_ARGUMENT", "ARGUMENT_ESCAPE", "ARGUMENT_STRING_LITERAL", 
                  "ARGUMENT_CHAR_LITERAL", "END_ARGUMENT", "UNTERMINATED_ARGUMENT", 
                  "ARGUMENT_CONTENT", "NESTED_ACTION", "ACTION_ESCAPE", 
                  "ACTION_STRING_LITERAL", "ACTION_CHAR_LITERAL", "ACTION_DOC_COMMENT", 
                  "ACTION_BLOCK_COMMENT", "ACTION_LINE_COMMENT", "END_ACTION", 
                  "UNTERMINATED_ACTION", "ACTION_CONTENT", "LEXER_CHAR_SET_BODY", 
                  "LEXER_CHAR_SET", "UNTERMINATED_CHAR_SET", "Id", "ANNOTATION_VALUE" ]

    grammarFileName = "ANTLRv4Lexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.BEGIN_ARGUMENT_action 
            actions[107] = self.END_ARGUMENT_action 
            actions[117] = self.END_ACTION_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def BEGIN_ARGUMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.handleBeginArgument() 
     

    def END_ARGUMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.handleEndArgument() 
     

    def END_ACTION_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             self.handleEndAction() 
     


