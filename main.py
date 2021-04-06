import os

def checkutf(file):
    try:
        f = open(file, 'r', encoding='utf8')
        for _ in range(3):
            f.readline()
    except UnicodeError:
        f.close()
        return 'not utf8'
    else:
        f.close()
        return 'utf8'


def compare_files(dir):
    files_dict = {}
    for dirpath, dirs, files in os.walk(os.path.abspath(dir)):
        files_dir = dirpath
        for file in files:
            if file[-4:] == '.txt':
                files_dict[file] = 0
                with open(os.path.join(dirpath, file), 'r', encoding='utf-8') as f:
                    for line in f:
                        files_dict[file] += 1
    return sorted(files_dict, key=lambda x: files_dict.get(x)), files_dir, files_dict

# print(compare_files('files', None))
def write_mode(file):
    if not os.path.isfile(file):
        return 'x'
    else:
        return 'w'

files, files_dir, files_dict = compare_files('files')

with open('output.txt', write_mode('output.txt'), encoding='utf-8') as f_out:
    for file in files:
        f_out.write(file + '\n')
        f_out.write(str(files_dict[file]) + '\n')
        with open(os.path.join(files_dir, file), encoding='utf-8') as f_in:
            f_out.write(f_in.read() + '\n')

with open('output1.txt', write_mode('output1.txt'), encoding='ansi') as f_out:
    for file in files:
        f_out.write(file + '\n')
        f_out.write(str(files_dict[file]) + '\n')
        with open(os.path.join(files_dir, file), encoding='utf-8') as f_in:
            f_out.write(f_in.read() + '\n')

print(checkutf('output.txt'))
print(checkutf('output1.txt'))
