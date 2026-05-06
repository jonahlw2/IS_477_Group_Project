"""
Clean and integrate PM2.5, WHO mortality, and emissions datasets.
"""

import argparse
from pathlib import Path

import pandas as pd


def ensure_parent(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def clean_pm25(pm25_path: str | Path) -> pd.DataFrame:
    pm25_df = pd.read_csv(pm25_path, header=2)

    pm25_clean = pm25_df.iloc[0:, [0, 1, 2]].copy()
    pm25_clean.columns = ["year", "site", "pm25_concentration"]

    pm25_clean["year"] = pd.to_numeric(pm25_clean["year"], errors="coerce")
    pm25_clean["pm25_concentration"] = pd.to_numeric(
        pm25_clean["pm25_concentration"], errors="coerce"
    )

    pm25_clean = pm25_clean.dropna(subset=["year", "pm25_concentration"])
    pm25_clean["year"] = pm25_clean["year"].astype(int)

    pm25_uk = pm25_clean[pm25_clean["site"] == "All sites (mean)"].copy()
    pm25_uk["geography"] = "United Kingdom"

    return pm25_uk[["year", "geography", "pm25_concentration"]]


def clean_who(who_path: str | Path) -> pd.DataFrame:
    who_df = pd.read_csv(who_path)

    who_uk = who_df[
        (who_df["Location"] == "United Kingdom of Great Britain and Northern Ireland")
        & (who_df["Dim1"] == "Both sexes")
        & (who_df["Dim2"] == "All causes")
    ][["Period", "Location", "Indicator", "FactValueNumeric"]].copy()

    who_uk.columns = ["year", "location", "indicator", "mortality_value"]
    who_uk["year"] = pd.to_numeric(who_uk["year"], errors="coerce")
    who_uk["mortality_value"] = pd.to_numeric(who_uk["mortality_value"], errors="coerce")

    who_uk = who_uk.dropna(subset=["year", "mortality_value"])
    who_uk["year"] = who_uk["year"].astype(int)
    who_uk["geography"] = "United Kingdom"

    return who_uk[["year", "geography", "mortality_value"]]


def clean_emissions(emissions_path: str | Path) -> pd.DataFrame:
    emissions_df = pd.read_csv(emissions_path)

    emissions_clean = emissions_df.copy()
    emissions_clean.columns = ["pollutant", "year", "emissions_thousand_tonnes"]

    emissions_clean["year"] = pd.to_numeric(emissions_clean["year"], errors="coerce")
    emissions_clean["emissions_thousand_tonnes"] = pd.to_numeric(
        emissions_clean["emissions_thousand_tonnes"], errors="coerce"
    )

    emissions_clean = emissions_clean.dropna(
        subset=["year", "emissions_thousand_tonnes"]
    )
    emissions_clean["year"] = emissions_clean["year"].astype(int)

    emissions_pm25 = emissions_clean[
        emissions_clean["pollutant"] == "PM2.5"
    ].copy()

    emissions_pm25["geography"] = "United Kingdom"

    emissions_pm25 = emissions_pm25[
        ["year", "geography", "emissions_thousand_tonnes"]
    ]

    return emissions_pm25


def build_integrated_master(
    pm25_uk: pd.DataFrame, who_uk: pd.DataFrame, emissions_pm25: pd.DataFrame
) -> pd.DataFrame:
    return (
        pm25_uk.merge(emissions_pm25, on=["year", "geography"], how="outer")
        .merge(who_uk, on=["year", "geography"], how="outer")
        .sort_values("year")
        .reset_index(drop=True)
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare cleaned PM2.5, WHO, emissions, and integrated datasets."
    )
    parser.add_argument("--pm25", required=True, help="Input Table2_1b.csv path")
    parser.add_argument("--who", required=True, help="Input WHO CSV path")
    parser.add_argument("--emissions", required=True, help="Input emissions CSV path")
    parser.add_argument("--pm25-out", required=True, help="Output cleaned PM2.5 CSV path")
    parser.add_argument("--who-out", required=True, help="Output cleaned WHO CSV path")
    parser.add_argument("--emissions-out", required=True, help="Output cleaned PM2.5 emissions CSV path")
    parser.add_argument("--final-out", required=True, help="Output integrated final CSV path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    pm25_uk = clean_pm25(args.pm25)
    who_uk = clean_who(args.who)
    emissions_pm25 = clean_emissions(args.emissions)
    integrated_master = build_integrated_master(pm25_uk, who_uk, emissions_pm25)

    outputs = [
        args.pm25_out,
        args.who_out,
        args.emissions_out,
        args.final_out,
    ]
    for output in outputs:
        ensure_parent(output)

    pm25_uk.to_csv(args.pm25_out, index=False)
    who_uk.to_csv(args.who_out, index=False)
    emissions_pm25.to_csv(args.emissions_out, index=False)
    integrated_master.to_csv(args.final_out, index=False)

    print(f"Saved {args.pm25_out}: {pm25_uk.shape}")
    print(f"Saved {args.who_out}: {who_uk.shape}")
    print(f"Saved {args.emissions_out}: {emissions_pm25.shape}")
    print(f"Saved {args.final_out}: {integrated_master.shape}")


if __name__ == "__main__":
    main()
