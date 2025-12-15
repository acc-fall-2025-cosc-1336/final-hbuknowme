def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    t_len = len(dna_string2)

    for i in range(len(dna_string1) - t_len + 1):
        if dna_string1[i:i+t_len] == dna_string2:
            positions.append(i + 1)  # +1 because problem wants 1-based positions

    return tuple(positions)


def main():
    while True:
        dna1 = input("Enter DNA string (9–16 chars): ")
        if len(dna1) < 9 or len(dna1) > 16:
            print("Invalid length.")
            continue

        dna2 = input("Enter DNA substring (exactly 4 chars): ")
        if len(dna2) != 4:
            print("Invalid length.")
            continue

        result = get_most_likely_ancestor_consensus(dna1, dna2)

        for pos in result:
            print(pos, end=" ")
        print()

        choice = input("Do you want to continue? (y/n): ").lower()
        if choice != "y":
            break


if __name__ == "__main__":
    main()
#add imports