from algorithm.ucs import ucs


def main() -> None:
    """
    The main function

    :returns: None
    """
    for i in range(1,6):
        print(f"=====================hard : {i}=====================")
        ucs(f"inputs/hard/hard{i}.txt")
        print("\n")


if __name__ == "__main__":
    main()
