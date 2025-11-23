Python OOP ATM System
    A robust, CLI-based ATM simulation built to master Object-Oriented Programming (OOP) principles and persistent state management.

## Architecture
    This system transitions away from procedural scripting into a modular class-based structure:
        - Account Class: Encapsulates user data (Name, PIN, Balance) and transactional logic.
        - ATM Class: Manages the system state, user sessions (Login/Logout), and file I/O.
        - Persistence Layer: Uses json serialization to ensure account data survives program restarts.

## Features
    - Session Management: Secure login/logout flow with PIN validation.
    - Data Persistence: Automated saving/loading of user data via atm_db.json.
    - Transaction Handling: Deposit and Withdrawal logic with validation checks (e.g., insufficient funds).
    - Error Handling: try-except blocks for graceful failure on invalid inputs.

## Installation & Usage

    1. Clone the repository:
        git clone [https://github.com/VishwajeetPwr/ATM_System.git](https://github.com/VishwajeetPwr/ATM_System.git)
    2. Run the application:
        python main.py
### Learning Outcomes
    - Implementing Encapsulation to protect user data.
    - Managing Application State (handling current_user).
    - Serializing objects to JSON for data storage.
