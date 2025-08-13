# Body Exercises Workout Planner

A PyQt6-based desktop application that helps users create personalized workout plans by selecting specific muscle groups on an interactive body diagram.

## Features

- **Interactive Body Selection**: Click on specific muscle groups on male/female body diagrams
- **Gender-Specific Exercises**: Different exercise recommendations for male and female users
- **Flexible Time Periods**: Create workout plans for one week or one month
- **Custom Start Dates**: Choose when to begin your workout routine
- **Detailed Exercise Instructions**: Each exercise includes step-by-step instructions and recommended sets/reps
- **Calendar Export**: Export your workout plan to Google Calendar (.ics format)
- **Visual Workout Calendar**: Interactive calendar view showing daily exercises

## Screenshots

The application features anatomically accurate body diagrams with clickable muscle regions for both male and female body types.

## Installation

### Prerequisites

- Python 3.13 or higher
- pipenv (recommended) or pip

### Using pipenv (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd body_exercises

# Install dependencies
pipenv install

# Activate virtual environment
pipenv shell

# Run the application
python main.py
```

### Using pip

```bash
# Clone the repository
git clone <repository-url>
cd body_exercises

# Install dependencies
pip install PyQt6

# Run the application
python main.py
```

## Usage

1. **Select Gender**: Choose between male or female body diagram
2. **Select Muscles**: Click on the muscle groups you want to target
3. **Choose Time Period**: Select either a one-week or one-month workout plan
4. **Set Start Date**: Pick when you want to begin your workout routine
5. **View Calendar**: Browse your personalized workout calendar
6. **Export to Google Calendar**: Save your workout plan as an .ics file for import into Google Calendar

## Supported Muscle Groups

### Core
- Higher abs, middle abs, lower abs
- Left and right obliques

### Upper Body
- Biceps (left/right)
- Triceps (left/right)
- Trapezius muscles

### Lower Body
- Quadriceps (left/right)
- Gluteus
- Gastrocnemius/Calves (left/right)

## Exercise Database

The application includes gender-specific exercise recommendations:

- **Male exercises**: Focus on strength training with weights, pull-ups, heavy compound movements
- **Female exercises**: Emphasize bodyweight exercises, resistance bands, and functional movements

Each exercise includes:
- Clear instructions
- Recommended sets and reps (3 sets of 12 reps)
- Rest periods (60 seconds)

## File Structure

```
body_exercises/
├── assets/
│   ├── female_body.png    # Female body diagram
│   └── male_body.png      # Male body diagram
├── ui/
│   └── body_viewer.py     # Alternative body viewer implementation
├── main.py                # Main application entry point
├── Pipfile               # Python dependencies
├── Pipfile.lock          # Locked dependency versions
└── workout_plan.ics      # Sample exported calendar file
```

## Technical Details

- **Framework**: PyQt6 for GUI
- **Image Format**: PNG images for body diagrams
- **Calendar Export**: ICS format compatible with Google Calendar, Outlook, and other calendar applications
- **Architecture**: Object-oriented design with separate classes for each application screen

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Future Enhancements

- Add more muscle groups and exercise variations
- Implement progress tracking
- Add workout difficulty levels
- Include exercise videos or animations
- Support for custom exercise creation
- Integration with fitness trackers