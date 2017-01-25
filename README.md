# flashcards
Just a little flash-card like program using my preferred method.

# Preferred Method
The entire point of flash cards is to quickly filter out the ones you don't need to pay attention to and focus on the specific ones you're having problems with.
In order to make this happen, we store a grade for each card - So if you answer right the first time, it's off the list. If you don't answer right the first time, you have to answer correctly three times - to get a score on the card of 70% or higher.

# Flashcard file format
The flashcard file format is simple, it's a single-line format with the Question and Answer separated by a "|" or pipe character. I've included a selection of the Periodic Table of Elements as an example.

# How do I run this?
This program is a script; an interpreted language. In order to run it, you need to have Python installed. It's written for Python 2.7, so we recommend you use that version for the time being.

There's two ways you can do this - first, by installing python for windows from www.python.org and running the .py script from inside of a command prompt.
Second, by installing cygwin and then simply running it from a cygwin prompt.

# Learning or reviewing?

When learning a deck of cards for the first time, it's easier to add them one at a time - this is now provided for with the --new flag. On any individual run through of cards, it will still enforce the 75% requirement, AND it will randomize the entire deck before picking the first card.

There is currently no provision to establish an arbitrary starting number.

# Usage
Usage is simple, so here's the program's own --help output:
> usage: flashcards.py [-h] [--new] file
> 
> Study some flashcards.
> 
> positional arguments:
>   file
> 
> optional arguments:
>   -h, --help  show this help message and exit
>   --new       Used to add new cards to the running deck one at a time in order
>               to learn them. Still requires 75 percent per card.
> 
