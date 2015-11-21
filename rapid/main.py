supports = ['html'];
data_loc = 'boilerplate'

def html_boilerplate(name):
    with open(data_loc +'/'+ name +'/' + 'code', 'r') as file:
        print file.read()

def main():
    html_boilerplate('html')

if __name__ == "__main__":
    main()
