import operator

def Symbol(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '%' : operator.mod,
        '^' : operator.xor,
        }

def tokenize(mystr):
    s = mystr.replace('(',' ( ').replace(')',' ) ').split()
    print(s)
    return s

def read_from_tokens(mystr):
    "Read an expression from a sequence of tokens."
    mystr=list(mystr)
    if len(mystr) == 0:
        raise SyntaxError('EOFError')
    token = mystr.pop(0)#this recieves the first index at 0
    if token=='(':
        mylist=[]
        while mystr[0]!=')':
            mylist.append(read_from_tokens(mystr))
        mystr.pop(0)
        return mystr
    elif token==')':
        raise SyntaxError('Syntax error')
    else:#this checks if its a number or a symbol and replaces
        try: return int(token)
        except ValueError:
            try: return float(token)
            except ValueError:
                return Symbol(token)
        
        