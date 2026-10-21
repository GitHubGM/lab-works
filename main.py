import argparse
import random


WORDS = (
    "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod "
    "tempor incididunt ut labore et dolore magna aliqua enim ad minim veniam "
    "quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo "
    "consequat duis aute irure in reprehenderit voluptate velit esse cillum "
    "eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident "
    "sunt culpa qui officia deserunt mollit anim id est laborum"
).split()

OPENING_SENTENCE = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."


def generate_lorem(
    paragraphs: int = 3,
    sentences_per_paragraph: int = 5,
    seed: int | None = None,
) -> str:

    for name, count in (
        ("paragraphs", paragraphs),
        ("sentences_per_paragraph", sentences_per_paragraph),
    ):
        if isinstance(count, bool) or not isinstance(count, int) or count < 1:
            raise ValueError(f"{name} must be a positive integer")

    rng = random.Random(seed)
    result = []

    for paragraph_index in range(paragraphs):
        sentences = []
        for sentence_index in range(sentences_per_paragraph):
            if paragraph_index == 0 and sentence_index == 0:
                sentences.append(OPENING_SENTENCE)
            else:
                words = rng.choices(WORDS, k=rng.randint(8, 16))
                sentences.append(" ".join(words).capitalize() + ".")
        result.append(" ".join(sentences))

    return "\n\n".join(result)


def positive_int(value: str) -> int:
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("must be a positive integer") from None
    if number < 1:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-p", "--paragraphs", type=positive_int, default=3,
        help="number of paragraphs (default: 3)",
    )
    parser.add_argument(
        "-s", "--sentences", type=positive_int, default=5,
        help="sentences per paragraph (default: 5)",
    )
    parser.add_argument("--seed", type=int, help="seed for repeatable output")
    args = parser.parse_args()
    print(generate_lorem(args.paragraphs, args.sentences, args.seed))


if __name__ == "__main__":
    main()
