from collections import deque
from random import shuffle
from matplotlib import pyplot as plt
import statistics as s

class Hand:
    def __init__(self, cards, name):
        self.name = name
        self.cards = deque(cards)

    def __repr__(self):
        return self.name

    def next(self):
        if self.size() > 0:
            return self.cards.popleft()
        return None

    def collect(self, cards):
        self.cards.extend(cards)

    def size(self):
        return len(self.cards)

class Card:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return str(self.value)

def generate_hands():
    cards = []
    for i in range(13):
        for j in range(4):
            cards.append(Card(i))
    shuffle(cards)
    a = Hand(cards[:26], "A")
    b = Hand(cards[26:], "B")
    return a,b

def play(a, b):
    # print("Stacks:", str(a.size()), "to", str(b.size()), end="; ")
    a_played = [a.next()]
    b_played = [b.next()]
    while True:
        a_card = a_played[-1]
        b_card = b_played[-1]

        if a_card is None:
            return b
        if b_card is None:
            return a

        # print("A:", a_card, " B:", b_card, end = "; ")
        if a_card != b_card:
            if a_card < b_card:
                # print("B takes.")
                b.collect(a_played + b_played)
            else:
                # print("A takes.")
                a.collect(b_played + a_played)
            return None
        # print("War", end = "; ")
        for _ in range(4):
            n = a.next()
            if n is not None:
                a_played.append(n)
            n = b.next()
            if n is not None:
                b_played.append(n)
        # print("A's pile:", a_played, end = "; ")
        # print("B's pile:", b_played, end = "; ")

##########################
##########################
##########################

def main():
    trials = []
    for i in range(20000):
        a,b = generate_hands()

        winner = None
        iterations = 0
        while winner is None:
            winner = play(a,b)
            iterations += 1
        # print(winner, "wins.", iterations, "iterations.")
        print(i)
        trials.append(iterations)

    print("Min:", min(trials), "Max:", max(trials), "Mean:", s.mean(trials), "Median:", s.median(trials), "StdDev:", s.stdev(trials))
    plt.hist(trials, bins=30)
    plt.show()

if __name__ == "__main__":
    main()
