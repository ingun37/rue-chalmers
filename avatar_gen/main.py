import argparse
from pathlib import Path

from lib import generate_avatar, save_avatar


def positive_int(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("number must be a positive integer")
    return number


def run(number, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    avatars = []
    for seed in range(number):
        avatars.append(generate_avatar(seed))

    for avatar in avatars:
        save_avatar(avatar, out_dir / str(avatar.seed))

    return avatars


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=positive_int)
    parser.add_argument("--out-dir", required=True, type=Path)
    args = parser.parse_args()

    run(args.number, args.out_dir)
