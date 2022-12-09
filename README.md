## This repository is created to demonstrate the process of code development using the best coding practices.
We implemented the AES-256 encryption over TCP/IP connection.

1. Folder original_code_before_improvements contains the code without unit tests, static code analysis, and vulnerability analysis 

2. Folder final_code contains the code with unit tests, code written following the proper coding practices, and fixed security vulnerabilities

We used pylint library for static code analysis and Bandit software to detect vilnerabilities

To run the code as client server functionality, from the root execute following commands:
1. To start the server: python3 final_code/main_decrypt_server.py --local_encryption="False" 
2. To encrypt data and send it over TCP: python3 final_code/main_encrypt_client.py --input_file_path={absolute path to file} --local_encryption="True"
