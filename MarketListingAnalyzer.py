from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd


def load_html(source_path: Path) -> str:
    return source_path.read_text(encoding="utf-8")


def parse_job_listings(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    job_listings = soup.select(".job-listing")

    jobs = []
    for listing in job_listings:
        title_element = listing.select_one(".job-title")
        company_element = listing.select_one(".company-name")
        location_element = listing.select_one(".job-location")

        title = title_element.get_text(strip=True) if title_element else "N/A"
        company = company_element.get_text(strip=True) if company_element else "N/A"
        location = location_element.get_text(strip=True) if location_element else "N/A"

        jobs.append(
            {
                "Title": title,
                "Company": company,
                "Location": location,
            }
        )

    return jobs


def print_summary(dataframe: pd.DataFrame) -> None:
    total_listings = len(dataframe)
    unique_companies = dataframe["Company"].nunique()
    unique_locations = dataframe["Location"].nunique()

    print()
    print("Market Summary")
    print("--------------")
    print(f"Total Listings: {total_listings}")
    print(f"Unique Companies: {unique_companies}")
    print(f"Unique Locations: {unique_locations}")

    print()
    print("Listings By Location")
    print("--------------------")
    print(dataframe["Location"].value_counts().to_string())

    print()
    print("Listings By Company")
    print("-------------------")
    print(dataframe["Company"].value_counts().to_string())


def main() -> None:
    print("Talent Market Listing Analyzer")
    print("------------------------------")
    print("Analyze a local HTML export of job listings and generate a structured CSV report.")
    print()

    path_input = input("Enter HTML source file path [sample_job_board.html]: ").strip()
    source_path = Path(path_input or "sample_job_board.html")

    if not source_path.exists():
        print(f"Source file not found: {source_path}")
        return

    html = load_html(source_path)
    jobs = parse_job_listings(html)

    if not jobs:
        print("No job listings were found in the provided file.")
        return

    dataframe = pd.DataFrame(jobs)
    output_path = Path("talent_market_listings.csv")
    dataframe.to_csv(output_path, index=False)

    print()
    print("Extracted Listings")
    print("------------------")
    print(dataframe.to_string(index=False))

    print_summary(dataframe)

    print()
    print(f"CSV report saved to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
