# Fair Billing Log Analyzer

This program reads a log file with user login and logout times. It then figures out the shortest total time each user spent logged in, in seconds.

## Request Input:
The program needs you to point it to a file (the path) where it will find user activity. This file has lines like "10:20:35 Gourav Start" or "18:45:12 Patidar End". It uses these lines to figure out the shortest total time each user spent logged in, in seconds.


## Output:
The program prints the following information for each user:
- Username
- Number of sessions
- Minimum possible total duration of sessions in seconds

## Assumptions:
1. The log file is in chronological order, meaning each entry happens after the previous one.
2. Everything happens in one day, no sessions starting one day and ending the next.
3. Any lines missing details (time, user, or action) are simply ignored.

## Usage:
To run the program, execute the following command in the terminal:

    python user_session.py <log_file_path>

Replace <log_file_path> with the path to your log file.

<b>Example</b>:
Assume you have a log file named sample.log containing session data. To analyze this file, run:

    python user_session.py log-file.log

Output will be displayed on the console.

<b>Run by shell script</b>:

Added a default sample_log file and you can directly run the sh file to execute the script:

    run.sh

Output will be displayed in output.txt file, Which will be created in root directory of the project.

## Test Cases

1. Logs with some test data

    `python user_session.py test-files/sample_log.log`

2. Blank log file

    `python user_session.py test-files/blank_log.log`

3. Logs without End

    `python user_session.py test-files/only_start_log.log`


Note:
Ensure that Python 3.x is installed on your system.

Author:
- Gourav Patidar
- gpatidar976@gmail.com
- Software Engineer
