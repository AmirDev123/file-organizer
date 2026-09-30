# file-organizer

Automatically sorts files in a directory into categorized subfolders (Images, Videos, Documents, Code, etc.) based on file extension.

## Usage

```bash
python main.py                        # organize current directory
python main.py ~/Downloads            # organize Downloads
python main.py ~/Downloads --dry-run  # preview without moving
python main.py . --verbose            # show each moved file
```

## Categories

`Images`, `Videos`, `Audio`, `Documents`, `Code`, `Archives`, `Data`, `Ebooks`, `Other`

## Requirements

No external dependencies — uses Python's built-in `pathlib` and `shutil`.
