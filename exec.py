import argparse
_parser = argparse.ArgumentParser(
    exit_on_error=1, description=' --execution file--'
)
_parser.add_argument('--letter',
                     help=' --execiution file--'
                     )
_arg = _parser.parse_args()

file = open('write.txt','a')

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
elif _arg.letter == '!':
    file.write('!')
elif _arg.letter == '?':
    file.write('?')
elif _arg.letter == '(':
    file.write('(')
elif _arg.letter == ')':
    file.write(')')
elif _arg.letter == ';':
    file.write(';')
elif _arg.letter == ':':
    file.write(':')

else:
    print('\n Not supported (yet).')

file.close()
