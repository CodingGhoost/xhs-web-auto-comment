# Xiaohongshu Web Auto Comment Script
[中文](./README.md) | English

## 📌 Introduction
A **Python** script for Xiaohongshu:  
Automatically matches homepage note titles based on keywords, and posts preset comments when a match is found.  

### 🔧 Configuration File: `config.ini`
Configure keywords and comment content.  

- **primary_match**: Must include all of these keywords  
- **secondary_match**: Must include at least one of these keywords  
- **comment**: The comment content to be automatically posted  

**Match Condition**: The title must contain all primary keywords + at least one secondary keyword  

### 🖥️ Main Program: `main.py`
Executes the automated process: **Filter → Match → Comment** based on configuration.  


## 🚀 Usage

### 1. Installation

```bash
# Download the program locally
git clone https://github.com/CodingGhoost/xhs-web-auto-comment.git

# Enter the program root directory
cd ./xhs-web-auto-comment

# Install dependencies
pip install drissionpage

# Run the program after configuring parameters
python main.py

```
### 2. Workflow
1. The program will open Google Chrome and prompt you to scan the QR code to log in  
2. After successful login, press Enter in the terminal → the program will maximize the browser window  
   - Recommended to reduce window scale to **33%** to load more posts on the homepage  
3. Press Enter again → the program navigates to the homepage and starts the loop:  
   **Fetch → Match → Comment → Refresh**  
4. During execution, the terminal will display: fetched titles / match results / comment progress  
5. The browser window can run in the background but must remain maximized for best effect  
6. Press **Ctrl + C** in the terminal to stop the program  


## ⚠️ Disclaimer
This project is for learning purposes only.  
Strictly prohibited for use in scenarios that violate Xiaohongshu's user agreement.  
Any losses caused by improper use are the responsibility of the user.  


## 📌 To-Do Features
- [ ] Translate to English documentation  
- [ ] Support pages other than the recommendation feed  
- [ ] Graceful exit mechanism  
- [ ] Graphical User Interface (GUI)  
- [ ] Match based on text recognition in post images  
