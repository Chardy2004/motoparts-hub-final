# MotoParts Hub

Motorcycle parts and accessories website for **Event-Driven Programming (Final Project)** and **Business Analytics**, Cebu Eastern College.
Built with HTML, CSS and **PyScript** (Python in the browser).

## Pages
- `index.html` Landing page: the video advertisement with a nav bar (Home, Products, Services, Contact)
- `home.html` Home page (banner, business info)
- `products.html` Product catalog (search, category filter) and shopping cart (`products.py`)
- `services.html` Services
- `contact.html` Feedback / interest form (`contact.py`)

## Video advertisement (Business Analytics)
- The 38-second cinematic ad is the landing page itself (`index.html`): English subtitles, animated scenes, effects
- `music.mp3` cinematic score and `sfx.mp3` sound effects, both played by the ad
- Optional voice-over files: `vo1.mp3` to `vo6.mp3` (if missing, the browser voice is used)
- Keep these files in the same folder as `index.html` and the `assets/` folder
- `assets/logo.png` and `assets/banner.png` are the logo and banner; product pictures go in `assets/products/` (1.png to 12.png)

## Event-driven features
| Event | Where | What happens |
|---|---|---|
| `input` | search box | catalog filters live as you type |
| `change` | category dropdown | catalog filters by category |
| `click` | Add to cart, +, -, remove | cart and live total update |
| `click` | Place order | validates cart, confirms, clears cart |
| `input` | feedback message | live character counter |
| `submit` | feedback form | validates, saves, updates the list |

## Run locally
`python -m http.server` in this folder, then open http://localhost:8000
(Opening the files by double-click may block PyScript; GitHub Pages also works.)

## Group
Taborada, John Richard · Cabanada, Ysiah · Navidad, Tirsnavs · Pulgo, Michael · Arcenal, Kianzel

## Run locally
Double-click `run.bat` (Windows) or run `python -m http.server` here and open http://localhost:8000. Opening the HTML files directly will NOT work with PyScript. GitHub Pages also works.
