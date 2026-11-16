#!/usr/bin/env python3
"""Check CSV gene IDs against a locally installed PyEnsembl annotation."""

import argparse
import csv
from pathlib import Path


def validate_file(path, genome):
    """Print mismatches and missing IDs; return their count."""
    problems = 0
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = csv.DictReader(handle)
        required = {"Symbol", "Ensembl_Gene_ID"}
        if not required.issubset(rows.fieldnames or []):
            raise ValueError(f"{path}: expected columns {sorted(required)}")
        for line, row in enumerate(rows, start=2):
            name, gene_id = row["Symbol"], row["Ensembl_Gene_ID"]
            try:
                gene = genome.gene_by_id(gene_id)
            except ValueError as error:
                print(f"{path}:{line}: {name} {gene_id}: {error}")
                problems += 1
                continue
            if gene.name != name:
                print(f"{path}:{line}: {gene_id}: CSV symbol {name!r}, annotation symbol {gene.name!r}")
                problems += 1
    return problems


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path, nargs="*", help="CSV paths (default: repository CSVs)")
    parser.add_argument("--release", type=int, help="Installed human Ensembl release (default: PyEnsembl's GRCh38 default)")
    args = parser.parse_args(argv)
    from pyensembl import EnsemblRelease, ensembl_grch38

    genome = ensembl_grch38 if args.release is None else EnsemblRelease(args.release, species="human")
    files = args.files or sorted(Path(__file__).resolve().parents[1].glob("*.csv"))
    problems = sum(validate_file(path, genome) for path in files)
    print(f"Checked {len(files)} files; {problems} gene ID or symbol discrepancies.")
    return int(problems != 0)


if __name__ == "__main__":
    raise SystemExit(main())
