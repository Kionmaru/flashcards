#!/usr/bin/python
"""
This is a short and simple program to give flashcard-style questions. The catch
is that you have to score over 70% on any given question for that question to
be done, forcing you to rehash questions you don't answer correctly the first
time for whatever reason.
"""

from __future__ import print_function
import argparse
import random

class Card(object):
    """
    This is our implimentation of a flashcard. Takes a string in to form of
    "question|answer" from the provided file, splits it into the question and
    the answer, and sets up housekeeping.
    """
    def __init__(self, data):
        lineparts = data.strip().split("|")
        self.question = lineparts[0]
        self.answer = lineparts[1]
        self.correct = 0.0
        self.incorrect = 0.0

    def average(self):
        """
        Get the average of self and return, or return False if no average can
        be obtained.
        """
        if self.correct and self.incorrect:
            return (self.correct / (self.correct + self.incorrect)) * 100
        if self.correct and not self.incorrect:
            return 100.0
        if not self.correct and not self.incorrect:
            return False

def parseargs():
    "Parse arguments on the command line. Basically, print help or get file."
    parser = argparse.ArgumentParser(description="Study some flashcards.")
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()
    return args

def leave(cards):
    """
    Handles exit output, by giving us information about cards we didn't handle
    perfectly. Makes it easier to track specific questions/answers that are
    being problematic.
    """
    def comp(card_a, card_b):
        "Just a pocket comparison function to sort cards by average."
        if card_a.average() > card_b.average():
            return 1
        if card_a.average() == card_b.average():
            return 0
        if card_a.average() < card_b.average():
            return -1
    cards.sort(cmp=comp)
    for card in cards:
        if card.average() < 100.0:
            print('{0}: {1}, got {2}%.'.format(
                card.question, card.answer, card.average()))
    exit(0)

def givecards(cards):
    """
    Give cards that need to be given or don't have a high enough score.
    """

    goodcards = [card for card in cards if card.average() < 70]
    if len(goodcards) == 0:
        leave(cards)
    for card in goodcards:
        data = raw_input("{0}: ".format(card.question))
        if str(data).strip() == "quit":
            leave(cards)
        elif str(data).strip() == card.answer:
            print("Correct!\n\n")
            card.correct += 1
        else:
            print("The correct answer was {0}.".format(card.answer))
            card.incorrect += 1
    return cards


def main():
    """
    Our pocket main function, handles setting up, asks questions, and leaves
    when we're done.

    Oh, and shuffles the deck, too.
    """
    args = parseargs()
    cards = []
    for line in args.file:
        cards.append(Card(line))
    print("Please simply answer 'quit' when ready to exit.\n")
    while True:
        random.shuffle(cards)
        cards = givecards(cards)


if __name__ == "__main__":
    main()