import openai
import json

def query_gpt4(studentName, subject, startDate, endDate, studentMetrics, studentCoaching):

    # Enter your API key. Will change to an environment variable in the future
    openai.api_key = "CHANGE TO YOUR OPENAI TOKEN"


    # Actual prompt
    promptText = f"""You will be provided with 2 json objects related to student performance in a school. The first json is a collection of student metrics for different dates. The second json is optional, and includes session coaching for the same dates. Both objects will be for {studentName} and for the subject of {subject}. You will ignore all data before {startDate} and after {endDate}. You will analyze both objects thoroughly, and strictly return a json object with the following keys and values:
* "studentName": #populate with the student's name 
* "subject": #populate with the chosen subject 
* "location": #populate with the student's location
* "dateRange": #populate with the date range for the provided data
* "levelVar": #populate with the student's level 
* "problemStatement": #populate with the main problem identified for this student
* "questionAns": #populated with the most important question that needs to be answered
* "importantProblem": #After you perform your analysis summarize your findings in a way that clearly explains the causes of the problem statement 
* "schoolStatement": #Clearly state what needs to be done and by whom to fix the problem and help the student learn more effectively. 
* "studentStatement": #Write what the student should do in a way that is clear and easy for the student to understand. If the student follows this recommendation they should learn more effectively. 
* "boolStudentProg": #Is the student progressing optimally? Suboptimal progress is indicated by mastering less than 70% of the lesson target in the period. Struggling students often have low accuracy (below 80%). accepted values for this key are either "Yes" or "No" 
* "evStudentProg": #provide direct proof for the boolStudentProg you've chosen. This value will be taken directly from the student metrics json
* "descStudentProgress": #Describe the steps you have taken to arrive at the conclusion stated on the in evStudentProg value. List and link all the sources consulted as long as any challenges in finding relevant information. 
* "boolStudentLevel": #Is the student working at the right level? Students should be bracketed by two standardized tests - one mastered (90%+ score) and one unmastered (score below 90%) in the grade immediately above. Accepted values for this value are either "Yes" or "No"
* "evStudentLevel": ##provide direct proof for the boolStudentLevel you've chosen. This value will be taken directly from the student metrics json
* "descStudentLevel": #Describe the steps you have taken to arrive at the conclusion stated on the in "evStudentLevel". List and link all the sources consulted, as long as any challenges in finding relevant information
* "bool2hr": #Is the student behaving as a '2hr learner'? To be considered a '2hr learner' the student needs at least 25 minutes/school day dedicated to learning, strived to meet their 'lessons mastered’ targets without squandering their learning time and used the apps correctly and avoided learning anti-patterns. Accepted values for this value are either "Yes", "No - not putting enough time", "No - 30% waste", "No - 50% waste", "No - 90% waste"
* "ev2hr": #provide direct proof for the bool2hr value you've chosen. This value will be taken directly from the student metrics json
* "desc2hr": #Describe the steps you have taken to arrive at the conclusion stated on the in "ev2hr". List and link all the sources consulted, as long as any challenges in finding relevant information
* "boolLackProg": #What are the reasons for the lack of progress? Struggling students consistently have low accuracy (below 80%) or take multiple sessions to master skills. This could be a consequence of anti-patterns, insufficient support, subpar skill plans, or knowledge gaps. Accepted values for this value are either "None - Optimal progress", "Wrong level", "Not enough time", "Waste / Anti - patterns", "Lack of scaffolding / support", "Unable to determine"
* "evLackProg": #provide direct proof for the boolLackProg value you've chosen. This value will be taken directly from the student metrics json
* "descLackProg": #Describe the steps you have taken to arrive at the conclusion stated on the in "evLackProg". List and link all the sources consulted, as long as any challenges in finding relevant information
* "boolOtherIns": #Other insights, Are there other insights or analyses that are pertinent to the issue raised by the customer? Accepted values for this value are "Yes" or "No"
* "evOtherIns": #provide direct proof for the boolOtherIns value you've chosen. This value will be taken directly from the student metrics json
* "descOtherIns": #Describe the steps you have taken to arrive at the conclusion stated on the in "evOtherIns". List and link all the sources consulted, as long as any challenges in finding relevant information
Example response:
* "studentName": Branson Pfiester 
* "subject": Language 
* "location": Austin K-8
* "dateRange": 01-01-2024 to 29-01-2024
* "levelVar": Level 3 
* "problemStatement": Branson wants their  ReadTheory app to be reset as unable to make any progress in lessons.
* "questionsAns": Is the student struggling?, Is there underlying friction or learning strategies that may assist her productivity as part of this new plan?
* "importantProblem": The student mentioned that he is facing difficulty with the current lessons on Read Theory.
* "schoolStatement": Recommend a 2hr coaching session to improve app usage.
* "studentStatement": Spend the required time working on Reading, 25 min/day. Read the explanations for the questions you get wrong and read the full article before attempting the questions.
* "boolStudentProg": No
* "evStudentProg":  'accuracy (cq/tq) (CUSTOM)': '0.772'
* "descStudentProgress": Student has 21% compliance with lessons mastered vs the target. Accuracy is below 80%
* "boolStudentLevel": Yes
* "evStudentLevel": 'Student': 'Branson Pfiester', 'Subject': 'Math', 'Lower Bound': '6', 'Upper Bound': '7', 'Status': 'Bracketed'
* "descStudentLevel": The student is bracketed between Grade 6 (lower bound) and Grade 7 (upper bound). They are rostered at 7th grade level math.
* "bool2hr": No - Not putting enough time.
* "ev2hr": 'Subject': 'Math', 'Total Minutes': '464.7400015592575', 'Mins / weekday': '9.781372625453802'
* "desc2hr": Since the beginning of January Branson has only spent an average of 9 min/day working on Math. They present two main usage problems: Not reading the articles fully before answering the questions, Not reading the explanations for the questions they get wrong.
* "boolLackProg": Waste / Anti-patterns
* "evLackProg": 'description': 'Student is rushing through the questions, and at the end the student skips the in-depth explanations provided by the app for incorrect answers, missing out on learning from their mistakes.'
* "descLackProg": One clue may be the coaching received from the 29th, indicating the student is rushing through questions & ignoring explanations after mistakes.
* "boolOtherIns": Yes
* "evOtherIns": Branson shows higher engagement and success rates in interactive problem-solving activities compared to traditional problem sets.
* "descOtherIns": Reviewing engagement data revealed Branson performs better and spends more time on tasks when presented in an interactive format, suggesting a potential strategy for increasing his engagement and understanding.
Hard constraints:
* The only response you will return is the processed json, without any commentary whatsoever.
* You will ignore all data before {startDate} and after {endDate}
* You will ignore all data for subjects other than {subject}
Student metrics json: {studentMetrics}
Student metrics coaching json: {studentCoaching}"""

    try:
        response = openai.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": promptText
                }
            ],
            response_format={ "type": "json_object" },
            model="gpt-4-turbo-preview"
        )

    except Exception as e:
        print(f"An error occurred: {e}")
        input("press anything to continue...")
    
    # Parsing the string into a dictionary
    content_dict = json.loads(response.choices[0].message.content)
    return content_dict
