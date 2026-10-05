# 🧵 Spinning Process Simulator

An interactive **Streamlit educational web application** designed for **2nd-year Bachelor of Textile Engineering students**.

The simulator demonstrates the conventional **cotton ring-spinning process**, beginning with the Blow Room and ending at the Autoconer.

---

## 🔄 Spinning Process Flow

**Blow Room → Carding → Pre-Comber Draw Frame → Combing → Post-Comber Draw Frame → Simplex/Roving → Ring Frame → Autoconer**

---

## 🎯 Project Objectives

The main purpose of this project is to make the spinning process easier to understand through an interactive web application.

The application allows students to:

- Understand what happens at every spinning stage.
- Follow the complete material flow from cotton bales to yarn cones.
- See the input and output of every process.
- Explore important machine/process parameters.
- Change educational parameter values interactively.
- Observe simplified cause-and-effect calculations.
- Test their knowledge through multiple-choice quizzes.
- Receive immediate correct/incorrect feedback.
- Track their quiz score.

---

## 🧵 Processes Included

### 1. Blow Room

**Input:** Cotton bales

Main functions:

- Opening
- Cleaning
- Blending
- Removal of large trash

**Output:** Opened and blended cotton tufts

Important parameters included:

- Production rate
- Opening intensity
- Cleaning intensity
- Waste extraction

---

### 2. Carding

**Input:** Opened cotton tufts

Main functions:

- Fiber individualization
- Cleaning
- Nep control
- Fiber straightening and partial parallelization
- Sliver formation

**Output:** Card sliver

Important parameters:

- Production
- Cylinder speed
- Flat speed
- Card waste

---

### 3. Pre-Comber Draw Frame

**Input:** Card sliver

Main functions:

- Doubling
- Drafting
- Improvement of sliver regularity
- Preparation for combing

**Output:** Prepared sliver

Important parameters:

- Number of doublings
- Total draft
- Production
- Sliver CV%

---

### 4. Combing

**Input:** Prepared sliver/lap

Main functions:

- Removal of selected short fibers
- Removal of neps and impurities
- Improved fiber parallelization
- Production of cleaner combed sliver

**Output:** Combed sliver + noil

Important parameters:

- Noil extraction
- Nipper cycles
- Production
- Combing intensity

---

### 5. Post-Comber Draw Frame

**Input:** Combed sliver

Main functions:

- Doubling
- Drafting
- Improvement of mass evenness
- Preparation for roving

**Output:** Uniform drawn sliver

Important parameters:

- Doublings
- Total draft
- Production
- Input CV%

---

### 6. Simplex / Roving Frame

**Input:** Drawn sliver

Main functions:

- Drafting
- Reduction of linear density
- Temporary twist insertion
- Roving winding

**Output:** Roving bobbin

Important parameters:

- Total draft
- Roving twist
- Spindle speed
- Roving count

---

### 7. Ring Frame

**Input:** Roving

Main functions:

- Final drafting
- Permanent twist insertion
- Yarn formation
- Winding onto cops

**Output:** Ring-spun yarn

Important parameters:

- Total draft
- Spindle speed
- Yarn twist
- Breakage rate

---

### 8. Autoconer

**Input:** Ring-spun yarn on cops

Main functions:

- Winding
- Yarn clearing
- Fault detection
- Fault removal
- Splicing
- Cone formation

**Output:** Cleared and spliced yarn on cone

Important parameters:

- Winding speed
- Splice quality
- Clearing sensitivity
- Machine efficiency

---

# 🧠 Quiz System

Each process contains **3 multiple-choice questions**.

The quiz difficulty is approximately **3/5**, suitable for a second-year Textile Engineering student.

After answering a question, the application provides:

- ✅ Correct answer feedback
- ❌ Incorrect answer feedback
- Explanation of the concept
- Correct answer
- Stage score

The application also calculates an overall quiz score.

---

# ⚙️ Interactive Simulator

The application includes educational parameter controls using Streamlit sliders.

For example, the user can change:

- Production
- Draft
- Spindle speed
- Twist
- Waste
- Noil extraction
- Winding speed
- Machine efficiency

The application then displays simplified calculated results.

### Important

The calculations are **educational models**, not exact industrial process equations.

Actual spinning parameters depend on:

- Fiber type and properties
- Fiber length
- Micronaire
- Strength
- Machine design
- Machine manufacturer
- Yarn count
- Twist requirement
- Production target
- Environmental conditions
- Mill process settings

Therefore, the simulator should be used for **learning and demonstration**, not for setting real industrial machinery.

---

# 🎨 Interface Design

The application uses a combination of:

- Modern educational interface
- Textile-engineering terminology
- Process-flow navigation
- Interactive controls
- Metrics
- Progress tracking
- Quiz feedback
- Technical explanations

The goal is to make the application useful both for **learning and assignment demonstration**.

---

# 🛠️ Technology Used

- **Python**
- **Streamlit**
- HTML/CSS styling through Streamlit
- Streamlit session state for quiz progress

No external database is required.

---

# 📁 Project Structure

```text
spinning-process-simulator/
│
├── app.py
├── requirement.txt
└── README.md
```

---

# 💻 Running the Project Locally

## Step 1 — Install Python

Install Python 3.10 or newer.

Check your installation:

```bash
python --version
```

---

## Step 2 — Install the requirement

Open a terminal inside the project folder and run:

```bash
pip install -r requirement.txt
```

---

## Step 3 — Run Streamlit

Run:

```bash
streamlit run app.py
```

Streamlit will provide a local web address, normally similar to:

```text
http://localhost:8501
```

Open that address in your browser.

---

# 🐙 Uploading to GitHub

Create a new GitHub repository, for example:

```text
spinning-process-simulator
```

Upload these three files:

```text
app.py
requirement.txt
README.md
```

Your repository should look like:

```text
spinning-process-simulator
│
├── app.py
├── requirement.txt
└── README.md
```

---

# ☁️ Deploying on Streamlit Community Cloud

1. Upload the project to GitHub.
2. Open Streamlit Community Cloud.
3. Create a new application.
4. Select your GitHub repository.
5. Select `app.py` as the main file.
6. Deploy the application.

Streamlit will install the package listed in:

```text
requirement.txt
```

and run:

```text
streamlit run app.py
```

---

# 🎓 Suggested Assignment Description

> **Spinning Process Simulator** is an interactive educational web application developed using Python and Streamlit for Textile Engineering students. The application demonstrates the complete cotton ring-spinning process from Blow Room to Autoconer. Each stage explains the function of the machine, material input and output, important process parameters, and simplified parameter relationships. Interactive controls allow students to observe how process parameters affect simulated results. Multiple-choice quizzes with immediate feedback are included after each stage to evaluate student understanding.

---

# 🚀 Possible Future Improvements

The current version can later be expanded with:

- Machine diagrams
- Animated fiber movement
- Interactive fiber visualization
- Detailed yarn-count calculations
- Production calculations
- Drafting calculations
- Twist calculations
- Waste calculations
- Final cumulative assessment
- Student result report
- Downloadable quiz results
- Images of actual spinning machines
- Separate machine sections for different manufacturers
- More advanced process simulation

---

## ⚠️ Educational Disclaimer

This application is intended for **educational and academic demonstration purposes**.

The parameter ranges and simulation relationships are simplified. They do not represent universal machine settings or production recommendations. Real textile mills must determine machine settings using appropriate machine documentation, material testing, process-control procedures and qualified technical personnel.
