#!/usr/bin/env python3
import pathlib

class Reminders:
    def __init__(self):
        current_path = pathlib.Path(__file__).parent
        self.reminder_file = current_path.joinpath("text_files",
                                              "reminders.txt")

    def get_reminders(self, reminder_file_location):
        remind_list = []
        with open(reminder_file_location) as reader:
            for line in reader:
                if line.strip() != "":
                    remind_list.append(line)
        return remind_list

    def add_reminder(self, reminder):
        reminders = self.reminder_file.read_text()
        self.reminder_file.write_text(f"{reminders} \n {reminder.strip()}\n")

#myremind = Reminders()
