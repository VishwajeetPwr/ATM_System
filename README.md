### 🏦 Enterprise-Grade Text-Based ATM System
    A robust, object-oriented backend simulation designed to master advanced OOP principles, design patterns, and persistent state management in Python.

### 🚀 Key Engineering Concepts
This is not just a calculator; it is a scalable backend architecture implementation.
    1. OOP Mastery: Implements Inheritance (SavingsAccount extends Account) and Polymorphism (Overridden deposit methods).
    2. Design Patterns: Uses the Factory Pattern in the Controller to instantiate the correct account type (Standard vs. Savings) based on data tags.
    3. State Management: persistent user sessions with secure Login/Logout flows.
    4. Data Persistence: Custom JSON Serialization engine to bridge the gap between volatile RAM objects and disk storage.
    5. Audit Logging: A timestamped Transaction Ledger that tracks every financial move for auditability.

### 📂 Project Structure
The monolithic script has been refactored into a modular MVC (Model-View-Controller) architecture:
    ├── Account_Class.py    # [Model] The Logic. Handles math, history, and polymorphism.
    ├── ATM_Class.py        # [Controller] The Manager. Handles Auth, DB I/O, and Menu routing.
    ├── main.py             # [Entry Point] The Runner. Initializes the system. 
    ├── test_atm.py         # [QA] Unit tests ensuring logic integrity.
    └── ATM_Database.json   # [Database] Persistent storage (Gitignored for security).
### ✨ Features
    1. Account Types (Polymorphism)
       1. Standard Account: Basic deposit/withdraw functionality.
       2. Savings Account: Inherits from Standard, but applies 5% Interest on every deposit automatically.
    2. Transaction History (Ledger)
       1. Every action is timestamped and recorded.
       2. Users can view a full log of their session history (e.g., [2023-11-28 14:00] Deposited: $500).
    3. Robust Error Handling
       1. Prevents overdrafts (insufficient funds).
       2. Validates inputs (prevents text input where numbers are required).
       3. Auto-creates database files if missing.

### 🛠️ Installation & Usage
1. Clone the repository:git clone [https://github.com/VishwajeetPwr/ATM_System.git](https://github.com/VishwajeetPwr/ATM_System.git)
cd ATM_System
2. Run the Application:
    python main.py
3. Run Unit Tests:
   python test_Account.py

### 🧠 Learning Outcomes
By building this, I moved beyond procedural scripting to understand:
   1. How to decouple Data (Account) from Control Logic (ATM).
   2. The importance of Serialization in preserving object state.
   3. How Inheritance reduces code duplication in scalable systems.
