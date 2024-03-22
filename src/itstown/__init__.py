import argparse

from . import main2

__project_name__ = "itstown"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Update GUI address in the config file."
    )
    parser.add_argument(
        "config_path", metavar="CONFIG_PATH", type=str, help="Path to the config file"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    main2.update_gui_address(args.config_path)
    return 0
