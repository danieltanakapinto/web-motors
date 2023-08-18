import os
from utils.string_utils import StringUtils

class DocumentFolderString:
    """
    Auxiliary class that can read text files in a folder, and return a python string
    """
    def __init__(self, folder):
        self.folder = folder
    
    def get_file_list_from_folder(self):
        file_list = []
        for file_path in os.listdir(self.folder):
            if os.path.isfile(os.path.join(self.folder, file_path)):
                file_list.append(os.path.join(self.folder,file_path))
        return file_list

    def get_string_from_folder(self):
        """
        Returns a appended string with words from a folder with different text files
        """
        files = self.get_file_list_from_folder()
        string_from_folder = ''
        for file in files:
            file_string = StringUtils.read_file(file_path=file)
            file_string = StringUtils.cleanup(file_string=file_string)
            string_from_folder = string_from_folder + file_string
        return string_from_folder