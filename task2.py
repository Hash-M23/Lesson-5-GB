my_file = open('test2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = my_file.readlines()
print(f'Кол строк в файле - {len(content)}')
my_file = open('test2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
	print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('test2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее Количество слов - {len(content)}')
my_file.close()
