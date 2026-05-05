# Assignment 1a — Dashboard (Bootstrap)

The main file is `WADrane/1a/dashboard.html`. Let's break it down.

## The Sidebar

```html
<div class="sidebar">
  <h2>Dashboard</h2>
  <a href="#homeTab" data-bs-toggle="tab">Home</a>
  <a href="#ordersTab" data-bs-toggle="tab">Orders</a>
</div>
```

`class="sidebar"` — this is a custom CSS class defined in the `<style>` block:

```css
.sidebar {
  position: fixed; /* stays in place when you scroll */
  top: 0;
  left: 0;
  height: 100%;
  width: 240px;
  background-color: #343a40; /* dark grey */
}
```

`position: fixed` — sidebar doesn't scroll with the page, always visible.

`data-bs-toggle="tab"` — Bootstrap attribute. Tells Bootstrap this link switches tabs without page reload.

## The Main Content

```html
<div class="main-content">
  <div class="container-fluid"></div>
</div>
```

`margin-left: 240px` on `.main-content` — pushes content right so it doesn't hide behind the sidebar.

`container-fluid` — Bootstrap class, makes container full width.

## The Stat Cards

```html
<div class="col-md-3 mb-4">
  <div class="card bg-primary text-white">
    <div class="card-body">
      <h5 class="card-title">Total Orders</h5>
      <p class="card-text">325</p>
    </div>
  </div>
</div>
```

`col-md-3` — Bootstrap grid. On medium+ screens, each card takes 3 of 12 columns → 4 cards fit in one row.

`bg-primary` — Bootstrap color class, blue background.

`text-white` — white text.

`card`, `card-body`, `card-title`, `card-text` — Bootstrap card component classes.

## The Tabs

```html
<ul class="nav nav-tabs" id="dashboardTab">
  <li class="nav-item">
    <a class="nav-link active" data-bs-toggle="tab" href="#home">Home</a>
  </li>
</ul>
<div class="tab-content">
  <div class="tab-pane fade show active" id="home">
    <!-- content -->
  </div>
</div>
```

`nav nav-tabs` — Bootstrap tab navigation.

`tab-pane fade show active` — Bootstrap classes. `fade` adds transition, `show active` makes this tab visible by default.

`data-bs-toggle="tab"` — Bootstrap JS handles the switching automatically, no custom JS needed.

## The Table

```html
<table class="table table-striped">
  <thead>
    <tr>
      <th>#</th>
      <th>Product</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Papers</td>
    </tr>
  </tbody>
</table>
```

`table-striped` — Bootstrap class, alternating row colors automatically.

**What examiner will ask:**

- What is Bootstrap grid? → 12-column system, `col-md-3` = 3/12 = 25% width
- What is `position: fixed`? → Element stays fixed relative to viewport, doesn't scroll
- What is a Bootstrap card? → Pre-styled container component with header, body, footer
- What does `data-bs-toggle="tab"` do? → Tells Bootstrap JS to handle tab switching
- What is `container-fluid`? → Full-width container, no max-width limit

---

# Assignment 1b — Registration + Local Storage

File: `WADrane/1b/regrestration.html`

```html
<form onsubmit="return Register()">
  <input type="text" id="name" />
  <input type="email" id="email" />
  <input type="password" id="password" />
  <button type="submit">Register</button>
</form>
```

`onsubmit="return Register()"` — calls Register() when form submits. The `return false` inside prevents page reload.

## The JavaScript

```javascript
function Register() {
  let name = document.getElementById("name").value;
  let email = document.getElementById("email").value;
  let password = document.getElementById("password").value;

  let users = JSON.parse(localStorage.getItem("user")) || [];

  if (users.some((user) => user.email === email)) {
    alert("Duplicate data found!");
  } else {
    users.push({ name: name, email: email, password: password });
    localStorage.setItem("user", JSON.stringify(users));
    alert("Registration Successful!");
  }
  return false;
}
```

**Line by line:**

`document.getElementById("name").value` — gets the value typed in the name input field.

`localStorage.getItem("user")` — retrieves previously stored data from browser's localStorage. Returns `null` if nothing stored yet.

`JSON.parse(...)` — localStorage only stores strings, so we parse the JSON string back into a JavaScript array.

`|| []` — if `getItem` returns null (first time), use empty array instead.

`users.some((user) => user.email === email)` — checks if any existing user already has this email. `.some()` returns true if at least one element matches the condition.

`users.push({...})` — adds new user object to the array.

`JSON.stringify(users)` — converts array back to JSON string for storage.

`localStorage.setItem("user", ...)` — saves the updated array back to localStorage.

`return false` — prevents the form from doing a normal submit (which would reload page).

**What examiner will ask:**

- What is localStorage? → Browser-based key-value storage, persists after page close
- Difference between localStorage and sessionStorage? → localStorage persists permanently, sessionStorage clears when tab closes
- What is JSON.stringify? → Converts JS object to JSON string
- What is JSON.parse? → Converts JSON string back to JS object
- What does `.some()` do? → Returns true if at least one array element satisfies the condition
- Why `return false`? → Prevents default form submission which would reload the page
- How to view localStorage? → F12 → Application tab → Local Storage

---

# Assignment 2a — Git

This is more commands than code. The `2a Github/index.html` is just a travel website to push. The important part is the Git workflow from `how.txt`:

```bash
git init                    # initialize empty repo in current folder
git add .                   # stage all files
git commit -m "Initial commit"   # save snapshot with message
git remote add origin https://github.com/username/repo.git   # link to GitHub
git branch -M main          # rename branch to main
git push -u origin main     # push to GitHub, set upstream
```

**What each command does:**

`git init` — creates a hidden `.git` folder that tracks everything. Your folder is now a repository.

`git add .` — moves all changed files to the staging area. Staging is the "waiting room" before committing.

`git commit -m "message"` — takes a permanent snapshot of staged files. The `-m` adds a message describing what changed.

`git remote add origin <url>` — tells your local repo where GitHub is. "origin" is just the conventional name for the remote.

`git branch -M main` — renames the default branch from "master" to "main" (GitHub's current default).

`git push -u origin main` — uploads commits to GitHub. `-u` sets origin/main as the default upstream so future pushes just need `git push`.

**What examiner will ask:**

- What is Git? → Distributed version control system by Linus Torvalds
- What is the difference between `git add` and `git commit`? → add stages changes, commit saves the snapshot permanently
- What is a branch? → Parallel version of the code for working on features independently
- What is `origin`? → Default name for the remote repository URL
- What is `git pull`? → Fetches and merges remote changes into local branch
- What is `git clone`? → Downloads an entire remote repository to your machine

---

# Assignment 2b — Docker

From the `how.txt` output:

```bash
docker pull openjdk          # download the openjdk image
docker run --name JAVA -it -d openjdk   # create and start container
docker exec -it JAVA jshell  # run jshell inside the container
```

**What each does:**

`docker pull openjdk` — downloads the OpenJDK image from Docker Hub. An image is like a blueprint.

`docker run --name JAVA -it -d openjdk`:

- `--name JAVA` — gives container the name "JAVA"
- `-i` — interactive mode (keeps stdin open)
- `-t` — allocates a terminal
- `-d` — detached mode, runs in background
- `openjdk` — the image to use

`docker exec -it JAVA jshell` — executes `jshell` command inside the running JAVA container. `-it` again for interactive terminal.

Inside jshell (Java's interactive shell):

```java
System.out.println("Hello world");   // prints output
int a = 30;                           // declares variable
System.out.println(a * b);            // arithmetic
/exit                                 // exits jshell
```

`docker stop JAVA` — stops the running container.

`docker image prune` — removes unused images to free disk space.

**What examiner will ask:**

- What is Docker? → Platform for containerizing applications with all dependencies
- Difference between image and container? → Image is blueprint, container is running instance of image
- What is Docker Hub? → Public registry where Docker images are stored and shared
- Why use Docker? → Consistent environment across different machines, "works on my machine" problem solved
- What is `-d` flag? → Detached mode, container runs in background
- What is `docker exec`? → Runs a command inside an already running container

---

# Assignment 2c — Angular

Files: `app.component.html` and `app.component.ts`

## The HTML Template

```html
<h1>{{title}}</h1>
<input type="text" #name placeholder="Enter your name" />
<input type="text" #address placeholder="Enter your address" />
<input type="text" #contact placeholder="Enter your contact" />
<input type="email" #email placeholder="Enter your email" />
<input type="password" #pwd placeholder="Enter your password" />
<button
  (click)="getValue(name.value, address.value, contact.value, email.value)"
>
  Register
</button>
<p>Name: {{displayname}}</p>
<p>Address: {{displayadd}}</p>
```

`{{title}}` — interpolation. Displays the value of `title` from the TypeScript class. This is one-way data binding (TS → HTML).

`#name` — template reference variable. Gives you a direct reference to that input element. So `name.value` gets whatever is typed in that box.

`(click)="getValue(...)"` — event binding. The `()` means we're listening to an event. When button is clicked, calls `getValue()` in the TypeScript class.

`name.value, address.value` etc — passes the current values of each input to the function.

`{{displayname}}` — displays the value of `displayname` variable from TypeScript. Updates automatically when variable changes.

## The TypeScript Class

```typescript
import { Component } from "@angular/core";
import { RouterOutlet } from "@angular/router";

@Component({
  selector: "app-root",
  imports: [RouterOutlet],
  templateUrl: "./app.component.html",
  styleUrl: "./app.component.css",
})
export class AppComponent {
  title = "Register Form";
  displayname = "";
  displayadd = "";
  displaycont = "";
  displaymail = "";

  getValue(name: string, address: string, contact: string, email: string) {
    this.displayname = name;
    this.displayadd = address;
    this.displaycont = contact;
    this.displaymail = email;
  }
}
```

`@Component` — decorator that tells Angular this class is a component. Metadata inside defines:

- `selector: 'app-root'` — the HTML tag name for this component (`<app-root>`)
- `templateUrl` — which HTML file to use
- `styleUrl` — which CSS file to use

`export class AppComponent` — the actual TypeScript class.

`title = 'Register Form'` — class property, displayed via `{{title}}` in HTML.

`displayname = ''` — starts empty, gets filled when Register is clicked.

`getValue(...)` — receives values from HTML, assigns them to class properties. Because of Angular's change detection, the `{{displayname}}` in HTML **automatically updates** when `this.displayname` changes. No manual DOM manipulation needed.

**What examiner will ask:**

- What is interpolation in Angular? → `{{}}` syntax to display component variables in HTML
- What is event binding? → `(event)="method()"` syntax to listen to DOM events
- What is a template reference variable? → `#name` gives direct reference to DOM element
- What is `@Component`? → Decorator that marks a class as an Angular component
- What is `selector`? → The HTML tag name used to insert this component
- What is change detection? → Angular automatically updates the DOM when component data changes

---

# Assignment 3a — Node.js Static Site

Two files: `index.js` (server) and `public/index.html` (webpage).

## `index.js`

```javascript
const express = require("express");
const app = express();
const port = 4000;

app.use(express.static("public"));

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

`require('express')` — imports the Express module (like Python's `import`).

`express()` — creates an Express application instance.

`app.use(express.static('public'))` — serves all files in the `public/` folder as static files. So `public/index.html` is accessible at `http://localhost:4000/index.html`.

`app.get('/', (req, res) => {...})` — defines a route. When someone visits `/` (root URL), run this callback. `req` is the request object, `res` is the response object.

`res.send('Hello World!')` — sends text response back to browser.

`app.listen(port, callback)` — starts the HTTP server on port 4000. The callback runs once server is ready.

## `public/index.html`

```html
<button class="button" onclick="changeContent()">Click Me!</button>

<script>
  function changeContent() {
    const heroSection = document.querySelector(".hero");
    heroSection.innerHTML = `
            <h1>Thank you for clicking!</h1>
            <button onclick="goBack()">Go Back</button>
        `;
  }
  function goBack() {
    window.location.reload();
  }
</script>
```

`document.querySelector('.hero')` — selects the first element with class `hero`.

`heroSection.innerHTML = ...` — replaces the entire inner HTML of that element with new content. Uses template literal (backticks) for multiline string.

`window.location.reload()` — reloads the current page, restoring original content.

**What examiner will ask:**

- What is Express.js? → Minimal web framework for Node.js
- What does `express.static()` do? → Serves files from a folder directly without defining routes for each
- What is `app.get()`? → Defines a GET route handler for a specific URL path
- What is `req` and `res`? → Request and Response objects — req has incoming data, res sends reply
- What is `app.listen()`? → Starts the HTTP server on the specified port
- What is `document.querySelector`? → Selects first matching DOM element using CSS selector syntax
- What is `innerHTML`? → Property to get or set the HTML content inside an element

---

# Assignment 4a — jQuery Mobile

Four files: `index.html`, `admission.html`, `courses.html`, `contact.html`.

## Core Structure

Every page follows this pattern:

```html
<div data-role="page" id="home">
  <div data-role="header">
    <h1>Welcome</h1>
    <div data-role="navbar">
      <ul>
        <li><a href="index.html" class="ui-btn-active">Home</a></li>
        <li><a href="admission.html">Admission</a></li>
      </ul>
    </div>
  </div>
  <div data-role="content">
    <!-- page content here -->
  </div>
</div>
```

`data-role="page"` — jQuery Mobile attribute. Marks this div as a page. jQuery Mobile can load multiple pages in one HTML file using these.

`data-role="header"` — styled as a header bar automatically by jQuery Mobile.

`data-role="navbar"` — creates a touch-friendly navigation bar with buttons.

`class="ui-btn-active"` — highlights the current page's nav button.

`data-role="content"` — the main content area of the page.

## Collapsible Sections

```html
<div
  data-role="collapsible"
  data-collapsed-icon="arrow-d"
  data-expanded-icon="arrow-u"
>
  <h3>About Our Institute</h3>
  <p>Content here...</p>
</div>
```

`data-role="collapsible"` — creates an accordion-style expandable section. Click the header to expand/collapse. Mobile-friendly.

`data-collapsed-icon` / `data-expanded-icon` — icons to show in each state.

## List View

```html
<ul data-role="listview" data-inset="true">
  <li><a href="courses.html" data-icon="grid">View All Courses</a></li>
</ul>
```

`data-role="listview"` — jQuery Mobile styles this as a touch-friendly list with large tap targets.

`data-inset="true"` — adds rounded corners and margin, looks like a card.

`data-icon="grid"` — adds an icon to the list item.

## Flip Switch

```html
<select data-role="flipswitch" id="notifications-toggle">
  <option value="off">Off</option>
  <option value="on">On</option>
</select>
```

`data-role="flipswitch"` — converts a regular select into a toggle switch (like iOS). No extra JS needed.

## Range Slider

```html
<input type="range" value="50" min="0" max="100" data-highlight="true" />
```

Standard HTML5 range input. `data-highlight="true"` is jQuery Mobile attribute that fills the track up to the thumb with color.

## Button

```html
<a href="admission.html" data-role="button" data-icon="arrow-r" data-theme="b">
  Get Started
</a>
```

`data-role="button"` — styles a plain link as a jQuery Mobile button.

`data-theme="b"` — applies theme B (blue) styling.

`data-icon="arrow-r"` — adds right arrow icon to the button.

**What examiner will ask:**

- What is jQuery Mobile? → Touch-optimized UI framework built on jQuery for mobile websites
- What is `data-role`? → HTML5 data attribute used by jQuery Mobile to identify and style components
- What is `data-role="page"`? → Marks a div as a jQuery Mobile page unit
- What is `data-role="listview"`? → Creates mobile-optimized touch-friendly list
- What is `data-role="collapsible"`? → Creates accordion-style expandable content section
- What is `data-role="flipswitch"`? → Converts select element into a toggle switch
- Difference between jQuery and jQuery Mobile? → jQuery is a general JS library, jQuery Mobile is a UI framework specifically for mobile built on top of jQuery

---

That's all 7 WAD assignments. Everything you need for tomorrow is covered. Go sleep at a reasonable time 😄
