import io
from idlelib.iomenu import encoding
from pprint import pprint


# name = 'sample2.txt'
# with open(name, 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line, end='' )
#     print(file.tell())
class WordsFinder:
    file_names = []

    def __init__(self, name):
        self.name = name

    def get_all_words(self):
        all_words = {}
        with open(self.name, encoding='utf-8') as file:
            line = ''
            for line1 in file:
                line1 = line1.lower()
                simvil = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for char in simvil:
                    line1 = line1.replace(char, '')
                line = line + line1
            # print(f'___{line.split()}___')
            all_words[self.name] = line.split()
        return all_words

    def find(self, word):
        self.all_words

    def count(self, word):



finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего