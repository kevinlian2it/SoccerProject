# COMS W3132 Individual Project

## Author
Kevin Lian
kl3451@columbia.edu

## Project Title
**Soccer Talent Identifier: Leveraging Machine Learning for Optimal Player-Team Fit**

## Project Description
The Soccer Talent Identifier project leverages machine learning to match soccer players with teams where they are most likely to excel. Motivated by the growing complexity and competitive nature of sports analytics, as well as a huge personal passion for the sport, this project seeks to solve the challenge of identifying optimal player-team fits using data-driven insights. By analyzing detailed player statistics from fbref, we aim to develop predictive models that can recommend player signings based on a team's strategic needs and playing style.

Although most high-level soccer teams already have detailed databases for player scouting, these databases are highly confidential. This project seeks to make player scouting and knowledge more accessible to everyday fans and make fans more informed about players and clubs. The main goals for the semester include successfully scraping and processing player data from fbref, developing and testing machine learning models for player-team matching, and creating a user-friendly interface for accessing these insights.

The project holds significant utility and interest for soccer clubs, scouts, and analytics enthusiasts, offering a novel tool for data-informed decision-making in player acquisition and team development. By harnessing the power of machine learning, the Soccer Talent Identifier promises to bring a new level of precision to the art of building winning teams.

## Timeline

*To track progress on the project, we will use the following intermediate milestones for your overall project. Each milestone will be marked with a tag in the git repository, and we will check progress and provide feedback at key milestones.*

| Date               | Milestone                                                                                              | Deliverables                | Git tag    |
|--------------------|--------------------------------------------------------------------------------------------------------|-----------------------------|------------|
| **March&nbsp;29**  | Submit project description                                                                             | README.md                   | proposal   |
| **April&nbsp;5**   | Update project scope/direction based on instructor/TA feedback                                         | README.md                   | approved   |
| **April&nbsp;12**  | Basic project structure with empty functions/classes (incomplete implementation), architecture diagram | Source code, comments, docs | milestone1 |
| **April&nbsp;19**  | Progress on implementation (data successfully mined and into a usable format)                          | Source code, unit tests     | milestone2 |
| **April&nbsp;26**  | Completely (or partially) finished implementation                                                      | Source code, documentation  | milestone3 |
| **May&nbsp;10**    | Final touches (conclusion, documentation, testing, etc.)                                               | Conclusion (README.md)      | conclusion |

*The column Deliverables lists deliverable suggestions, but you can choose your own, depending on the type of your project.*

## Requirements, Features and User Stories

**Feature 1: Data Scraping**

User Story: As a data scientist, I need to automatically extract player statistics and historical performance data from fbref.com, so I can analyze and utilize up-to-date data without manual intervention.

Scenario: The system schedules daily scraping tasks that pull the latest player statistics from fbref.com, ensuring that the dataset is always current and reflects the most recent games.

**Feature 2: Data Preprocessing**

User Story: As a developer, I need tools to clean and preprocess the raw data, transforming it into a structured format, ready for analysis and model training.

Scenario: Once data is scraped, it undergoes preprocessing to remove inconsistencies, handle missing values, and convert text data into numerical values that can be used in machine learning models.

**Feature 3: Player Performance Prediction Model**

User Story: As a team strategist, I want to use historical data to predict future performance of players, so I can make informed decisions about potential signings.

Scenario: A team strategist inputs desired player characteristics, and the system provides predictions and insights on how well players matching these characteristics are expected to perform in the upcoming season.

**Feature 4: Player-Team Fit Analysis**

User Story: As a soccer club scout, I need a tool that can suggest players who fit our team’s style and needs, optimizing our recruitment strategy.

Scenario: The scout specifies the team’s playing style and needs using the system interface. The system then analyzes available players and suggests those whose past performance and skills best match the criteria.

**Feature 5: Interactive Dashboard**

User Story: As a coach, I need an interactive dashboard to visualize player statistics and model outputs, helping me to easily understand data-driven insights.

Scenario: The coach logs into the dashboard to view a visual representation of data on player performance trends, predictions, and recommended signings, with options to drill down into specific aspects like defensive skills or goal scoring.

**Requirements**

_Hardware:_

Computer with enough processing power to handle large datasets and run computations.

_Software:_

Python 3.11: The core programming language for the project.

Pandas and NumPy: For data manipulation and numerical analysis.

Scikit-learn: For implementing machine learning models. (For future implementation)

Matplotlib: For data visualization. (For future implementation)

_Online Services:_

GitHub: For version control and collaboration.

transfermarkt.com: Data to generate market fees. (For future implementation)

fbref.com: As the primary data source.

URL used for player data: https://fbref.com/en/comps/Big5/gca/players/Big-5-European-Leagues-Stats#stats_gca

URL used for team data: https://fbref.com/en/comps/9/gca/Premier-League-Stats

## Technical Specification

### How to Run the Code
The code can be run by downloading all the python files first. Then, the user would have to install the library pandas on their environment, before simply executing the command 'python main.py' in the terminal. 

### Main Algorithms and Libraries
- **Pandas**: Utilized for its high-performance data manipulation and analysis capabilities, perfect for handling the extensive datasets from FBref.
- **Scikit-learn**: Will be used for implementing machine learning algorithms that will drive the recommendation system. Its ease of use and wide range of algorithms support our goal to match players with teams effectively.
- **NumPy**: This library is the cornerstone for numerical computing in Python and works seamlessly with Pandas and Scikit-learn, providing an efficient array processing for numerical operations.

### Development and Version Control
- **Git**: The standard for version control, allowing us to manage code changes and collaborate efficiently.
- **GitHub**: Hosts our repository and facilitates issue tracking and documentation.

### Choice of Technology
The selected technologies each play a vital role in the project's infrastructure:
- **Pandas** forms the data extraction and preprocessing layer, transforming unstructured data from web pages into a structured form ready for analysis.
- **Scikit-learn** will be pivotal for predictive analytics, enabling the creation of machine learning models that can predict player performance and suitability.
- **NumPy** enhances performance in data manipulation tasks, essential for handling large-scale data with speed and precision.
- **Git and GitHub** provide robust tools for source control management and collaborative development, ensuring that project milestones are met with a high standard of code quality and collaboration.

These technologies collectively support the project’s goal of developing an intelligent, data-driven recommendation system for soccer player-team fit analysis.

## System or Software Architecture Diagram
![SoccerProject](https://github.com/coms-w3132/final-project-kevinlian2it/assets/52785160/72c01a40-8f64-47ee-8a0d-2ec747b1f6da)


## Development Methodology

The project will employ an agile and iterative development approach, utilizing various features of GitHub to organize, track, and progress the work:

- **GitHub Project Board**: I utilize a projects board on GitHub to manage tasks and milestones. The board will be organized with deliverables and due dates to provide a clear view of the project’s status at any given moment.

- **Commits**: For having up to date code, commits and push requests will be done constantly in order to ensure the latest work is represented in the repository.

### Testing and Evaluation

Testing is a critical component of the development lifecycle to ensure functionality, performance, and reliability:

- **Manual Testing**: Manual testing will be conducted to verify the user interface and the system as a whole. This approach is particularly useful for exploratory testing, usability testing, and to ensure that the project meets the user requirements.

By employing this development and testing methodology, the project aims to achieve a high standard of code quality and maintainability, ensuring that the final product is reliable.

## Potential Challenges and Roadblocks

### Challenge 1: Data Scraping Robustness
**Anticipated Issue**: The structure of FBref.com may change, which could break the scraping logic.

**Strategies**: To mitigate this, I could:
- Write scraping functions with BeautifulSoup that target class names or IDs that are less likely to change.
- Set up monitoring scripts that alert us if the output data format changes unexpectedly.

### Challenge 2: Data Quality and Preprocessing
**Anticipated Issue**: Ensuring the quality of data after scraping and during preprocessing.

**Strategies**: 
- Implement thorough validation checks post-scraping.
- Use Pandas to handle missing or inconsistent data effectively, possibly with custom cleaning functions.

### Challenge 3: Model Accuracy and Performance
**Anticipated Issue**: Creating a machine learning model with satisfactory accuracy and performance.

**Strategies**:
- Begin with simple models using Scikit-learn to establish a baseline before moving to more complex algorithms.
- Experiment with different feature engineering techniques to improve model performance.

### Challenge 4: Automated Testing
**Anticipated Issue**: Developing a comprehensive suite of automated tests.

**Strategies**:
- Utilize pytest for unit testing from the outset.

## Conclusion and Future Work
As I reflect on the progress of this project, I am filled with a sense of accomplishment. The journey of transforming a concept into a tangible, functioning system has been both challenging and immensely rewarding. The experience has not only honed my technical skills but also deepened my understanding of how data can influence and enrich the beautiful game.

I am excited for the future of this project. There is so much more to do—refining algorithms, expanding functionality, and possibly venturing into new territories of predictive analytics.

This project has boosted my confidence in taking on large and complex endeavors. I felt that I have grown more adept and assured in my abilities. I look forward to building on this foundation and keep working on larger projects.

### Potential Future Work
Looking to the future, there are several possibilities:

- **Advanced Modeling**: Leveraging cutting-edge machine learning techniques to refine our recommendations, ensuring they're as accurate and insightful as possible.
  
- **User Experience**: Crafting an engaging user interface that invites interaction and demystifies the underlying complexities of data analysis.

- **Real-time Analytics**: Striving for a system that operates on live data, providing instant, up-to-date recommendations.