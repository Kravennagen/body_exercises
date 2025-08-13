import sys
from datetime import datetime, timedelta
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget, QMessageBox, QTextEdit, QHBoxLayout, QGridLayout, QFileDialog, QDateEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QRect, Qt, QDate


class GenderSelector(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Select Gender")
        self.setGeometry(100, 100, 300, 150)

        self.layout = QVBoxLayout()
        
        # Add label for instructions
        self.label = QLabel("Choose your gender:", self)
        self.layout.addWidget(self.label)

        # Create buttons for selecting gender
        self.male_button = QPushButton("Male", self)
        self.female_button = QPushButton("Female", self)

        # Connect buttons to gender selection handler
        self.male_button.clicked.connect(lambda: self.select_gender("male"))
        self.female_button.clicked.connect(lambda: self.select_gender("female"))

        # Add buttons to layout
        self.layout.addWidget(self.male_button)
        self.layout.addWidget(self.female_button)

        # Set layout for gender selection window
        self.setLayout(self.layout)

    def select_gender(self, gender):
        """ When gender is selected, open BodyViewer and pass gender """
        self.body_viewer = BodyViewer(gender)
        self.body_viewer.show()
        self.close()


class BodyViewer(QWidget):
    def __init__(self, gender):
        super().__init__()

        self.setWindowTitle(f"{gender.capitalize()} Body Viewer")
        
        self.selected_muscles = set()
        self.gender = gender

        # Load the image
        self.pixmap = QPixmap(f"assets/{gender}_body.png")
        
        # Set window size to match image size
        self.setFixedSize(self.pixmap.width(), self.pixmap.height())
        
        # Create image label that fills the entire widget
        self.image_label = QLabel(self)
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setGeometry(0, 0, self.pixmap.width(), self.pixmap.height())

        # Create clickable regions for muscles
        self.create_clickable_regions()
        
        # Add Continue button
        self.continue_button = QPushButton("Continue", self)
        self.continue_button.setGeometry(10, 10, 100, 30)
        self.continue_button.clicked.connect(self.validate_and_continue)
        self.continue_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

    def create_clickable_regions(self):
        # Define muscles and their corresponding regions as rectangles
        if self.gender == "female":
            muscles = {
                "higher-abs": QRect(int(self.pixmap.width() * 0.236), int(self.pixmap.height() * 0.275), int(self.pixmap.width() * 0.090), int(self.pixmap.height() * 0.039)),
                "middle-abs": QRect(int(self.pixmap.width() * 0.234), int(self.pixmap.height() * 0.320), int(self.pixmap.width() * 0.091), int(self.pixmap.height() * 0.020)),
                "lower-abs": QRect(int(self.pixmap.width() * 0.234), int(self.pixmap.height() * 0.350), int(self.pixmap.width() * 0.091), int(self.pixmap.height() * 0.022)),
                "right-abs": QRect(int(self.pixmap.width() * 0.196), int(self.pixmap.height() * 0.348), int(self.pixmap.width() * 0.036), int(self.pixmap.height() * 0.051)),
                "left-abs": QRect(int(self.pixmap.width() * 0.330), int(self.pixmap.height() * 0.347), int(self.pixmap.width() * 0.034), int(self.pixmap.height() * 0.053)),
                "left-trapezus": QRect(int(self.pixmap.width() * 0.311), int(self.pixmap.height() * 0.139), int(self.pixmap.width() * 0.060), int(self.pixmap.height() * 0.030)),
                "right-trapezus": QRect(int(self.pixmap.width() * 0.193), int(self.pixmap.height() * 0.136), int(self.pixmap.width() * 0.062), int(self.pixmap.height() * 0.034)),
                "right-biceps": QRect(int(self.pixmap.width() * 0.144), int(self.pixmap.height() * 0.223), int(self.pixmap.width() * 0.046), int(self.pixmap.height() * 0.096)),
                "left-biceps": QRect(int(self.pixmap.width() * 0.370), int(self.pixmap.height() * 0.224), int(self.pixmap.width() * 0.048), int(self.pixmap.height() * 0.100)),
                "right-quadriceps": QRect(int(self.pixmap.width() * 0.164), int(self.pixmap.height() * 0.481), int(self.pixmap.width() * 0.104), int(self.pixmap.height() * 0.222)),
                "left-quadriceps": QRect(int(self.pixmap.width() * 0.296), int(self.pixmap.height() * 0.477), int(self.pixmap.width() * 0.103), int(self.pixmap.height() * 0.228)),
                "trapezes": QRect(int(self.pixmap.width() * 0.673), int(self.pixmap.height() * 0.113), int(self.pixmap.width() * 0.177), int(self.pixmap.height() * 0.048)),
                "left-triceps": QRect(int(self.pixmap.width() * 0.615), int(self.pixmap.height() * 0.195), int(self.pixmap.width() * 0.070), int(self.pixmap.height() * 0.117)),
                "right-triceps": QRect(int(self.pixmap.width() * 0.837), int(self.pixmap.height() * 0.196), int(self.pixmap.width() * 0.071), int(self.pixmap.height() * 0.119)),
                "gluteus": QRect(int(self.pixmap.width() * 0.661), int(self.pixmap.height() * 0.400), int(self.pixmap.width() * 0.208), int(self.pixmap.height() * 0.118)),
                "left-gastrocnemius": QRect(int(self.pixmap.width() * 0.671), int(self.pixmap.height() * 0.711), int(self.pixmap.width() * 0.080), int(self.pixmap.height() * 0.174)),
                "right-gastrocnemius": QRect(int(self.pixmap.width() * 0.776), int(self.pixmap.height() * 0.714), int(self.pixmap.width() * 0.085), int(self.pixmap.height() * 0.172)),
            }
        else:
            muscles = {
                "higher-abs": QRect(int(self.pixmap.width() * 0.282), int(self.pixmap.height() * 0.308), int(self.pixmap.width() * 0.087), int(self.pixmap.height() * 0.035)),
                "middle-abs": QRect(int(self.pixmap.width() * 0.283), int(self.pixmap.height() * 0.344), int(self.pixmap.width() * 0.086), int(self.pixmap.height() * 0.027)),
                "lower-abs": QRect(int(self.pixmap.width() * 0.287), int(self.pixmap.height() * 0.375), int(self.pixmap.width() * 0.076), int(self.pixmap.height() * 0.025)),
                "right-biceps": QRect(int(self.pixmap.width() * 0.175), int(self.pixmap.height() * 0.254), int(self.pixmap.width() * 0.050), int(self.pixmap.height() * 0.096)),
                "left-biceps": QRect(int(self.pixmap.width() * 0.418), int(self.pixmap.height() * 0.250), int(self.pixmap.width() * 0.061), int(self.pixmap.height() * 0.109)),
                "right-trapezus": QRect(int(self.pixmap.width() * 0.221), int(self.pixmap.height() * 0.166), int(self.pixmap.width() * 0.085), int(self.pixmap.height() * 0.034)),
                "left-trapezus": QRect(int(self.pixmap.width() * 0.354), int(self.pixmap.height() * 0.160), int(self.pixmap.width() * 0.087), int(self.pixmap.height() * 0.042)),
                "left-quadriceps": QRect(int(self.pixmap.width() * 0.217), int(self.pixmap.height() * 0.496), int(self.pixmap.width() * 0.091), int(self.pixmap.height() * 0.221)),
                "right-quadriceps": QRect(int(self.pixmap.width() * 0.341), int(self.pixmap.height() * 0.496), int(self.pixmap.width() * 0.094), int(self.pixmap.height() * 0.222)),
                "trapezus": QRect(int(self.pixmap.width() * 0.698), int(self.pixmap.height() * 0.155), int(self.pixmap.width() * 0.154), int(self.pixmap.height() * 0.058)),
                "gluteus": QRect(int(self.pixmap.width() * 0.681), int(self.pixmap.height() * 0.446), int(self.pixmap.width() * 0.183), int(self.pixmap.height() * 0.120)),
                "left-triceps": QRect(int(self.pixmap.width() * 0.622), int(self.pixmap.height() * 0.255), int(self.pixmap.width() * 0.048), int(self.pixmap.height() * 0.119)),
                "right-triceps": QRect(int(self.pixmap.width() * 0.865), int(self.pixmap.height() * 0.266), int(self.pixmap.width() * 0.058), int(self.pixmap.height() * 0.111)),
                "left-gastrocnemius": QRect(int(self.pixmap.width() * 0.662), int(self.pixmap.height() * 0.759), int(self.pixmap.width() * 0.079), int(self.pixmap.height() * 0.172)),
                "right-gastrocnemius": QRect(int(self.pixmap.width() * 0.802), int(self.pixmap.height() * 0.761), int(self.pixmap.width() * 0.072), int(self.pixmap.height() * 0.173)),
                "right-abs": QRect(int(self.pixmap.width() * 0.243), int(self.pixmap.height() * 0.372), int(self.pixmap.width() * 0.043), int(self.pixmap.height() * 0.062)),
                "left-abs": QRect(int(self.pixmap.width() * 0.366), int(self.pixmap.height() * 0.374), int(self.pixmap.width() * 0.038), int(self.pixmap.height() * 0.060)),
            }

        for muscle, rect in muscles.items():
            # Create a transparent button for each muscle
            btn = QPushButton(self)
            btn.setGeometry(rect)

            # Make button checkable to toggle selection state
            btn.setCheckable(True)

            btn.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    border: 2px solid red;
                }
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.3);  /* Light gray on hover */
                }
                QPushButton:checked {
                    background-color: rgba(0, 128, 0, 0.3);  /* Green on selection */
                }
            """)

            
            btn.clicked.connect(lambda checked, muscle=muscle: self.on_muscle_click(muscle))


    def on_muscle_click(self, muscle):
        """ Handle click event for each muscle """
        if muscle in self.selected_muscles:
            self.selected_muscles.remove(muscle)
            print(f"{muscle} deselected")
        else:
            self.selected_muscles.add(muscle)
            print(f"{muscle} selected")

        print(f"Selected muscles: {self.selected_muscles}")
    
    def validate_and_continue(self):
        """ Validate selections and proceed to time period selection """
        if not self.selected_muscles:
            QMessageBox.warning(self, "No Selection", "Please select at least one muscle group before continuing.")
            return
        
        # Open time period selector
        self.time_selector = TimePeriodSelector(self.gender, self.selected_muscles)
        self.time_selector.show()
        self.close()


class TimePeriodSelector(QWidget):
    def __init__(self, gender, selected_muscles):
        super().__init__()
        
        self.gender = gender
        self.selected_muscles = selected_muscles
        
        self.setWindowTitle("Select Time Period")
        self.setGeometry(100, 100, 300, 200)
        
        self.layout = QVBoxLayout()
        
        # Add label for start date
        self.date_label = QLabel("Select start date:", self)
        self.layout.addWidget(self.date_label)
        
        # Date picker
        self.date_picker = QDateEdit(self)
        self.date_picker.setDate(QDate.currentDate())
        self.date_picker.setCalendarPopup(True)
        self.layout.addWidget(self.date_picker)
        
        # Add label for instructions
        self.label = QLabel("Choose your workout period:", self)
        self.layout.addWidget(self.label)
        
        # Create buttons for time periods
        self.week_button = QPushButton("One Week", self)
        self.month_button = QPushButton("One Month", self)
        
        # Connect buttons to selection handler
        self.week_button.clicked.connect(lambda: self.select_period("week"))
        self.month_button.clicked.connect(lambda: self.select_period("month"))
        
        # Add buttons to layout
        self.layout.addWidget(self.week_button)
        self.layout.addWidget(self.month_button)
        
        # Set layout
        self.setLayout(self.layout)
    
    def select_period(self, period):
        """ Handle time period selection """
        qdate = self.date_picker.date()
        start_date = datetime(qdate.year(), qdate.month(), qdate.day()).date()
        # Open workout calendar
        self.calendar = WorkoutCalendar(self.gender, self.selected_muscles, period, start_date)
        self.calendar.show()
        self.close()


class WorkoutCalendar(QWidget):
    def __init__(self, gender, selected_muscles, period, start_date=None):
        super().__init__()
        
        self.gender = gender
        self.selected_muscles = selected_muscles
        self.period = period
        self.start_date = start_date or datetime.now().date()
        
        # Calculate end date
        days = 7 if period == "week" else 30
        self.end_date = self.start_date + timedelta(days=days-1)
        
        self.setWindowTitle(f"Workout Calendar - {period.capitalize()} ({self.start_date.strftime('%m/%d/%Y')} - {self.end_date.strftime('%m/%d/%Y')})")
        self.setGeometry(100, 100, 1000, 700)
        
        # Gender-specific exercise database
        if self.gender == "male":
            self.exercises = {
                "higher-abs": ["Weighted Crunches", "Plank", "Hanging Knee Raises"],
                "middle-abs": ["Russian Twists", "Dead Bug", "Cable Crunches"],
                "lower-abs": ["Leg Raises", "V-Ups", "Dragon Flags"],
                "right-abs": ["Side Plank", "Oblique Crunches", "Wood Choppers"],
                "left-abs": ["Side Plank", "Oblique Crunches", "Wood Choppers"],
                "right-biceps": ["Barbell Curls", "Hammer Curls", "Pull-ups"],
                "left-biceps": ["Barbell Curls", "Hammer Curls", "Pull-ups"],
                "right-triceps": ["Close-Grip Push-ups", "Dips", "Overhead Press"],
                "left-triceps": ["Close-Grip Push-ups", "Dips", "Overhead Press"],
                "right-trapezus": ["Heavy Shrugs", "Upright Rows", "Face Pulls"],
                "left-trapezus": ["Heavy Shrugs", "Upright Rows", "Face Pulls"],
                "trapezus": ["Heavy Shrugs", "Upright Rows", "Deadlifts"],
                "trapezes": ["Heavy Shrugs", "Upright Rows", "Deadlifts"],
                "right-quadriceps": ["Squats", "Bulgarian Split Squats", "Leg Press"],
                "left-quadriceps": ["Squats", "Bulgarian Split Squats", "Leg Press"],
                "gluteus": ["Hip Thrusts", "Romanian Deadlifts", "Squats"],
                "right-gastrocnemius": ["Standing Calf Raises", "Jump Rope", "Calf Press"],
                "left-gastrocnemius": ["Standing Calf Raises", "Jump Rope", "Calf Press"]
            }
        else:  # female
            self.exercises = {
                "higher-abs": ["Crunches", "Pilates Roll-ups", "Mountain Climbers"],
                "middle-abs": ["Russian Twists", "Dead Bug", "Bicycle Crunches"],
                "lower-abs": ["Leg Raises", "Reverse Crunches", "Flutter Kicks"],
                "right-abs": ["Side Plank", "Oblique Crunches", "Side Bends"],
                "left-abs": ["Side Plank", "Oblique Crunches", "Side Bends"],
                "right-biceps": ["Light Dumbbell Curls", "Resistance Band Curls", "Wall Push-ups"],
                "left-biceps": ["Light Dumbbell Curls", "Resistance Band Curls", "Wall Push-ups"],
                "right-triceps": ["Tricep Dips", "Modified Push-ups", "Arm Circles"],
                "left-triceps": ["Tricep Dips", "Modified Push-ups", "Arm Circles"],
                "right-trapezus": ["Light Shrugs", "Shoulder Rolls", "Yoga Poses"],
                "left-trapezus": ["Light Shrugs", "Shoulder Rolls", "Yoga Poses"],
                "trapezus": ["Light Shrugs", "Shoulder Rolls", "Cat-Cow Stretch"],
                "trapezes": ["Light Shrugs", "Shoulder Rolls", "Cat-Cow Stretch"],
                "right-quadriceps": ["Bodyweight Squats", "Lunges", "Step-ups"],
                "left-quadriceps": ["Bodyweight Squats", "Lunges", "Step-ups"],
                "gluteus": ["Glute Bridges", "Clamshells", "Donkey Kicks"],
                "right-gastrocnemius": ["Calf Raises", "Toe Taps", "Ankle Circles"],
                "left-gastrocnemius": ["Calf Raises", "Toe Taps", "Ankle Circles"]
            }
        
        # Exercise descriptions database
        self.exercise_descriptions = {
            "Weighted Crunches": "Lie on back, hold weight on chest, lift shoulders off ground",
            "Plank": "Hold body straight in push-up position, engage core",
            "Hanging Knee Raises": "Hang from bar, lift knees to chest",
            "Russian Twists": "Sit with knees bent, rotate torso side to side",
            "Dead Bug": "Lie on back, extend opposite arm and leg slowly",
            "Cable Crunches": "Kneel at cable machine, crunch down with rope",
            "Leg Raises": "Lie on back, lift straight legs up and down",
            "V-Ups": "Lie flat, simultaneously lift legs and torso to form V",
            "Dragon Flags": "Lie on bench, lift body straight using core strength",
            "Side Plank": "Lie on side, lift body up on forearm",
            "Oblique Crunches": "Lie on side, crunch elbow to hip",
            "Wood Choppers": "Rotate torso diagonally with weight",
            "Barbell Curls": "Stand, curl barbell up with both arms",
            "Hammer Curls": "Curl dumbbells with neutral grip",
            "Pull-ups": "Hang from bar, pull body up until chin over bar",
            "Close-Grip Push-ups": "Push-ups with hands close together",
            "Dips": "Lower and raise body between parallel bars",
            "Overhead Press": "Press weight overhead from shoulder level",
            "Heavy Shrugs": "Lift shoulders up with heavy weights",
            "Upright Rows": "Pull weight up to chest, elbows high",
            "Face Pulls": "Pull rope to face level, elbows high",
            "Deadlifts": "Lift weight from ground to standing position",
            "Squats": "Lower body by bending knees, keep back straight",
            "Bulgarian Split Squats": "Single leg squat with rear foot elevated",
            "Leg Press": "Push weight with legs on leg press machine",
            "Hip Thrusts": "Lie on back, thrust hips up with weight",
            "Romanian Deadlifts": "Hinge at hips, lower weight with straight legs",
            "Standing Calf Raises": "Rise up on toes, lower slowly",
            "Jump Rope": "Jump over rope continuously",
            "Calf Press": "Press weight with toes on leg press machine",
            "Crunches": "Lie on back, lift shoulders toward knees",
            "Pilates Roll-ups": "Roll up vertebra by vertebra from lying position",
            "Mountain Climbers": "In plank position, alternate bringing knees to chest",
            "Bicycle Crunches": "Lie on back, alternate elbow to opposite knee",
            "Reverse Crunches": "Lie on back, lift knees toward chest",
            "Flutter Kicks": "Lie on back, alternate small leg kicks",
            "Side Bends": "Stand, bend sideways at waist",
            "Light Dumbbell Curls": "Curl light dumbbells with controlled movement",
            "Resistance Band Curls": "Curl using resistance band",
            "Wall Push-ups": "Push-ups against wall, easier variation",
            "Tricep Dips": "Dip body using chair or bench",
            "Modified Push-ups": "Push-ups on knees instead of toes",
            "Arm Circles": "Make circles with arms extended",
            "Light Shrugs": "Lift shoulders with light weights",
            "Shoulder Rolls": "Roll shoulders in circular motion",
            "Yoga Poses": "Hold various yoga positions",
            "Cat-Cow Stretch": "Arch and round back on hands and knees",
            "Bodyweight Squats": "Squats using only body weight",
            "Lunges": "Step forward, lower back knee toward ground",
            "Step-ups": "Step up onto platform, alternate legs",
            "Glute Bridges": "Lie on back, lift hips up",
            "Clamshells": "Lie on side, open and close top leg",
            "Donkey Kicks": "On hands and knees, kick leg back",
            "Calf Raises": "Rise up on toes, lower slowly",
            "Toe Taps": "Tap toes alternately in front of body",
            "Ankle Circles": "Make circles with feet"
        }
        
        self.setup_ui()
        self.generate_workout_plan()
    
    def setup_ui(self):
        main_layout = QVBoxLayout()
        
        # Export button
        self.export_button = QPushButton("Export to Google Calendar")
        self.export_button.clicked.connect(self.export_to_calendar)
        self.export_button.setStyleSheet("""
            QPushButton {
                background-color: #4285f4;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3367d6;
            }
        """)
        main_layout.addWidget(self.export_button)
        
        # Calendar and details layout
        content_layout = QHBoxLayout()
        
        # Calendar grid
        calendar_widget = QWidget()
        self.calendar_layout = QGridLayout(calendar_widget)
        content_layout.addWidget(calendar_widget)
        
        # Workout details panel
        self.workout_details = QTextEdit()
        self.workout_details.setReadOnly(True)
        self.workout_details.setMaximumWidth(300)
        content_layout.addWidget(self.workout_details)
        
        main_layout.addLayout(content_layout)
        self.setLayout(main_layout)
    
    def generate_workout_plan(self):
        """ Generate workout plan based on selected muscles and period """
        self.workout_plan = {}
        
        # Get all exercises for selected muscles
        all_exercises = []
        for muscle in self.selected_muscles:
            if muscle in self.exercises:
                all_exercises.extend(self.exercises[muscle])
        
        # Remove duplicates
        unique_exercises = list(set(all_exercises))
        
        # Generate plan based on period
        days = 7 if self.period == "week" else 30
        
        # Create day buttons
        cols = 7 if self.period == "week" else 6
        for i in range(days):
            day_num = i + 1
            
            # Assign 2-3 exercises per day
            day_exercises = []
            for j in range(min(3, len(unique_exercises))):
                exercise_index = (i * 3 + j) % len(unique_exercises)
                day_exercises.append(unique_exercises[exercise_index])
            
            self.workout_plan[day_num] = day_exercises
            
            # Create day button with exercises
            button_text = f"Day {day_num}\n\n"
            for exercise in day_exercises[:4]:  # Show first 4 exercises
                button_text += f"• {exercise}\n"
            if len(day_exercises) > 4:
                button_text += f"+ {len(day_exercises) - 4} more"
            
            day_button = QPushButton(button_text)
            day_button.setMinimumSize(220, 200)
            day_button.clicked.connect(lambda checked, day=day_num: self.day_selected(day))
            day_button.setStyleSheet("""
                QPushButton {
                    background-color: #000000;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    text-align: left;
                    padding: 5px;
                    font-size: 10px;
                }
                QPushButton:hover {
                    background-color: #d0d0d0;
                }
            """)
            
            row = i // cols
            col = i % cols
            self.calendar_layout.addWidget(day_button, row, col)
    
    def day_selected(self, day):
        """ Show workout details for selected day """
        if day in self.workout_plan:
            exercises = self.workout_plan[day]
            workout_text = f"Day {day} Workout:\n\n"
            
            for i, exercise in enumerate(exercises, 1):
                description = self.exercise_descriptions.get(exercise, "No description available")
                workout_text += f"{i}. {exercise}\n   How to: {description}\n   - 3 sets of 12 reps\n   - Rest 60 seconds\n\n"
            
            self.workout_details.setText(workout_text)
        else:
            self.workout_details.setText(f"No workout for Day {day}")
    
    def export_to_calendar(self):
        """ Export workout plan to ICS file for Google Calendar """
        filename, _ = QFileDialog.getSaveFileName(self, "Export Workout Calendar", "workout_plan.ics", "ICS files (*.ics)")
        
        if filename:
            try:
                self.create_ics_file(filename)
                QMessageBox.information(self, "Export Successful", f"Workout plan exported to {filename}\n\nYou can now import this file into Google Calendar.")
            except Exception as e:
                QMessageBox.critical(self, "Export Failed", f"Failed to export: {str(e)}")
    
    def create_ics_file(self, filename):
        """ Create ICS calendar file """
        start_date = self.start_date
        
        ics_content = "BEGIN:VCALENDAR\n"
        ics_content += "VERSION:2.0\n"
        ics_content += "PRODID:-//Workout App//Workout Calendar//EN\n"
        
        for day, exercises in self.workout_plan.items():
            event_date = start_date + timedelta(days=day-1)
            
            # Create event
            ics_content += "BEGIN:VEVENT\n"
            ics_content += f"DTSTART;VALUE=DATE:{event_date.strftime('%Y%m%d')}\n"
            ics_content += f"DTEND;VALUE=DATE:{event_date.strftime('%Y%m%d')}\n"
            ics_content += f"SUMMARY:Day {day} Workout\n"
            
            # Add exercises to description
            description = f"Workout for Day {day}:\\n\\n"
            for i, exercise in enumerate(exercises, 1):
                exercise_desc = self.exercise_descriptions.get(exercise, "No description available")
                description += f"{i}. {exercise}\\nHow to: {exercise_desc}\\n- 3 sets of 12 reps\\n- Rest 60 seconds\\n\\n"
            
            ics_content += f"DESCRIPTION:{description}\n"
            ics_content += f"UID:workout-day-{day}-{datetime.now().strftime('%Y%m%d%H%M%S')}\n"
            ics_content += "END:VEVENT\n"
        
        ics_content += "END:VCALENDAR\n"
        
        with open(filename, 'w') as f:
            f.write(ics_content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Show Gender Selector initially
    gender_selector = GenderSelector()
    gender_selector.show()
    
    sys.exit(app.exec())
