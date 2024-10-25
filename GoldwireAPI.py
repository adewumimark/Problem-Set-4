import requests

def get_literature_by_species(species_name):
    # URL for the GBIF literature search API
    literature_url = "https://api.gbif.org/v1/literature/search"
    
    # Define parameters for the search query
    params = {
        "q": species_name,
        "limit": 5  # Limit the results to only 5 entries
    }

    # Make the request to the GBIF API
    response = requests.get(literature_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        literature_data = response.json()

        # Print out relevant literature details
        for item in literature_data['results']:
            title = item['title']
            authors = ', '.join([f"{author['firstName']} {author['lastName']}" for author in item.get('authors', [])])
            year = item.get('year', 'N/A')  # Use 'N/A' if year is not available
            print("")
            print(f"Title: {title}\nAuthors: {authors}\nYear: {year}\n")
    else:
        print("Error:", response.status_code, response.text)

# Input species name and get 5 relevant literatures
species_name = input("Enter a species name: ")
get_literature_by_species(species_name)
