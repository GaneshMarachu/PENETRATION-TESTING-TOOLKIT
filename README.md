COMPANY: CODTECH IT SOLUTIONS

NAME: Marachu Ganesh

INTERN ID:CT06DL1340

DOMAIN: SQL

DURATION: 6 WEEEKS

MENTOR: NEELA SANTOSH

# PENETRATION TESTING TOOLKIT

This project is a Python-based modular penetration testing toolkit developed as part of a cybersecurity internship project. The toolkit is designed to help beginners understand the fundamentals of penetration testing by providing two core modules: a basic port scanner and a brute-force login module for FTP and SSH services. It acts as an introductory framework for understanding how real-world penetration testing tools function and can be expanded upon in the future for more complex scenarios.

The primary purpose of this toolkit is to automate simple penetration testing tasks and gain hands-on experience with network and service-level enumeration. The port scanner works by attempting TCP connections to a list of commonly used ports and reporting which ones are open on the target system. This helps the tester identify potential services running on a remote machine. The brute-forcer module is designed to try different passwords from a provided wordlist against either an FTP or SSH service on the target host. This demonstrates the concept of password-based attacks and highlights the importance of using strong, unguessable credentials.

Throughout the development of this project, care has been taken to maintain clean and readable code using Python’s standard libraries such as `socket`, `ftplib`, and `paramiko`. The modular structure allows users to choose between different tools within a single script, making it both user-friendly and flexible. Users are first prompted to select a module to use, then provide the necessary input such as target IP address, username, and path to a wordlist file.

The toolkit has been tested with public and legally accessible test servers like `test.rebex.net`, which offer FTP access for demonstration purposes. This ensures ethical usage and safe learning environments. During scanning, the output clearly displays the open ports found or login attempts made, along with any successful authentication. This immediate feedback helps users understand the effectiveness of each module and the concept of vulnerability exploitation.

This project is intended strictly for educational and ethical use only. It is not designed for unauthorized access or malicious activity. By practicing these skills in a controlled environment or on designated test servers, students and aspiring cybersecurity professionals can gain valuable knowledge and confidence without breaching any legal or ethical boundaries.

Working on this toolkit helped reinforce several foundational concepts in cybersecurity, including the importance of reconnaissance, the risks of weak passwords, and the techniques used by attackers during the early phases of a cyberattack. It also provided an opportunity to improve Python coding skills, understand module imports, error handling, user input validation, and network programming.

This toolkit can be expanded in the future by including additional modules such as directory brute-forcing, banner grabbing, vulnerability checking via CVEs, or even a basic web scanner. The goal of this task is not to build a professional-grade tool, but to explore the components and logic that make up such tools. It serves as a great entry point into the world of ethical hacking and penetration testing.

This marks the successful completion of the task titled “PENETRATION TESTING TOOLKIT” as part of the CodTech cybersecurity internship program.

output:

![Image](https://github.com/user-attachments/assets/346e85af-1887-47c3-8d1b-d88300e02c39)
