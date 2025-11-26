import streamlit as st

st.title("Guided Decision System for Data Structures")
st.write("Answer the following questions to get a recommended data structure.")

# --- QUESTIONS ---
q1 = st.selectbox("1. Do you need fast random access by index?", ["No", "Yes"])
q2 = st.selectbox("2. Are frequent insertions/deletions in the middle required?", ["No", "Yes"])
q3 = st.selectbox("3. Do you need key→value lookups as the main operation?", ["No", "Yes"])
q4 = st.selectbox("4. Do you need to maintain elements in sorted order?", ["No", "Yes"])
q5 = st.selectbox("5. Do you need FIFO or LIFO processing?", ["None", "FIFO", "LIFO"])
q6 = st.selectbox("6. Do you need to always retrieve the highest/lowest priority element?", ["No", "Yes"])
q7 = st.selectbox("7. Does the problem involve graph-like relationships?", ["No", "Yes"])
q8 = st.selectbox("8. Do you need prefix search on strings?", ["No", "Yes"])

if st.button("Recommend Data Structure"):
    # --- DECISION LOGIC ---
    if q7 == "Yes":
        ds = "Graph"
    elif q8 == "Yes":
        ds = "Trie"
    elif q6 == "Yes":
        ds = "Heap (Priority Queue)"
    elif q5 == "FIFO":
        ds = "Queue"
    elif q5 == "LIFO":
        ds = "Stack"
    elif q3 == "Yes":
        ds = "Hash Table"
    elif q1 == "Yes" and q2 == "No":
        ds = "Array"
    elif q2 == "Yes" and q4 == "No":
        ds = "Linked List"
    elif q4 == "Yes":
        ds = "Binary Search Tree (BST)"
    else:
        ds = "Linked List"

    st.header(f"Recommended: {ds}")

    # --- RATIONALE ---
    st.subheader("Why this recommendation?")
    rationale = {
        "Graph": "Because your problem involves relationships between entities.",
        "Trie": "Because you need fast prefix-based searches.",
        "Heap (Priority Queue)": "Because priority-based retrieval is required.",
        "Queue": "Because FIFO (first-in-first-out) processing is needed.",
        "Stack": "Because LIFO (last-in-first-out) processing is needed.",
        "Hash Table": "Because key→value lookup is the main operation.",
        "Array": "Because you need fast O(1) index access and few mid insertions.",
        "Linked List": "Because you do frequent insertions/deletions in the middle.",
        "Binary Search Tree (BST)": "Because you need sorted structure with efficient search."
    }
    st.write(rationale[ds])

    # --- DIAGRAMS ---
    st.subheader("Visual Diagram (ASCII)")

    diagrams = {
        "Array": "[0] [1] [2] [3] [4] ...",
        "Linked List": "HEAD -> [A|*] -> [B|*] -> [C|*] -> NULL",
        "Stack": "TOP -> [C]\n        [B]\n        [A]",
        "Queue": "FRONT -> [A] [B] [C] <- REAR",
        "Binary Search Tree (BST)": "      (8)\n     /   \\\n   (3)   (10)\n   / \\      \\\n (1) (6)    (14)",
        "Heap (Priority Queue)": "        [1]\n    [3]     [4]\n  [8] [5] [7] [9]",
        "Graph": "(A) -- (B)\n | \\      \n |  (C) -- (D)",
        "Hash Table": "0: → [ ]\n1: → [key:value]\n2: → [ ]\n3: → [key:value] → [key:value]",
        "Trie": "(root)\n  ├─ c\n  │   └─ a\n  │       └─ t*\n  └─ d\n      └─ o\n          └─ g*"
    }
    st.code(diagrams[ds])

    # --- PSEUDOCODE ---
    st.subheader("Pseudocode of Main Operations")

    pseudocode = {
        "Array": """INSERT(A, i, x):
  A[i] = x

SEARCH(A, x):
  for i in 0..n:
    if A[i] == x: return i
  return -1
""",
        "Linked List": """INSERT(head, x):
  new = Node(x)
  new.next = head
  head = new

SEARCH(head, x):
  while head != null:
    if head.value == x: return true
    head = head.next
  return false
""",
        "Stack": """PUSH(S, x):
  S[top] = x
  top++

POP(S):
  top--
  return S[top]
""",
        "Queue": """ENQUEUE(Q, x):
  Q[rear] = x
  rear++

DEQUEUE(Q):
  x = Q[front]
  front++
  return x
""",
        "Binary Search Tree (BST)": """INSERT(root, x):
  if root == null: return Node(x)
  if x < root.val: root.left = INSERT(root.left, x)
  else: root.right = INSERT(root.right, x)
  return root
""",
        "Heap (Priority Queue)": """INSERT(H, x):
  add x to end
  bubble-up

POP-MIN(H):
  swap root with last
  remove last
  bubble-down
""",
        "Graph": """ADD_EDGE(G, u, v):
  G[u].append(v)
  G[v].append(u)
""",
        "Hash Table": """PUT(T, key, value):
  i = hash(key)
  T[i].append((key, value))

GET(T, key):
  i = hash(key)
  search list T[i]
""",
        "Trie": """INSERT(root, word):
  node = root
  for c in word:
    if c not in node.children:
      node.children[c] = new Node()
    node = node.children[c]
  node.end = true
"""
    }
    st.code(pseudocode[ds])

    # --- EXAMPLE ---
    st.subheader("Concrete Example")

    examples = {
        "Array": "Example: Storing student grades and accessing grade[i] in O(1).",
        "Linked List": "Example: Music playlist where you frequently insert/delete songs.",
        "Stack": "Example: Undo/Redo functionality in an editor.",
        "Queue": "Example: Process scheduling (first-in-first-out).",
        "Binary Search Tree (BST)": "Example: Searching numbers in sorted structure efficiently.",
        "Heap (Priority Queue)": "Example: Always taking the smallest job in OS scheduling.",
        "Graph": "Example: Finding shortest paths between cities.",
        "Hash Table": "Example: User lookup by username.",
        "Trie": "Example: Autocomplete suggestions for 'ca': car, cat, cart."
    }
    st.write(examples[ds])
