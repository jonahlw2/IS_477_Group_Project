import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path



Path("figures").mkdir(exist_ok=True)

# Read cleaned files created by prepare_data.py
pm25_uk = pd.read_csv("final_snake_data/pm25_uk.csv")
who_uk = pd.read_csv("final_snake_data/who_uk.csv")
emissions_pm25 = pd.read_csv("final_snake_data/emissions.csv")
integrated_master_df = pd.read_csv("final_snake_data/final_data.csv")

# Read raw emissions file 
emissions_df = pd.read_csv("data_final/fig03_particulate_matter_annual_emissions.csv")
emissions_yearwise = emissions_df.copy()
emissions_yearwise.columns = ["pollutant", "year", "emissions_thousand_tonnes"]

emissions_yearwise["year"] = pd.to_numeric(emissions_yearwise["year"], errors="coerce")
emissions_yearwise["emissions_thousand_tonnes"] = pd.to_numeric(
    emissions_yearwise["emissions_thousand_tonnes"], errors="coerce"
)

emissions_yearwise = emissions_yearwise.dropna(
    subset=["year", "emissions_thousand_tonnes"]
)
emissions_yearwise["year"] = emissions_yearwise["year"].astype(int)

emissions_yearwise = emissions_yearwise[
    emissions_yearwise["pollutant"].isin(["PM2.5", "PM10"])
].copy()

emissions_yearwise = emissions_yearwise.pivot(
    index="year",
    columns="pollutant",
    values="emissions_thousand_tonnes"
).reset_index()

emissions_yearwise.columns.name = None
emissions_yearwise = emissions_yearwise.rename(columns={
    "PM2.5": "pm25_emissions",
    "PM10": "pm10_emissions"
})

# Read raw WHO file
who_raw = pd.read_csv("data_final/b7450f71-eae9-4c95-98e4-022ddec4a93f.csv")

who_disease = who_raw[
    (who_raw["Location"] == "United Kingdom of Great Britain and Northern Ireland") &
    (who_raw["Dim1"] == "Both sexes")
].copy()

who_disease = who_disease.rename(columns={
    "Period": "year",
    "Dim2": "disease_category",
    "FactValueNumeric": "mortality_value"
})

who_disease = who_disease[["year", "disease_category", "mortality_value"]]
who_disease["year"] = pd.to_numeric(who_disease["year"], errors="coerce")
who_disease["mortality_value"] = pd.to_numeric(
    who_disease["mortality_value"], errors="coerce"
)
who_disease = who_disease.dropna(subset=["year", "mortality_value"])
who_disease["year"] = who_disease["year"].astype(int)

#integrated data
mortality_data = integrated_master_df.dropna(
    subset=["mortality_value", "emissions_thousand_tonnes", "pm25_concentration"]
).sort_values("year")

mortality_pm_data = integrated_master_df.merge(
    emissions_yearwise,
    on="year",
    how="left"
)

mortality_pm_data = mortality_pm_data.dropna(
    subset=[
        "mortality_value",
        "pm25_concentration",
        "pm25_emissions",
        "pm10_emissions"
    ]
).sort_values("year")

# Plot 1: PM2.5 concentration over time
plt.figure(figsize=(10, 6))
plt.plot(
    pm25_uk["year"],
    pm25_uk["pm25_concentration"],
    marker="o"
)
plt.title("Particulate Matter Concentration Over Time")
plt.xlabel("Year")
plt.ylabel("PM2.5 concentration")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/(1)_pm25_concentration_over_time.png", dpi=300)
plt.close()

# Plot 2: mortality over time
plt.figure(figsize=(10, 6))
plt.plot(
    mortality_data["year"],
    mortality_data["mortality_value"],
    marker="o"
)
plt.title("UK WHO Mortality Value Over Time")
plt.xlabel("Year")
plt.ylabel("Mortality value")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/(2)_mortality_over_time.png", dpi=300)
plt.close()

# Plot 3: PM2.5 emissions over time
plt.figure(figsize=(10, 6))
plt.plot(
    mortality_data["year"],
    mortality_data["emissions_thousand_tonnes"],
    marker="o"
)
plt.title("Particulate Matter Emissions Over Time")
plt.xlabel("Year")
plt.ylabel("Emissions, thousand tonnes")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/(3)_pm25_emissions_over_time.png", dpi=300)
plt.close()

# Plot 4: PM2.5 emissions and PM2.5 concentration
plt.figure(figsize=(10, 6))
plt.scatter(
    mortality_data["emissions_thousand_tonnes"],
    mortality_data["pm25_concentration"]
)
plt.title("PM2.5 Emissions and PM2.5 Concentrations")
plt.xlabel("PM2.5 emissions, thousand tonnes")
plt.ylabel("PM2.5 concentration")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/(4)_pm25_emissions_vs_concentration.png", dpi=300)
plt.close()

# Plot 5: indexed PM2.5, PM10, and mortality
compare_data = mortality_pm_data.copy()

compare_data["pm25_emissions_index"] = (
    compare_data["pm25_emissions"] / compare_data["pm25_emissions"].iloc[0] * 100
)
compare_data["pm10_emissions_index"] = (
    compare_data["pm10_emissions"] / compare_data["pm10_emissions"].iloc[0] * 100
)
compare_data["mortality_index"] = (
    compare_data["mortality_value"] / compare_data["mortality_value"].iloc[0] * 100
)

plt.figure(figsize=(10, 6))
plt.plot(
    compare_data["year"],
    compare_data["pm25_emissions_index"],
    marker="o",
    label="PM2.5 emissions index"
)
plt.plot(
    compare_data["year"],
    compare_data["pm10_emissions_index"],
    marker="o",
    label="PM10 emissions index"
)
plt.plot(
    compare_data["year"],
    compare_data["mortality_index"],
    marker="o",
    label="Mortality index"
)
plt.title("Indexed PM2.5 Emissions, PM10 Emissions, and Mortality Over Time")
plt.xlabel("Year")
plt.ylabel("Index, first overlapping year = 100")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/(5)_indexed_emissions_and_mortality.png", dpi=300)
plt.close()

# Plot 6: mortality compared with PM2.5 and PM10 emissions
plt.figure(figsize=(8, 5))
plt.scatter(
    mortality_pm_data["pm25_emissions"],
    mortality_pm_data["mortality_value"],
    label="PM2.5 emissions"
)
plt.scatter(
    mortality_pm_data["pm10_emissions"],
    mortality_pm_data["mortality_value"],
    label="PM10 emissions"
)
plt.title("Mortality Compared with PM2.5 and PM10 Emissions")
plt.xlabel("Emissions, thousand tonnes")
plt.ylabel("Mortality value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/(6)_emissions_vs_mortality.png", dpi=300)
plt.close()

# Plot 7: mortality by disease category
disease_data = who_disease[who_disease["disease_category"] != "All causes"]

plt.figure(figsize=(10, 6))
for disease in disease_data["disease_category"].unique():
    one_disease = disease_data[disease_data["disease_category"] == disease]
    plt.plot(
        one_disease["year"],
        one_disease["mortality_value"],
        marker="o",
        label=disease
    )

plt.title("Air Pollution-Attributable Mortality by Disease Category")
plt.xlabel("Year")
plt.ylabel("Mortality value")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/(7)_disease_mortality_over_time.png", dpi=300)
plt.close()

# Plot 8: average mortality by disease category
avg_disease_mortality = (
    disease_data
    .groupby("disease_category")["mortality_value"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

plt.figure(figsize=(10, 6))
plt.bar(
    avg_disease_mortality["disease_category"],
    avg_disease_mortality["mortality_value"]
)
plt.title("Average Air Pollution-Attributable Mortality by Disease Category")
plt.xlabel("Disease category")
plt.ylabel("Average mortality value")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("figures/(8)_average_disease_mortality.png", dpi=300)
plt.close()

print("Visualization script completed.")
print("Figures saved in the figures/ directory.")
