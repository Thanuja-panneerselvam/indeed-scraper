
##Indeed Job Scraper

This project utilizes the Apify platform to scrape job listings from Indeed for a specified position and location. The script is designed to fetch job data efficiently and store it in a dataset for easy access.

Prerequisites

- Python 3.x
- An Apify account
- An Apify token

Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/indeed-job-scraper.git
   cd indeed-job-scraper
   ```

2. Install the required packages:

   ```bash
   pip install apify-client
   ```

## Usage

1. Replace `"copy-paste-your-apify-token-name"` in the script with your actual Apify token.

2. Modify the `run_input` dictionary to specify the job position, country, location, and maximum number of items you want to scrape. For example:

   ```python
   run_input = {
       "position": "web developer",
       "country": "US",
       "location": "San Francisco",
       "maxItems": 150,
   }
   ```

3. Run the script:

   ```bash
   python your_script_name.py
   ```

4. After the script finishes running, you can check the scraped data at the following URL:

   ```
   https://console.apify.com/storage/datasets/{your_dataset_id}
   ```

   Replace `{your_dataset_id}` with the actual dataset ID printed in the console.

## Example Output

The script will print each job listing item to the console. The output will include details such as job title, company, location, and more.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Apify](https://apify.com/) for providing the scraping platform.
- [Indeed](https://www.indeed.com/) for the job listings.
