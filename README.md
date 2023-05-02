# GSearch - A Python Package for Automated Google Searches and Scraping of Search Results

Introduction: gsearch is a Python package that allows users to perform automated Google searches and extract information from the search results using Python code. The package uses the Playwright and Selectolax libraries to scrape search results and provides a convenient way to automate and extract information from Google searches.

## Installation

To install gsearch, you can use pip:

`pip install gsearch-nyaa`

## Usage

To use gsearch, first import the `Google` class from the package:

`from gsearch import Google`

Then, create a new instance of the `Google` class and call the `search` method with the desired query:

`with Google() as google:     results = google.search("Python tutorial")`

The `search` method returns a list of `GoogleSearchResult` objects, each containing the URL, title, and description of a search result.

To print the search results, you can use the following code:

```
for result in results:
    print(f"Title: {result.title}")
    print(f"URL: {result.url}")
    print(f"Description: {result.description}\n")
```

Here is an example of using gsearch to perform a Google search for "how to use Python":

```
from gsearch import Google
with Google() as google:
    results = google.search("how to use Python")
    for result in results:
        print(f"Title: {result.title}")
        print(f"URL: {result.url}")
        print(f"Description: {result.description}\n")
```

This will perform a Google search for "how to use Python" and print the title, URL, and description of each search result.

## Contributing

If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request on GitHub.

## License

gsearch is released under the MIT License. See `LICENSE` for more information.

Conclusion: gsearch is a powerful Python package that makes it easy to automate Google searches and extract information from the search results. Whether you need to perform a one-time search or automate a search process, gsearch is a great tool to have in your Python toolbox.
