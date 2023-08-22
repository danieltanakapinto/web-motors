import os
import string

from utils.string_utils import StringUtils
from utils.document_folder_string_utils import DocumentFolderString
from utils.list_utils import ListUtils

class WordDict:
    """
        Receives a string
        and can generate an unique dict of words 
        with the following key-value configuration:
        word and word_id
    """
    def __init__(self, document_string:string):
        self.document_string = document_string

    def get_word_set(self):
        """
        Returns a set of words based on a string
        A word is defined by a whitespace split
        """
        set_of_words = set(self.document_string.split(' '))
        return set_of_words
    
    def get_word_dict(self):
        """
        Converts the set format of words to a dictionary
        with the configuration word and word_id
        """
        set_of_words = self.get_word_set()
        word_dict = {}
        i = 0
        for val in set_of_words:
            word_dict[val] = i
            i = i + 1
        return word_dict



class Jobs:
    """
    This class contains two jobs
    1 - job to generate a word dict lookup table
    2 - job to create the block sort based index using the words lookup table
    """

    @staticmethod
    def word_dict_job(folder):
        """
        This Job gets a string from all the text files inside a folder
        after that it returns a dict with unique words with an word_id
        """
        print("Running Job - word_dict_job...")
        documents_string = DocumentFolderString(folder=folder)
        string = documents_string.get_string_from_folder()
        word_dict = WordDict(document_string=string)
        word_dict = word_dict.get_word_dict()
        return word_dict
    
        
    @staticmethod
    def get_processing_job_list(folder):
        """
        This job uses as advantage the fact the the documents were
        ordered by an integer/vectorial logic
        If the filename is not an integer, it is going to be ignored
        """
        documents_string = DocumentFolderString(folder=folder)
        files = documents_string.get_file_list_from_folder()
        file_list = []
        for file in files:
            try:
                file_dict = {
                    'filepath': file,
                    'document_id': int(os.path.basename(file))
                }
                file_list.append(file_dict)
            except:
                print(f"File found:{file} not in the integer desired format... skipping it from BSBI")
        file_list = ListUtils.sort_by_document_id(file_list)
        return file_list

    @staticmethod
    def block_sort_based_index_job(folder, word_dict):
        """
        Performs the Block Sort Based Index
        It uses a sorted file list and uses the word_dict as a lookup table
        After merging all the data from the lookup table, performs a sort and a groupby
        """
        print("Running 2nd Job - BSBI...")
        files_sorted = Jobs.get_processing_job_list(folder=folder)
        full_list = []
        for file in files_sorted:
            document_string = StringUtils.read_file(file.get('filepath'))
            document_string = StringUtils.cleanup(document_string)
            document_string_set = WordDict(document_string=document_string).get_word_set()
            for val in document_string_set:    
                new_dict = {
                    'word_id':word_dict.get(val),
                    'document_id': file.get('document_id')
                }
                full_list.append(new_dict)
        sorted_full_list = ListUtils.sort_by_word_id(list=full_list)
        grouped_full_list = ListUtils.group_by_word_id(list=sorted_full_list)
        
        return grouped_full_list
    
    
if __name__ == '__main__':
    folder = os.path.abspath("dataset")
    # Get Word dict from Job 1:
    word_dict = Jobs.word_dict_job(folder=folder)
    # Get BSBI from Job 2:
    bsbi = Jobs.block_sort_based_index_job(folder=folder, word_dict=word_dict)
    # Save the desired results in a temp folder:
    ListUtils.save_word_dict_results(word_dict=word_dict)
    ListUtils.save_bsbi_results(bsbi=bsbi)
