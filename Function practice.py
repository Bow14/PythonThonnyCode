def some_function(x):
    x[0] = 'green'
    print(f'in some_function: {x}')
def main():
    colors = ['pink' 'green' 'purple']
    some_function(colors)
    print(f'in main {colors}')

if __name__ == '__main__':
    main()