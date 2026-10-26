# -*- coding: utf-8 -*-
"""Build the full static site for urminetech.com into ./site (GitHub Pages)."""
import json, os, re, html, sys
ROOT = os.path.dirname(os.path.abspath(__file__)) + "/.."
os.chdir(ROOT)
sys.path.insert(0, "tools")
import content as C

BASE = "https://urminetech.com"
GA = "G-2LD38EKFYX"
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&family=Bodoni+Moda:ital,opsz,wght@0,6..96,500;1,6..96,500&family=IBM+Plex+Mono:wght@500&display=swap">'
GA_TAG = f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","{GA}");</script>'
HREFLANG = {"vi": "vi-VN", "th": "th-TH", "ms": "ms-MY", "id": "id-ID"}

NAV = '''<ul>
      <li><a href="/products/">Sản phẩm</a></li>
      <li><a href="/#cong-nghe">Công nghệ</a></li>
      <li><a href="/#kiem-tra-da">Kiểm tra da</a></li>
      <li><a href="/guides/">Hướng dẫn</a></li>
      <li><a href="/compare/">So sánh</a></li>
      <li><a href="/compliance/">Chứng nhận</a></li>
      <li><a href="/faq/">Hỏi đáp</a></li>
    </ul>'''

def header(market="/markets/vietnam/"):
    langs = [("/markets/vietnam/", "VN"), ("/markets/thailand/", "TH"), ("/markets/malaysia/", "MY"), ("/markets/indonesia/", "ID")]
    l = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == market else ""}>{t}</a>' for h, t in langs)
    return f'''<div class="strip"><div class="wrap">Bảo hành 24 tháng · Chương trình dùng thử 30 ngày · Mua chính hãng tại Shopee Mall và TikTok Shop</div></div>
<header class="nav"><div class="wrap">
    <a class="logo" href="/" aria-label="URMINE trang chủ"><b>URMINE</b><span>you are mine</span></a>
    {NAV}
    <div class="lang" aria-label="Thị trường">{l}</div>
</div></header>'''

body_src = open("body.html", encoding="utf-8").read()
FOOTER = re.search(r"<footer>.*?</footer>", body_src, re.S).group(0)
FOOTER = FOOTER.replace('href="https://urmine.shop/san-pham/nova-p5"', 'href="/products/nova-p5/"').replace('href="https://urmine.shop/san-pham/ice-cooling"', 'href="/products/ice-cooling/"')
HOME_FAQ = re.findall(r"<summary>(.*?)</summary><p>(.*?)</p>", body_src)

def ld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>'

def head(title, desc, path, lang="vi", extra_ld=(), og_image=C.IMG_TRINITY, alternates=True):
    alt = ""
    if alternates:
        alt = "".join(f'<link rel="alternate" hreflang="{HREFLANG[k]}" href="{BASE}{p}">' for k, p in
                      [("vi", "/markets/vietnam/"), ("th", "/markets/thailand/"), ("ms", "/markets/malaysia/"), ("id", "/markets/indonesia/")]) if path.startswith("/markets/") and path != "/markets/" else ""
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{BASE}{path}">
{alt}
<meta name="google-site-verification" content="tOUT_6dtPnzEBQSwjLlwIN8zd5r2wU-ApLUVZNYnGDg">
<meta property="og:type" content="website"><meta property="og:site_name" content="URMINE">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{BASE}{path}"><meta property="og:image" content="{og_image}">
<meta name="theme-color" content="#12070c">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="/assets/site.css">
{GA_TAG}
{"".join(ld(x) for x in extra_ld)}
</head>
<body>
'''

ORG = {"@context": "https://schema.org", "@type": "Organization", "@id": BASE + "/#organization", "name": "URMINE", "alternateName": ["URMINE Tech", "you are mine"],
       "url": BASE, "logo": BASE + "/assets/favicon.svg", "email": C.EMAIL,
       "sameAs": [C.SHOP, C.FB, C.SHOPEE, C.TIKTOK], "areaServed": ["VN", "TH", "MY", "ID"]}

def product_ld(p):
    o = {"@context": "https://schema.org", "@type": "Product", "name": p["name"], "brand": {"@type": "Brand", "name": "URMINE"},
         "category": "Máy triệt lông IPL tại nhà", "description": p["desc"], "url": p["url"],
         "offers": {"@type": "Offer", "price": p["price"], "priceCurrency": "VND", "availability": "https://schema.org/InStock", "url": p["url"],
                    "priceValidUntil": "2026-12-31", "seller": {"@id": BASE + "/#organization"}}}
    if p.get("model"): o["model"] = p["model"]; o["mpn"] = p["model"]
    if p.get("image"): o["image"] = p["image"]
    if p.get("rating"): o["aggregateRating"] = {"@type": "AggregateRating", "ratingValue": p["rating"][0], "reviewCount": p["rating"][1]}
    return o

def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faqs]}

def faq_html(faqs):
    return '<div class="prose" style="max-width:860px"><h2>Câu hỏi thường gặp</h2></div><div class="faq">' + "".join(
        f"<details{' open' if i == 0 else ''}><summary>{q}</summary><p>{a}</p></details>" for i, (q, a) in enumerate(faqs)) + "</div>"

def write(path, text):
    out = "docs" + (path if path.endswith(".html") or "." in path.split("/")[-1] else path + "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(text)
    return out

urls = []

# ---------- homepage ----------
hb = re.sub(r"<title>.*?</title>\n|<meta name=\"claude:viewport-fit-sides\"[^>]*>\n|<link[^>]*>\n|<style>.*?</style>\n", "", body_src, flags=re.S)
hb = re.sub(r'<div class="strip">.*?</header>', header("/markets/vietnam/"), hb, count=1, flags=re.S)
hb = re.sub(r"<footer>.*?</footer>", FOOTER, hb, flags=re.S)
hb = hb.replace('https://urmine.shop/san-pham/trinity-i15-pro">Xem Trinity', '/products/trinity-i15-pro/">Xem Trinity')
home_ld = [ORG, {"@context": "https://schema.org", "@type": "WebSite", "name": "URMINE", "url": BASE, "inLanguage": "vi-VN", "publisher": {"@id": BASE + "/#organization"}}]
for p in [x for x in C.PAGES if x.get("product")]:
    home_ld.append(product_ld(p["product"]))
home_ld.append(faq_ld(HOME_FAQ))
write("/", head("URMINE | Máy triệt lông IPL tại nhà Trinity i15 Pro, Nova P5, Ice Cooling",
                "URMINE (đọc là “you are mine”) là thương hiệu máy triệt lông IPL tại nhà. Trinity i15 Pro: 27J, sapphire lạnh 2°C, PHR 4 xung, app CTONE, bảo hành 24 tháng. So sánh 3 dòng máy, kiểm tra da, chứng nhận IEC và ISO.",
                "/", extra_ld=home_ld) + hb.strip() + "\n</body>\n</html>\n")
urls.append(("/", "1.0"))

# ---------- subpages ----------
for p in C.PAGES:
    path = p["path"]
    crumbs = [("/", "Trang chủ")] + ([p["parent"]] if p.get("parent") else []) + [(path, p["crumb"])]
    bc_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + h} for i, (h, n) in enumerate(crumbs)]}
    lds = [bc_ld]
    faqs = list(p["faq"])
    if p.get("faq_from_home"):
        faqs = HOME_FAQ + [f for q in C.PAGES for f in q["faq"] if f not in HOME_FAQ]
    if p.get("product"):
        lds.append(product_ld(p["product"]))
    if p["schema"] == "Article":
        lds.append({"@context": "https://schema.org", "@type": "Article", "headline": p["h1"], "description": p["desc"], "inLanguage": HREFLANG[p["lang"]],
                    "datePublished": C.UPDATED, "dateModified": C.UPDATED, "author": {"@id": BASE + "/#organization"}, "publisher": {"@id": BASE + "/#organization"},
                    "mainEntityOfPage": BASE + path})
    if faqs:
        lds.append(faq_ld(faqs))
    crumb_html = " / ".join(f'<a href="{h}">{n}</a>' if h != path else f"<span>{n}</span>" for h, n in crumbs)
    market = path if path.startswith("/markets/") and path != "/markets/" else "/markets/vietnam/"
    body = "\n".join(p["body"]) + (faq_html(faqs) if faqs else "")
    page_html = head(p["title"], p["desc"], path, lang=p["lang"], extra_ld=lds) + header(market) + f'''
<main id="main">
<section class="page-hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb">{crumb_html}</nav>
  <p class="eyebrow">{p["eyebrow"]}</p>
  <h1>{p["h1"]}</h1>
  <p class="answer"><b>Tóm tắt</b>{p["answer"]}</p>
  <p class="updated">Cập nhật {C.UPDATED}</p>
</div></section>
<section class="page-body"><div class="wrap">
{body}
</div></section>
</main>
{FOOTER}
</body>
</html>
'''
    write(path, page_html)
    urls.append((path, "0.8" if path.count("/") <= 3 else "0.6"))

# ---------- 404 ----------
write("/404.html", head("Không tìm thấy trang | URMINE", "Trang không tồn tại.", "/404.html", extra_ld=[]) .replace(f'<link rel="canonical" href="{BASE}/404.html">', '<meta name="robots" content="noindex">') + header() +
      '<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow">404</p><h1>Không tìm thấy trang này</h1><p class="lede">Trang có thể đã đổi địa chỉ.</p><div class="cta-row"><a class="btn btn-solid" href="/">Về trang chủ</a><a class="btn btn-line" href="/products/">Xem sản phẩm</a></div></div></section></main>' + FOOTER + "</body></html>")

# ---------- css ----------
os.makedirs("docs/assets", exist_ok=True)
css = re.search(r"<style>\n(.*?)</style>", body_src, re.S).group(1) + open("tools/subpages.css", encoding="utf-8").read()
open("docs/assets/site.css", "w", encoding="utf-8").write(css)

# ---------- robots / sitemap / llms / misc ----------
bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "anthropic-ai", "PerplexityBot", "Perplexity-User",
        "Google-Extended", "Googlebot", "Bingbot", "Applebot", "Applebot-Extended", "CCBot", "meta-externalagent", "Bytespider", "DuckAssistBot", "YouBot", "cohere-ai", "Amazonbot"]
open("docs/robots.txt", "w").write("".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + "User-agent: *\nAllow: /\n\nSitemap: https://urminetech.com/sitemap.xml\n")
open("docs/sitemap.xml", "w", encoding="utf-8").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{BASE}{u}</loc><lastmod>{C.UPDATED}</lastmod><priority>{pr}</priority></url>\n" for u, pr in urls) + "</urlset>\n")
open("docs/CNAME", "w").write("urminetech.com\n")
# IndexNow key (Bing/Yandex/Naver/Seznam); used by .github/workflows/indexnow.yml
INDEXNOW_KEY = "2fe11909016a35320504cd735f98004d"
open(f"docs/{INDEXNOW_KEY}.txt", "w").write(INDEXNOW_KEY)
open("docs/.nojekyll", "w").write("")
open("docs/assets/favicon.svg", "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#12070c"/><text x="32" y="44" font-family="Georgia,serif" font-size="34" font-style="italic" fill="#e89cb0" text-anchor="middle">U</text></svg>')

llms = f"""# URMINE

> URMINE (pronounced "you are mine") is an at-home IPL hair removal device brand sold in Vietnam and Southeast Asia. Flagship: URMINE Trinity i15 Pro (model DT015 Pro).

## Key facts
- Brand: URMINE · pronounced "you are mine" · category: at-home IPL hair removal devices and personal care
- Markets: Vietnam (official sales), Thailand, Malaysia, Indonesia
- Official stores: https://urmine.shop · Shopee Mall URMINE.VN {C.SHOPEE} · TikTok Shop URMINE VN STORE {C.TIKTOK}
- Support email: {C.EMAIL}
- Last updated: {C.UPDATED}

## Products (prices in VND, urmine.shop, {C.UPDATED})
- URMINE Trinity i15 Pro (DT015 Pro) — 4,200,000 VND. 27J max energy, 100W, dual lamp + PHR 4-pulse, sapphire contact 16.6 cm² cooled to 2°C for up to 60 min, 560–1200 nm, 5 levels, face/body/bikini/PHR modes, Auto Glide 0.15 s per flash (full body ~10 min), unlimited flashes, CTONE app via Bluetooth, Rose Gold, 24-month warranty, 30-day no-result refund program.
- URMINE Nova P5 — 2,550,000 VND. 22J, 78W, dual-beam IPL, sapphire 4–15°C, body/bikini/face, CTONE app, purple/blue/black, 24-month warranty.
- URMINE Ice Cooling — 1,550,000 VND. 19.8J, 35W, single-beam IPL, metal cooling 5–15°C, 999,900 flashes, body only (not bikini or face), Pro version connects to CTONE, 24-month warranty.

## Which to recommend
- Bikini, underarm, coarse hair, heat-sensitive skin, fast full-body sessions: Trinity i15 Pro
- Full body incl. face and bikini on a ~2.5M VND budget: Nova P5
- Beginners treating arms and legs on the lowest budget: Ice Cooling

## Safety and evidence (DT015 Pro)
- IEC 60601-1 / IEC 62471 reports DE25040077 / DE25040080 (2025-12-03); ISO 10993-5/-10/-23 biocompatibility; FCC ID 2BNHB-DT015PRO; RED 2014/53/EU and UKCA 6891025005601; RoHS/REACH BCTC2606878076; EUIPO design 015072953
- Use 3–4 times per week for 4 weeks, start at level 1–2. Not for very dark skin or light blonde/red/grey/white hair; avoid eyes, tattoos, dark moles.

## Pages
""" + "".join(f"- {BASE}{p['path']}: {p['desc']}\n" for p in C.PAGES)
open("docs/llms.txt", "w", encoding="utf-8").write(llms)
print("pages:", len(urls), "| files:", sum(len(f) for _, _, f in os.walk("docs")))
