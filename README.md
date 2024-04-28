# Advanced STV Voting System

The Advanced STV (Single Transferable Vote) Voting System is a robust, Python-based application designed to facilitate and manage electoral processes with a high level of security and user accessibility. This system leverages the tkinter library for its graphical user interface, offering a straightforward and intuitive interaction platform for both voters and administrators.

## Goal 
The primary goal of the Advanced STV (Single Transferable Vote) Voting System is to provide a secure, transparent, and accessible platform for conducting elections using the Single Transferable Vote mechanism. This project aims to ensure that all participants can cast their votes in a secure environment where voter confidentiality and vote integrity are paramount. It seeks to prevent unauthorized access and vote manipulation through robust authentication and data handling procedures. Additionally, the system is designed to be user-friendly, allowing voters to easily register, log in, and vote without needing technical expertise. For administrators, the project aims to provide a comprehensive dashboard for managing the electoral process, including candidate management and real-time vote tallying. Ultimately, this voting system strives to enhance the democratic process by making voting more accessible, secure, and efficient, thus increasing voter turnout and trust in electoral outcomes.

## Significance 
* The Advanced STV (Single Transferable Vote) Voting System is significant in the context of elections for several key reasons:
   
   1. **Enhanced Fairness and Representation**: The STV method allows voters to rank candidates by preference, which helps to ensure that the election results more accurately reflect the voters' preferences across a broader spectrum of options. This system reduces the waste of votes and prevents the spoiler effect common in simpler voting systems, thereby promoting    a more representative and democratic outcome.
   2. **Increased Voter Engagement**: By implementing a system that is secure and easy to use, the project aims to reduce barriers to participation. A user-friendly interface that simplifies the voting process can help increase voter turnout, especially among populations that might otherwise feel disenfranchised or intimidated by more complex voting procedures.
   3. **Promotion of Trust in the Electoral System**: Trust in electoral processes is crucial for the legitimacy of democracy. The Advanced STV Voting System incorporates robust security measures that safeguard against fraud and ensure the integrity of the voting process. By maintaining high standards of transparency and accountability, the system helps build          public confidence in the electoral outcomes.
   4. **Adaptability and Scalability**: The system is designed to be adaptable to various electoral contexts, from small-scale organizational elections to larger public governmental elections. Its scalability ensures that it can handle growing numbers of voters and candidates without a loss in performance or security.
   5. **Innovation in Voting Technology**: By leveraging modern software technologies and methodologies, the project contributes to ongoing efforts to modernize electoral systems around the world. This innovation not only improves current practices but also paves the way for future advancements in voting technology.
* In summary, the significance of the Advanced STV Voting System lies in its potential to enhance electoral fairness, increase voter participation, ensure the security and integrity of elections, and innovate electoral practices through technology. These factors are critical in strengthening democratic processes and ensuring that elections truly reflect the will of the people.

## Features

- **User Authentication**: Secure login and registration system to manage voter access.
- **Voting**: Users can cast their votes once they are logged in.
- **Admin Panel**: Administrators can view vote counts, manage candidates, and see detailed voting logs.
- **Security**: Emphasis on secure handling of votes and user information.

## Installation

To get started with the Advanced STV Voting System, follow these steps:

1. **Clone the Repository**
   ```
   bash
   git clone https://github.com/yourusername/advanced-stv-voting-system.git
   cd advanced-stv-voting-system
   ```
2. **Install Required Packages**
    Ensure you have Python installed on your system. Then install the required packages:
    ```
   pip install tkinter
    ```

4. **Run the Application**
   ```
   python login.py
   ```

# Usage
## Registering 
* Open the application and click on the "Sign Up" button on the login page.
* Fill in the username , password and role fields and click "Register".
* Upon successful registration, you will be taken to your voting screen.

![image](https://github.com/Glory-Be-Upon-Me/Poejct2/assets/162085036/146bb6a5-7349-443a-86de-4b54234a8bc5)

## Logging In
* If already registered, enter your username and password on the login screen and click "Login".
* Once authenticated, you will be directed to the voting interface.

![image](https://github.com/Glory-Be-Upon-Me/Poejct2/assets/162085036/37fade1a-0426-424c-9f11-f148b37cde89)

![image](https://github.com/Glory-Be-Upon-Me/Poejct2/assets/162085036/b9e8bfc7-ef7f-43b1-b3de-25f58f017a6d)

## Voting
* Select a candidate from the dropdown menu.
* Click "Cast Vote" to submit your vote.
* Repeat until all candidates are exhausted; the system will prioritize the first votes while using your secondary, tertiary, etc. choices in the case that your favored candidate loses.
* The system ensures that each user can only have one set of preferred candidates. Voting again will overwrite the previous votes.

![image](https://github.com/Glory-Be-Upon-Me/Poejct2/assets/162085036/c3c364aa-c80c-48ba-8c6d-e6bc05ff7c2c)

![image](https://github.com/Glory-Be-Upon-Me/Poejct2/assets/162085036/416208c4-3ed9-4af5-9398-1acd2fbfef67)

## Admin Panel
* You can login to the Admin account using default credentials for admin. Username - admin , Password - password
* The admin panel allows viewing detailed logs of all votes and managing candidates.
* It also allows the admin to view the Real time voting results

## Adding a candidate
* Enter the desired name of the candidate to add and then press "Add Candidate".

![image](https://github.com/Glory-Be-Upon-Me/Poejct2/assets/162085036/6d458476-a73e-4c9e-86e0-9bcdeeb909d1)

## Discussion

### Project Issues and Challenges:
* **Data Integrity**: Ensuring the integrity of vote data was critical. The challenge was to implement a system where votes could not only be cast securely but also counted accurately without risk of tampering.
* **Concurrency**: Handling multiple users accessing the system simultaneously (especially in the admin and voter versions) posed challenges in ensuring that vote data remains consistent and that the user experience is seamless.
* **Data Persistence**: Using a simple text file (user_db.txt) to manage user data and another ('votes_db.txt') for votes required careful consideration of how data is read and written to avoid issues like data corruption or loss.

### Limitations:
* **Scalability**: While the current system using text files for storage works for a small scale, it might not scale well for a larger number of users or in a more robust electoral process. Performance issues could arise when handling large datasets.
* **Security**: Although basic security measures were implemented, the system still relies on plain text for storing sensitive information, which is not suitable for a real-world application where data encryption and more sophisticated security protocols are necessary.
* **User Interface**: The GUI, while functional, is quite basic and might not offer the best user experience for less technical users or in situations where quick data processing is required.

## Conclusions

### Application of Course Learnings:
* **Data Structures**: Throughout the project, fundamental data structures like dictionaries and lists were extensively used to manage users and votes. These structures facilitated efficient data manipulation and retrieval operations, which are crucial for the real-time requirements of a voting system.
* **File Handling**: The project provided a practical application of file handling in Python, teaching how to read from and write to files, which is crucial for data persistence. Handling data consistency when multiple sessions access the file simultaneously was particularly instructive.
* **Exception Handling**: Implementing robust error and exception handling mechanisms to deal with potential runtime errors (like file access issues or data format problems) helped in making the application more reliable and user-friendly.
* **Modular Programming**: The division of the project into different modules (admin and voter systems) demonstrated the importance of modular programming in making code more organized, manageable, and reusable.

### Reflections:
* This project not only allowed for the application of theoretical knowledge from the course into a practical, functioning program but also highlighted the importance of considering real-world constraints such as security and user accessibility in software development. It was a valuable exercise in seeing how even simple systems must carefully balance functionality, user experience, and data integrity.

## Future Enhancements
* To address these limitations, future versions could:
   1. Integrate a database system for better scalability and security.
   2. Employ encryption techniques for sensitive data to enhance security.
   3. Improve the GUI for a better user experience and incorporate more interactive elements for real-time data updates.

   
