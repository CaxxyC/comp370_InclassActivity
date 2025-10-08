import os.path
import requests
import json

# script_dir = os.path.dirname(__file__)
# raw_path = os.path.join(script_dir, "..", "data", "raw")
def main():

    # parse = argparse.ArgumentParser
    # parse.add_argument("author")

    # args = parse.parse_args()

    author_name = r"j%20k%20rowling"

    # get the author's key
    query_url = "https://openlibrary.org/search/authors.json?q=" + author_name
    r = requests.get(query_url)

    author_data = r.json()
    author_key = author_data["docs"][0]["key"]
    print("Author key:", author_key)

    # get the author's key
    query_url = "https://openlibrary.org/authors/" + author_key + "/works.json"
    r = requests.get(query_url)
    author_works_data = r.json()

    # write out the raw data
    # fname = f"author_{author_key}_works.json"
    with open("data/jkRowlingWorks.json", "w") as f:
        json.dump(author_works_data, f, indent=4)

if __name__ == "__main__":
    main()