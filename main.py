"""The Elevator Mirror Caught Me: one-line entry for make.fun.

The program writes exactly one line - the drafted winning line for the 'Everyday Wonder: Two Days to Find the Line' bounty - to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader). The line is a fixed constant with no trailing newline, so both of the grader's runs
write byte-identical output: 135 UTF-8 characters, inside the 1-200 gate.
"""
import os

LINE = 'The elevator mirror caught me mid-yawn this morning, and for one floor I was a stranger who looked exactly like someone I used to know.'

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
