import csv
from operator import itemgetter
from itertools import groupby

class ListUtils:
    """
    Contains auxiliary methods to perform sorting and
    save to disk operations
    """
    @staticmethod
    def sort_by_word_id(list):
        """
        Performs a list of dicts sort by the word_id key
        """
        return sorted(list, key=itemgetter('word_id'))
    
    @staticmethod
    def sort_by_document_id(list):
        """
        Performs a list of dicts sort by the document_id key
        """
        return sorted(list, key=itemgetter('document_id'))
    
    @staticmethod
    def group_by_word_id(list):
        """
        Performs a group by of a list of dicts by the word_id key
        """
        grouped_list = [{"word_id": key, "document_id": [(g['document_id']) for g in group]} 
            for key, group in groupby(list, lambda x: x['word_id'])]
        return grouped_list
    
    @staticmethod
    def save_word_dict_results(word_dict):
        """
        Save the generated word_dict to disk
        """
        print('saving results in /tmp/word_dictionary.csv')
        with open('/tmp/word_dictionary.csv', 'w') as f:
            for key in word_dict.keys():
                f.write("%s, %s\n" % (key, word_dict[key]))
    
    @staticmethod
    def save_bsbi_results(bsbi):
        """
        Save the generated BSBI results to disk
        """
        print('saving results in /tmp/bsbi_results.csv')
        with open('/tmp/bsbi_results.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=['word_id','document_id'])
            writer.writeheader()
            writer.writerows(bsbi)
