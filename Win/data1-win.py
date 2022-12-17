import argparse
_parser = argparse.ArgumentParser(
    exit_on_error=1, description=' --execution file--'
)
_parser.add_argument('--letter',
                     help=' --execiution file--'
                     )
_parser.add_argument('--translation',
                     help=' --execiution file--'
                     )
_arg = _parser.parse_args()

file = open('write.txt','a')

if _arg.translation == 'lttr':
    if _arg.letter == 'a':
        file.write('fa')
    elif _arg.letter == 'b':
       file.write('fe')
    elif _arg.letter == 'c':
      file.write('fu')
    elif _arg.letter == 'd':
        file.write('ja')
    elif _arg.letter == 'e':
        file.write('je')
    elif _arg.letter == 'f':
        file.write('ju')
    elif _arg.letter == 'g':
        file.write('ka')
    elif _arg.letter == 'h':
       file.write('ke')
    elif _arg.letter == 'i':
       file.write('ku')
    elif _arg.letter == 'j':
       file.write('na')
    elif _arg.letter == 'k':
     file.write('ne')
    elif _arg.letter == 'l':
      file.write('nu')
    elif _arg.letter == 'm':
        file.write('ra')
    elif _arg.letter == 'n':
        file.write('re')
    elif _arg.letter == 'o':
       file.write('ru')
    elif _arg.letter == 'p':
        file.write('sa')
    elif _arg.letter == 'q':
       file.write('se')
    elif _arg.letter == 'r':
       file.write('su')
    elif _arg.letter == 's':
       file.write('ta')
    elif _arg.letter == 't':
       file.write('te')
    elif _arg.letter == 'u':
       file.write('tu')
    elif _arg.letter == 'v':
       file.write('za')
    elif _arg.letter == 'w':
        file.write('ze')
    elif _arg.letter == 'x':
        file.write('zu')
    elif _arg.letter == 'y':
        file.write('ga')
    elif _arg.letter == 'z':
        file.write('ge')

    elif _arg.letter == ' ':
       file.write(' ')
    elif _arg.letter == ',':
        file.write(',')
    elif _arg.letter == '.':
       file.write('.')
    elif _arg.letter == '(':
        file.write('(')
    elif _arg.letter == ')':
       file.write(')')
    elif _arg.letter == ';':
       file.write(';')
    elif _arg.letter == ':':
       file.write(':')
    elif _arg.letter == '/':
        file.write('/')
    elif _arg.letter == '?':
        file.write('?')
    elif _arg.letter == '\'':
        file.write('\'')
    elif _arg.letter == '[':
        file.write('[')
    elif _arg.letter == ']':
        file.write(']')
    elif _arg.letter == '\\':
        file.write('\\')
    elif _arg.letter == '<':
        file.write('<')
    elif _arg.letter == '>':
        file.write('>')
    elif _arg.letter == '"':
        file.write('"')
    elif _arg.letter == '{':
        file.write('{')
    elif _arg.letter == '}':
        file.write('}')
    elif _arg.letter == '|':
        file.write('|')

    elif _arg.letter == '!':
       file.write('!')
    elif _arg.letter == '@':
       file.write('@')
    elif _arg.letter == '#':
       file.write('#')
    elif _arg.letter == '$':
       file.write('$')
    elif _arg.letter == '%':
       file.write('%')
    elif _arg.letter == '^':
       file.write('^')
    elif _arg.letter == '&':
       file.write('&')
    elif _arg.letter == '*':
       file.write('*')
    elif _arg.letter == '(':
       file.write('(')
    elif _arg.letter == ')':
       file.write(')')
    elif _arg.letter == '~':
       file.write('~')
    elif _arg.letter == '_':
       file.write('_')
    elif _arg.letter == '+':
       file.write('+')

    elif _arg.letter == '`':
       file.write('`')
    elif _arg.letter == 'ca':
       file.write('1')
    elif _arg.letter == 'ce':
       file.write('2')
    elif _arg.letter == 'cu':
       file.write('3')
    elif _arg.letter == 'da':
       file.write('4')
    elif _arg.letter == 'de':
       file.write('5')
    elif _arg.letter == 'du':
       file.write('6')
    elif _arg.letter == 'pa':
       file.write('7')
    elif _arg.letter == 'pe':
       file.write('8')
    elif _arg.letter == 'pu':
       file.write('9')
    elif _arg.letter == 'wo':
       file.write('0')
    elif _arg.letter == '-':
       file.write('-')
    elif _arg.letter == '=':
       file.write('=')

    else:
      print('\n Not supported (yet).')
elif _arg.translation == 'trlt':
    if _arg.letter == 'a':
        file.write('fa')
    elif _arg.letter == 'b':
       file.write('fe')
    elif _arg.letter == 'c':
      file.write('fu')
    elif _arg.letter == 'd':
        file.write('ja')
    elif _arg.letter == 'e':
        file.write('je')
    elif _arg.letter == 'f':
        file.write('ju')
    elif _arg.letter == 'g':
        file.write('ka')
    elif _arg.letter == 'h':
       file.write('ke')
    elif _arg.letter == 'i':
       file.write('ku')
    elif _arg.letter == 'j':
       file.write('na')
    elif _arg.letter == 'k':
     file.write('ne')
    elif _arg.letter == 'l':
      file.write('nu')
    elif _arg.letter == 'm':
        file.write('ra')
    elif _arg.letter == 'n':
        file.write('re')
    elif _arg.letter == 'o':
       file.write('ru')
    elif _arg.letter == 'p':
        file.write('sa')
    elif _arg.letter == 'q':
       file.write('se')
    elif _arg.letter == 'r':
       file.write('su')
    elif _arg.letter == 's':
       file.write('ta')
    elif _arg.letter == 't':
       file.write('te')
    elif _arg.letter == 'u':
       file.write('tu')
    elif _arg.letter == 'v':
       file.write('za')
    elif _arg.letter == 'w':
        file.write('ze')
    elif _arg.letter == 'x':
        file.write('zu')
    elif _arg.letter == 'y':
        file.write('ga')
    elif _arg.letter == 'z':
        file.write('ge')

    elif _arg.letter == ' ':
       file.write(' ')
    elif _arg.letter == ',':
        file.write(',')
    elif _arg.letter == '.':
       file.write('.')
    elif _arg.letter == '(':
        file.write('(')
    elif _arg.letter == ')':
       file.write(')')
    elif _arg.letter == ';':
       file.write(';')
    elif _arg.letter == ':':
       file.write(':')
    elif _arg.letter == '/':
        file.write('/')
    elif _arg.letter == '?':
        file.write('?')
    elif _arg.letter == '\'':
        file.write('\'')
    elif _arg.letter == '[':
        file.write('[')
    elif _arg.letter == ']':
        file.write(']')
    elif _arg.letter == '\\':
        file.write('\\')
    elif _arg.letter == '<':
        file.write('<')
    elif _arg.letter == '>':
        file.write('>')
    elif _arg.letter == '"':
        file.write('"')
    elif _arg.letter == '{':
        file.write('{')
    elif _arg.letter == '}':
        file.write('}')
    elif _arg.letter == '|':
        file.write('|')

    elif _arg.letter == '!':
       file.write('!')
    elif _arg.letter == '@':
       file.write('@')
    elif _arg.letter == '#':
       file.write('#')
    elif _arg.letter == '$':
       file.write('$')
    elif _arg.letter == '%':
       file.write('%')
    elif _arg.letter == '^':
       file.write('^')
    elif _arg.letter == '&':
       file.write('&')
    elif _arg.letter == '*':
       file.write('*')
    elif _arg.letter == '(':
       file.write('(')
    elif _arg.letter == ')':
       file.write(')')
    elif _arg.letter == '~':
       file.write('~')
    elif _arg.letter == '_':
       file.write('_')
    elif _arg.letter == '+':
       file.write('+')

    elif _arg.letter == '`':
       file.write('`')
    elif _arg.letter == '1':
       file.write('ca')
    elif _arg.letter == '2':
       file.write('ce')
    elif _arg.letter == '3':
       file.write('cu')
    elif _arg.letter == '4':
       file.write('da')
    elif _arg.letter == '5':
       file.write('de')
    elif _arg.letter == '6':
       file.write('du')
    elif _arg.letter == '7':
       file.write('pa')
    elif _arg.letter == '8':
       file.write('pe')
    elif _arg.letter == '9':
       file.write('pu')
    elif _arg.letter == '0':
       file.write('wo')
    elif _arg.letter == '-':
       file.write('-')
    elif _arg.letter == '=':
       file.write('=')

    else:
      print('\n Not supported (yet).')

file.close()