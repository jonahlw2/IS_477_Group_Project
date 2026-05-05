rule prepare_data:
    input:
        pm25="data_final/Table2_1b.csv",
        who="data_final/b7450f71-eae9-4c95-98e4-022ddec4a93f.csv",
        emissions="data_final/fig03_particulate_matter_annual_emissions.csv"
    output:
        pm25="final_snake_data/pm25_uk.csv",
        who="final_snake_data/who_uk.csv",
        emissions="final_snake_data/emissions.csv",
        final="final_snake_data/final_data.csv"
    shell:
        """
        python scripts/prepare_data.py \
            --pm25 {input.pm25} \
            --who {input.who} \
            --emissions {input.emissions} \
            --pm25-out {output.pm25} \
            --who-out {output.who} \
            --emissions-out {output.emissions} \
            --final-out {output.final}
        """