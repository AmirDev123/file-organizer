#!/usr/bin/env python3
"""
File Organizer — automatically moves files in a directory into
categorized subfolders based on extension.
"""
import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico"],
    "Videos":     [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"],
    "Audio":      [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Documents":  [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".txt", ".rtf"],
    "Code":       [".py", ".js", ".ts", ".html", ".css", ".java", ".c", ".cpp", ".go", ".rs", ".sh"],
    "Archives":   [".zip", ".tar", ".gz", ".bz2", ".rar", ".7z", ".xz"],
    "Data":       [".csv", ".json", ".xml", ".yaml", ".yml", ".toml", ".sql"],
    "Ebooks":     [".epub", ".mobi", ".azw"],
}


def ext_to_category() -> dict[str, str]:
    mapping = {}
    for cat, exts in CATEGORIES.items():
        for ext in exts:
            mapping[ext] = cat
    return mapping


def organize(directory: str, dry_run: bool = False, verbose: bool = False):
    target = Path(directory).resolve()
    if not target.is_dir():
        raise SystemExit(f"Not a directory: {target}")

    mapping = ext_to_category()
    moved = 0
    skipped = 0

    for file in sorted(target.iterdir()):
        if not file.is_file():
            continue
        category = mapping.get(file.suffix.lower(), "Other")
        dest_dir = target / category
        dest = dest_dir / file.name

        if dest == file:
            skipped += 1
            continue

        if dry_run:
            print(f"[dry-run] {file.name}  →  {category}/")
        else:
            dest_dir.mkdir(exist_ok=True)
            if dest.exists():
                base = dest.stem
                ext = dest.suffix
                i = 1
                while dest.exists():
                    dest = dest_dir / f"{base}_{i}{ext}"
                    i += 1
            shutil.move(str(file), str(dest))
            if verbose:
                print(f"Moved: {file.name}  →  {category}/")
        moved += 1

    action = "Would move" if dry_run else "Moved"
    print(f"\n{action} {moved} file(s). Skipped {skipped}.\n")


def main():
    parser = argparse.ArgumentParser(description="Organize files into category folders")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to organize (default: current)")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Preview without moving files")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print each moved file")
    args = parser.parse_args()
    organize(args.directory, args.dry_run, args.verbose)


if __name__ == "__main__":
    main()
