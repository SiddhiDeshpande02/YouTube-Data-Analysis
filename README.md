YouTube-Data-Analysis
A project exploring data from YouTube education creators using Google Cloud API, Pandas, Matplotlib, and Power BI.
YouTube Education Creators Analysis Overview: This project is a personal learning initiative inspired by the completion of the Kaggle Pandas course. The goal was to build a full data analysis pipeline, starting from collecting real-world YouTube data, cleaning and processing it, and producing insightful visualizations to uncover patterns in the educational content space.
Project Pipeline Data Extraction: Fetched data from five educational YouTube channels using the Google Cloud YouTube API, learning how to work with APIs and authentication in real environments.
Data Cleaning & Exploration: Used Python Pandas for data manipulation, organization, and preliminary exploration to identify useful features and build comparative analyses.
Visualization: Utilized Matplotlib in Python to create bar, line, and scatter plots to clarify metrics such as engagement rates and audience distribution.
Developed interactive dashboards in Power BI, featuring pie charts, donut graphs, line, and bar graphs for deeper comparative visual insights.

Key Insights:  Shorter videos consistently achieve higher engagement than longer ones.
Audience size and engagement varies noticeably among different creators, even within the same educational space.
Visualizing across platforms (Python & Power BI) enriched the understanding and clarity of data-driven trends.
Project Files Included Python scripts for data extraction, cleaning, and visualization

Project Statistical Highlights
- Analysis shows that long videos (over 10 minutes) had an average engagement of 0.045, while short videos (10 minutes or less) averaged 0.031 engagement.
- Shorter videos actually saw 46.7% lower average engagement than longer videos in this dataset, contrary to many general assumptions.
- The overall average engagement across all educational YouTube videos analyzed was 0.037, with individual values ranging from as low as 0.002 to as high as 0.119.
- The channel “CrashCourse” had the highest average engagement at 0.054, indicating stronger audience interaction compared to peers.

Strong positive correlations were found between views and likes (correlation coefficient: 0.93), and between views and comments (correlation coefficient: 0.80), showing that higher view counts are strongly associated with more active audience feedback.

Cleaned dataset: youtube_education_trends.csv

Power BI report: Report.pdf

Engagement summary: channel-vice-average-engagement.pdf

Example outputs and visuals: This README file

Tools Used:
 - Python 3.x
 - Pandas
 - Matplotlib
 - Google Cloud YouTube API
 - Power BI

How to Reproduce: Clone this repository.
Ensure you have a Google Cloud API key (instructions in the script or comments).
Run the provided Python scripts (.py or .ipynb files) to fetch and clean YouTube data.
Visualise data in Python or import the dataset into Power BI for interactive dashboards.

Learning Notes & Future Work: This project was conceived as a practical exercise in mastering the end-to-end data workflow. Future extensions could include automation, expanding the dataset, or integrating deeper metrics such as comment analysis or temporal trends.

Contact: Feel free to reach out via LinkedIn if you'd like to discuss the methodology or have feedback on the analysis!
