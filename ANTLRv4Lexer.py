# Generated from ./Python3/ANTLRv4Lexer.g4 by ANTLR 4.13.1
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
        4,0,61,780,6,-1,6,-1,6,-1,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,
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
        2,119,7,119,2,120,7,120,2,121,7,121,2,122,7,122,1,0,1,0,1,0,1,0,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,
        1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,285,
        8,8,10,8,12,8,288,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,
        9,300,8,9,10,9,12,9,303,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,5,10,317,8,10,10,10,12,10,320,9,10,1,10,1,10,
        1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,
        1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,
        1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,31,1,31,
        1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,1,36,1,36,1,37,1,37,1,38,
        1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,44,1,44,
        1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,4,50,478,
        8,50,11,50,12,50,479,1,50,1,50,1,51,1,51,1,51,1,51,1,52,1,52,3,52,
        490,8,52,1,53,1,53,1,54,1,54,1,55,1,55,1,55,1,55,5,55,500,8,55,10,
        55,12,55,503,9,55,1,55,1,55,1,55,3,55,508,8,55,1,56,1,56,1,56,1,
        56,1,56,5,56,515,8,56,10,56,12,56,518,9,56,1,56,1,56,1,56,3,56,523,
        8,56,1,57,1,57,1,57,1,57,5,57,529,8,57,10,57,12,57,532,9,57,1,58,
        1,58,1,58,1,58,1,58,3,58,539,8,58,1,59,1,59,1,59,1,60,1,60,1,60,
        1,60,1,60,3,60,549,8,60,3,60,551,8,60,3,60,553,8,60,3,60,555,8,60,
        1,61,1,61,1,61,5,61,560,8,61,10,61,12,61,563,9,61,3,61,565,8,61,
        1,62,1,62,1,63,1,63,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,
        3,64,580,8,64,1,65,1,65,1,65,3,65,585,8,65,1,65,1,65,1,66,1,66,1,
        66,5,66,592,8,66,10,66,12,66,595,9,66,1,66,1,66,1,67,1,67,1,67,5,
        67,602,8,67,10,67,12,67,605,9,67,1,67,1,67,1,68,1,68,1,68,5,68,612,
        8,68,10,68,12,68,615,9,68,1,69,1,69,1,69,1,69,1,69,3,69,622,8,69,
        1,70,1,70,1,71,1,71,1,71,1,71,1,72,1,72,1,73,1,73,1,74,1,74,1,74,
        1,75,1,75,1,76,1,76,1,77,1,77,1,78,1,78,1,79,1,79,1,80,1,80,1,81,
        1,81,1,82,1,82,1,83,1,83,1,83,1,84,1,84,1,85,1,85,1,86,1,86,1,87,
        1,87,1,88,1,88,1,89,1,89,1,90,1,90,1,90,1,91,1,91,1,92,1,92,1,93,
        1,93,1,94,1,94,1,95,1,95,1,96,1,96,1,97,1,97,1,98,1,98,1,98,1,99,
        1,99,1,100,1,100,1,101,1,101,1,102,1,102,1,102,1,102,1,102,1,103,
        1,103,1,103,1,103,1,104,1,104,1,104,1,104,1,105,1,105,1,105,1,105,
        1,106,1,106,1,106,1,107,1,107,1,107,1,107,1,108,1,108,1,109,1,109,
        1,109,1,109,1,109,1,110,1,110,1,110,1,110,1,111,1,111,1,111,1,111,
        1,112,1,112,1,112,1,112,1,113,1,113,1,113,1,113,1,114,1,114,1,114,
        1,114,1,115,1,115,1,115,1,115,1,116,1,116,1,116,1,117,1,117,1,117,
        1,117,1,118,1,118,1,119,1,119,4,119,760,8,119,11,119,12,119,761,
        1,119,1,119,1,120,1,120,1,120,1,120,1,121,1,121,1,121,1,121,1,122,
        1,122,5,122,776,8,122,10,122,12,122,779,9,122,2,501,516,0,123,4,
        4,6,5,8,6,10,7,12,8,14,9,16,10,18,11,20,12,22,13,24,14,26,0,28,15,
        30,16,32,17,34,18,36,19,38,20,40,21,42,22,44,23,46,24,48,25,50,26,
        52,27,54,28,56,29,58,30,60,31,62,32,64,33,66,34,68,35,70,36,72,37,
        74,38,76,39,78,40,80,41,82,42,84,43,86,44,88,45,90,46,92,47,94,48,
        96,49,98,50,100,51,102,52,104,53,106,54,108,0,110,0,112,0,114,0,
        116,0,118,0,120,0,122,0,124,0,126,0,128,0,130,0,132,0,134,0,136,
        0,138,0,140,0,142,0,144,0,146,0,148,0,150,0,152,0,154,0,156,0,158,
        0,160,0,162,0,164,0,166,0,168,0,170,0,172,0,174,0,176,0,178,0,180,
        0,182,0,184,0,186,0,188,0,190,0,192,0,194,0,196,0,198,0,200,0,202,
        0,204,0,206,0,208,0,210,0,212,0,214,0,216,55,218,56,220,57,222,0,
        224,0,226,0,228,0,230,0,232,0,234,0,236,58,238,59,240,60,242,0,244,
        3,246,61,248,0,4,0,1,2,3,13,3,0,9,10,12,13,32,32,2,0,9,9,32,32,2,
        0,10,10,12,13,2,0,10,10,13,13,8,0,34,34,39,39,92,92,98,98,102,102,
        110,110,114,114,116,116,1,0,49,57,3,0,48,57,65,70,97,102,1,0,48,
        57,4,0,10,10,13,13,39,39,92,92,4,0,10,10,13,13,34,34,92,92,3,0,183,
        183,768,879,8255,8256,13,0,65,90,97,122,192,214,216,246,248,767,
        880,893,895,8191,8204,8205,8304,8591,11264,12271,12289,55295,63744,
        64975,65008,65533,1,0,92,93,758,0,4,1,0,0,0,0,6,1,0,0,0,0,8,1,0,
        0,0,0,10,1,0,0,0,0,12,1,0,0,0,0,14,1,0,0,0,0,16,1,0,0,0,0,18,1,0,
        0,0,0,20,1,0,0,0,0,22,1,0,0,0,0,24,1,0,0,0,0,28,1,0,0,0,0,30,1,0,
        0,0,0,32,1,0,0,0,0,34,1,0,0,0,0,36,1,0,0,0,0,38,1,0,0,0,0,40,1,0,
        0,0,0,42,1,0,0,0,0,44,1,0,0,0,0,46,1,0,0,0,0,48,1,0,0,0,0,50,1,0,
        0,0,0,52,1,0,0,0,0,54,1,0,0,0,0,56,1,0,0,0,0,58,1,0,0,0,0,60,1,0,
        0,0,0,62,1,0,0,0,0,64,1,0,0,0,0,66,1,0,0,0,0,68,1,0,0,0,0,70,1,0,
        0,0,0,72,1,0,0,0,0,74,1,0,0,0,0,76,1,0,0,0,0,78,1,0,0,0,0,80,1,0,
        0,0,0,82,1,0,0,0,0,84,1,0,0,0,0,86,1,0,0,0,0,88,1,0,0,0,0,90,1,0,
        0,0,0,92,1,0,0,0,0,94,1,0,0,0,0,96,1,0,0,0,0,98,1,0,0,0,0,100,1,
        0,0,0,0,102,1,0,0,0,0,104,1,0,0,0,0,106,1,0,0,0,1,208,1,0,0,0,1,
        210,1,0,0,0,1,212,1,0,0,0,1,214,1,0,0,0,1,216,1,0,0,0,1,218,1,0,
        0,0,1,220,1,0,0,0,2,222,1,0,0,0,2,224,1,0,0,0,2,226,1,0,0,0,2,228,
        1,0,0,0,2,230,1,0,0,0,2,232,1,0,0,0,2,234,1,0,0,0,2,236,1,0,0,0,
        2,238,1,0,0,0,2,240,1,0,0,0,3,242,1,0,0,0,3,244,1,0,0,0,3,246,1,
        0,0,0,4,250,1,0,0,0,6,254,1,0,0,0,8,258,1,0,0,0,10,262,1,0,0,0,12,
        264,1,0,0,0,14,266,1,0,0,0,16,268,1,0,0,0,18,271,1,0,0,0,20,275,
        1,0,0,0,22,291,1,0,0,0,24,306,1,0,0,0,26,323,1,0,0,0,28,325,1,0,
        0,0,30,332,1,0,0,0,32,341,1,0,0,0,34,347,1,0,0,0,36,354,1,0,0,0,
        38,362,1,0,0,0,40,372,1,0,0,0,42,379,1,0,0,0,44,387,1,0,0,0,46,395,
        1,0,0,0,48,402,1,0,0,0,50,409,1,0,0,0,52,415,1,0,0,0,54,423,1,0,
        0,0,56,428,1,0,0,0,58,430,1,0,0,0,60,432,1,0,0,0,62,434,1,0,0,0,
        64,436,1,0,0,0,66,438,1,0,0,0,68,440,1,0,0,0,70,442,1,0,0,0,72,444,
        1,0,0,0,74,446,1,0,0,0,76,448,1,0,0,0,78,450,1,0,0,0,80,452,1,0,
        0,0,82,454,1,0,0,0,84,456,1,0,0,0,86,458,1,0,0,0,88,460,1,0,0,0,
        90,462,1,0,0,0,92,464,1,0,0,0,94,466,1,0,0,0,96,468,1,0,0,0,98,470,
        1,0,0,0,100,472,1,0,0,0,102,474,1,0,0,0,104,477,1,0,0,0,106,483,
        1,0,0,0,108,489,1,0,0,0,110,491,1,0,0,0,112,493,1,0,0,0,114,495,
        1,0,0,0,116,509,1,0,0,0,118,524,1,0,0,0,120,533,1,0,0,0,122,540,
        1,0,0,0,124,543,1,0,0,0,126,564,1,0,0,0,128,566,1,0,0,0,130,568,
        1,0,0,0,132,579,1,0,0,0,134,581,1,0,0,0,136,588,1,0,0,0,138,598,
        1,0,0,0,140,608,1,0,0,0,142,621,1,0,0,0,144,623,1,0,0,0,146,625,
        1,0,0,0,148,629,1,0,0,0,150,631,1,0,0,0,152,633,1,0,0,0,154,636,
        1,0,0,0,156,638,1,0,0,0,158,640,1,0,0,0,160,642,1,0,0,0,162,644,
        1,0,0,0,164,646,1,0,0,0,166,648,1,0,0,0,168,650,1,0,0,0,170,652,
        1,0,0,0,172,655,1,0,0,0,174,657,1,0,0,0,176,659,1,0,0,0,178,661,
        1,0,0,0,180,663,1,0,0,0,182,665,1,0,0,0,184,667,1,0,0,0,186,670,
        1,0,0,0,188,672,1,0,0,0,190,674,1,0,0,0,192,676,1,0,0,0,194,678,
        1,0,0,0,196,680,1,0,0,0,198,682,1,0,0,0,200,684,1,0,0,0,202,687,
        1,0,0,0,204,689,1,0,0,0,206,691,1,0,0,0,208,693,1,0,0,0,210,698,
        1,0,0,0,212,702,1,0,0,0,214,706,1,0,0,0,216,710,1,0,0,0,218,713,
        1,0,0,0,220,717,1,0,0,0,222,719,1,0,0,0,224,724,1,0,0,0,226,728,
        1,0,0,0,228,732,1,0,0,0,230,736,1,0,0,0,232,740,1,0,0,0,234,744,
        1,0,0,0,236,748,1,0,0,0,238,751,1,0,0,0,240,755,1,0,0,0,242,759,
        1,0,0,0,244,765,1,0,0,0,246,769,1,0,0,0,248,773,1,0,0,0,250,251,
        3,116,56,0,251,252,1,0,0,0,252,253,6,0,0,0,253,5,1,0,0,0,254,255,
        3,114,55,0,255,256,1,0,0,0,256,257,6,1,0,0,257,7,1,0,0,0,258,259,
        3,118,57,0,259,260,1,0,0,0,260,261,6,2,0,0,261,9,1,0,0,0,262,263,
        3,126,61,0,263,11,1,0,0,0,264,265,3,136,66,0,265,13,1,0,0,0,266,
        267,3,140,68,0,267,15,1,0,0,0,268,269,3,166,81,0,269,270,6,6,1,0,
        270,17,1,0,0,0,271,272,3,162,79,0,272,273,1,0,0,0,273,274,6,7,2,
        0,274,19,1,0,0,0,275,276,5,111,0,0,276,277,5,112,0,0,277,278,5,116,
        0,0,278,279,5,105,0,0,279,280,5,111,0,0,280,281,5,110,0,0,281,282,
        5,115,0,0,282,286,1,0,0,0,283,285,3,26,11,0,284,283,1,0,0,0,285,
        288,1,0,0,0,286,284,1,0,0,0,286,287,1,0,0,0,287,289,1,0,0,0,288,
        286,1,0,0,0,289,290,5,123,0,0,290,21,1,0,0,0,291,292,5,116,0,0,292,
        293,5,111,0,0,293,294,5,107,0,0,294,295,5,101,0,0,295,296,5,110,
        0,0,296,297,5,115,0,0,297,301,1,0,0,0,298,300,3,26,11,0,299,298,
        1,0,0,0,300,303,1,0,0,0,301,299,1,0,0,0,301,302,1,0,0,0,302,304,
        1,0,0,0,303,301,1,0,0,0,304,305,5,123,0,0,305,23,1,0,0,0,306,307,
        5,99,0,0,307,308,5,104,0,0,308,309,5,97,0,0,309,310,5,110,0,0,310,
        311,5,110,0,0,311,312,5,101,0,0,312,313,5,108,0,0,313,314,5,115,
        0,0,314,318,1,0,0,0,315,317,3,26,11,0,316,315,1,0,0,0,317,320,1,
        0,0,0,318,316,1,0,0,0,318,319,1,0,0,0,319,321,1,0,0,0,320,318,1,
        0,0,0,321,322,5,123,0,0,322,25,1,0,0,0,323,324,7,0,0,0,324,27,1,
        0,0,0,325,326,5,105,0,0,326,327,5,109,0,0,327,328,5,112,0,0,328,
        329,5,111,0,0,329,330,5,114,0,0,330,331,5,116,0,0,331,29,1,0,0,0,
        332,333,5,102,0,0,333,334,5,114,0,0,334,335,5,97,0,0,335,336,5,103,
        0,0,336,337,5,109,0,0,337,338,5,101,0,0,338,339,5,110,0,0,339,340,
        5,116,0,0,340,31,1,0,0,0,341,342,5,108,0,0,342,343,5,101,0,0,343,
        344,5,120,0,0,344,345,5,101,0,0,345,346,5,114,0,0,346,33,1,0,0,0,
        347,348,5,112,0,0,348,349,5,97,0,0,349,350,5,114,0,0,350,351,5,115,
        0,0,351,352,5,101,0,0,352,353,5,114,0,0,353,35,1,0,0,0,354,355,5,
        103,0,0,355,356,5,114,0,0,356,357,5,97,0,0,357,358,5,109,0,0,358,
        359,5,109,0,0,359,360,5,97,0,0,360,361,5,114,0,0,361,37,1,0,0,0,
        362,363,5,112,0,0,363,364,5,114,0,0,364,365,5,111,0,0,365,366,5,
        116,0,0,366,367,5,101,0,0,367,368,5,99,0,0,368,369,5,116,0,0,369,
        370,5,101,0,0,370,371,5,100,0,0,371,39,1,0,0,0,372,373,5,112,0,0,
        373,374,5,117,0,0,374,375,5,98,0,0,375,376,5,108,0,0,376,377,5,105,
        0,0,377,378,5,99,0,0,378,41,1,0,0,0,379,380,5,112,0,0,380,381,5,
        114,0,0,381,382,5,105,0,0,382,383,5,118,0,0,383,384,5,97,0,0,384,
        385,5,116,0,0,385,386,5,101,0,0,386,43,1,0,0,0,387,388,5,114,0,0,
        388,389,5,101,0,0,389,390,5,116,0,0,390,391,5,117,0,0,391,392,5,
        114,0,0,392,393,5,110,0,0,393,394,5,115,0,0,394,45,1,0,0,0,395,396,
        5,108,0,0,396,397,5,111,0,0,397,398,5,99,0,0,398,399,5,97,0,0,399,
        400,5,108,0,0,400,401,5,115,0,0,401,47,1,0,0,0,402,403,5,116,0,0,
        403,404,5,104,0,0,404,405,5,114,0,0,405,406,5,111,0,0,406,407,5,
        119,0,0,407,408,5,115,0,0,408,49,1,0,0,0,409,410,5,99,0,0,410,411,
        5,97,0,0,411,412,5,116,0,0,412,413,5,99,0,0,413,414,5,104,0,0,414,
        51,1,0,0,0,415,416,5,102,0,0,416,417,5,105,0,0,417,418,5,110,0,0,
        418,419,5,97,0,0,419,420,5,108,0,0,420,421,5,108,0,0,421,422,5,121,
        0,0,422,53,1,0,0,0,423,424,5,109,0,0,424,425,5,111,0,0,425,426,5,
        100,0,0,426,427,5,101,0,0,427,55,1,0,0,0,428,429,3,150,73,0,429,
        57,1,0,0,0,430,431,3,152,74,0,431,59,1,0,0,0,432,433,3,194,95,0,
        433,61,1,0,0,0,434,435,3,196,96,0,435,63,1,0,0,0,436,437,3,158,77,
        0,437,65,1,0,0,0,438,439,3,160,78,0,439,67,1,0,0,0,440,441,3,162,
        79,0,441,69,1,0,0,0,442,443,3,164,80,0,443,71,1,0,0,0,444,445,3,
        170,83,0,445,73,1,0,0,0,446,447,3,172,84,0,447,75,1,0,0,0,448,449,
        3,174,85,0,449,77,1,0,0,0,450,451,3,176,86,0,451,79,1,0,0,0,452,
        453,3,178,87,0,453,81,1,0,0,0,454,455,3,180,88,0,455,83,1,0,0,0,
        456,457,3,184,90,0,457,85,1,0,0,0,458,459,3,182,89,0,459,87,1,0,
        0,0,460,461,3,190,93,0,461,89,1,0,0,0,462,463,3,192,94,0,463,91,
        1,0,0,0,464,465,3,200,98,0,465,93,1,0,0,0,466,467,3,198,97,0,467,
        95,1,0,0,0,468,469,3,202,99,0,469,97,1,0,0,0,470,471,3,204,100,0,
        471,99,1,0,0,0,472,473,3,206,101,0,473,101,1,0,0,0,474,475,3,248,
        122,0,475,103,1,0,0,0,476,478,3,108,52,0,477,476,1,0,0,0,478,479,
        1,0,0,0,479,477,1,0,0,0,479,480,1,0,0,0,480,481,1,0,0,0,481,482,
        6,50,3,0,482,105,1,0,0,0,483,484,9,0,0,0,484,485,1,0,0,0,485,486,
        6,51,4,0,486,107,1,0,0,0,487,490,3,110,53,0,488,490,3,112,54,0,489,
        487,1,0,0,0,489,488,1,0,0,0,490,109,1,0,0,0,491,492,7,1,0,0,492,
        111,1,0,0,0,493,494,7,2,0,0,494,113,1,0,0,0,495,496,5,47,0,0,496,
        497,5,42,0,0,497,501,1,0,0,0,498,500,9,0,0,0,499,498,1,0,0,0,500,
        503,1,0,0,0,501,502,1,0,0,0,501,499,1,0,0,0,502,507,1,0,0,0,503,
        501,1,0,0,0,504,505,5,42,0,0,505,508,5,47,0,0,506,508,5,0,0,1,507,
        504,1,0,0,0,507,506,1,0,0,0,508,115,1,0,0,0,509,510,5,47,0,0,510,
        511,5,42,0,0,511,512,5,42,0,0,512,516,1,0,0,0,513,515,9,0,0,0,514,
        513,1,0,0,0,515,518,1,0,0,0,516,517,1,0,0,0,516,514,1,0,0,0,517,
        522,1,0,0,0,518,516,1,0,0,0,519,520,5,42,0,0,520,523,5,47,0,0,521,
        523,5,0,0,1,522,519,1,0,0,0,522,521,1,0,0,0,523,117,1,0,0,0,524,
        525,5,47,0,0,525,526,5,47,0,0,526,530,1,0,0,0,527,529,8,3,0,0,528,
        527,1,0,0,0,529,532,1,0,0,0,530,528,1,0,0,0,530,531,1,0,0,0,531,
        119,1,0,0,0,532,530,1,0,0,0,533,538,3,148,72,0,534,539,7,4,0,0,535,
        539,3,124,60,0,536,539,9,0,0,0,537,539,5,0,0,1,538,534,1,0,0,0,538,
        535,1,0,0,0,538,536,1,0,0,0,538,537,1,0,0,0,539,121,1,0,0,0,540,
        541,3,148,72,0,541,542,9,0,0,0,542,123,1,0,0,0,543,554,5,117,0,0,
        544,552,3,128,62,0,545,550,3,128,62,0,546,548,3,128,62,0,547,549,
        3,128,62,0,548,547,1,0,0,0,548,549,1,0,0,0,549,551,1,0,0,0,550,546,
        1,0,0,0,550,551,1,0,0,0,551,553,1,0,0,0,552,545,1,0,0,0,552,553,
        1,0,0,0,553,555,1,0,0,0,554,544,1,0,0,0,554,555,1,0,0,0,555,125,
        1,0,0,0,556,565,5,48,0,0,557,561,7,5,0,0,558,560,3,130,63,0,559,
        558,1,0,0,0,560,563,1,0,0,0,561,559,1,0,0,0,561,562,1,0,0,0,562,
        565,1,0,0,0,563,561,1,0,0,0,564,556,1,0,0,0,564,557,1,0,0,0,565,
        127,1,0,0,0,566,567,7,6,0,0,567,129,1,0,0,0,568,569,7,7,0,0,569,
        131,1,0,0,0,570,571,5,116,0,0,571,572,5,114,0,0,572,573,5,117,0,
        0,573,580,5,101,0,0,574,575,5,102,0,0,575,576,5,97,0,0,576,577,5,
        108,0,0,577,578,5,115,0,0,578,580,5,101,0,0,579,570,1,0,0,0,579,
        574,1,0,0,0,580,133,1,0,0,0,581,584,3,154,75,0,582,585,3,120,58,
        0,583,585,8,8,0,0,584,582,1,0,0,0,584,583,1,0,0,0,585,586,1,0,0,
        0,586,587,3,154,75,0,587,135,1,0,0,0,588,593,3,154,75,0,589,592,
        3,120,58,0,590,592,8,8,0,0,591,589,1,0,0,0,591,590,1,0,0,0,592,595,
        1,0,0,0,593,591,1,0,0,0,593,594,1,0,0,0,594,596,1,0,0,0,595,593,
        1,0,0,0,596,597,3,154,75,0,597,137,1,0,0,0,598,603,3,156,76,0,599,
        602,3,120,58,0,600,602,8,9,0,0,601,599,1,0,0,0,601,600,1,0,0,0,602,
        605,1,0,0,0,603,601,1,0,0,0,603,604,1,0,0,0,604,606,1,0,0,0,605,
        603,1,0,0,0,606,607,3,156,76,0,607,139,1,0,0,0,608,613,3,154,75,
        0,609,612,3,120,58,0,610,612,8,8,0,0,611,609,1,0,0,0,611,610,1,0,
        0,0,612,615,1,0,0,0,613,611,1,0,0,0,613,614,1,0,0,0,614,141,1,0,
        0,0,615,613,1,0,0,0,616,622,3,144,70,0,617,622,2,48,57,0,618,622,
        3,186,91,0,619,622,3,188,92,0,620,622,7,10,0,0,621,616,1,0,0,0,621,
        617,1,0,0,0,621,618,1,0,0,0,621,619,1,0,0,0,621,620,1,0,0,0,622,
        143,1,0,0,0,623,624,7,11,0,0,624,145,1,0,0,0,625,626,5,105,0,0,626,
        627,5,110,0,0,627,628,5,116,0,0,628,147,1,0,0,0,629,630,5,92,0,0,
        630,149,1,0,0,0,631,632,5,58,0,0,632,151,1,0,0,0,633,634,5,58,0,
        0,634,635,5,58,0,0,635,153,1,0,0,0,636,637,5,39,0,0,637,155,1,0,
        0,0,638,639,5,34,0,0,639,157,1,0,0,0,640,641,5,40,0,0,641,159,1,
        0,0,0,642,643,5,41,0,0,643,161,1,0,0,0,644,645,5,123,0,0,645,163,
        1,0,0,0,646,647,5,125,0,0,647,165,1,0,0,0,648,649,5,91,0,0,649,167,
        1,0,0,0,650,651,5,93,0,0,651,169,1,0,0,0,652,653,5,45,0,0,653,654,
        5,62,0,0,654,171,1,0,0,0,655,656,5,60,0,0,656,173,1,0,0,0,657,658,
        5,62,0,0,658,175,1,0,0,0,659,660,5,61,0,0,660,177,1,0,0,0,661,662,
        5,63,0,0,662,179,1,0,0,0,663,664,5,42,0,0,664,181,1,0,0,0,665,666,
        5,43,0,0,666,183,1,0,0,0,667,668,5,43,0,0,668,669,5,61,0,0,669,185,
        1,0,0,0,670,671,5,95,0,0,671,187,1,0,0,0,672,673,5,45,0,0,673,189,
        1,0,0,0,674,675,5,124,0,0,675,191,1,0,0,0,676,677,5,36,0,0,677,193,
        1,0,0,0,678,679,5,44,0,0,679,195,1,0,0,0,680,681,5,59,0,0,681,197,
        1,0,0,0,682,683,5,46,0,0,683,199,1,0,0,0,684,685,5,46,0,0,685,686,
        5,46,0,0,686,201,1,0,0,0,687,688,5,64,0,0,688,203,1,0,0,0,689,690,
        5,35,0,0,690,205,1,0,0,0,691,692,5,126,0,0,692,207,1,0,0,0,693,694,
        3,166,81,0,694,695,1,0,0,0,695,696,6,102,5,0,696,697,6,102,6,0,697,
        209,1,0,0,0,698,699,3,122,59,0,699,700,1,0,0,0,700,701,6,103,5,0,
        701,211,1,0,0,0,702,703,3,138,67,0,703,704,1,0,0,0,704,705,6,104,
        5,0,705,213,1,0,0,0,706,707,3,136,66,0,707,708,1,0,0,0,708,709,6,
        105,5,0,709,215,1,0,0,0,710,711,3,168,82,0,711,712,6,106,7,0,712,
        217,1,0,0,0,713,714,5,0,0,1,714,715,1,0,0,0,715,716,6,107,8,0,716,
        219,1,0,0,0,717,718,9,0,0,0,718,221,1,0,0,0,719,720,3,162,79,0,720,
        721,1,0,0,0,721,722,6,109,9,0,722,723,6,109,2,0,723,223,1,0,0,0,
        724,725,3,122,59,0,725,726,1,0,0,0,726,727,6,110,9,0,727,225,1,0,
        0,0,728,729,3,138,67,0,729,730,1,0,0,0,730,731,6,111,9,0,731,227,
        1,0,0,0,732,733,3,136,66,0,733,734,1,0,0,0,734,735,6,112,9,0,735,
        229,1,0,0,0,736,737,3,116,56,0,737,738,1,0,0,0,738,739,6,113,9,0,
        739,231,1,0,0,0,740,741,3,114,55,0,741,742,1,0,0,0,742,743,6,114,
        9,0,743,233,1,0,0,0,744,745,3,118,57,0,745,746,1,0,0,0,746,747,6,
        115,9,0,747,235,1,0,0,0,748,749,3,164,80,0,749,750,6,116,10,0,750,
        237,1,0,0,0,751,752,5,0,0,1,752,753,1,0,0,0,753,754,6,117,8,0,754,
        239,1,0,0,0,755,756,9,0,0,0,756,241,1,0,0,0,757,760,8,12,0,0,758,
        760,3,122,59,0,759,757,1,0,0,0,759,758,1,0,0,0,760,761,1,0,0,0,761,
        759,1,0,0,0,761,762,1,0,0,0,762,763,1,0,0,0,763,764,6,119,11,0,764,
        243,1,0,0,0,765,766,3,168,82,0,766,767,1,0,0,0,767,768,6,120,8,0,
        768,245,1,0,0,0,769,770,5,0,0,1,770,771,1,0,0,0,771,772,6,121,8,
        0,772,247,1,0,0,0,773,777,3,144,70,0,774,776,3,142,69,0,775,774,
        1,0,0,0,776,779,1,0,0,0,777,775,1,0,0,0,777,778,1,0,0,0,778,249,
        1,0,0,0,779,777,1,0,0,0,33,0,1,2,3,286,301,318,479,489,501,507,516,
        522,530,538,548,550,552,554,561,564,579,584,591,593,601,603,611,
        613,621,759,761,777,12,0,3,0,1,6,0,5,2,0,0,2,0,0,1,0,7,57,0,5,1,
        0,1,106,1,4,0,0,7,60,0,1,116,2,3,0,0
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
    MODE = 28
    COLON = 29
    COLONCOLON = 30
    COMMA = 31
    SEMI = 32
    LPAREN = 33
    RPAREN = 34
    LBRACE = 35
    RBRACE = 36
    RARROW = 37
    LT = 38
    GT = 39
    ASSIGN = 40
    QUESTION = 41
    STAR = 42
    PLUS_ASSIGN = 43
    PLUS = 44
    OR = 45
    DOLLAR = 46
    RANGE = 47
    DOT = 48
    AT = 49
    POUND = 50
    NOT = 51
    ID = 52
    WS = 53
    ERRCHAR = 54
    END_ARGUMENT = 55
    UNTERMINATED_ARGUMENT = 56
    ARGUMENT_CONTENT = 57
    END_ACTION = 58
    UNTERMINATED_ACTION = 59
    ACTION_CONTENT = 60
    UNTERMINATED_CHAR_SET = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"OFF_CHANNEL", 
                                                          u"COMMENT" ]

    modeNames = [ "DEFAULT_MODE", "Argument", "TargetLanguageAction", "LexerCharSet" ]

    literalNames = [ "<INVALID>",
            "'import'", "'fragment'", "'lexer'", "'parser'", "'grammar'", 
            "'protected'", "'public'", "'private'", "'returns'", "'locals'", 
            "'throws'", "'catch'", "'finally'", "'mode'" ]

    symbolicNames = [ "<INVALID>",
            "TOKEN_REF", "RULE_REF", "LEXER_CHAR_SET", "DOC_COMMENT", "BLOCK_COMMENT", 
            "LINE_COMMENT", "INT", "STRING_LITERAL", "UNTERMINATED_STRING_LITERAL", 
            "BEGIN_ARGUMENT", "BEGIN_ACTION", "OPTIONS", "TOKENS", "CHANNELS", 
            "IMPORT", "FRAGMENT", "LEXER", "PARSER", "GRAMMAR", "PROTECTED", 
            "PUBLIC", "PRIVATE", "RETURNS", "LOCALS", "THROWS", "CATCH", 
            "FINALLY", "MODE", "COLON", "COLONCOLON", "COMMA", "SEMI", "LPAREN", 
            "RPAREN", "LBRACE", "RBRACE", "RARROW", "LT", "GT", "ASSIGN", 
            "QUESTION", "STAR", "PLUS_ASSIGN", "PLUS", "OR", "DOLLAR", "RANGE", 
            "DOT", "AT", "POUND", "NOT", "ID", "WS", "ERRCHAR", "END_ARGUMENT", 
            "UNTERMINATED_ARGUMENT", "ARGUMENT_CONTENT", "END_ACTION", "UNTERMINATED_ACTION", 
            "ACTION_CONTENT", "UNTERMINATED_CHAR_SET" ]

    ruleNames = [ "DOC_COMMENT", "BLOCK_COMMENT", "LINE_COMMENT", "INT", 
                  "STRING_LITERAL", "UNTERMINATED_STRING_LITERAL", "BEGIN_ARGUMENT", 
                  "BEGIN_ACTION", "OPTIONS", "TOKENS", "CHANNELS", "WSNLCHARS", 
                  "IMPORT", "FRAGMENT", "LEXER", "PARSER", "GRAMMAR", "PROTECTED", 
                  "PUBLIC", "PRIVATE", "RETURNS", "LOCALS", "THROWS", "CATCH", 
                  "FINALLY", "MODE", "COLON", "COLONCOLON", "COMMA", "SEMI", 
                  "LPAREN", "RPAREN", "LBRACE", "RBRACE", "RARROW", "LT", 
                  "GT", "ASSIGN", "QUESTION", "STAR", "PLUS_ASSIGN", "PLUS", 
                  "OR", "DOLLAR", "RANGE", "DOT", "AT", "POUND", "NOT", 
                  "ID", "WS", "ERRCHAR", "Ws", "Hws", "Vws", "BlockComment", 
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
                  "LEXER_CHAR_SET", "UNTERMINATED_CHAR_SET", "Id" ]

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
            actions[106] = self.END_ARGUMENT_action 
            actions[116] = self.END_ACTION_action 
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
     


