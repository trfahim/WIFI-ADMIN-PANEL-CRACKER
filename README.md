# WiFi Admin Panel Cracker 🛜

A Python-based tool for brute-forcing router login credentials using a wordlist. This script simulates login attempts to a router's web interface and attempts to crack the password.

---

## Features 🤖
- Customizable target IP address.
- Reads passwords from a user-provided wordlist file.
- Base64 encoding of passwords for login payloads.
- Detailed logging of attempts and successful matches.

---

## Installation 📊

### Prerequisites
- Python 3.8 or higher.
- Required Python modules: `requests`, `pyfiglet`, `colorama`.

# How to use 😎
### Step 1: Clone the Repository
- git clone https://github.com/trfahim/WiFi-Panel-Cracker.git
- cd WiFi-Panel-Cracker
### Step 2:Install Required Libraries
- pip install requests
- pip install pyfiglet
- pip insatll colorama
### Step 3: Run the Script
- python panel_cracker.py
### Step 4: Choose an IP Option
- Option 1: Use the default IP (192.168.0.1).
- Option 2: Enter a custom target IP.
### Step 5: Provide a Wordlist Path
- Input the full path to your password wordlist (e.g., wordlist.txt).
### Step 6: View Results
- The script will log all attempts.
- If a password is cracked, it will be displayed as:
-PASSWORD FOUND :: <password>
### Example
- [1] DEFAULT IP [2] SET IP >>> 1
- Input Wordlist Path >>> wordlist.txt
- Attempt[1]: Trying >> admin
- Attempt[2]: Trying >> password123
- ******************************
  - PASSWORD FOUND :: password123
- ******************************


## Disclaimer ⚠️
 This tool is created for educational purposes only. Unauthorized use of this script to gain access to networks without permission is illegal and unethical. The author, TR Fahim, is not responsible for any misuse of this tool.

