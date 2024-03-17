# EduBot

EduBot is an innovative tool designed to perform deep analysis on student data metrics, leveraging the power of GPT through OpenAI's API. By connecting to the Student Data Metrics API and the Coaching API, EduBot provides insightful feedback and actionable advice in a professionally formatted Word document.

## Features

- Connects to Student Data Metrics and Coaching APIs.
- Uses `gptConn.py` to prompt ChatGPT for deep analysis of the JSON data retrieved from API calls.
- Processes the analysis and integrates it into a `template.docx` file, producing a comprehensive report in DOCX format.

## Prerequisites

- Connection to Kerio VPN for API functionality.
- An OpenAI API token (to be placed in `gptConn.py`, line 7).

## Supported Subjects

EduBot accepts the following subjects for analysis:

- Language
- Math
- Science
- Reading
- Social Science
- Social Studies

## Installation

Before running EduBot, ensure you have Python installed on your system and then set up the required environment by installing the necessary packages.

If using the Python interpreter directly:

```bash
pip install -r requirements.txt
```

If not using the Python interpreter directly:

```bash
python -m pip install -r requirements.txt
```

## Usage

1. Ensure you are connected to the Kerio VPN.
2. Open `gptConn.py` and enter your OpenAI API token at line 7.
3. Run `main.py` from your terminal or command prompt:

```bash
python main.py
```

4. When prompted, enter:
   - The student's full name.
   - The subject (choose from the supported subjects listed above).
   - The start and end dates for the analysis period (format: `YYYY-MM-DD`).

EduBot will then perform the analysis and generate a DOCX report based on the `template.docx` file.

## Notes

- Program uses the 'gpt-4' model which is limited to around 8k tokens. Keep the date ranges short to ensure proper operations.
- If longer date ranges are required, use the 'gpt-4-32k' model by editing the gptConn.py file and changing the model.

## Left to do

- Create a GUI for the main app
- refactor the code where needed
- add proper validation for additional bad user input such as a endDate ending sooner than the startDate

## Contributing

We welcome contributions to EduBot! If you have suggestions for improvements or encounter any issues, please feel free to open an issue or submit a pull request.

## License

EduBot is made available under the GNU Lesser General Public License version 3 (LGPLv3). For more details, see the [LICENSE](LICENSE) file in this repository.
