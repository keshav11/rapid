supports = ['html'];
def html():
    pass

def html_boilerplate():
    with open('boilerplate/html/index.html', 'r') as file:
        print file.read()


def main():
    html_boilerplate()

if __name__ == "__main__":
    main()
