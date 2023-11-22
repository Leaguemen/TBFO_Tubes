import sys
import re
from fa import *
import os


# Token dari syntax ke token
tokenExprs = [
    (r'[ \t]+', None),          # spaces
    (r'<!--[\s\S]*?-->', None),  # comment
    (r'\n', None),
    (r'\<', "KD"),              # kurang dari
    (r'\>', "LD"),              # lebih dari


    #tags
    (r'\bhtml\b', "HTML"),
    (r'/\bhtml\b', "CHTML"),
    (r'\bhead\b', "HEAD"),
    (r'/\bhead\b', "CHEAD"),
    (r'\bbody\b', "BODY"),
    (r'/\bbody\b', "CBODY"),
    (r'\btitle\b', "TITLE"),
    (r'/\btitle\b', "CTITLE"),
    (r'\blink\b', "LINK"),
    (r'\bscript\b', "SCRIPT"),
    (r'\bh1\b', "H1"),
    (r'/\bh1\b', "CH1"),
    (r'\bh2\b', "H2"),
    (r'/\bh2\b', "CH2"),
    (r'\bh3\b', "H3"),
    (r'/\bh3\b', "CH3"),
    (r'\bh4\b', "H4"),
    (r'/\bh4\b', "CH4"),
    (r'\bh5\b', "H5"),
    (r'/\bh5\b', "CH5"),
    (r'\bh6\b', "H6"),
    (r'/\bh6\b', "CH6"),
    (r'\bbr\b', "BR"),
    (r'\bem\b', "EM"),
    (r'/\bem\b', "CEM"),
    (r'\bb\b', "B"),
    (r'/\bb\b', "CB"),
    (r'\babbr\b', "ABBR"),
    (r'/\babbr\b', "CABBR"),
    (r'\bstrong\b', "STR"),
    (r'/\bstrong\b', "CSTR"),
    (r'\bsmall\b', "SML"),
    (r'/\bsmall\b', "CSML"),
    (r'\bhr\b', "HR"),
    (r'\ba\b', "A"),
    (r'/\ba\b', "CA"),
    (r'\bimg\b', "IMG"),
    (r'\bbutton\b', "BUT"),
    (r'/\bbutton\b', "CBUT"),
    (r'\bform\b', "FORM"),
    (r'/\bform\b', "CFORM"),
    (r'\binput\b', "INP"),
    (r'\btable\b', "TBL"),
    (r'/\btable\b', "CTBL"),
    (r'\btr\b', "TR"),
    (r'/\btr\b', "CTR"),
    (r'\btd\b', "TD"),
    (r'/\btd\b', "CTD"),
    (r'\bth\b', "TH"),
    (r'/\bth\b', "CTH"),
    (r'\bp\b', "P"),
    (r'/\bp\b', "CP"),
    (r'\bdiv\b', "DIV"),
    (r'/\bdiv\b', "CP"),

    #attributes
    (r'id="([^"]*)"', "ID"),
    (r'class="([^"]*)"', "CLASS"),
    (r'style="([^"]*)"', "STYLE"),
    (r'href="([^"]*)"', "HREF"),
    (r'ref="([^"]*)"', "REL"),
    (r'src="([^"]*)"', "SRC"),
    (r'alt="([^"]*)"', "ALT"),
    (r'type="(submit|reset|button)"', "TYPEB"), #attribut type untuk button
    (r'action="([^"]*)"', "ACT"),
    (r'method="(GET|POST)"', "MET"),
    (r'type="(text|password|email|number|checkbox)"', "TYPEI"),

    (r'([^<>]*)', "CONTENT"),  # content between tags
    
]

def tokenize(text, tokenExprs):
    # Current column, position, and line
    currCol = 0
    currPos = 0
    currLine = 1

    # Token result
    tokens = []

    while currCol < len(text):
        if text[currCol] == "\n":
            currLine += 1
            currPos = 1

        isMatch = None

        for tokenExpr in tokenExprs:
            pattern, tag = tokenExpr
            regex = re.compile(pattern)
            isMatch = regex.match(text, currCol)
            if isMatch:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not isMatch:
            print(f"\n\033[91mSyntax error\033[0m\nTerdapat karakter tidak valid \033[91m{text[currCol]}\033[0m pada baris {currLine}")
            sys.exit(1)
        else:
            currCol = isMatch.end(0)
        currPos += 1

    return tokens

def createToken(fileName):
    # Open and read file
    file = open(fileName, encoding="utf8")
    text = file.read()
    file.close()

    tokens = tokenize(text, tokenExprs)
    tokenResult = []


    for token in tokens:
        tokenResult.append(token)

    # # Write file testing
    # path = os.getcwd()
    # fileWrite = open(path + "/result/tokenResult.txt", 'w')
    # for token in tokenResult:
    #     fileWrite.write(str(token)+" ")
    #     # print(token)
    # fileWrite.close()

    return " ".join(tokenResult)

if __name__ == "__main__": 
    path = os.getcwd()
    print(createToken(path + "/test/inputAcc.txt"))