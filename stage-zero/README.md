# HackBio Biocoding Internship: Stage 0  

## Objective
This task involved using the data structure of either R or Python to create a simple scripts in order to organise the names, slack usernames, emails, hobbies, countries, disciplines, and preferred programming languages of all the members in my team. As per the instructions given, this script excludes the use of functions, loops, conditionals, and complex concepts.

Therefore, this repository contains a Python script which organises the details of team members of the **Team Alanine** in the HackBio internship (Coding for Bio) in a systematic manner. 

## Task Description  
For **Stage 0**, we were required to write a Python script that prints:  

✅ **Names of the team members.**  
✅ **Their Slack Usernames.**  
✅ **Their Email Ids.**  
✅ **Their Hobbies.**  
✅ **Their Countries.**  
✅ **Their Disciplines.**  
✅ **Preferred Programming Language.**

## Steps Followed  
1️⃣ **Set up the script** – Created a new Python file `stage_zero.py`.  
2️⃣ **Defined variables** – Assigned my details to different variables.  
3️⃣ **Used formatted printing** – Used an f-string to neatly display all the information.  
4️⃣ **Run the script** – Executed the Python file to verify the output.  

## My Solution (Python Code)  
Here's the Python script I wrote introducing myself and my other teammates:  

```python
# Stage 0 Task - HackBio Biocoding Internship

# Defining my details
name = "Priyanjali Chowdhury"
slack_username = "Priyanjali"
email = "priyanjali150803@gmail.com"
hobbies = "Listening to music"
country = "India"
discipline = "Bioinformatics"
programming_language = "Python"

# Details of my other teammates
 Names = [
  "Ncumisa Madolo",
  "Chelson Boakye" ,
  "Emanueal Osei-Frempong" ,
  "Ayiti",
  "Priyanjali Chowdhury"
]
Slack_names = [
  "Ncumisa",
  "Chelson",
  "Emanueal",
  "Ayiti",
  "Priyanjali"
]
Email = [
  "ncumisam00@gmail.com" ,
  "boakyechelson@gmail.com" ,
  "eosei-frempong@tamu.edu" ,
  "ayitikola@yahoo.com" ,
  "priyanjali150803@gmail.com"
]
Hobbies = [
  "Listening to music",
  "Travelling" ,
  "Tennis" ,
  "Fixing things" ,
  "Watching movies"
]
Countries = [
  "South Africa" ,
  "Ghana" ,
  "Nigeria" ,
  "Nigeria" ,
  "India"
]
Disciplines = [
  "Neuroscience" ,
  "Biochemistry" ,
  "Biology" ,
  "Biochemistry" ,
  "Bioinformatics"
]
programming_language = [
  "Python" ,
  "Python" ,
  "Python" ,
  "R" ,
  "Python"
]
txt = f'Alanine-2 group members names {Names}, and our Slack usernames {Slack_names}.You can email us on {Email}. Our Hobbies include {Hobbies}. We have a diverse group with members coming from {Countries}, with disciplines in {Disciplines}. Our preferred programming lanuages are {programming_language}'
print(txt)

---
```

## Contributors
| S/N | GROUP MEMBERS (Team Alanine)                                                                                                                   |
|-----|-------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Priyanjali Chowdhury  [GitHub](https://github.com/reeshho/Hackbio-biocoding-internship/tree/main)           |
| 2   | Kolawole Stephen Ayiti  [GitHub](https://github.com/ifoundmercy/HackBio)                     |
| 3   | Ncumisa Madolo [GitHub](https://github.com/ncumi-m/Hackbio-Internship/tree/main)             |
| 4   | Emmanuel Osei-Frempong              |
| 5   | Chelson Osei Mensah Boakye    |
