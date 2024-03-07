"""
This module will print the completed session details and minimum duration time
according to username.
"""
import sys
from datetime import datetime

class LogSession:
    def __init__(self):
        """
        Log Session class initialization
        """
        self.completed_log = {}

    def fetch_log_details(self, log_file: str):
        """
        This function will fetch the completed log details in list

        Args:
            log_file (str): Path of the log file

        Returns:
            None (Print the session details)
        """
        try:
            with open(log_file, 'r') as file:
                for line in file:
                    # Get single log and split the values
                    parts = line.strip().split()

                    # Skip the Invalid fields and continue to next
                    if len(parts) != 3:
                        continue

                    # Split the details
                    timestamp_str, username, action = parts

                    try:
                        timestamp = datetime.strptime(timestamp_str, '%H:%M:%S')
                    except ValueError:
                        continue

                    # Check the start log details for each row
                    if action == 'Start':
                        # Create list for start times if it doesn't exist
                        if username not in self.completed_log:
                            self.completed_log[username] = {
                                'start_times': [],
                                'end_times': [],
                                'durations': []
                            }
                        self.completed_log[username]['start_times'].append(timestamp)

                    if action == 'End':
                        # Append end time to corresponding start time list
                        if username in self.completed_log:
                            self.completed_log[username]['end_times'].append(timestamp)

        except FileNotFoundError as fnfe:
            print(str(fnfe))

    def initiate_log(self):
        """
        This function will print the details in required response.
        """
        if not self.completed_log:
            print("Log file is empty!")

        # # Calculate durations for completed sessions
        for username, session_details in self.completed_log.items():
            start_times = session_details['start_times']
            end_times = session_details['end_times']
            durations = [(end - start).total_seconds()
                        for start, end in zip(start_times, end_times)]
            session_details['durations'] = durations

        # Aggregate durations for each user
        aggregated_durations = {}

        for username, session_details in self.completed_log.items():
            durations = session_details['durations']
            total_duration = sum(durations)

            # Duration counts with username
            aggregated_durations[username] = aggregated_durations.get(
                username, 0) + total_duration

        # Print aggregated durations for each user with completed sessions
        for username, total_duration in aggregated_durations.items():
            num_sessions = len(self.completed_log.get(
                username, {}).get('durations', []))
            
            # If total number of completed session is more then zero
            if num_sessions > 0:
                print(f"{username} {num_sessions} {int(total_duration)}")


if __name__ == "__main__":
    # Fetch the list of command line arguments
    command_arguments = sys.argv

    # Check the length and required arguments
    if len(command_arguments) != 2:
        sys.exit(1)

    # Log file path/name
    log_file = sys.argv[1]

    # Fetch the details of the completed logs
    session_obj = LogSession()
    session_obj.fetch_log_details(log_file)
    session_obj.initiate_log()
