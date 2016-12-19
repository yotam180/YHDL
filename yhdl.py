import sys
import re

def eev(c):
    return str(eval(c.group()[1:-1]))

forreg = re.compile("for\(\d+\.\.\d+\)")
def main():
    if len(sys.argv) < 2:
        print "You must provide a file to yhdlize"
        return
    finalCode = ""
    with open(sys.argv[1], "r") as f:
        for line in f:
            if re.search("for\(\d+\.\.\d+\)", line.strip(' \n\t\r')):
                for mtch in forreg.finditer(line.strip(' \n\t\r')):
                    prccd = mtch.group().replace('for(', '').replace(')', '')
                    strt = int(prccd[:prccd.index('..')])
                    end = int(prccd[prccd.index('..') + 2:])
                    for i in range(strt, end):
                        processed_line = line.strip(' \n\t\r')[mtch.start() + len(mtch.group()):].replace('for', str(i))
                        evaled_line = re.sub("\<(.+?)\>", eev, processed_line)
                        finalCode +=  evaled_line + "\n"
                    break
            else:
                finalCode += line.strip(' \t\n\r') + "\n"

    if len(sys.argv) < 3:
        with open(sys.argv[1].replace('.yhdl', '.hdl'), "w") as f:
            f.write(finalCode)
    else:
        with open(sys.argv[2].replace('.yhdl', '.hdl'), "w") as f:
            f.write(finalCode)

main()