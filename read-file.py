long_names = []

with open('horse-names.txt') as file:
    names = file.read().split('\n')
    for name in names:
        if len(name.split(' ')) > 2:
            long_names.append(name)

    print(long_names)

    with open('long-horse-names.txt', 'w') as output_file:
        output_file.write('\n'.join(long_names))
