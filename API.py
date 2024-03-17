import requests

def api_url_academic_data(student_name, subject, start_date, end_date, AUTH_TOKEN):
    # Define the API endpoint
    url = "https://hpjgmbk65zgzff64b6y7vhw2ua0sytlh.lambda-url.us-east-1.on.aws/"
    
    # Define the headers including the authorization token
    headers = {
        "Authorization": AUTH_TOKEN
    }
    
    # Define the query parameters
    params = {
        "student": student_name,
        "subject": subject,
        "startDate": start_date,
        "endDate": end_date
    }
    
    # Make the GET request
    response = requests.get(url, headers=headers, params=params, timeout=180)
    
    # Check if the request was successful and return the unprocessed json
    if response.status_code == 200:
        print("Success!")
        response = response.json()
        return requests.get(response["url"]).json()
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return 1

def api_session_coaching(email, subject, start_date, end_date, AUTH_TOKEN2):


    url = "https://mk62mbxkbe6flyv44eli5shrhi0hinml.lambda-url.us-east-1.on.aws"

    headers = {
        "Authorization": AUTH_TOKEN2
    }

    params = {
        "email": email,
        "subject": subject,
        "startDate": start_date,
        "endDate": end_date
    }

    response = requests.get(url, headers=headers, params=params, timeout=180)
    if response.status_code == 200:
        print("Success!")
        return response.json()
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return 1

if __name__ == "__main__":
    api_url_academic_data()
    api_session_coaching()