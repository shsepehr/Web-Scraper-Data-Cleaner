import pandas as pd

def clean_data(df, output_path, report_path):
    """
    Clean the DataFrame and save CSV + report.
    Args:
        df (pd.DataFrame): Input DataFrame
        output_path (str): CSV output path
        report_path (str): Report output path
    Returns:
        cleaned_df (pd.DataFrame), report (str)
    """
    report = ""

    # Drop duplicate
    dup_count = df.duplicated().sum()
    df = df.drop_duplicates()
    report += f"Removed {dup_count} duplicate rows\n"

    # Replacing empty values
    missing_count = df.isnull().sum().sum()
    df = df.fillna("N/A")
    report += f"Filled {missing_count} missing values\n"

    # Save CSV
    df.to_csv(output_path, index=False)

    # Save report
    with open(report_path, "w") as f:
        f.write(report)

    return df, report
