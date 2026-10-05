import streamlit as st

st.set_page_config(
    page_title="Spinning Process Simulator",
    page_icon="🧵",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Process data
# -----------------------------
STAGES = [
    {
        "id": "blowroom",
        "name": "Blow Room",
        "icon": "🌬️",
        "input": "Cotton bales",
        "output": "Opened, cleaned and blended cotton tufts",
        "purpose": [
            "Opens compressed cotton from bales into smaller tufts.",
            "Removes large trash and foreign matter.",
            "Blends cotton from different bales for better uniformity.",
        ],
        "parameters": {
            "Production (kg/h)": (80, 500, 250, 10),
            "Opening intensity (%)": (40, 90, 65, 1),
            "Cleaning intensity (%)": (30, 85, 60, 1),
            "Waste extraction (%)": (1.0, 6.0, 3.0, 0.1),
        },
        "quiz": [
            ("What is the main purpose of opening?", ["Adding twist", "Separating compressed cotton into smaller tufts", "Making yarn cones", "Dyeing cotton"], 1,
             "Opening breaks compressed cotton into smaller tufts so subsequent processes can work more effectively."),
            ("Why is blending carried out in the blow room?", ["To improve uniformity", "To add yarn twist", "To make roving", "To create fabric"], 0,
             "Blending distributes differences between cotton bales and helps improve material consistency."),
            ("What normally enters the blow room?", ["Finished yarn", "Roving", "Cotton bales", "Fabric"], 2,
             "The spinning process begins with compressed cotton bales."),
        ],
    },
    {
        "id": "carding",
        "name": "Carding",
        "icon": "🪮",
        "input": "Opened cotton tufts",
        "output": "Card sliver",
        "purpose": [
            "Individualizes cotton fibers.",
            "Removes remaining impurities and helps control neps.",
            "Straightens and partially parallelizes fibers.",
            "Condenses the processed fibers into sliver.",
        ],
        "parameters": {
            "Production (kg/h)": (10, 80, 35, 1),
            "Cylinder speed (rpm)": (250, 600, 400, 10),
            "Flat speed (mm/min)": (50, 400, 200, 10),
            "Card waste (%)": (1.5, 8.0, 4.0, 0.1),
        },
        "quiz": [
            ("Which operation is strongly associated with carding?", ["Fiber individualization", "Cone winding", "Ring twisting", "Fabric finishing"], 0,
             "Carding works on the tufts so that fibers become much more individualized."),
            ("What is the normal output of a card?", ["Bale", "Card sliver", "Finished cone", "Fabric"], 1,
             "The card produces a continuous card sliver."),
            ("A major function of carding is to reduce:", ["Impurities and neps", "Spindle diameter", "Cone height", "Fabric width"], 0,
             "Carding removes remaining impurities and helps control neps."),
        ],
    },
    {
        "id": "precomber",
        "name": "Pre-Comber Draw Frame",
        "icon": "📏",
        "input": "Card slivers",
        "output": "Prepared sliver for combing",
        "purpose": [
            "Doubles several card slivers together.",
            "Drafts the combined material.",
            "Improves regularity before combing.",
        ],
        "parameters": {
            "Doublings": (4, 10, 8, 1),
            "Total draft": (3.0, 10.0, 7.5, 0.1),
            "Production (kg/h)": (30, 150, 80, 5),
            "Input sliver CV (%)": (2.0, 8.0, 4.5, 0.1),
        },
        "quiz": [
            ("Why are slivers doubled at the draw frame?", ["To add twist", "To average mass variations", "To dye the sliver", "To remove every short fiber"], 1,
             "Doubling averages variations from multiple slivers and improves regularity."),
            ("What does drafting mainly do?", ["Attenuates and arranges fibers", "Creates a cone", "Adds final twist", "Dyes cotton"], 0,
             "Drafting reduces linear density and helps arrange fibers in the direction of production."),
            ("The pre-comber draw frame prepares material for:", ["Combing", "Winding", "Weaving", "Finishing"], 0,
             "The prepared sliver is fed to the comber."),
        ],
    },
    {
        "id": "combing",
        "name": "Combing",
        "icon": "🧹",
        "input": "Prepared sliver / lap",
        "output": "Combed sliver + noil",
        "purpose": [
            "Removes a controlled proportion of short fibers.",
            "Removes additional neps and impurities.",
            "Improves fiber parallelization.",
            "Produces a cleaner and more uniform sliver.",
        ],
        "parameters": {
            "Noil extraction (%)": (8, 24, 16, 1),
            "Nipper cycles/min": (150, 450, 300, 10),
            "Production (kg/h)": (10, 70, 35, 1),
            "Combing intensity (%)": (40, 90, 65, 1),
        },
        "quiz": [
            ("What is noil?", ["Lubricant", "Removed short fibers and waste", "Final yarn", "A cone type"], 1,
             "Noil is the material removed during combing, including short fibers and other unwanted material."),
            ("Combing generally improves:", ["Fiber parallelization and cleanliness", "Cone color", "Fabric width", "Spindle lubrication"], 0,
             "Combing improves the cleanliness and parallelization of the fiber population."),
            ("Combing is especially useful for:", ["Finer and higher-quality yarns", "Only coarse waste yarn", "Direct fabric production", "Bale formation"], 0,
             "Combing is commonly used when a cleaner and more uniform fiber population is required."),
        ],
    },
    {
        "id": "postcomber",
        "name": "Post-Comber Draw Frame",
        "icon": "📐",
        "input": "Combed sliver",
        "output": "Uniform drawn sliver",
        "purpose": [
            "Doubles and drafts combed slivers.",
            "Improves sliver mass evenness.",
            "Prepares material for roving production.",
        ],
        "parameters": {
            "Doublings": (4, 10, 8, 1),
            "Total draft": (3.0, 10.0, 7.0, 0.1),
            "Production (kg/h)": (30, 160, 85, 5),
            "Input CV (%)": (1.5, 6.0, 3.0, 0.1),
        },
        "quiz": [
            ("The post-comber draw frame mainly prepares sliver for:", ["Roving production", "Dyeing", "Fabric inspection", "Cone packing"], 0,
             "The drawn combed sliver is suitable for feeding the roving frame."),
            ("Increasing doublings generally helps to:", ["Average mass variation", "Add final twist", "Remove all neps", "Create yarn directly"], 0,
             "Doubling averages variations among individual slivers."),
            ("What is produced by this stage?", ["Uniform drawn sliver", "Finished cone", "Fabric roll", "Cotton bale"], 0,
             "The main output is a more uniform drawn sliver."),
        ],
    },
    {
        "id": "simplex",
        "name": "Simplex / Roving Frame",
        "icon": "🧶",
        "input": "Drawn sliver",
        "output": "Roving on bobbin",
        "purpose": [
            "Drafts sliver into a finer strand.",
            "Inserts temporary twist for cohesion.",
            "Winds roving onto bobbins for ring spinning.",
        ],
        "parameters": {
            "Total draft": (4.0, 15.0, 9.0, 0.5),
            "Roving twist (T/m)": (15, 80, 45, 1),
            "Spindle speed (rpm)": (500, 1600, 1000, 50),
            "Roving count (Ne)": (0.5, 2.0, 1.0, 0.1),
        },
        "quiz": [
            ("Why is twist inserted into roving?", ["To give cohesion", "To make the final cone", "To dye the roving", "To remove all short fibers"], 0,
             "Roving needs temporary twist so it can be handled and drafted at the ring frame."),
            ("The main attenuation operation at the simplex is:", ["Drafting", "Combing", "Dyeing", "Cleaning"], 0,
             "The simplex drafts the sliver into a much finer roving strand."),
            ("The normal output of a simplex is:", ["Roving bobbin", "Card sliver", "Finished cone", "Cotton bale"], 0,
             "Roving is wound onto bobbins for feeding the ring frame."),
        ],
    },
    {
        "id": "ring",
        "name": "Ring Frame",
        "icon": "⭕",
        "input": "Roving",
        "output": "Ring-spun yarn on cop",
        "purpose": [
            "Drafts roving to final yarn linear density.",
            "Inserts permanent twist.",
            "Winds spun yarn onto cops.",
        ],
        "parameters": {
            "Total draft": (10.0, 50.0, 30.0, 1),
            "Spindle speed (rpm)": (7000, 22000, 15000, 500),
            "Yarn twist (T/m)": (400, 1200, 800, 10),
            "Breakage rate": (1.0, 12.0, 5.0, 0.5),
        },
        "quiz": [
            ("What is the major permanent operation at the ring frame?", ["Twist insertion", "Bale opening", "Combing", "Dyeing"], 0,
             "The ring frame inserts permanent twist that gives the yarn cohesion and contributes to its properties."),
            ("Increasing draft generally makes the delivered strand:", ["Finer", "Coarser", "More contaminated", "A larger cone"], 0,
             "For the same feed material, greater draft attenuates the strand to lower linear density."),
            ("What is produced directly by the ring frame?", ["Ring-spun yarn", "Card sliver", "Roving only", "Fabric"], 0,
             "The ring frame produces spun yarn, commonly wound onto cops."),
        ],
    },
    {
        "id": "autoconer",
        "name": "Autoconer",
        "icon": "🧵",
        "input": "Ring-spun yarn on cops",
        "output": "Cleared and spliced yarn on cone",
        "purpose": [
            "Transfers yarn from small cops to larger cones.",
            "Detects selected yarn faults using electronic clearing.",
            "Removes unacceptable faults according to settings.",
            "Splices yarn ends to create a continuous package.",
        ],
        "parameters": {
            "Winding speed (m/min)": (600, 1800, 1200, 50),
            "Splice quality target (%)": (70, 100, 90, 1),
            "Clearing sensitivity (%)": (40, 95, 75, 1),
            "Machine efficiency (%)": (70, 98, 90, 1),
        },
        "quiz": [
            ("Why is yarn cleared at the autoconer?", ["To detect selected yarn faults", "To comb fibers", "To make roving", "To open bales"], 0,
             "Electronic yarn clearers detect selected faults according to the clearing criteria."),
            ("What is the purpose of splicing?", ["Join yarn ends continuously", "Insert ring-frame twist", "Remove all short fibers", "Make sliver"], 0,
             "Splicing joins yarn ends so the final package remains continuous."),
            ("What is the usual final package from an autoconer?", ["Cone", "Bale", "Lap", "Roving bobbin"], 0,
             "The autoconer winds yarn into a larger cone package."),
        ],
    },
]

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.7rem;
        font-weight: 800;
        margin-bottom: 0;
    }
    .subtitle {
        font-size: 1.05rem;
        opacity: 0.75;
    }
    .stage-box {
        border: 1px solid rgba(128,128,128,.25);
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 12px;
    }
    .flow {
        display: flex;
        gap: 7px;
        overflow-x: auto;
        padding: 10px 0 18px;
    }
    .flow-item {
        min-width: 110px;
        text-align: center;
        border: 1px solid rgba(128,128,128,.30);
        border-radius: 12px;
        padding: 9px;
    }
    .flow-arrow {
        display: flex;
        align-items: center;
        font-size: 1.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Session state
# -----------------------------
if "scores" not in st.session_state:
    st.session_state.scores = {stage["id"]: 0 for stage in STAGES}

if "attempted" not in st.session_state:
    st.session_state.attempted = {stage["id"]: set() for stage in STAGES}

# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="main-title">🧵 Spinning Process Simulator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Interactive cotton ring-spinning learning tool • Difficulty 3/5</div>',
    unsafe_allow_html=True
)

st.info(
    "Educational simulator: the numerical values are simplified learning values. "
    "Actual spinning settings depend on fiber properties, yarn specification, machine design and mill conditions."
)

# -----------------------------
# Sidebar
# -----------------------------
stage_names = [s["name"] for s in STAGES]
selected_name = st.sidebar.radio(
    "🧭 Select a process stage",
    stage_names
)
stage = next(s for s in STAGES if s["name"] == selected_name)

total_questions = sum(len(s["quiz"]) for s in STAGES)
total_correct = sum(st.session_state.scores.values())

st.sidebar.divider()
st.sidebar.metric("Correct answers", f"{total_correct}/{total_questions}")
st.sidebar.progress(
    total_correct / total_questions if total_questions else 0,
    text="Overall quiz score"
)

if st.sidebar.button("🔄 Reset all quiz scores"):
    st.session_state.scores = {s["id"]: 0 for s in STAGES}
    st.session_state.attempted = {s["id"]: set() for s in STAGES}
    st.rerun()

# -----------------------------
# Process flow
# -----------------------------
st.markdown("### 🔄 Complete Spinning Process")

flow_cols = st.columns(len(STAGES))
for i, (col, s) in enumerate(zip(flow_cols, STAGES)):
    with col:
        if s["id"] == stage["id"]:
            st.success(f"{s['icon']} **{s['name']}**")
        else:
            st.write(f"{s['icon']} **{s['name']}**")
        if i < len(STAGES) - 1:
            st.caption("↓")

# -----------------------------
# Stage overview
# -----------------------------
st.divider()
st.header(f"{stage['icon']} {stage['name']}")

c1, c2 = st.columns(2)

with c1:
    st.subheader("🎯 What happens here?")
    for point in stage["purpose"]:
        st.markdown(f"- {point}")

with c2:
    st.subheader("📦 Material flow")
    st.markdown(f"**Input:** {stage['input']}")
    st.markdown(f"**Output:** {stage['output']}")

# -----------------------------
# Interactive simulation
# -----------------------------
st.divider()
st.subheader("⚙️ Interactive Parameter Simulator")
st.write(
    "Change the educational parameters below and observe the simplified simulated result."
)

params = {}
param_cols = st.columns(2)

for i, (label, values) in enumerate(stage["parameters"].items()):
    minimum, maximum, default, step = values
    with param_cols[i % 2]:
        params[label] = st.slider(
            label,
            min_value=minimum,
            max_value=maximum,
            value=default,
            step=step,
            key=f"{stage['id']}_{label}",
        )

# Simplified calculations
if stage["id"] == "blowroom":
    production = params["Production (kg/h)"]
    waste = params["Waste extraction (%)"]
    output = production * (1 - waste / 100)
    cleanliness = min(99, 70 + .18 * params["Cleaning intensity (%)"] + .08 * params["Opening intensity (%)"])
    metrics = [
        ("Usable material", f"{output:.1f} kg/h"),
        ("Estimated cleaning index", f"{cleanliness:.1f}%"),
        ("Estimated waste", f"{production-output:.1f} kg/h"),
    ]

elif stage["id"] == "carding":
    production = params["Production (kg/h)"]
    waste = params["Card waste (%)"]
    output = production * (1 - waste / 100)
    card_index = min(99, 65 + .05 * params["Cylinder speed (rpm)"] / 10 + .06 * params["Flat speed (mm/min)"])
    metrics = [
        ("Sliver output", f"{output:.1f} kg/h"),
        ("Indicative processing index", f"{card_index:.1f}%"),
        ("Waste", f"{production-output:.1f} kg/h"),
    ]

elif stage["id"] in ("precomber", "postcomber"):
    cv = params.get("Input sliver CV (%)", params.get("Input CV (%)"))
    doublings = params["Doublings"]
    draft = params["Total draft"]
    new_cv = max(1.0, cv / (1 + .06 * (doublings - 4)))
    metrics = [
        ("Estimated CV", f"{new_cv:.2f}%"),
        ("Doubling", f"{doublings}×"),
        ("Draft", f"{draft:.1f}"),
    ]

elif stage["id"] == "combing":
    noil = params["Noil extraction (%)"]
    retained = 100 - noil
    quality = min(99, 75 + .18 * params["Combing intensity (%)"])
    metrics = [
        ("Fiber retained", f"{retained:.1f}%"),
        ("Noil removed", f"{noil:.1f}%"),
        ("Indicative quality index", f"{quality:.1f}%"),
    ]

elif stage["id"] == "simplex":
    draft = params["Total draft"]
    twist = params["Roving twist (T/m)"]
    spindle = params["Spindle speed (rpm)"]
    count = params["Roving count (Ne)"]
    effective_count = count * (9 / draft)
    metrics = [
        ("Illustrative roving count", f"{effective_count:.2f} Ne"),
        ("Roving twist", f"{twist:.0f} T/m"),
        ("Spindle speed", f"{spindle:.0f} rpm"),
    ]

elif stage["id"] == "ring":
    draft = params["Total draft"]
    spindle = params["Spindle speed (rpm)"]
    twist = params["Yarn twist (T/m)"]
    breaks = params["Breakage rate"]
    illustrative_ne = 30 * (30 / draft)
    metrics = [
        ("Illustrative yarn count", f"Ne {illustrative_ne:.1f}"),
        ("Yarn twist", f"{twist:.0f} T/m"),
        ("Breakage index", f"{breaks:.1f}"),
    ]

else:
    speed = params["Winding speed (m/min)"]
    efficiency = params["Machine efficiency (%)"]
    splice = params["Splice quality target (%)"]
    clearing = params["Clearing sensitivity (%)"]
    effective_speed = speed * efficiency / 100
    package_index = .6 * splice + .4 * clearing
    metrics = [
        ("Effective winding speed", f"{effective_speed:.0f} m/min"),
        ("Package quality index", f"{package_index:.1f}%"),
        ("Machine efficiency", f"{efficiency:.0f}%"),
    ]

metric_cols = st.columns(len(metrics))
for col, (label, value) in zip(metric_cols, metrics):
    col.metric(label, value)

st.caption(
    "The simulator uses simplified relationships for learning. "
    "It is not a machine-control or production-setting tool."
)

# -----------------------------
# Quiz
# -----------------------------
st.divider()
st.subheader("🧠 Stage Quiz — Difficulty 3/5")

for q_index, (question, options, correct, explanation) in enumerate(stage["quiz"]):
    st.markdown(f"**Q{q_index + 1}. {question}**")

    answer = st.radio(
        "Choose one answer:",
        options,
        index=None,
        key=f"{stage['id']}_q_{q_index}",
        label_visibility="collapsed",
    )

    if st.button("Check answer", key=f"{stage['id']}_check_{q_index}"):
        if answer is None:
            st.warning("Please select an answer first.")
        elif q_index in st.session_state.attempted[stage["id"]]:
            st.info("This question has already been attempted.")
        elif options.index(answer) == correct:
            st.success(f"✅ Correct! {explanation}")
            st.session_state.scores[stage["id"]] += 1
            st.session_state.attempted[stage["id"]].add(q_index)
        else:
            st.error(
                f"❌ Incorrect. {explanation} "
                f"Correct answer: **{options[correct]}**"
            )
            st.session_state.attempted[stage["id"]].add(q_index)

st.caption(
    f"Stage score: {st.session_state.scores[stage['id']]}/{len(stage['quiz'])}"
)

# -----------------------------
# Educational flow explanation
# -----------------------------
st.divider()
st.subheader("📚 Position in the spinning process")

index = STAGES.index(stage)

previous_stage = STAGES[index - 1]["name"] if index > 0 else "Starting material"
next_stage = STAGES[index + 1]["name"] if index < len(STAGES) - 1 else "Final spinning preparation"

st.write(f"**Previous:** {previous_stage}")
st.write(f"**Current:** {stage['name']}")
st.write(f"**Next:** {next_stage}")

if stage["id"] == "blowroom":
    st.success("Bales are opened and cleaned before the material reaches the card.")
elif stage["id"] == "carding":
    st.success("Carding is the key fiber-individualizing stage and produces card sliver.")
elif stage["id"] == "precomber":
    st.success("Draw frame preparation improves regularity before combing.")
elif stage["id"] == "combing":
    st.success("Combing removes selected short fibers and improves fiber arrangement.")
elif stage["id"] == "postcomber":
    st.success("Post-comber drawing produces a controlled sliver for roving.")
elif stage["id"] == "simplex":
    st.success("The simplex changes sliver into a fine roving with temporary twist.")
elif stage["id"] == "ring":
    st.success("The ring frame performs final drafting and permanent twist insertion.")
else:
    st.success("The autoconer converts cops into larger, cleared and spliced yarn cones.")

st.divider()
st.markdown(
    "**Learning objective:** Understand what enters each stage, what the machine "
    "does, which parameters matter, and what material leaves the stage."
)
