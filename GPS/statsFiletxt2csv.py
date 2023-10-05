import pandas as pd


# this procedure transform a txt file into csv 

def statsFileTxt2csv(file_path):
    # Initialize an empty list to hold the data rows
    data_list = []

    # Initialize an empty dictionary to hold the current row of data
    current_row = {}

    # Read the txt file line by line
    with open(f"{file_path}/GPS/stats_analysis.txt", 'r') as f:
        for line in f:
            line = line.strip()
            
            # Parse the Year, Day, Month, Time of Day, GPS Name
            if line.startswith("Year:"):
                parts = line.split(", ")
                year, day, month, time_of_day, gps_name = parts
                current_row['Year'] = year.split(":")[1]
                current_row['Day'] = day.split(": ")[1]
                current_row['Month'] = month.split(": ")[1]
                current_row['Time of Day'] = time_of_day.split(": ")[1]
                current_row['GPS Name'] = gps_name.split(": ")[1]
            
            # Parse the statistical metrics
            elif line:
                metric, value = line.split(": ")
                current_row[metric] = value
            
            # End of a block, save the row and clear current_row
            elif not line:
                if current_row:
                    data_list.append(current_row)
                    current_row = {}

    # Create a DataFrame from the list of rows
    df = pd.DataFrame(data_list)

    # Reorder columns
    columns_order = ['GPS Name', 'Day', 'Month', 'Year', 'Time of Day', 'Minimum', 'Maximum', 'Mean', 'Median', 'Variance', 'Standard Deviation', 'Standard Error', '95% Confidence Interval', 'Margin of Error']
    df = df[columns_order]

    # Save DataFrame to CSV
    df.to_csv(f'{file_path}/GPS/stats_analysis.csv', index=False)