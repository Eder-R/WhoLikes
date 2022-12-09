names = [
    ["Alex"], 
    ["Jacob"], 
    ["Mark"], 
    ["Max"]
]

def likes(val:str):
    lenght = len(val)
    if lenght == 0:
        print('no one likes this')
    elif lenght == 1:
        print(f'{val[0]} likes this')
    elif lenght == 2:
        print(f'{val[0]} and {val[1]} like this')
    elif lenght == 3:
        print(f'{val[0]}, {val[1]} and {val[2]} like this')
    else:
        print(f'{val[0]}, {val[1]} and {lenght - 2} others like this')
