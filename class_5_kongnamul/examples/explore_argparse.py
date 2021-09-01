

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str)
    args = parser.parse_args()
    print(args.text)


if __name__ == '__main__':
    main()