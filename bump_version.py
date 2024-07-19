# bump_version.py

import subprocess
import sys


def main():
    # Check for the current branch
    branch = (
        subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
        .strip()
        .decode()
    )

    # Bump the version
    try:
        subprocess.run(["bump", "patch"], check=True)
        subprocess.run(
            ["git", "add", "setup.py", "ratchada_utils/_version.py"], check=True
        )
        subprocess.run(["git", "commit", "-m", "Bump version"], check=True)
        subprocess.run(["git", "push"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
