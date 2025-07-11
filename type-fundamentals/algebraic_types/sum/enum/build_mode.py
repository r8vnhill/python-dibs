from enum import Flag, auto


class BuildMode(Flag):
    COMPILE = auto()
    DOCS = auto()
    TEST = auto()


def run_build(mode: BuildMode):
    print(f"Running build mode: {mode}")

    if BuildMode.COMPILE in mode:
        print("- Compiling source files...")

    if BuildMode.DOCS in mode:
        print("- Generating documentation...")

    if BuildMode.TEST in mode:
        print("- Running test suite...")


if __name__ == "__main__":
    full_build = BuildMode.COMPILE | BuildMode.TEST
    run_build(full_build)
