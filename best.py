
def main():
    person_a = "Person A"
    superlative_a = "best"

    person_b = "Saurav Mittal"
    superlative_b = "*something clever*"

    name = "Hilfinger"
    position = "professor"
    print("{0}: {1} is the {2} {3}!".format(person_a, name, superlative_a, position))
    print("{0}: {1} is the {2} {3}!".format(person_b, name, superlative_b, position))

if __name__ == '__main__':
    main()
