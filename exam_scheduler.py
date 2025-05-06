"""
Zanoon Hassan
Lab 5
3139132
"""

class Time:

    def __init__(self, time):
        self.time = time

        self.hour, self.minuite = self.time.split(":")

    def __str__(self):
        return self.time

    def get_hour(self):
        return self.hour
    
    def get_minuite(self):
        return self.minuite
    
    def __eq__(self, other):
        return self.hour == other.hour and self.minuite == other.minuite

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return self.hour < other.hour or (self.hour == other.hour and self.minuite < other.minuite)

    def __le__(self, other):
        return self.hour < other.hour or (self.hour == other.hour and self.minuite <= other.minuite)

    def __gt__(self, other):
        return self.hour > other.hour or (self.hour == other.hour and self.minuite > other.minuite)

    def __ge__(self, other):
        return self.hour > other.hour or (self.hour == other.hour and self.minuite >= other.minuite)


class TimeInterval:

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.start_time}-{self.end_time}"
    

    def disjoint(self, other):
        return self.end_time <= other.start_time or other.end_time <= self.start_time
    
    def contain(self, other):
        return self.start_time <= other.start_time and self.end_time >= other.end_time


class Schedule:
    def __init__(self, exam_file, avail_file):
        self.exam_file = exam_file
        self.avail_file = avail_file

        # Reading exam_file
        self.exam_classes = []  # List to store exam names
        self.exam_times = []    # List to store exam time intervals
        
        try:
            exam = open(f"Lab_5/{self.exam_file}", "r") #Note* Here I simply initalized Lab_5/ because thats the directory for where the exam & room files are for me 
            for line in exam:
                parts = line.strip().split(",")
                exam_name = parts[0].strip()
                beginning_exam_time = Time(parts[1].strip())
                ending_exam_time = Time(parts[2].strip())
                time_exam_interval = TimeInterval(beginning_exam_time, ending_exam_time)
                
                self.exam_classes.append(exam_name)
                self.exam_times.append(time_exam_interval)
            exam.close()
        except:
            print(f"No such file name with the given name: {self.exam_file}")
            return

        # Reading avail_file
        self.room_numbers = []  # List to store room names
        self.avail_times = []   # List to store room availability intervals
        
        try:
            room = open(f"Lab_5/{self.avail_file}", "r") # Same here, I set the reading of the room_avail files using Lab_5/ because thats the directory that all the files are placed in
            for line in room:
                parts = line.strip().split(",")
                room_name = parts[0].strip()
                beginning_room_time = Time(parts[1].strip())
                ending_room_time = Time(parts[2].strip())
                time_room_interval = TimeInterval(beginning_room_time, ending_room_time)
                
                self.room_numbers.append(room_name)
                self.avail_times.append(time_room_interval)
            room.close()
        except:
            print(f"No such file name with the given name: {self.avail_file}")
            return
        
        # Initialize room assignments as an empty list
        self.room_assignments = []
        
        # Find a valid schedule & initialize as a variable
        self.found_solution = self.recursiveBacktracking(0)

    def recursiveBacktracking(self, exam_idx=0): #initialized exam_index to 0
        # Base case: All exams have been scheduled
        if exam_idx >= len(self.exam_times):
            return True
        
        current_exam_interval = self.exam_times[exam_idx]
        
        # Try each room for the current exam
        for room_idx in range(len(self.room_numbers)):
            current_room_interval = self.avail_times[room_idx]
            
            # Check if exam fits within room time
            if current_room_interval.contain(current_exam_interval):
                # Ensure self.room_assignments has a list for this room if it doesn't exist
                while len(self.room_assignments) <= room_idx:
                    self.room_assignments.append([])  # Create an empty list for this room (this is what I will track each room with all the available exam times) -> if no rooms, it makes it

                # Check if exam conflicts with any existing exams in this room
                has_conflict = False 
                for assigned_exam_idx in self.room_assignments[room_idx]:
                    assigned_exam_interval = self.exam_times[assigned_exam_idx]
                    if not current_exam_interval.disjoint(assigned_exam_interval):
                        has_conflict = True
                        break

                if not has_conflict:
                    # Assign exam to this room and try next exam
                    self.room_assignments[room_idx].append(exam_idx)

                    if self.recursiveBacktracking(exam_idx + 1):
                        return True

                    # backtrack call remove this assignment
                    self.room_assignments[room_idx].pop()
            
        # No valid room found for this exam
        return False

    def __str__(self):
        if not self.found_solution:
            return f"No schedule is possible using room availability in {self.avail_file}\n"
        print(f"Room assignment for exams in {self.avail_file}\n")
        result = f"Using room availability in {self.avail_file}\n\n"
        
        for room_idx, assignments in enumerate(self.room_assignments):
            if assignments:
                room_name = self.room_numbers[room_idx]
                room_interval = self.avail_times[room_idx]
                
                result += f"Room {room_name}: {room_interval} :\n"
                
                for exam_idx in assignments:
                    exam_name = self.exam_classes[exam_idx]
                    exam_interval = self.exam_times[exam_idx]
                    result += f"\t{exam_name}: {exam_interval}\n"
                
                result += "\n"
        
        return result

# Main function which isnt being called, and is only doing simple checking of the files themselves

def main():
    exam_file = input("Please Enter the name of the exam file: ")

    try:
        exam = open(f"Lab_5/{exam_file}", "r")
    except:
        print(f"Cant open file {exam_file}")
    
    room_file = input("Please Enter the name of the exam file: ")
    try:
        room = open(f"Lab_5/{room_file}", "r")
    except:
        print(f"Cant open file {room_file}")



def tester():
    exam_list = ['exam_times_1.csv', 'exam_times_2.csv', 'exam_times_3.csv', 'exam_times_4.csv', 'exam_times_5.csv', 'exam_times_6.csv']
    room_list = ['room_avail_1.csv', 'room_avail_2.csv', 'room_avail_3.csv', 'room_avail_4.csv', 'room_avail_5.csv', 'room_avail_6.csv']

    for exam_file in exam_list:
        for room_file in room_list:
            schedule = Schedule(exam_file, room_file)
            print(schedule)
        print("====================================================")
tester()
