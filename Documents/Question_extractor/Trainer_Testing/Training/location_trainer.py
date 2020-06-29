import sys
sys.path.append('..')
from sentence_divider import get_sents
from important_sents import get_important
from tag_sents import sent_tagger
from chunk_sents import chunk_sentences
import pickle
from file_extractor import text_from_file
from html_extractor import extract
import os

model = open("../models/location_model", 'wb')
locations_model = {}


def check_for_location(sents):
    # Check location database
    locations = open('../test_files/data_sets/', 'r')
    length = locations.readlines()

    j = 0
    for line in length:
        j += 1
        # Get location name from database
        line = line.split('\t')
        location = line[2].split()
        # print(location)

        # Iterate over all sentances
        for sent in sents:
            i = 0
            while i < len(sent):
                word = sent[i]

                # Look for Noun Phrases or nouns
                if word[1] == 'NNP' or word[1] == 'NN':
                    # Check to see if it is in the location
                    if word[0] in location:
                        # print(word[0], location)
                        locations_model[word[i][0]] = 1
                i += 1

        print('Lines processed: ' + str(j) + " Of " + str(len(length)) + ' lines total.')


def split_doc(text):
    sentences = get_sents(text)
    important, words = get_important(sentences, 10)
    tagged_sents = sent_tagger(important)
    chunked_sents = chunk_sentences(tagged_sents)
    return chunked_sents


def main():
    """ Take text & process it
        Then send in words to check location.
        Write to location model.
        location dict: 0 is not location 1 is location
    """
    # Send in website data

    websites = open('../test_files/websites/urls.txt', 'r')
    websites = websites.readlines()
    total_sents = []

    for url in websites:
        text = extract(url)
        sents = split_doc(text)
        #check_for_location(sents)
        total_sents = total_sents + sents

    # Send in file data

    directory = "../test_files/CASE_Notes/"
    for d in os.listdir(directory):
        for file in os.listdir(directory + d):
            text = text_from_file(directory + d + '/' + file)
            sents = split_doc(text)
            #check_for_location(sents)
            total_sents = total_sents + sents

    print("Number of sentences to be iterated: " + str(len(total_sents)))
    check_for_location(total_sents)
    print(locations_model)

    # Write to file
    pickle.dump(locations_model, model)


if __name__ == '__main__':
    main()
