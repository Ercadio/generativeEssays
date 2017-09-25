"""
    ~~ DataCleaner Class ~~

    I. Static Methods
        - parse_txt_from_prog(txt, program)
            Returns the parsed text. A program is an array of vectors(2). Each vector must have a compiled
            Regular Expression Object at index 0 and replacement at index 1
        - search_rfile(path)
            Returns a vector will the absolute paths of all files contained in that directory or a subdirectory.
        - copy_dir_structure(path, destination)
            Copy all subdirectories inside a directory(path) to a destination without copying files.
        - parse_all_from_dir_to(path, destination, program)
            Parses all the file inside a directory given a program and writes them to destination
    II. Programs
        - ONLY_WORDS_SPACES
            Removes emails, all non-alphabetic characters and extra whitespace
"""



import os
import re
import sys
import Containers

class DataCleaner:

    ONLY_WORDS_SPACES = [
        [re.compile("[<]*[a-z0-9_.-]+@[a-z0-9_.-]+\.[a-z]+[>]*", flags=re.UNICODE), ""],  # Remove emails
        [re.compile("[a-zA-Z]*[0-9.]+[a-zA-Z0-9.]*", flags=re.UNICODE), " "],  # Removes alphanumeric
        [re.compile("[^a-zA-Z']", re.UNICODE), " "],  # Remove non letters
        [re.compile("\s{2,}", re.UNICODE), " "]  # Remove extra whitespace
    ]

    @staticmethod
    def parse_txt_from_prog(txt, program):
        words = txt
        for step in program:
            words = step[0].sub(step[1], words)
        words = words.strip()
        return words

    @staticmethod
    def search_rfile(path):
        result = []
        for fna in os.listdir(path):
            fna = os.path.join(path, fna)
            if os.path.isdir(fna):
                result.extend(DataCleaner.search_rfile(fna))
            elif os.path.isfile(fna):
                result.append(fna)
        return result

    @staticmethod
    def copy_dir_structure(path, destination):
        for fna in os.listdir(path):
            if isdir(os.path.join(path, fna)):
                if not os.path.exists(join(destination, fna)):
                    os.makedirs(join(destination, fna))
                DataCleaner.copy_dir_structure(os.path.join(path, fna),os.path.join(destination, fna))

    # Parses all the files inside a give path according to a given program, moves them to destination folder
    @staticmethod
    def parse_all_from_dir_to(path, destination, program):
        unparsed_textfiles = DataCleaner.search_rfile(path)
        for fname in unparsed_textfiles:
            with open(fname) as file:
                txt = file.read()
            txt = DataCleaner.parse_txt_from_prog(txt,program)
            open(fname.replace(path, destination), mode="w+").write(txt)
            print("Parsed {}\n".format(fname))


if __name__ == "__main__":
    # Parse all from ./Unparsed to ./Parsed
    DataCleaner.parse_all_from_dir_to("./Unparsed","./Parsed", DataCleaner.ONLY_WORDS_SPACES)

    # Get a sorted list of all words from all files inside ./Parsed
    # tree = Containers.BST()
    # for fname in DataCleaner.search_rfile("./Parsed"):
    #     file = open(fname)
    #     txt = file.read()
    #     file.close()
    #     tokens = txt.split(" ")
    #     for token in tokens:
    #         print("Pushing", token)
    #         tree.push(token)
    # with open("./tokens.data", "w+") as file:
    #     file.writelines("\n".join())
    # tree.toList()