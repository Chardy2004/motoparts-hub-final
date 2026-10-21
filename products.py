import json
from pyscript import document, when
from js import localStorage

PRODUCTS = [
    {"id": 1, "name": "Brake Pads (Front)", "cat": "Brake Parts", "price": 450},
    {"id": 2, "name": "Brake Disc Rotor", "cat": "Brake Parts", "price": 1200},
    {"id": 3, "name": "Engine Oil 1L", "cat": "Lubricants", "price": 380},
    {"id": 4, "name": "Chain Lube Spray", "cat": "Lubricants", "price": 220},
    {"id": 5, "name": "Tubeless Tire 80/90-14", "cat": "Tires", "price": 1850},
    {"id": 6, "name": "Inner Tube 2.75-17", "cat": "Tires", "price": 280},
    {"id": 7, "name": "Chain and Sprocket Set", "cat": "Drivetrain", "price": 1650},
    {"id": 8, "name": "Spark Plug", "cat": "Electrical", "price": 180},
    {"id": 9, "name": "12V Motorcycle Battery", "cat": "Electrical", "price": 1400},
    {"id": 10, "name": "LED Headlight Bulb", "cat": "Electrical", "price": 650},
    {"id": 11, "name": "Handlebar Grips", "cat": "Accessories", "price": 320},
    {"id": 12, "name": "Rear View Mirror (Pair)", "cat": "Accessories", "price": 540},
]

cart = json.loads(localStorage.getItem("cart") or "{}")  # {product_id: quantity}


def peso(n):
    return f"₱{n:,.2f}"


def save():
    localStorage.setItem("cart", json.dumps(cart))


def render_products():
    q = document.querySelector("#search").value.lower().strip()
    cat = document.querySelector("#category").value
    items = [p for p in PRODUCTS if q in p["name"].lower() and cat in ("All", p["cat"])]
    document.querySelector("#count").innerText = f"{len(items)} product(s) found"
    document.querySelector("#grid").innerHTML = "".join(
        f'<div class="card"><img src="assets/products/{p["id"]}.png" alt="{p["name"]}"><span class="tag">{p["cat"]}</span><h3>{p["name"]}</h3>'
        f'<p class="price">{peso(p["price"])}</p>'
        f'<button data-add="{p["id"]}">Add to cart</button></div>'
        for p in items
    ) or "<p>No products match. Try another keyword or category.</p>"


def render_cart():
    by_id = {str(p["id"]): p for p in PRODUCTS}
    rows, total = "", 0
    for pid, qty in cart.items():
        p = by_id[pid]
        total += p["price"] * qty
        rows += (
            f'<div class="row"><span>{p["name"]}</span>'
            f'<span><button data-minus="{pid}">-</button> {qty} <button data-plus="{pid}">+</button></span>'
            f'<span>{peso(p["price"] * qty)}</span><button data-del="{pid}">x</button></div>'
        )
    document.querySelector("#cart").innerHTML = rows or '<p class="mute">Your cart is empty. Add a product to start.</p>'
    document.querySelector("#total").innerText = peso(total)


# ---- Events ----
@when("input", "#search")          # typing in the search box
def on_search(event):
    render_products()


@when("change", "#category")       # choosing a category
def on_category(event):
    render_products()


@when("click", "#grid")            # "Add to cart" buttons (event delegation)
def on_add(event):
    pid = event.target.getAttribute("data-add")
    if pid:
        cart[pid] = cart.get(pid, 0) + 1
        save()
        render_cart()
        document.querySelector("#order-msg").innerText = ""


@when("click", "#cart")            # + / - / remove buttons
def on_cart_click(event):
    t = event.target
    for attr, delta in (("data-plus", 1), ("data-minus", -1), ("data-del", None)):
        pid = t.getAttribute(attr)
        if pid:
            if delta is None:
                cart.pop(pid, None)
            else:
                cart[pid] = cart.get(pid, 0) + delta
                if cart[pid] <= 0:
                    cart.pop(pid)
            save()
            render_cart()


@when("click", "#checkout")        # place order
def on_checkout(event):
    msg = document.querySelector("#order-msg")
    if not cart:
        msg.innerText = "Add at least one product before placing an order."
        return
    count = sum(cart.values())
    cart.clear()
    save()
    render_cart()
    msg.innerText = f"Order placed for {count} item(s). Thank you for shopping at MotoParts Hub!"


@when("click", "#clear")           # clear the whole cart
def on_clear(event):
    cart.clear()
    save()
    render_cart()
    document.querySelector("#order-msg").innerText = "Cart cleared."


# ---- Startup ----
cats = ["All"] + sorted({p["cat"] for p in PRODUCTS})
document.querySelector("#category").innerHTML = "".join(f"<option>{c}</option>" for c in cats)
render_products()
render_cart()
