import re

def read_expression(expression):
    regex = expression.replace(' ', '') #eliminate spaces
    regex = list(regex)
    
    i = 0
    while i < len(regex):
        if(regex[i] == '+' and regex[i-1] != '^'):
            regex[i] = '|'
        else:
            if(regex[i-1] == '^'):
                regex[i-1] = ''

        if(regex[i] == '*' and regex[i-1] == '^'):
            regex[i-1] = ''

        if(regex[i] == ')'):
            if(i < len(regex) - 2):
                if ((regex[i+1] == '^' and regex[i+2] == '+') or (regex[i+1] == '^' and regex[i+2] == '*')):
                    print('se encuentra )')
                else:
                    regex[i] = '){1}'

        if(regex[i] == 'ϵ' or regex[i] == 'ε'):
            regex[i] = ''       

        if(regex[i] == 'e'  and regex[i+1] =='p' and  regex[i+2] =='s' and regex[i+3] == 'i'  and regex[i+4] =='l' and  regex[i+5] =='o' and regex[i+6] == 'n'):
            regex[i] = ''
            regex[i+1] = ''
            regex[i+2] = ''
            regex[i+3] = ''
            regex[i+4] = ''
            regex[i+5] = ''
            regex[i+6] = ''

        i+=1

    new_expression = ''.join(regex)
    new_expression =  '(' + new_expression + ')$'
    print(new_expression)

    return new_expression
   
    
def match_expression(expression, value_expression):
    regex = read_expression(expression)
    compile_regex = re.compile(regex)
    match_expression = compile_regex.match(value_expression)
    
    if(match_expression):
        print('Valid Match!')
        return True
    else:
        print('Invalid Match!')
        return False    

read_expression('')