# Prayer Journal CLI 🙏

![Tests](https://github.com/vestinie/-is4010-final-prayer-journal/actions/workflows/tests.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)

A command-line application for tracking and managing prayer requests. Keep a digital journal of your prayers, mark them as answered, and organize them by category.

## Features

- ✨ **Add Prayer Requests** - Create new prayers with custom categories
- 📋 **List All Prayers** - View all your prayers with status (active/answered)
- ✅ **Mark as Answered** - Celebrate answered prayers with timestamps
- 🗑️ **Delete Prayers** - Remove prayers you no longer want to track
- 💾 **Persistent Storage** - All prayers saved in JSON format
- 🏷️ **Categories** - Organize by Family, Health, Guidance, Thanksgiving, etc.

## Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
```bash
   git clone https://github.com/vestinie/-is4010-final-prayer-journal.git
   cd -is4010-final-prayer-journal
```

2. **Install dependencies**
```bash
   py -m pip install -r requirements.txt
```

## Usage

### Add a Prayer
```bash
py prayer_journal.py add "Please give me wisdom for my exams" --category School
```

With default category (General):
```bash
py prayer_journal.py add "Thank you for this beautiful day"
```

### List All Prayers
```bash
py prayer_journal.py list
```

Show only active (unanswered) prayers:
```bash
py prayer_journal.py list --active-only
```

**Example Output:**
```
============================================================
YOUR PRAYER JOURNAL
============================================================

ID: 1 | ✓ ANSWERED | [School]
Date: 2024-11-27 15:30:45
Prayer: Please give me wisdom for my exams
Answered: 2024-11-28 10:15:22

ID: 2 | ⏳ ACTIVE | [Family]
Date: 2024-11-27 16:45:12
Prayer: Heal my grandmother

============================================================
```

### Mark Prayer as Answered
```bash
py prayer_journal.py answered 1
```

Output:
```
✓ Prayer 1 marked as answered! Praise God! 🙏
```

### Delete a Prayer
```bash
py prayer_journal.py delete 2
```

### Get Help
```bash
py prayer_journal.py --help
py prayer_journal.py add --help
```

## Testing

This project includes comprehensive automated tests.

### Run All Tests
```bash
py -m pytest test_prayer_journal.py -v
```

### Run with Coverage
```bash
py -m pytest test_prayer_journal.py -v --cov=prayer_journal
```

### Test Results
All 10 tests pass, covering:
- Adding prayers
- Listing prayers
- Marking prayers as answered
- Deleting prayers
- Data persistence (save/load)
- Error handling

## Project Structure
```
-is4010-final-prayer-journal/
├── prayer_journal.py          # Main application
├── test_prayer_journal.py     # Test suite
├── prayers.json               # Data storage (created automatically)
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── LICENSE                    # MIT License
├── AGENTS.md                  # AI assistance documentation
└── .github/
    └── workflows/
        └── tests.yml          # CI/CD pipeline
```

## Categories

Suggested categories for organizing prayers:
- **Family** - Prayers for family members
- **Health** - Healing and health requests
- **Guidance** - Seeking direction and wisdom
- **Thanksgiving** - Gratitude and praise
- **Work/School** - Career and education
- **Relationships** - Friendships and connections
- **General** - Default category

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## AI-Assisted Development

This project was developed with AI assistance from Claude (Anthropic). See [AGENTS.md](AGENTS.md) for detailed documentation of how AI tools were used in the development process.

## Author

Vestinie - IS4010 Final Project