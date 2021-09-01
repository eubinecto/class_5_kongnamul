

import argparse
from transformers import pipeline

# 사전훈련된 모델을 로드
summarizer = pipeline("summarization")


def main():
    global summarizer
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str)
    args = parser.parse_args()
    text: str = args.text
    res = summarizer(text, min_length=10, max_length=20)
    print(res)


if __name__ == '__main__':
    main()
