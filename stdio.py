import io
def printf(format_string, *args):
    format_string = format_string%args
    print(format_string)
def scanf(format_string=None):
    if format_string:
        user_input = input(format_string)
        return user_input
    else:
        return input()
class iofile:
    def fopen(self,filename,mode):
        return io.StringIO()
    def fclose(self,file):
        file.close()
    def fread(self,file, size):
        return file.read(size)

def fwrite(self,file, data):
    file.write(data)

def fscanf(self,file, format_str, *args):
    data = file.read(len(format_str))
    for i, specifier in enumerate(format_str):
        if specifier == '%':
            if format_str[i + 1] == 'd':
                args[i] = int(data[i])
            elif format_str[i + 1] == 's':
                args[i] = data[i]
    return len(data)

def fprintf(self,file, format_str, *args):
    data = ""
    for i, specifier in enumerate(format_str):
        if specifier == '%':
            if format_str[i + 1] == 'd':
                data += str(args[i])
            elif format_str[i + 1] == 's':
                data += str(args[i])
    fwrite(file, data)
    return len(data)