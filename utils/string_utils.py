import os
import re

ENCODING = 'iso8859-1'


class StringUtils:
    """
    Utils class - perform string reads from file and
    a cleanup on a given String removing ponctuation
    """
    @staticmethod
    def cleanup(file_string):
        file_string = re.sub(r"[:,.;@#?!&$]+\ *", " ", file_string)\
        .replace('(','') \
        .replace(')','') \
        .replace('[','') \
        .replace(']','')\
        .replace('{','')\
        .replace('}','')
        return file_string
    
    @staticmethod
    def read_file(file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding=ENCODING) as file:
                data = file.read().replace('\n', ' ')
        return data