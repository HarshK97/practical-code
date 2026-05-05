# Code Assessment & How to Run

## CS Codes

**Assignment 1 — Packet Sniffer**

Use **`sniffer.py`** — it's the cleaner, class-based version with argparse. `sniff.py` also works but it's hardcoded to interface `enp3s0` which may not be your interface name.

```bash
pip install scapy --break-system-packages
# Find your interface name first:
ip a
# Then run:
sudo python3 sniffer.py -i eth0        # replace eth0 with your interface
sudo python3 sniffer.py -i eth0 -v     # verbose mode shows full packet details
```

If asked what `-v` does in oral: "It calls `packet.show()` instead of `packet.summary()`, giving full layer-by-layer packet breakdown."

---

**Assignment 2a — DDoS**

Use **`Ddos.py`** — it's the cleaner version. `dos.py` uses the deprecated `random._urandom` without renaming the variable `bytes` (which shadows Python's built-in). `Ddos.py` fixes both.

```bash
# No install needed, uses built-in socket
python3 Ddos.py
# It targets 127.0.0.1 (localhost) by default — safe for demo
# Ctrl+C to stop
```

When it runs, you'll see the progress bar then packets flooding. The examiner will ask you to stop it with Ctrl+C.

---

**Assignment 2b — IP Spoofing**

Use **`spoof.py`**.

```bash
pip install scapy --break-system-packages
sudo python3 spoof.py
# Ctrl+C to stop
```

Note: The IPs in the file (192.168.5.x) are hardcoded. If examiner asks why those IPs, say "A is the spoofed source, B is the destination — we're making it look like packets come from A when they don't."

---

**Assignment 2c — DNS Attack**

Use **`DNS_Attack.py`** over `dns.py` — it's cleaner, has better logging messages, and the `callBack` function properly calls `packet.accept()` outside the `if` block (which is the correct behavior).

```bash
pip install scapy netfilterqueue --break-system-packages
sudo python3 DNS_Attack.py
# Ctrl+C to stop — it auto-cleans iptables rule on exit
```

Fair warning: `netfilterqueue` is Linux-only and needs root. If it fails to install, just show the code and explain the concept — that's usually enough for the oral.

---

**Assignment 3 — Spam Detection**

`assign3.py` has a syntax error — there are leading spaces before `from nltk...` which will cause an IndentationError. Also it's incomplete (only shows half the code — no model training, no prediction output). You'll need the dataset file `spam.csv` too.

For the oral, just explain the concept: Naive Bayes, CountVectorizer, TF-IDF, train/test split. If they want to run it, you need the full file and dataset. You can download the spam.csv from Kaggle (search "SMS Spam Collection Dataset").

---

## WAD Codes

**Assignment 1a — Dashboard + Forms**

Use the files in **`WAD/WADrane/1a/`** — that folder has the complete set: `login.html` → `regrestration.html` → `dashboard.html`, all properly linked.

```bash
# No server needed, just open in browser:
# In terminal, navigate to the folder then:
xdg-open login.html
# Or just double-click login.html in file manager
```

Flow to show the examiner: open `login.html` → click Register → fills `regrestration.html` → submit → goes to `dashboard.html` which shows the Bootstrap sidebar + stat cards.

---

**Assignment 1b — Local Storage / AJAX**

Use **`WAD/WADrane/1b/regrestration.html`** — it's cleaner than the one in `Ass1b local storage`. The `WADrane` version uses `onsubmit="return Register()"` which properly prevents form reload. The other version uses `onclick` on the button which has a timing issue.

```bash
xdg-open regrestration.html
```

To demo for examiner: fill name/email/password → click Register → alert pops → open DevTools (F12) → Application tab → Local Storage → show the stored JSON. That's your proof it worked.

---

**Assignment 1b — AJAX (ajax1.html)**

The `ajax/ajax1.html` uses jQuery's `.load()` to fetch `ajax2.html`. There's no `ajax2.html` in the repo so it'll fail at that step. But the localStorage part works fine. Just demo the form → localStorage part and explain AJAX conceptually.

---

**Assignment 2a — Git**

The `WAD/2a Github/` folder has a travel website. Use this to demo Git commands.

```bash
cd "WAD/2a Github"
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main
```

Open `index.html` in browser to show the site. Images won't load (paris.jpg etc. are missing) but the structure is there.

---

**Assignment 2b — Docker**

The `how.txt` in that folder has the full Docker session output — it's a Windows screenshot but the commands are the same on Linux:

```bash
docker pull openjdk
docker run --name JAVA -it -d openjdk
docker exec -it JAVA jshell
# Inside jshell:
System.out.println("Hello World");
/exit
docker stop JAVA
```

---

**Assignment 2c — Angular**

Use files from **`WAD/WADrane/2c/`** or **`WAD/2c Angular application/`** — they're identical. Replace the files in your Angular project's `src/app/` folder.

```bash
npm install -g @angular/cli@latest
ng new partc
# select CSS, yes, yes
cd partc
# Replace app.component.html, app.component.ts, app.component.css with the repo files
ng serve
# Open browser: http://localhost:4200
```

What it does: input boxes for name/address/contact/email, click Register, values display below. Simple but covers the assignment.

---

**Assignment 3a — Node.js Static Site**

Use **`WAD/3a nodejs/`**. The `index.html` goes inside a `public/` folder, `index.js` stays outside.

```bash
cd "WAD/3a nodejs"
mkdir public
mv index.html public/
npm init -y
npm install express
node index.js
# Open browser: http://localhost:4000
```

---

**Assignment 4a — jQuery Mobile**

Use **`WAD/4ajQuery Mobile/`** — all 4 pages are there: `index.html`, `admission.html`, `courses.html`, `contact.html`. All CDN-linked so no install needed.

```bash
xdg-open index.html
```

Navigate through the pages, show the mobile-style navbar, collapsibles, and flipswitch toggle. That's your demo.

---

## Summary Table

| Assignment | Use This           | Skip This                    |
| ---------- | ------------------ | ---------------------------- |
| CS Sniff   | `sniffer.py`       | `sniff.py` (hardcoded iface) |
| CS DDoS    | `Ddos.py`          | `dos.py` (bad variable name) |
| CS DNS     | `DNS_Attack.py`    | `dns.py` (minor bug)         |
| WAD 1a     | `WADrane/1a/`      | `Ass1a/` (incomplete links)  |
| WAD 1b     | `WADrane/1b/`      | `Ass1b/` (minor issue)       |
| WAD 2c     | Either one         | Both are identical           |
| WAD 3a     | `3a nodejs/`       | —                            |
| WAD 4a     | `4ajQuery Mobile/` | —                            |

---

```bash
history
```

This shows all commands with numbers. Then:

```bash
history -d 42        # deletes line 42
history -d 42 45     # deletes lines 42 to 45
```

Or if you want to wipe specific commands by searching:

```bash
history | grep "sudo python3 Ddos.py"   # find the line number
history -d <that number>
```

To clear **entire** history:

```bash
history -c
```

Also after deleting, force-write to the history file so it's gone permanently:

```bash
history -w
```

Because by default the deletions only apply to the current session — `-w` writes it to `~/.bash_history` permanently.

If you're on zsh (Mac default):

```bash
fc -p    # to manipulate history
```

Or just edit the file directly:

```bash
nano ~/.zsh_history   # find and delete the line manually
```
