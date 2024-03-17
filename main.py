import re
import pandas as pd
import API
import gptConn
import wordDoc

def main():

    # Master roster sheet
    URL = "https://docs.google.com/spreadsheets/d/1wBLO22hSTrKfDDXCrHIEZ1WCYIgyc-J2krKizrpx500/export?format=csv"

    # Queries the google sheet for the current roster of students and declares all constants
    df = pd.read_csv(URL)

    FULL_NAMES = [f"{row['Full Name']}" for index, row in df.iterrows()]
    EMAILS = [f"{row['Student Alpha Email']}" for index, row in df.iterrows()]
    ALLOWED_SUBJECT = ["Language", "Math", "Reading", "Science", "Social Science", "Social Studies"]

    # Stats API
    AUTH_TOKEN = "-ehN=MkFaIk/iDMinaaoar?fJwbRlKpqEqWQ11cFxU=ibqwQe9Uj0eF6XP-6JgvT"

    # Analysis API
    AUTH_TOKEN2 = "qVSA4LC9SdTrsKezwHlhD9r=5cH5tPZLrG3e24kRZNaLrnLIm4jk0cN2YfgquIRN"

    # Main program
    while True:
        
        while True:
            student_name = input("Enter the student's name: ").title()
            if student_name in FULL_NAMES:
                break
            else:
                print("Invalid name. Please make sure the name of the student is valid...")
        while True:
            subject = input("Enter the Subject: ").title()
            if subject in ALLOWED_SUBJECT:
                break
            else:
                print('Not a valid subject. Available subject are: Language, Math, Reading, Science, Social Science, Social Studies. Please try again...')
        
        # checking student name against all emails and automatically entering email
        try:
            email = next(email for email in EMAILS if email.startswith(student_name.lower().replace(" ", ".")))
        except StopIteration:
            print(f"No email found for {student_name}")
            input("Enter anything to exit...")
            break

        # Validates if dates are real
        def validate_date(date):
            regex = r"^(200[0-9]|201[0-9]|202[0-4])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"

            if re.match(regex, date):
                return True
            else:
                return False
        while True:
            start_date = input("Enter the Start Date (YYYY-MM-DD): ")
            if validate_date(start_date):
                break
            else:
                print("Bad date. Please enter a properly formatted date from the year 2000 to 2024.")
        while True:
            end_date = input("Enter the End Date (YYYY-MM-DD): ")
            if validate_date(end_date):
                break
            else:
                print("Bad date. Please enter a properly formatted date from the year 2000 to 2024.")
        
        try:
            response_ac_data = API.api_url_academic_data(student_name, subject, start_date, end_date, AUTH_TOKEN)
        except:
            print("Error connecting to API endpoint. Please try again, make sure you're connected to Kerio VPN")
            input("Press any key to quit...")
            break

        try:
            response_coach_data = API.api_session_coaching(email, subject, start_date, end_date, AUTH_TOKEN2)[0]

        except:
            response_coach_data = "No coaching data"

        response = {"stats_api": response_ac_data, "coaching_api": response_coach_data}

        response_dict = gptConn.query_gpt4(student_name, subject, start_date, end_date, response["stats_api"], response["coaching_api"])

        template_path = './template.docx'
        output_path = f'./Academics Deep Dive - {student_name} - {start_date} to {end_date}.docx'

        wordDoc.copy_and_replace_text_in_docx(template_path, output_path, response_dict)

        print(f"Finished creating document: {output_path}.\n")

        # Runs again or ends the program
        query = input("Enter 'Q' to quit, or enter any other key to run another process...: ")
        if query.lower() == "q":
            break
        else:
            continue

if __name__ == "__main__":
    main()
