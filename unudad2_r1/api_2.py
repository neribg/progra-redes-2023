import requests

def search_program(title):
    url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

    querystring = {"q":title,"t":"show"}

    headers = {
        "X-RapidAPI-Host": "unogs-unogs-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "KEY"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        for result in data['res']:
            print(f"Title: {result['title']}\nType: {result['type']}\nStart Year: {result['start_year']}\nEnd Year: {result['end_year']}\nGenres: {', '.join(result['genres'])}")
            print("----------------------------------------------")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    program_title = input("Enter the name of a TV program: ")
    search_program(program_title)