from datetime import date
from flask import Flask, render_template_string, request

app = Flask(__name__)

SERVICES = [
    ("Computer Repair", "Slow computer, errors, crashes, and virus removal", "💻"),
    ("Wi-Fi & Networking", "Wi-Fi setup, connectivity issues, and troubleshooting", "📶"),
    ("Printer Setup", "Installation, wireless setup, and printing issues", "🖨️"),
    ("Microsoft 365 & Email", "Outlook, account setup, and email troubleshooting", "✉️"),
    ("Data Transfer & Backup", "Transfer files, create backups, and recover data", "☁️"),
    ("Smart Devices", "Smart TVs, streaming devices, cameras, and more", "🏠"),
]

PAGE = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PC Solutions NYC | On-Site Computer & IT Support</title>
  <meta name="description" content="Book reliable on-site computer and IT support in New York City.">
  <style>
    :root{--navy:#071a3a;--blue:#0d5bd7;--sky:#eef5ff;--ink:#15233b;--muted:#657189;--line:#dbe5f2;--white:#fff;--green:#11845b}
    *{box-sizing:border-box} body{margin:0;font-family:Inter,Segoe UI,Arial,sans-serif;color:var(--ink);background:#f6f9fd}
    a{text-decoration:none;color:inherit}.nav{height:72px;background:var(--navy);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 max(5vw,24px);position:sticky;top:0;z-index:5}
    .brand{font-weight:800;letter-spacing:.04em}.brand span{color:#67a7ff}.nav a.btn{background:#fff;color:var(--navy);padding:12px 18px;border-radius:10px;font-weight:700}
    .hero{background:linear-gradient(135deg,#071a3a 0%,#0b3676 62%,#0d5bd7 100%);color:#fff;padding:70px max(5vw,24px) 82px}
    .hero-inner{max-width:1120px;margin:auto;display:grid;grid-template-columns:1.15fr .85fr;gap:48px;align-items:center}
    .eyebrow{font-size:.8rem;font-weight:800;letter-spacing:.15em;text-transform:uppercase;color:#9bc5ff}.hero h1{font-size:clamp(2.4rem,6vw,4.8rem);line-height:1.02;margin:14px 0 20px;max-width:760px}
    .hero p{font-size:1.15rem;line-height:1.7;color:#d9e8ff;max-width:650px}.actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
    .btn-primary,.btn-secondary{display:inline-block;padding:14px 20px;border-radius:10px;font-weight:800;border:1px solid transparent}.btn-primary{background:#fff;color:var(--blue)}.btn-secondary{border-color:#8dbbff;color:#fff}
    .trust-card{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.25);border-radius:22px;padding:28px;backdrop-filter:blur(8px)}
    .trust-row{display:flex;gap:14px;align-items:flex-start;padding:14px 0;border-bottom:1px solid rgba(255,255,255,.14)}.trust-row:last-child{border:0}.trust-row b{display:block;margin-bottom:4px}.trust-row small{color:#d9e8ff}
    main{max-width:1120px;margin:auto;padding:64px max(5vw,24px)}.section-head{max-width:650px;margin-bottom:28px}.section-head h2{font-size:2rem;margin:0 0 10px}.section-head p{color:var(--muted);line-height:1.6}
    .services{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.service{background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px;box-shadow:0 8px 24px rgba(22,52,91,.06)}
    .service .icon{font-size:1.75rem}.service h3{margin:14px 0 8px}.service p{color:var(--muted);line-height:1.5;margin:0}
    .booking{margin-top:64px;background:#fff;border:1px solid var(--line);border-radius:22px;overflow:hidden;display:grid;grid-template-columns:.72fr 1.28fr;box-shadow:0 16px 40px rgba(22,52,91,.1)}
    .booking-copy{padding:38px;background:var(--navy);color:#fff}.booking-copy h2{font-size:2rem;margin-top:0}.booking-copy p{color:#d9e8ff;line-height:1.65}.check{margin:22px 0;display:flex;gap:10px}.check i{font-style:normal;color:#73b1ff}
    form{padding:38px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}.field{display:flex;flex-direction:column;gap:7px}.field.full{grid-column:1/-1}label{font-weight:700;font-size:.92rem}
    input,select,textarea{width:100%;font:inherit;border:1px solid #bdcadb;border-radius:9px;padding:12px;background:#fff;color:var(--ink)}textarea{min-height:110px;resize:vertical}input:focus,select:focus,textarea:focus{outline:3px solid #d8e8ff;border-color:var(--blue)}
    button{border:0;background:var(--blue);color:#fff;padding:14px 22px;border-radius:10px;font:inherit;font-weight:800;cursor:pointer}.note{color:var(--muted);font-size:.86rem;margin-top:12px;line-height:1.5}
    .success{max-width:680px;margin:80px auto;padding:40px;background:#fff;border:1px solid var(--line);border-radius:22px;text-align:center;box-shadow:0 16px 40px rgba(22,52,91,.1)}.success .mark{width:70px;height:70px;border-radius:50%;background:#e7f8f1;color:var(--green);display:grid;place-items:center;font-size:2rem;margin:auto}.success h1{margin:20px 0 8px}.summary{text-align:left;background:#f5f8fc;border-radius:14px;padding:20px;margin:26px 0}.summary p{margin:9px 0}.back{color:var(--blue);font-weight:800}
    footer{background:#06152e;color:#b9cbe3;padding:28px max(5vw,24px);text-align:center;font-size:.9rem}
    @media(max-width:820px){.hero-inner,.booking{grid-template-columns:1fr}.hero{padding-top:48px}.trust-card{display:none}.services{grid-template-columns:1fr 1fr}.booking-copy,form{padding:26px}}
    @media(max-width:560px){.nav{height:64px}.nav a.btn{padding:9px 12px}.services,.grid{grid-template-columns:1fr}.hero h1{font-size:2.55rem}.field.full{grid-column:auto}main{padding-top:44px}}
  </style>
</head>
<body>
{% if confirmation %}
  <main><section class="success"><div class="mark">✓</div><h1>Request received</h1><p>Thank you, {{ confirmation.name }}. PC Solutions NYC will contact you to confirm availability.</p><div class="summary"><p><b>Service:</b> {{ confirmation.service }}</p><p><b>Preferred date:</b> {{ confirmation.date }}</p><p><b>Preferred time:</b> {{ confirmation.time }}</p><p><b>Service area:</b> {{ confirmation.area }}</p></div><a class="back" href="/">← Return to home</a></section></main>
{% else %}
  <nav class="nav"><div class="brand">PC <span>SOLUTIONS</span> NYC</div><a class="btn" href="#book">Book service</a></nav>
  <header class="hero"><div class="hero-inner"><div><div class="eyebrow">On-site computer & IT support</div><h1>Tech help that comes to you.</h1><p>Reliable computer, Wi-Fi, printer, email, and smart-device support for homes and small businesses across New York City.</p><div class="actions"><a class="btn-primary" href="#book">Request an appointment</a><a class="btn-secondary" href="#services">View services</a></div></div><aside class="trust-card"><div class="trust-row"><span>🛡️</span><div><b>Trusted local support</b><small>Clear explanations and professional service.</small></div></div><div class="trust-row"><span>📍</span><div><b>On-site in NYC</b><small>Help at your home or small business.</small></div></div><div class="trust-row"><span>🗓️</span><div><b>Simple scheduling</b><small>Choose the service, date, and time you prefer.</small></div></div></aside></div></header>
  <main><section id="services"><div class="section-head"><h2>How can we help?</h2><p>Choose the service that best matches your needs. If you are unsure, describe the problem in the appointment form.</p></div><div class="services">{% for title, desc, icon in services %}<article class="service"><div class="icon">{{ icon }}</div><h3>{{ title }}</h3><p>{{ desc }}</p></article>{% endfor %}</div></section>
  <section class="booking" id="book"><div class="booking-copy"><h2>Request an appointment</h2><p>Tell us what you need and when you are available. We will contact you to confirm the appointment and estimated price.</p><div class="check"><i>✓</i><span>No payment required to request service</span></div><div class="check"><i>✓</i><span>Your information is used only for this request</span></div></div>
  <form method="post" action="https://formsubmit.co/pcsolutionsnyc@outlook.com"><div class="grid"><div class="field"><label for="name">Full name</label><input id="name" name="name" autocomplete="name" required></div><div class="field"><label for="contact">Phone or email</label><input id="contact" name="contact" required></div><div class="field full"><label for="service">Service needed</label><select id="service" name="service" required><option value="">Choose a service</option>{% for title, desc, icon in services %}<option>{{ title }}</option>{% endfor %}<option>Other / Request a quote</option></select></div><div class="field"><label for="date">Preferred date</label><input id="date" name="date" type="date" min="{{ today }}" required></div><div class="field"><label for="time">Preferred time</label><select id="time" name="time" required><option value="">Choose a time</option><option>9:00 AM</option><option>10:00 AM</option><option>12:00 PM</option><option>2:00 PM</option><option>4:00 PM</option><option>6:00 PM</option></select></div><div class="field full"><label for="area">NYC borough or neighborhood</label><input id="area" name="area" placeholder="Example: Washington Heights, Manhattan" required></div><div class="field full"><label for="issue">Describe the problem</label><textarea id="issue" name="issue" placeholder="Tell us what is happening and which device needs help." required></textarea></div><div class="field full"><button type="submit">Send appointment request</button><p class="note">This first version confirms the request on screen. Direct email notifications and online payments will be added in a later version.</p></div></div></form></section></main>
  <footer>© {{ year }} PC Solutions NYC · Professional on-site computer and IT support</footer>
{% endif %}
</body></html>'''


@app.get("/")
def home():
    return render_template_string(PAGE, services=SERVICES, today=date.today().isoformat(), year=date.today().year)


@app.post("/book")
def book():
    confirmation = {
        "name": request.form.get("name", "Customer"),
        "service": request.form.get("service", "IT Support"),
        "date": request.form.get("date", "To be confirmed"),
        "time": request.form.get("time", "To be confirmed"),
        "area": request.form.get("area", "New York City"),
    }
    return render_template_string(PAGE, confirmation=confirmation, year=date.today().year)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
