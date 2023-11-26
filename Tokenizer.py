import sys
import re
import os


# Token dari syntax ke token
tokenExprs = [
    (r'[ \t]+', None),          # spaces
    (r'<!--[\s\S]*?-->', None),  # comment
    (r'\n', None),
    (r'\<', "kd"),              # kurang dari
    (r'\>', "ld"),              # lebih dari


    #tags
    (r'\bhtml\b', "html"),
    (r'/\bhtml\b', "chtml"),
    (r'\bhead\b', "head"),
    (r'/\bhead\b', "chead"),
    (r'\bbody\b', "body"),
    (r'/\bbody\b', "cbody"),
    (r'\btitle\b', "title"),
    (r'/\btitle\b', "ctitle"),
    (r'\blink\b', "link"),
    (r'\bscript\b', "script"),
    (r'/\bscript\b', "cscript"),
    (r'\bh1\b', "h1"),
    (r'/\bh1\b', "ch1"),
    (r'\bh2\b', "h2"),
    (r'/\bh2\b', "ch2"),
    (r'\bh3\b', "h3"),
    (r'/\bh3\b', "ch3"),
    (r'\bh4\b', "h4"),
    (r'/\bh4\b', "ch4"),
    (r'\bh5\b', "h5"),
    (r'/\bh5\b', "ch5"),
    (r'\bh6\b', "h6"),
    (r'/\bh6\b', "ch6"),
    (r'\bbr\b', "br"),
    (r'\bem\b', "em"),
    (r'/\bem\b', "cem"),
    (r'\bb\b', "b"),
    (r'/\bb\b', "cb"),
    (r'\babbr\b', "abbr"),
    (r'/\babbr\b', "cabbr"),
    (r'\bstrong\b', "strong"),
    (r'/\bstrong\b', "cstrong"),
    (r'\bsmall\b', "small"),
    (r'/\bsmall\b', "csmall"),
    (r'\bhr\b', "hr"),
    (r'\ba\b', "a"),
    (r'/\ba\b', "ca"),
    (r'\bimg\b', "img"),
    (r'\bbutton\b', "button"),
    (r'/\bbutton\b', "cbutton"),
    (r'\bform\b', "form"),
    (r'/\bform\b', "cform"),
    (r'\binput\b', "input"),
    (r'\btable\b', "table"),
    (r'/\btable\b', "ctable"),
    (r'\btr\b', "tr"),
    (r'/\btr\b', "ctr"),
    (r'\btd\b', "td"),
    (r'/\btd\b', "ctd"),
    (r'\bth\b', "th"),
    (r'/\bth\b', "cth"),
    (r'\bp\b', "p"),
    (r'/\bp\b', "cp"),
    (r'\bdiv\b', "div"),
    (r'/\bdiv\b', "cdiv"),

    #attributes
    (r'id="([^"]*)"', "id"),
    (r'class="([^"]*)"', "class"),
    (r'style="([^"]*)"', "style"),
    (r'href="([^"]*)"', "href"),
    (r'ref="([^"]*)"', "ref"),
    (r'src="([^"]*)"', "src"),
    (r'alt="([^"]*)"', "alt"),
    (r'type="(submit|reset|button)"', "typeb"), #attribut type untuk button
    (r'action="([^"]*)"', "action"),
    (r'method="(GET|POST)"', "method"),
    (r'type="(text|password|email|number|checkbox)"', "typei"),

    (r'([^<>]*)', "content"),  # content between tags and other typos
    
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

    return tokenResult