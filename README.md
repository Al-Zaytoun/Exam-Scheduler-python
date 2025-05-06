

This implements an **Exam Scheduler** in Python using recursive backtracking. It attempts to assign exams to available rooms based on their scheduled times and room availability windows, without any time conflicts.

The program uses custom time and interval classes and operates entirely through reading from `.csv` files that list exam times and room availability.

## Features

- Parses input files for exam schedules and room availabilities
- Supports multiple files and batch testing
- Assigns exams to rooms without overlap
- Displays the final schedule or indicates if no valid assignment is possible
- Uses recursion and backtracking to find a valid room allocation

## File Structure

```
Lab_5/
├── exam_scheduler.py        # Main program with all class and function definitions
├── exam_times_1.csv         # Exam schedule input files
├── exam_times_2.csv
├── ...
├── room_avail_1.csv         # Room availability input files
├── room_avail_2.csv
├── ...
```

## ▶️ How to Run

Run the tester function in `exam_scheduler.py` to automatically test all combinations of exam and room files:

```bash
python exam_scheduler.py
```

Or, if you'd like, you can simply change the names and values of whatever classes, and their respective times to your choosing to test it out

## 📌 Notes

- Files must be located in the `Lab_5` directory
- The program assumes 24-hour time format (e.g., 13:00 for 1 PM)
- Avoid overlapping exams in your input files unless intentional

