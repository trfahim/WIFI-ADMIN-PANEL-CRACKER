# WiFi Admin Panel Cracker

A Python-based tool for brute-forcing router login credentials using a wordlist. This script simulates login attempts to a router's web interface and attempts to crack the password.

---

## Features
- Customizable target IP address.
- Reads passwords from a user-provided wordlist file.
- Base64 encoding of passwords for login payloads.
- Detailed logging of attempts and successful matches.

---

## Installation

### Prerequisites
- Python 3.8 or higher.
- Required Python modules: `requests`, `pyfiglet`, `colorama`.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/trfahim/WIFI-ADMIN-PANEL-CRACKER.git
   cd panel_cracker.py

## Example Output
WIFI CRACKER
------------------------------
      GITHUB >>> TRFAHIM
------------------------------

[1] DEFAULT IP [2] SET IP >>> 1
Input Wordlist Path >>> wordlist.txt
========= Start Scanning ==========

Attempt[1]: Trying >> admin
Attempt[2]: Trying >> password123
Attempt[3]: Trying >> qwerty
******************************
   PASSWORD FOUND :: qwerty
******************************
