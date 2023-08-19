count = 0

questions = [
    ("What does CPU stand for? 1) Central Processing Unit 2) Computer Personal Unit:", "1"),
    ("Which programming language is known as the 'mother of all languages'? 1) Java 2) C:", "2"),
    ("What protocol is used to send email over the Internet? 1) FTP 2) SMTP:", "2"),
    ("Which data structure uses LIFO? 1) Queue 2) Stack:", "2"),
    ("What is the process of converting source code into machine code called? 1) Compilation 2) Interpretation:", "1"),
    ("In networking, what does LAN stand for? 1) Local Area Network 2) Large Area Network:", "1"),
    ("Which sorting algorithm has an average and worst-case time complexity of O(n log n)? 1) Bubble Sort 2) Merge Sort:", "2"),
    ("What is the binary representation of the decimal number 10? 1) 1010 2) 1100:", "1"),
    ("Which type of database is suitable for handling complex queries and large datasets? 1) Relational Database 2) NoSQL Database:", "2"),
    ("What does HTTPS stand for? 1) Hypertext Transfer Protocol Secure 2) Hypertext Transfer Protocol Standard:", "1"),
    ("Which programming paradigm is based on the concept of 'objects'? 1) Procedural 2) Object-Oriented:", "2"),
    ("What is the primary purpose of an operating system? 1) Running applications 2) Managing hardware and software resources:", "2"),
    ("What is the smallest unit of data in a computer's memory? 1) Byte 2) Bit:", "2"),
    ("Which data structure is used to implement a Last-In-First-Out (LIFO) behavior? 1) Queue 2) Stack:", "2"),
    ("In which year was Python programming language first released? 1) 1991 2) 2000:", "1"),
    ("What does SQL stand for? 1) Structured Query Language 2) Simple Query Language:", "1"),
    ("Which layer of the OSI model is responsible for routing and forwarding data packets? 1) Physical Layer 2) Network Layer:", "2"),
    ("Which encryption algorithm is commonly used to secure internet communications? 1) ROT13 2) AES:", "2"),
    ("What is the main purpose of an index in a database? 1) Improving database performance 2) Adding colors to data:", "1"),
    ("Which programming language is commonly used for web development and has a tagline 'The language of the web'? 1) JavaScript 2) Ruby:", "1"),
    ("What is the default port for HTTP communication? 1) 80 2) 443:", "1"),
    ("What is the process of finding errors and fixing them in a program called? 1) Debugging 2) Compiling:", "1"),
    ("Which protocol is used to transfer files from a local machine to a remote server? 1) SMTP 2) FTP:", "2"),
    ("Which search algorithm is known for its efficiency in sorted arrays? 1) Linear Search 2) Binary Search:", "2"),
    ("What is the purpose of a firewall in computer networks? 1) Blocking physical access 2) Filtering network traffic:", "2"),
    ("Which programming language is often used for scientific computing and data analysis? 1) Python 2) PHP:", "1"),
    ("What is the concept of 'polymorphism' in object-oriented programming? 1) Having a single form 2) Having many forms:", "2"),
    ("Which type of network topology involves connecting each device to a central hub? 1) Star Topology 2) Bus Topology:", "1"),
    ("What is the difference between an interpreter and a compiler? 1) Interpreters run code faster 2) Compilers generate executable files:", "2"),
    ("Which data structure stores elements in key-value pairs? 1) Array 2) Dictionary:", "2"),
    ("What is the purpose of a primary key in a database table? 1) Providing extra security 2) Uniquely identifying records:", "2"),
    ("Which type of attack aims to deceive users into revealing confidential information? 1) DDoS Attack 2) Phishing Attack:", "2"),
    ("What does RAID stand for in the context of data storage? 1) Redundant Array of Inexpensive Disks 2) Random Access and Inclusive Design:", "1"),
    ("Which HTTP status code indicates that a requested resource was not found on the server? 1) 200 OK 2) 404 Not Found:", "2"),
    ("What is the purpose of DNS (Domain Name System) in networking? 1) Securing websites 2) Resolving domain names to IP addresses:", "2"),
    ("Which type of software provides an interface for users to interact with the computer system? 1) Compiler 2) Operating System:", "2"),
    ("What is the concept of 'inheritance' in object-oriented programming? 1) Acquiring properties of another class 2) Creating new classes:", "1"),
    ("Which web development framework is written in Python and known for its simplicity? 1) Django 2) Ruby on Rails:", "1"),
    ("What is the purpose of a cache in computing? 1) Storing permanent data 2) Storing frequently accessed data for faster retrieval:", "2"),
    ("Which type of network is limited to a small geographic area, such as a home or office? 1) WAN 2) LAN:", "2"),
    ("What is the purpose of a foreign key in a database table? 1) Storing encrypted data 2) Establishing a relationship between tables:", "2"),
    ("Which programming language is commonly used for system programming and developing operating systems? 1) Java 2) C:", "2"),
    ("What is the primary function of a router in a computer network? 1) Blocking malware 2) Forwarding data packets between networks:", "2"),
    ("Which type of attack involves overwhelming a system or network with excessive traffic? 1) Phishing Attack 2) DDoS Attack:", "2"),
    ("What does API stand for? 1) Application Programming Interface 2) Advanced Programming Interface:", "1"),
]


for i, (question, answer) in enumerate(questions, start=1):
    user_answer = input(f"Question {i}: {question} ")
    if user_answer == answer:
        count += 1

print("Number of correct answers:", count)
