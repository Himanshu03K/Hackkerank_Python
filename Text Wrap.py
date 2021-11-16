def wrap(string, max_width):
    x=0
    str=""
    while(x<=len(string)):
        
        str=str + string[x:x+max_width] + "\n"
        x+=max_width
    return str

