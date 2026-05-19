def print_report(counted_words: int, sorted_chars: dict[str, int]) -> None:
    print("----------- Word Count ----------")
    print(f"Found {counted_words:,} total words")
    print("--------- Character Count -------")

    for key, value in sorted_chars.items():
        print(f"{key}: {value:,}")
