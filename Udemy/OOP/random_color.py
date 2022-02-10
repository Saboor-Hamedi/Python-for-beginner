import random 
class RandomColor:
    # define color
    read = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    rgb = [read ,green, blue]
    def __init__(self):
            self.random_olors(self.rgb)
            self.hex_color()
            self.color_bunch()
            self.random_string()
    def random_olors(self, rgb):
        print(rgb)
    #Hexadecimal 
    def hex_color(self):
        hash = '#'
        alpha = 'ABCDEF'
        number = '0123456789'
        lower_case = alpha.lower()
        hex = [hash+ "" . join([random.choice(lower_case+number) for x in range(6)])]
        print(hex)

        print('---------------')
    def color_bunch(self):
        hash = '#'
        alpha = 'ABCDEF'
        number = '0123456789'
        lower_case = alpha.lower()
        for x in range(10):
             hex = [hash+ "" . join([random.choice(lower_case+number) for x in range(6)])]
             print(hex)
    
    def random_string(self):
        rand_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        generate_str = '' .join(random.choice(rand_str) for i in range(0,10))
        print(generate_str.lower().capitalize())