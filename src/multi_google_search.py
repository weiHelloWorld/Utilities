import subprocess, argparse

def multi_google_search(search_queries):
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Windows
    # chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # macOS
    # chrome_path = "google-chrome"  # Linux

    for query in search_queries:
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        subprocess.Popen([chrome_path, "--incognito", url])
    return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query_f", type=str, help="query file", required=True)
    args = parser.parse_args()
    query_f = args.query_f
    with open(query_f, "r") as my_file:
        lines = [line.strip() for line in my_file]
    multi_google_search(search_queries=lines)
    return


if __name__ == "__main__":
    main()

    