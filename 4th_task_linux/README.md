# 📦 Task 4 – Installation and Maintenance


## 🛠️ 1. Package Manager: APT vs Snap

### 🧩 Snap
Snap packages run in a **confined (sandboxed) environment**, which helps protect the system from dependency conflicts and potentially malicious software 🔒.  
Snaps **update automatically in the background**, ensuring applications stay up to date without manual intervention 🔄.  

A key advantage of Snap is **cross-distribution compatibility** — the same Snap package can run consistently across multiple Linux distributions 🌍.


### ⚙️ APT (Advanced Package Tool)
APT is the **default package manager** for Debian and Ubuntu-based Linux distributions 🐧.  
It installs software directly from official repositories and integrates closely with the system, resulting in lightweight and efficient applications ⚡.


## 🔍 2. Search Tools: `grep` vs `ripgrep (rg)`

### 🧠 ripgrep (`rg`)
`rg` automatically ignores `.gitignore` files and directories like `node_modules`.  
It searches the entire directory tree and is **faster and more efficient**, especially for large projects 🚀.


### 🧰 grep
`grep` is a traditional and widely available search tool.  
It is reliable, flexible, and works well for simple text searching tasks 📜.


## 🌐 3. Internet Utilities

### 📡 curl
`curl` is used for interacting with REST APIs that require:
- Custom HTTP methods  
- Headers  
- Authentication  

It is ideal for API requests and data transfer 🔗.

### 📥 wget
`wget` is a superior choice when downloading:
- Large files  
- Entire websites  

It supports recursive downloads, resume capability, and unattended operation 📦.


## 🔗 4. Pipe (`|`)
The pipe is used to **connect different commands**, allowing the output of one command to be used as input for another without changing context 🧩.

This makes command-line workflows more powerful, efficient, and readable.

