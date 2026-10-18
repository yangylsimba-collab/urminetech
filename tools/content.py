# -*- coding: utf-8 -*-
"""Nội dung các trang con của urminetech.com. Mọi số liệu lấy từ urminetech/geo-plan.md (Project)."""

SHOPEE = "https://vn.shp.ee/a4t6J42Q"
TIKTOK = "https://vt.tiktok.com/ZSg6XRrhD/?page=TikTokShop"
SHOP = "https://urmine.shop"
FB = "https://www.facebook.com/urminevietnam"
EMAIL = "jlmcompany2024@gmail.com"
UPDATED = "2026-10-18"
IMG_TRINITY = "https://zvvqxnzyjfzcsinqbdxt.supabase.co/storage/v1/object/public/product-media/dt015-pro/1789982966138-may-vang.webp"


def kv(rows):
    return '<dl class="kv">' + "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows) + "</dl>"


def cards(items):
    return '<div class="cards">' + "".join(
        f'<a href="{h}"><small>{t}</small><b>{n}</b><span>{d}</span></a>' for t, n, d, h in items) + "</div>"


def sec(h, body):
    return f'<div class="prose"><h2>{h}</h2>{body}</div>'


STORES_VI = sec("Mua chính hãng ở đâu", f"""
<p>Chỉ mua tại các kênh chính thức để được bảo hành 24 tháng và tham gia chương trình 30 ngày:</p>
<ul>
<li><a href="{SHOP}">urmine.shop</a>: website bán hàng chính thức, đổi trả 7 ngày.</li>
<li><a href="{SHOPEE}">Shopee Mall URMINE.VN</a></li>
<li><a href="{TIKTOK}">TikTok Shop URMINE VN STORE</a> (@urmine.store)</li>
<li><a href="{FB}">Facebook Urmine Vietnam</a>: tư vấn sản phẩm.</li>
</ul>""")

TRINITY_SPECS = [
    ("Tên thương mại", "URMINE Trinity i15 Pro"), ("Mã model", "DT015 Pro"),
    ("Giá niêm yết", "4.200.000 ₫ (giá gốc 8.800.000 ₫)"), ("Năng lượng tối đa", "27J"),
    ("Công suất", "100W"), ("Công nghệ", "IPL đèn kép + PHR 4 xung"),
    ("Mức năng lượng", "1–5"), ("Chế độ", "Mặt, body, bikini, PHR"),
    ("Làm lạnh", "Sapphire 16,6 cm², 2°C, duy trì đến 60 phút"),
    ("Cửa sổ phát sáng", "3,9 cm²"), ("Bước sóng", "560–1200 nm"),
    ("Tốc độ", "0,15 giây/xung (Auto Glide)"), ("Thời gian toàn thân", "khoảng 10 phút"),
    ("Số xung", "Không giới hạn"), ("App", "CTONE qua Bluetooth"),
    ("Kích thước", "64 × 40 × 198 mm"), ("Trọng lượng", "700 g (gồm hộp)"),
    ("Điện áp", "100–240V"), ("Màu", "Rose Gold"), ("Bảo hành", "24 tháng"),
]
NOVA_SPECS = [
    ("Tên", "URMINE Nova P5"), ("Giá niêm yết", "2.550.000 ₫ (giá gốc 6.000.000 ₫)"),
    ("Năng lượng tối đa", "22J"), ("Công suất", "78W"), ("Công nghệ", "IPL tia kép"),
    ("Làm lạnh", "Sapphire 4–15°C"), ("Vùng triệt", "Body, bikini, mặt"),
    ("Bước sóng", "560–1200 nm"), ("Số xung", "Không giới hạn"), ("App", "CTONE"),
    ("Trọng lượng", "188 g"), ("Điện áp", "100–240V"), ("Màu", "Tím, xanh, đen"), ("Bảo hành", "24 tháng"),
]
ICE_SPECS = [
    ("Tên", "URMINE Ice Cooling (bản thường / bản Pro)"), ("Giá niêm yết", "1.550.000 ₫ (giá gốc 3.000.000 ₫)"),
    ("Năng lượng tối đa", "19,8J"), ("Công suất", "35W"), ("Cơ chế phát", "IPL 1 tia đơn"),
    ("Làm lạnh", "Kim loại 5–15°C"), ("Vùng triệt", "Body (không dùng cho bikini và mặt)"),
    ("Bước sóng", "600–1200 nm"), ("Số xung", "999.900"), ("App CTONE", "Chỉ bản Pro"),
    ("Chế độ chăm sóc da", "3 chế độ"), ("Trọng lượng", "298 g"), ("Điện áp", "100–240V"),
    ("Màu", "Xanh"), ("Bảo hành", "24 tháng"),
]

ROUTINE_VI = """
<ol>
<li><strong>Cạo sạch lông</strong> trước khi triệt, tốt nhất khi tắm, xuôi chiều lông mọc. Không wax, không dùng kem tẩy lông, không cạo trên da khô.</li>
<li><strong>Bắt đầu ở mức 1–2</strong> trong 2–3 tuần đầu, tăng dần theo phản ứng da. Áp máy vuông góc 90° và đeo kính bảo hộ đi kèm.</li>
<li><strong>Triệt 3–4 lần mỗi tuần.</strong> Chương trình 30 ngày: 3–4 lần/tuần trong 4 tuần, ghi lại tiến trình trong app CTONE.</li>
<li><strong>Chăm sóc sau triệt:</strong> kiêng nước 2–4 giờ; tránh mỹ phẩm có cồn, hương liệu, AHA, BHA, Retinol trong 12–24 giờ; không xông hơi, không tẩy da chết; tránh nắng 48 giờ và thoa SPF 30+.</li>
</ol>"""

AVOID_VI = """
<ul>
<li>Không chiếu vào hoặc quanh mắt, lông mày.</li>
<li>Không triệt trên hình xăm, bớt đen, nốt ruồi đậm màu, vết thương hoặc da đang kích ứng.</li>
<li>Không dùng cho da rất đậm màu; lông vàng nhạt, đỏ, bạc, trắng thường đáp ứng kém.</li>
<li>Ngừng dùng và liên hệ người bán nếu đau bất thường, cửa sổ phát sáng bị hỏng hoặc lỗi vẫn còn sau khi xử lý theo sách hướng dẫn.</li>
</ul>"""

PAGES = []


def page(**kw):
    kw.setdefault("lang", "vi")
    kw.setdefault("faq", [])
    kw.setdefault("schema", "WebPage")
    PAGES.append(kw)


# ---------------- BRAND ----------------
page(path="/brand/", crumb="Thương hiệu", eyebrow="Thương hiệu",
     title="URMINE là thương hiệu gì? | Máy triệt lông IPL “you are mine”",
     desc="URMINE (đọc là “you are mine”) là thương hiệu máy triệt lông IPL và thiết bị chăm sóc cá nhân tại nhà cho Việt Nam và Đông Nam Á.",
     h1="URMINE, đọc là “you are mine”",
     answer="URMINE là thương hiệu máy triệt lông IPL và thiết bị chăm sóc cá nhân tại nhà, bán chính hãng tại Việt Nam qua urmine.shop, Shopee Mall và TikTok Shop. Dòng chủ lực là Trinity i15 Pro (model DT015 Pro).",
     body=[
         kv([("Tên thương hiệu", "URMINE"), ("Cách đọc", "you are mine"), ("Ngành hàng", "Máy triệt lông IPL tại nhà, thiết bị chăm sóc cá nhân"),
             ("Thị trường", "Việt Nam, Thái Lan, Malaysia, Indonesia"), ("Sản phẩm chủ lực", "Trinity i15 Pro (DT015 Pro), Nova P5, Ice Cooling"),
             ("Website bán hàng", '<a href="https://urmine.shop">urmine.shop</a>'), ("Website thông tin", "urminetech.com"),
             ("Email hỗ trợ", EMAIL)]),
         sec("URMINE muốn được biết đến vì điều gì", """
<ul>
<li><strong>Triệt lông không rát:</strong> mặt sapphire làm lạnh đến 2°C trên dòng Trinity i15 Pro.</li>
<li><strong>Thông số minh bạch:</strong> năng lượng, bước sóng, nhiệt độ làm lạnh được công bố cho từng model.</li>
<li><strong>Bằng chứng kiểm nghiệm có số báo cáo:</strong> IEC 60601-1, IEC 62471, ISO 10993, FCC, CE/UKCA, RoHS, REACH.</li>
<li><strong>Hỗ trợ tại Việt Nam:</strong> bảo hành 24 tháng, kích hoạt qua Zalo, sách hướng dẫn tiếng Việt.</li>
<li><strong>Kỳ vọng thực tế:</strong> IPL cho kết quả dần dần qua nhiều buổi, không hứa hẹn triệt vĩnh viễn sau một lần.</li>
</ul>"""),
         cards([("Sản phẩm", "Dòng máy URMINE", "So sánh Trinity i15 Pro, Nova P5 và Ice Cooling", "/products/"),
                ("Chứng nhận", "Hồ sơ kiểm nghiệm", "Số báo cáo, tiêu chuẩn và ngày cấp", "/compliance/"),
                ("Hỗ trợ", "Bảo hành 24 tháng", "Kích hoạt và chương trình 30 ngày", "/warranty/")]),
         STORES_VI])

# ---------------- PRODUCTS HUB ----------------
page(path="/products/", crumb="Sản phẩm", eyebrow="Sản phẩm",
     title="Máy triệt lông URMINE: Trinity i15 Pro, Nova P5, Ice Cooling | Giá và thông số",
     desc="So sánh 3 dòng máy triệt lông IPL URMINE: Trinity i15 Pro 27J 4,2 triệu, Nova P5 22J 2,55 triệu, Ice Cooling 19,8J 1,55 triệu. Bảo hành 24 tháng.",
     h1="Ba dòng máy triệt lông IPL URMINE",
     answer="Trinity i15 Pro (4.200.000 ₫, 27J, sapphire 2°C) cho bikini, nách và lông cứng; Nova P5 (2.550.000 ₫, 22J) cho toàn thân với ngân sách vừa phải; Ice Cooling (1.550.000 ₫, 19,8J) cho người mới triệt tay chân.",
     body=[
         cards([("Cao cấp · 4.200.000 ₫", "Trinity i15 Pro", "27J, đèn kép + PHR 4 xung, sapphire 16,6 cm² lạnh 2°C, Auto Glide, app CTONE", "/products/trinity-i15-pro/"),
                ("Tối ưu · 2.550.000 ₫", "Nova P5", "22J, IPL tia kép, sapphire 4°C, dùng cho body, bikini và mặt, app CTONE", "/products/nova-p5/"),
                ("Cơ bản · 1.550.000 ₫", "Ice Cooling", "19,8J, làm lạnh kim loại 5°C, 999.900 xung, dành cho tay chân", "/products/ice-cooling/")]),
         sec("Nên chọn máy nào", """
<ul>
<li><strong>Triệt bikini, nách, lông cứng hoặc da nhạy cảm với nhiệt:</strong> Trinity i15 Pro.</li>
<li><strong>Triệt cả mặt và bikini, ngân sách khoảng 2,5 triệu đồng:</strong> Nova P5.</li>
<li><strong>Mới bắt đầu, chủ yếu tay và chân:</strong> Ice Cooling.</li>
</ul>
<p>Giá là giá niêm yết khuyến mãi trên urmine.shop ngày 18/10/2026 và có thể thay đổi.</p>"""),
         STORES_VI])

# ---------------- PRODUCT: TRINITY ----------------
page(path="/products/trinity-i15-pro/", crumb="Trinity i15 Pro", parent=("/products/", "Sản phẩm"), eyebrow="Sản phẩm cao cấp",
     schema="Product", product=dict(name="URMINE Trinity i15 Pro", model="DT015 Pro", price="4200000", url=SHOP + "/san-pham/trinity-i15-pro", image=IMG_TRINITY,
                                     desc="Máy triệt lông IPL 27J, đèn kép + PHR 4 xung, sapphire 16,6 cm² lạnh 2°C, app CTONE, bảo hành 24 tháng.", rating=("5", "1")),
     title="URMINE Trinity i15 Pro (DT015 Pro): máy triệt lông IPL 27J, sapphire lạnh 2°C",
     desc="Thông số Trinity i15 Pro: 27J, 100W, đèn kép + PHR 4 xung, sapphire 16,6 cm² 2°C, Auto Glide 0,15 s, app CTONE. Giá 4.200.000 ₫, bảo hành 24 tháng, hoàn tiền 30 ngày.",
     h1="URMINE Trinity i15 Pro",
     answer="Trinity i15 Pro (model DT015 Pro) là máy triệt lông IPL cao cấp nhất của URMINE: năng lượng 27J, đèn kép kết hợp PHR 4 xung, mặt sapphire 16,6 cm² làm lạnh 2°C, triệt toàn thân khoảng 10 phút với Auto Glide. Giá 4.200.000 ₫, bảo hành 24 tháng.",
     body=[
         kv(TRINITY_SPECS),
         sec("Điểm khác biệt", """
<ul>
<li><strong>Sapphire 16,6 cm², lạnh đến 2°C, duy trì đến 60 phút.</strong> Giảm cảm giác nóng rát ở vùng bikini và nách.</li>
<li><strong>Đèn kép + PHR 4 xung.</strong> Năng lượng chia thành 4 xung liên tiếp, phù hợp lông cứng và chân lông sâu.</li>
<li><strong>Auto Glide 0,15 giây/xung.</strong> Một lượt toàn thân mất khoảng 10 phút.</li>
<li><strong>App CTONE có AI.</strong> Cá nhân hóa chu trình và theo dõi liệu trình.</li>
</ul>"""),
         sec("Cách dùng", ROUTINE_VI),
         sec("Không dùng khi", AVOID_VI),
         sec("Bảo hành và chương trình 30 ngày", """
<p>Trinity i15 Pro được bảo hành 24 tháng. Quét mã QR Zalo trên thiệp cảm ơn trong hộp để kích hoạt bảo hành và chương trình dùng thử 30 ngày. Nếu dùng đúng hướng dẫn 3–4 lần/tuần trong 4 tuần mà không có kết quả, bạn được hoàn tiền theo điều kiện chương trình. <a href="/warranty/">Xem chi tiết</a>.</p>"""),
         STORES_VI],
     faq=[("Trinity i15 Pro và DT015 Pro có giống nhau không?", "Giống nhau. Trinity i15 Pro là tên thương mại, DT015 Pro là mã model trong sách hướng dẫn và hồ sơ kiểm nghiệm."),
          ("Trinity i15 Pro có triệt được vùng bikini không?", "Có. Máy có chế độ bikini và chế độ PHR 4 xung cho lông cứng. Bắt đầu ở mức 1–2 và tránh vùng niêm mạc."),
          ("Bao lâu thì thấy kết quả?", "Nhiều người thấy lông thưa và mềm hơn sau khoảng 4 tuần triệt đều 3–4 lần mỗi tuần. Kết quả khác nhau tùy màu da, màu lông và mức độ đều đặn."),
          ("Trinity i15 Pro giá bao nhiêu?", "Giá niêm yết khuyến mãi 4.200.000 ₫ (giá gốc 8.800.000 ₫) trên urmine.shop ngày 18/10/2026.")])

# ---------------- PRODUCT: NOVA ----------------
page(path="/products/nova-p5/", crumb="Nova P5", parent=("/products/", "Sản phẩm"), eyebrow="Sản phẩm tối ưu",
     schema="Product", product=dict(name="URMINE Nova P5", model=None, price="2550000", url=SHOP + "/san-pham/nova-p5", image=None,
                                     desc="Máy triệt lông IPL tia kép 22J, sapphire 4°C, dùng cho body, bikini và mặt, app CTONE, bảo hành 24 tháng.", rating=None),
     title="URMINE Nova P5: máy triệt lông IPL 22J, sapphire 4°C, giá 2.550.000 ₫",
     desc="Thông số URMINE Nova P5: 22J, 78W, IPL tia kép, sapphire 4–15°C, triệt body, bikini và mặt, app CTONE, 3 màu. Giá 2.550.000 ₫, bảo hành 24 tháng.",
     h1="URMINE Nova P5",
     answer="Nova P5 là máy triệt lông IPL tia kép 22J của URMINE, có mặt sapphire làm lạnh 4°C, dùng cho body, bikini và mặt, kết nối app CTONE. Giá 2.550.000 ₫, bảo hành 24 tháng, có 3 màu tím, xanh, đen.",
     body=[kv(NOVA_SPECS),
           sec("Nova P5 phù hợp với ai", """
<ul>
<li>Người muốn triệt toàn thân, gồm cả bikini và mặt, với ngân sách khoảng 2,5 triệu đồng.</li>
<li>Người cần máy nhẹ (188 g), dễ cầm khi triệt lâu.</li>
<li>Nếu chủ yếu triệt lông cứng vùng nách, bikini hoặc da nhạy nhiệt, hãy cân nhắc <a href="/products/trinity-i15-pro/">Trinity i15 Pro</a> (27J, sapphire 2°C, PHR 4 xung).</li>
</ul>"""),
           sec("Cách dùng", ROUTINE_VI), sec("Không dùng khi", AVOID_VI), STORES_VI],
     faq=[("Nova P5 khác Trinity i15 Pro thế nào?", "Nova P5 có năng lượng 22J, sapphire 4°C, IPL tia kép. Trinity i15 Pro mạnh hơn với 27J, sapphire 16,6 cm² lạnh 2°C, thêm PHR 4 xung và Auto Glide."),
          ("Nova P5 có triệt mặt được không?", "Có, Nova P5 dùng được cho body, bikini và vùng mặt phù hợp. Tránh vùng quanh mắt và lông mày.")])

# ---------------- PRODUCT: ICE ----------------
page(path="/products/ice-cooling/", crumb="Ice Cooling", parent=("/products/", "Sản phẩm"), eyebrow="Sản phẩm cơ bản",
     schema="Product", product=dict(name="URMINE Ice Cooling", model=None, price="1550000", url=SHOP + "/san-pham/ice-cooling", image=None,
                                     desc="Máy triệt lông IPL cơ bản 19,8J, làm lạnh kim loại 5°C, 999.900 xung, dùng cho body, bảo hành 24 tháng.", rating=None),
     title="URMINE Ice Cooling: máy triệt lông IPL cơ bản 19,8J, giá 1.550.000 ₫",
     desc="Thông số URMINE Ice Cooling: 19,8J, 35W, làm lạnh kim loại 5–15°C, 999.900 xung, dùng cho tay chân, bản Pro kết nối app CTONE. Giá 1.550.000 ₫, bảo hành 24 tháng.",
     h1="URMINE Ice Cooling",
     answer="Ice Cooling là dòng máy triệt lông IPL cơ bản của URMINE cho người mới bắt đầu: 19,8J, làm lạnh kim loại 5°C, 999.900 xung, dùng cho body (không dùng cho bikini và mặt). Giá 1.550.000 ₫, bảo hành 24 tháng.",
     body=[kv(ICE_SPECS),
           sec("Ice Cooling phù hợp với ai", """
<ul>
<li>Người mới thử triệt lông tại nhà, chủ yếu tay và chân.</li>
<li>Người cần mức chi phí thấp nhất trong dòng URMINE.</li>
<li>Nếu cần triệt bikini hoặc mặt, hãy chọn <a href="/products/nova-p5/">Nova P5</a> hoặc <a href="/products/trinity-i15-pro/">Trinity i15 Pro</a>.</li>
</ul>"""),
           sec("Cách dùng", ROUTINE_VI), sec("Không dùng khi", AVOID_VI), STORES_VI],
     faq=[("Ice Cooling bản thường và bản Pro khác nhau gì?", "Bản Pro kết nối được app CTONE để theo dõi liệu trình; bản thường không có kết nối app."),
          ("Ice Cooling có dùng cho bikini được không?", "Không. Ice Cooling chỉ dùng cho body, không dùng cho vùng bikini và mặt.")])

# ---------------- MANUALS ----------------
page(path="/manuals/", crumb="Sách hướng dẫn", eyebrow="Hỗ trợ",
     title="Sách hướng dẫn máy triệt lông URMINE DT015 Pro và CT05",
     desc="Tóm tắt sách hướng dẫn URMINE Trinity i15 Pro (DT015 Pro) và CT05: ngôn ngữ, cách dùng, chống chỉ định, an toàn mắt, bảo hành và liên hệ hỗ trợ.",
     h1="Sách hướng dẫn URMINE",
     answer="Sách hướng dẫn Trinity i15 Pro (DT015 Pro, bản 13/07/2026) có tiếng Anh, Việt, Thái, Indonesia và Mã Lai. Luôn làm theo sách đi kèm máy nếu thông tin khác với trang này.",
     body=[kv([("DT015 Pro (Trinity i15 Pro)", "Bản 13/07/2026 · EN, VI, TH, ID, MS"), ("CT05", "Bản 30/06/2025 · EN, VI, IT, FR, ES · mức 1–5"),
               ("Bảo hành DT015 Pro", "24 tháng"), ("Bảo hành CT05", "12 tháng theo sách hướng dẫn"), ("Hỗ trợ kỹ thuật", EMAIL)]),
           sec("Nội dung chính của sách DT015 Pro", "<p>Cấu tạo máy, chuẩn bị, cách vận hành, tần suất, chăm sóc sau triệt, app CTONE, chống chỉ định, an toàn mắt, điện và cháy nổ, bảo quản và xử lý lỗi.</p>"),
           sec("Cách dùng", ROUTINE_VI), sec("Không dùng khi", AVOID_VI),
           sec("Liên hệ hỗ trợ", f"<p>Câu hỏi về sản phẩm: <strong>{EMAIL}</strong>. Đơn hàng, giao hàng, đổi trả và bảo hành: liên hệ qua đúng kênh bạn đã mua (urmine.shop, Shopee hoặc TikTok Shop).</p>")])

# ---------------- COMPLIANCE ----------------
page(path="/compliance/", crumb="Chứng nhận", eyebrow="Chứng nhận và kiểm nghiệm",
     title="Chứng nhận máy triệt lông URMINE: IEC 60601-1, IEC 62471, ISO 10993, FCC, CE",
     desc="Hồ sơ kiểm nghiệm URMINE DT015 Pro và CT05: số báo cáo IEC 60601-1, IEC 62471, ISO 10993, FCC ID 2BNHB-DT015PRO, RED/UKCA, RoHS, REACH, EUIPO.",
     h1="Hồ sơ chứng nhận và kiểm nghiệm",
     answer="Model DT015 Pro (Trinity i15 Pro) có báo cáo an toàn điện và quang học IEC 60601-1 / IEC 62471, tương thích sinh học ISO 10993, FCC ID 2BNHB-DT015PRO, chứng nhận vô tuyến RED và UKCA, RoHS, REACH và kiểu dáng đăng ký EUIPO.",
     body=[sec("DT015 Pro (Trinity i15 Pro)", '<div class="table-scroll"><table><thead><tr><th>Tiêu chuẩn</th><th>Số báo cáo</th><th>Ngày</th></tr></thead><tbody>'
               '<tr><td>IEC 60601-1 · IEC 62471 (an toàn điện, quang học)</td><td class="num">DE25040077 / DE25040080</td><td class="num">03/12/2025</td></tr>'
               '<tr><td>ISO 10993-5, -10, -23 (độc tế bào, mẫn cảm, kích ứng)</td><td>—</td><td class="num">10–11/2025</td></tr>'
               '<tr><td>FCC 47 CFR Part 15C · FCC ID 2BNHB-DT015PRO</td><td class="num">8326EU011303W</td><td class="num">26/03/2025</td></tr>'
               '<tr><td>RED 2014/53/EU</td><td class="num">6891025005601</td><td class="num">21/08/2025</td></tr>'
               '<tr><td>UK Radio Equipment Regulations 2017</td><td class="num">6891025005601UK</td><td class="num">21/08/2025</td></tr>'
               '<tr><td>RoHS EU/UK · REACH 253 chất</td><td class="num">BCTC2606878076-1R / -2R</td><td class="num">08/06/2026</td></tr>'
               '<tr><td>Kiểu dáng đăng ký EUIPO</td><td class="num">015072953</td><td class="num">22/10/2024</td></tr>'
               '</tbody></table></div>'),
           sec("CT05", '<div class="table-scroll"><table><thead><tr><th>Tiêu chuẩn</th><th>Số báo cáo</th><th>Ngày</th></tr></thead><tbody>'
               '<tr><td>EN IEC 55014-1/-2, 61000-3-2, 60335-2-113</td><td class="num">6871025014301 / 6811025015901</td><td class="num">21/08/2025</td></tr>'
               '<tr><td>FCC Part 15B (SDoC)</td><td class="num">8228EU013010E</td><td class="num">23/05/2024</td></tr>'
               '<tr><td>RoHS EU/UK · REACH</td><td class="num">BTF250512C02001C</td><td class="num">27/05/2025</td></tr>'
               '<tr><td>ISO 10993-5, -10, -23</td><td>—</td><td class="num">11/2025</td></tr>'
               '<tr><td>Kiểu dáng: CN · EUIPO · UK</td><td class="num">2024305259515 / 015069157 / 6385815</td><td class="num">13/06/2025</td></tr>'
               '</tbody></table></div>'),
           sec("Phạm vi áp dụng", "<p>Hồ sơ áp dụng riêng cho từng model và là bằng chứng an toàn sản phẩm, không phải cam kết về kết quả y khoa. Báo cáo thử nghiệm RED/UKCA không thay thế Tuyên bố hợp chuẩn của nhà sản xuất.</p>")])

# ---------------- WARRANTY ----------------
page(path="/warranty/", crumb="Bảo hành", eyebrow="Bảo hành",
     title="Bảo hành máy triệt lông URMINE 24 tháng và chương trình hoàn tiền 30 ngày",
     desc="URMINE bảo hành 24 tháng cho Trinity i15 Pro, Nova P5, Ice Cooling. Trinity i15 Pro có chương trình hoàn tiền nếu dùng đúng hướng dẫn 30 ngày không hiệu quả. Kích hoạt qua Zalo.",
     h1="Bảo hành 24 tháng và chương trình 30 ngày",
     answer="Cả ba dòng Trinity i15 Pro, Nova P5 và Ice Cooling được bảo hành 24 tháng. Với Trinity i15 Pro (DT015 Pro), nếu dùng đúng hướng dẫn 3–4 lần/tuần trong 30 ngày mà không có kết quả, bạn được hoàn tiền theo điều kiện chương trình.",
     body=[kv([("Bảo hành", "24 tháng (Trinity i15 Pro, Nova P5, Ice Cooling)"), ("Chương trình 30 ngày", "Trinity i15 Pro / DT015 Pro"),
               ("Điều kiện", "Dùng đúng hướng dẫn 3–4 lần/tuần trong 4 tuần, ghi lại tiến trình"), ("Kích hoạt", "Quét mã QR Zalo trên thiệp cảm ơn trong hộp"),
               ("Đổi trả", "7 ngày khi mua tại urmine.shop"), ("Xử lý yêu cầu", "Qua kênh bạn đã đặt hàng")]),
           sec("Các bước kích hoạt", "<ol><li>Giữ lại mã đơn hàng.</li><li>Quét mã QR Zalo trên thiệp cảm ơn trong hộp.</li><li>Gửi thông tin đơn hàng để xác nhận bảo hành và đăng ký chương trình 30 ngày.</li><li>Triệt đúng lịch 3–4 lần/tuần và ghi tiến trình trong app CTONE.</li></ol>"),
           STORES_VI])

# ---------------- GUIDES ----------------
page(path="/guides/", crumb="Hướng dẫn", eyebrow="Hướng dẫn",
     title="Hướng dẫn triệt lông IPL tại nhà | URMINE",
     desc="Các hướng dẫn triệt lông IPL tại nhà của URMINE: cách bắt đầu, lịch triệt và chăm sóc sau triệt, an toàn vùng bikini.",
     h1="Hướng dẫn triệt lông IPL tại nhà",
     answer="Bắt đầu từ bài cơ bản về IPL tại nhà, sau đó xem lịch triệt và chăm sóc sau triệt, và lưu ý riêng cho vùng bikini.",
     body=[cards([("Cơ bản", "Triệt lông IPL tại nhà", "IPL là gì, ai phù hợp, kỳ vọng thế nào", "/guides/ipl-hair-removal-at-home/"),
                  ("Lộ trình", "Lịch triệt và chăm sóc sau triệt", "Tần suất, mức năng lượng, những điều cần kiêng", "/guides/ipl-routine-and-aftercare/"),
                  ("An toàn", "Triệt vùng bikini", "Chuẩn bị, chế độ phù hợp, những gì tránh", "/guides/bikini-ipl-safety/")])])

page(path="/guides/ipl-hair-removal-at-home/", crumb="Triệt lông IPL tại nhà", parent=("/guides/", "Hướng dẫn"), eyebrow="Hướng dẫn cơ bản", schema="Article",
     title="Triệt lông IPL tại nhà: có hiệu quả không, ai nên dùng, chọn máy thế nào",
     desc="IPL tại nhà hoạt động thế nào, ai phù hợp, bao lâu có kết quả và cách chọn máy triệt lông IPL: năng lượng, làm lạnh, kiểm nghiệm, bảo hành.",
     h1="Triệt lông IPL tại nhà: hướng dẫn cho người mới",
     answer="IPL (ánh sáng xung cường độ cao) làm yếu nang lông qua nhiều buổi. Hiệu quả nhất khi lông sẫm màu hơn da. Thường cần triệt đều 3–4 lần/tuần trong khoảng 4 tuần để thấy lông thưa và mềm hơn, sau đó duy trì.",
     body=[sec("IPL hoạt động thế nào", "<p>Máy phát ánh sáng phổ rộng (khoảng 560–1200 nm). Sắc tố melanin trong sợi lông hấp thụ ánh sáng và chuyển thành nhiệt, làm yếu nang lông đang ở giai đoạn phát triển. Vì lông mọc theo chu kỳ, cần nhiều buổi để tác động đến hết các nang lông.</p>"),
           sec("Ai phù hợp", "<ul><li><strong>Phù hợp:</strong> da sáng đến ngăm, lông đen hoặc nâu.</li><li><strong>Cần thận trọng:</strong> da nâu đậm, lông nâu sáng. Dùng mức thấp và thử trên vùng nhỏ.</li><li><strong>Không phù hợp:</strong> da rất đậm; lông vàng nhạt, đỏ, bạc, trắng.</li></ul>"),
           sec("Chọn máy IPL theo 5 tiêu chí", """<ol>
<li><strong>Năng lượng:</strong> từ khoảng 20J trở lên cho lông cứng.</li>
<li><strong>Làm lạnh mặt tiếp xúc:</strong> sapphire làm lạnh giúp giảm rát, đặc biệt ở bikini và nách.</li>
<li><strong>Bằng chứng kiểm nghiệm:</strong> có số báo cáo IEC 60601-1, IEC 62471, ISO 10993.</li>
<li><strong>Bảo hành tại Việt Nam:</strong> thời hạn rõ ràng, kênh hỗ trợ cụ thể.</li>
<li><strong>Chế độ cho từng vùng:</strong> mặt, bikini, chế độ cho lông cứng.</li>
</ol><p>Ví dụ: URMINE <a href="/products/trinity-i15-pro/">Trinity i15 Pro</a> có 27J, sapphire 2°C, kiểm nghiệm IEC và ISO 10993, bảo hành 24 tháng.</p>"""),
           sec("Triệt tại nhà hay ra spa", "<p>Spa dùng máy công suất lớn và có kỹ thuật viên, nhưng tính phí theo buổi và cần đặt lịch. Máy tại nhà trả tiền một lần, chủ động thời gian và riêng tư, đổi lại bạn cần tự triệt đều đặn.</p>")],
     faq=[("Triệt lông IPL tại nhà có vĩnh viễn không?", "IPL giúp giảm lông lâu dài và làm lông mọc lại thưa, mềm hơn. Phần lớn người dùng cần triệt duy trì định kỳ."),
          ("Triệt IPL có đau không?", "Cảm giác thường là ấm nhẹ như dây thun búng. Máy có mặt làm lạnh sapphire giúp giảm cảm giác nóng rát.")])

page(path="/guides/ipl-routine-and-aftercare/", crumb="Lịch triệt và chăm sóc", parent=("/guides/", "Hướng dẫn"), eyebrow="Lộ trình", schema="Article",
     title="Lịch triệt lông IPL và chăm sóc da sau triệt | URMINE",
     desc="Lịch triệt IPL 3–4 lần/tuần trong 4 tuần, cách tăng mức năng lượng, những điều cần kiêng sau triệt và lỗi thường gặp.",
     h1="Lịch triệt IPL và chăm sóc sau triệt",
     answer="Triệt 3–4 lần mỗi tuần trong 4 tuần đầu, bắt đầu ở mức 1–2 và tăng dần. Sau triệt kiêng nước 2–4 giờ, tránh mỹ phẩm có cồn và hoạt chất mạnh 12–24 giờ, tránh nắng 48 giờ.",
     body=[sec("Lộ trình 4 tuần", ROUTINE_VI),
           sec("Lỗi thường gặp", "<ul><li>Triệt không đều, bỏ nhiều buổi liên tiếp.</li><li>Wax hoặc nhổ lông giữa các buổi, làm mất chân lông cần tác động.</li><li>Tăng mức quá nhanh khi da chưa quen.</li><li>Ra nắng ngay sau triệt mà không chống nắng.</li></ul>"),
           sec("Không dùng khi", AVOID_VI)])

page(path="/guides/bikini-ipl-safety/", crumb="Triệt vùng bikini", parent=("/guides/", "Hướng dẫn"), eyebrow="An toàn", schema="Article",
     title="Triệt lông vùng bikini bằng IPL tại nhà: cách làm an toàn",
     desc="Hướng dẫn triệt bikini bằng IPL tại nhà: chọn máy có chế độ bikini và làm lạnh, mức năng lượng khởi đầu, vùng cần tránh và chăm sóc sau triệt.",
     h1="Triệt lông vùng bikini bằng IPL tại nhà",
     answer="Chọn máy có chế độ bikini và mặt làm lạnh, cạo sạch trước, bắt đầu ở mức 1–2, chỉ triệt vùng da ngoài, tránh niêm mạc và nốt ruồi đậm màu. Lông bikini thường cứng, chế độ nhiều xung như PHR giúp tác động sâu hơn mà không tăng nhiệt đột ngột.",
     body=[sec("Chuẩn bị", "<ul><li>Cạo sạch khi tắm, xuôi chiều lông mọc.</li><li>Lau khô da, không thoa kem hay dầu.</li><li>Đeo kính bảo hộ.</li></ul>"),
           sec("Khi triệt", "<ul><li>Dùng chế độ bikini hoặc PHR, bắt đầu mức 1–2.</li><li>Áp máy vuông góc, phủ kín cửa sổ phát sáng lên da.</li><li>Không triệt lên niêm mạc, vùng da sẫm màu đậm, nốt ruồi, hình xăm.</li><li>Dừng lại nếu đau bất thường.</li></ul>"),
           sec("Máy URMINE dùng được cho bikini", '<p><a href="/products/trinity-i15-pro/">Trinity i15 Pro</a> (chế độ bikini + PHR 4 xung, sapphire 2°C) và <a href="/products/nova-p5/">Nova P5</a>. Ice Cooling không dùng cho vùng bikini.</p>')])

# ---------------- COMPARE ----------------
page(path="/compare/", crumb="So sánh", eyebrow="So sánh",
     title="So sánh máy triệt lông IPL | URMINE",
     desc="So sánh URMINE với máy IPL không thương hiệu, với máy IPL phổ thông và với triệt lông tại spa.",
     h1="So sánh trước khi mua",
     answer="Các trang so sánh dưới đây dùng số liệu công bố của URMINE và tiêu chí kiểm chứng được: năng lượng, làm lạnh, kiểm nghiệm, bảo hành, giá.",
     body=[cards([("So sánh", "URMINE và máy IPL không thương hiệu", "Thông số, kiểm nghiệm, bảo hành, hỗ trợ", "/compare/urmine-vs-generic-ipl/"),
                  ("So sánh", "Trinity i15 Pro và máy IPL phổ thông", "Năng lượng, làm lạnh, tốc độ, giá", "/compare/trinity-i15-pro-vs-entry-ipl/"),
                  ("Dòng URMINE", "Trinity, Nova, Ice Cooling", "Bảng so sánh 3 dòng máy", "/products/")])])

page(path="/compare/urmine-vs-generic-ipl/", crumb="URMINE và IPL không thương hiệu", parent=("/compare/", "So sánh"), eyebrow="So sánh",
     title="Máy triệt lông URMINE và máy IPL không thương hiệu: khác nhau ở đâu",
     desc="So sánh URMINE với máy triệt lông IPL không thương hiệu trên sàn: thông số công bố, hồ sơ kiểm nghiệm, sách hướng dẫn tiếng Việt, bảo hành và hỗ trợ.",
     h1="URMINE và máy IPL không thương hiệu",
     answer="Khác biệt chính nằm ở những gì kiểm chứng được: URMINE công bố thông số từng model, có số báo cáo kiểm nghiệm IEC và ISO 10993, sách hướng dẫn tiếng Việt và bảo hành 24 tháng tại Việt Nam.",
     body=['<div class="table-scroll"><table><thead><tr><th>Tiêu chí</th><th class="col-hero">URMINE</th><th>IPL không thương hiệu</th></tr></thead><tbody>'
           '<tr><td>Thông số</td><td class="col-hero">Công bố năng lượng, bước sóng, nhiệt độ làm lạnh cho từng model</td><td>Thường thiếu hoặc không nhất quán</td></tr>'
           '<tr><td>Kiểm nghiệm</td><td class="col-hero">IEC 60601-1, IEC 62471, ISO 10993, FCC, RED/UKCA có số báo cáo</td><td>Thường không công bố</td></tr>'
           '<tr><td>Sách hướng dẫn</td><td class="col-hero">Tiếng Việt, Thái, Indonesia, Mã Lai, Anh</td><td>Thường chỉ tiếng Anh hoặc tiếng Trung</td></tr>'
           '<tr><td>Bảo hành</td><td class="col-hero">24 tháng, kích hoạt qua Zalo</td><td>Không rõ ràng</td></tr>'
           '<tr><td>Kênh bán</td><td class="col-hero">urmine.shop, Shopee Mall, TikTok Shop chính hãng</td><td>Nhiều người bán, khó truy nguồn</td></tr>'
           '</tbody></table></div>', STORES_VI])

page(path="/compare/trinity-i15-pro-vs-entry-ipl/", crumb="Trinity i15 Pro và IPL phổ thông", parent=("/compare/", "So sánh"), eyebrow="So sánh",
     title="Trinity i15 Pro và máy IPL phổ thông: có đáng tiền hơn không",
     desc="So sánh URMINE Trinity i15 Pro (27J, sapphire 2°C, PHR, Auto Glide) với máy IPL phổ thông như URMINE Ice Cooling (19,8J, kim loại 5°C).",
     h1="Trinity i15 Pro và máy IPL phổ thông",
     answer="Trinity i15 Pro đáng chọn hơn nếu bạn triệt bikini, nách, lông cứng hoặc muốn triệt toàn thân nhanh. Nếu chỉ triệt tay chân với ngân sách thấp, máy phổ thông như Ice Cooling là đủ.",
     body=['<div class="table-scroll"><table><thead><tr><th>Tiêu chí</th><th class="col-hero">Trinity i15 Pro</th><th>Ice Cooling (phổ thông)</th></tr></thead><tbody>'
           '<tr><td>Giá</td><td class="col-hero num">4.200.000 ₫</td><td class="num">1.550.000 ₫</td></tr>'
           '<tr><td>Năng lượng</td><td class="col-hero num">27J</td><td class="num">19,8J</td></tr>'
           '<tr><td>Làm lạnh</td><td class="col-hero">Sapphire 16,6 cm², 2°C</td><td>Kim loại 5–15°C</td></tr>'
           '<tr><td>Công nghệ</td><td class="col-hero">Đèn kép + PHR 4 xung</td><td>1 tia đơn</td></tr>'
           '<tr><td>Vùng triệt</td><td class="col-hero">Body, bikini, mặt</td><td>Body</td></tr>'
           '<tr><td>Toàn thân</td><td class="col-hero">~10 phút (Auto Glide)</td><td>—</td></tr>'
           '<tr><td>Số xung</td><td class="col-hero">Không giới hạn</td><td class="num">999.900</td></tr>'
           '</tbody></table></div>', STORES_VI])

# ---------------- FAQ / CONTACT / PRIVACY ----------------
page(path="/faq/", crumb="Hỏi đáp", eyebrow="Hỏi đáp",
     title="Hỏi đáp về máy triệt lông IPL URMINE",
     desc="Giải đáp về URMINE: thương hiệu, chọn máy, IPL có đau không, bao lâu có kết quả, da ngăm có dùng được không, bảo hành, mua chính hãng ở đâu.",
     h1="Câu hỏi thường gặp",
     answer="Những câu hỏi người mua hay hỏi nhất trước khi chọn máy triệt lông IPL URMINE.",
     body=[], faq_from_home=True)

page(path="/contact/", crumb="Liên hệ", eyebrow="Liên hệ",
     title="Liên hệ URMINE Việt Nam",
     desc="Kênh liên hệ chính thức của URMINE: email hỗ trợ sản phẩm, Facebook Urmine Vietnam, Shopee Mall URMINE.VN, TikTok Shop URMINE VN STORE, urmine.shop.",
     h1="Liên hệ URMINE",
     answer=f"Câu hỏi về sản phẩm: {EMAIL}. Đơn hàng và bảo hành: liên hệ qua đúng kênh bạn đã mua.",
     body=[kv([("Email hỗ trợ sản phẩm", EMAIL), ("Facebook", f'<a href="{FB}">Urmine Vietnam</a>'), ("Website bán hàng", f'<a href="{SHOP}">urmine.shop</a>'),
               ("Shopee Mall", f'<a href="{SHOPEE}">URMINE.VN</a>'), ("TikTok Shop", f'<a href="{TIKTOK}">URMINE VN STORE</a>'),
               ("Zalo bảo hành", "Mã QR trên thiệp cảm ơn trong hộp máy")])])

page(path="/privacy/", crumb="Quyền riêng tư", eyebrow="Pháp lý",
     title="Chính sách quyền riêng tư | URMINE Tech",
     desc="urminetech.com dùng Google Analytics 4 để đo lượt truy cập tổng hợp và không cố ý gửi thông tin định danh cá nhân.",
     h1="Chính sách quyền riêng tư",
     answer="urminetech.com dùng Google Analytics 4 để đo lượt xem trang, nguồn truy cập và lượt nhấp liên kết ở dạng tổng hợp. Trang không thu thập tên, email hay số điện thoại.",
     body=[sec("Dữ liệu được đo", "<ul><li>Số lượt truy cập và nguồn giới thiệu.</li><li>Lượt xem trang, cuộn trang, nhấp liên kết ra ngoài.</li><li>Cookie hoặc định danh trình duyệt do Google Analytics sử dụng.</li></ul>"),
           sec("Lựa chọn của bạn", "<p>Bạn có thể chặn hoặc giới hạn phân tích qua cài đặt quyền riêng tư của trình duyệt hoặc tiện ích chặn Google Analytics.</p>"),
           sec("Liên hệ", f"<p>{EMAIL}</p>")])

# ---------------- MARKETS ----------------
page(path="/markets/", crumb="Thị trường", eyebrow="Thị trường",
     title="URMINE tại Việt Nam, Thái Lan, Malaysia, Indonesia",
     desc="Trang thông tin URMINE theo từng thị trường: Việt Nam, Thái Lan, Malaysia, Indonesia.",
     h1="URMINE theo thị trường",
     answer="URMINE có trang riêng bằng ngôn ngữ của từng thị trường. Kênh bán chính hãng hiện tại là Việt Nam.",
     body=[cards([("vi-VN", "Việt Nam", "Tiếng Việt · kênh bán chính hãng", "/markets/vietnam/"),
                  ("th-TH", "ประเทศไทย", "ภาษาไทย", "/markets/thailand/"),
                  ("ms-MY", "Malaysia", "Bahasa Melayu", "/markets/malaysia/"),
                  ("id-ID", "Indonesia", "Bahasa Indonesia", "/markets/indonesia/")])])

page(path="/markets/vietnam/", crumb="Việt Nam", parent=("/markets/", "Thị trường"), eyebrow="Việt Nam",
     title="Máy triệt lông IPL URMINE tại Việt Nam: giá, nơi mua chính hãng, bảo hành",
     desc="URMINE tại Việt Nam: Trinity i15 Pro 4,2 triệu, Nova P5 2,55 triệu, Ice Cooling 1,55 triệu. Mua chính hãng tại urmine.shop, Shopee Mall, TikTok Shop. Bảo hành 24 tháng.",
     h1="URMINE tại Việt Nam",
     answer="Tại Việt Nam, URMINE bán chính hãng qua urmine.shop, Shopee Mall URMINE.VN và TikTok Shop URMINE VN STORE. Giá: Trinity i15 Pro 4.200.000 ₫, Nova P5 2.550.000 ₫, Ice Cooling 1.550.000 ₫. Bảo hành 24 tháng.",
     body=[cards([("4.200.000 ₫", "Trinity i15 Pro", "27J, sapphire 2°C, PHR 4 xung", "/products/trinity-i15-pro/"),
                  ("2.550.000 ₫", "Nova P5", "22J, sapphire 4°C", "/products/nova-p5/"),
                  ("1.550.000 ₫", "Ice Cooling", "19,8J, cho tay chân", "/products/ice-cooling/")]),
           sec("Cách dùng", ROUTINE_VI), STORES_VI])

page(path="/markets/thailand/", crumb="ประเทศไทย", parent=("/markets/", "Thị trường"), eyebrow="ประเทศไทย", lang="th",
     title="เครื่องกำจัดขน IPL URMINE: Trinity i15 Pro สเปก วิธีใช้ การรับประกัน",
     desc="URMINE (อ่านว่า you are mine) เครื่องกำจัดขน IPL ใช้ที่บ้าน Trinity i15 Pro 27J หน้าสัมผัสแซฟไฟร์เย็น 2°C PHR 4 พัลส์ แอป CTONE รับประกัน 24 เดือน",
     h1="URMINE เครื่องกำจัดขน IPL ใช้ที่บ้าน",
     answer="URMINE (อ่านว่า “you are mine”) เป็นแบรนด์เครื่องกำจัดขน IPL สำหรับใช้ที่บ้าน รุ่นเรือธง Trinity i15 Pro (รุ่น DT015 Pro) มีพลังงานสูงสุด 27J ไฟคู่ร่วมกับ PHR 4 พัลส์ หน้าสัมผัสแซฟไฟร์ 16.6 ตร.ซม. เย็นถึง 2°C เชื่อมต่อแอป CTONE และรับประกัน 24 เดือน",
     body=[kv([("รุ่น", "Trinity i15 Pro / DT015 Pro"), ("พลังงานสูงสุด", "27J"), ("กำลังไฟ", "100W"), ("เทคโนโลยี", "IPL ไฟคู่ + PHR 4 พัลส์"),
               ("ระบบทำความเย็น", "แซฟไฟร์ 16.6 ตร.ซม. 2°C นานสูงสุด 60 นาที"), ("ความยาวคลื่น", "560–1200 nm"), ("ระดับพลังงาน", "1–5"),
               ("โหมด", "ใบหน้า ร่างกาย บิกินี PHR"), ("แอป", "CTONE ผ่านบลูทูธ"), ("คู่มือ", "มีภาษาไทย"), ("รับประกัน", "24 เดือน")]),
           sec("วิธีใช้", "<ol><li>โกนขนให้สะอาดก่อนใช้ ห้ามแว็กซ์หรือใช้ครีมกำจัดขน</li><li>เริ่มที่ระดับ 1–2 วางเครื่องตั้งฉาก 90° กับผิว และสวมแว่นป้องกัน</li><li>ใช้ 3–4 ครั้งต่อสัปดาห์ เป็นเวลา 4 สัปดาห์ แล้วใช้เพื่อคงสภาพ</li><li>หลีกเลี่ยงแดด 48 ชั่วโมงหลังใช้ และทาครีมกันแดด SPF 30 ขึ้นไป</li></ol>"),
           sec("ข้อควรระวัง", "<ul><li>ห้ามยิงแสงใกล้ดวงตาหรือคิ้ว</li><li>ห้ามใช้บนรอยสัก ปานดำ ไฝสีเข้ม แผล หรือผิวที่ระคายเคือง</li><li>ไม่เหมาะกับผิวคล้ำมาก และขนสีบลอนด์อ่อน แดง เทา หรือขาว</li></ul>"),
           sec("ความปลอดภัย", "<p>รุ่น DT015 Pro มีรายงานทดสอบ IEC 60601-1 และ IEC 62471 (DE25040077 / DE25040080), ISO 10993, FCC ID 2BNHB-DT015PRO และ RED/UKCA <a href=\"/compliance/\">ดูรายละเอียด</a></p>")])

page(path="/markets/malaysia/", crumb="Malaysia", parent=("/markets/", "Thị trường"), eyebrow="Malaysia", lang="ms",
     title="Peranti IPL URMINE untuk kegunaan di rumah: Trinity i15 Pro, spesifikasi dan waranti",
     desc="URMINE (disebut you are mine) peranti IPL di rumah. Trinity i15 Pro 27J, permukaan nilam sejuk 2°C, PHR 4 denyut, aplikasi CTONE, waranti 24 bulan.",
     h1="URMINE, peranti IPL untuk kegunaan di rumah",
     answer="URMINE (disebut “you are mine”) ialah jenama peranti penghilang bulu IPL untuk kegunaan di rumah. Model utama Trinity i15 Pro (model DT015 Pro) mempunyai tenaga maksimum 27J, lampu berkembar dengan PHR 4 denyut, permukaan nilam 16.6 cm² sejuk hingga 2°C, aplikasi CTONE dan waranti 24 bulan.",
     body=[kv([("Model", "Trinity i15 Pro / DT015 Pro"), ("Tenaga maksimum", "27J"), ("Kuasa", "100W"), ("Teknologi", "IPL lampu berkembar + PHR 4 denyut"),
               ("Penyejukan", "Nilam 16.6 cm², 2°C, sehingga 60 minit"), ("Panjang gelombang", "560–1200 nm"), ("Tahap tenaga", "1–5"),
               ("Mod", "Muka, badan, bikini, PHR"), ("Aplikasi", "CTONE melalui Bluetooth"), ("Manual", "Termasuk Bahasa Melayu"), ("Waranti", "24 bulan")]),
           sec("Cara guna", "<ol><li>Cukur bulu dengan bersih. Jangan wax atau guna krim penghilang bulu.</li><li>Mulakan pada tahap 1–2, letakkan peranti tegak 90° pada kulit dan pakai cermin mata pelindung.</li><li>Guna 3–4 kali seminggu selama 4 minggu, kemudian teruskan untuk penyelenggaraan.</li><li>Elakkan matahari 48 jam selepas rawatan dan sapukan SPF 30+.</li></ol>"),
           sec("Jangan guna", "<ul><li>Berhampiran mata atau kening.</li><li>Pada tatu, tanda lahir gelap, tahi lalat gelap, luka atau kulit yang merengsa.</li><li>Pada kulit sangat gelap, atau bulu perang muda, merah, kelabu atau putih.</li></ul>"),
           sec("Keselamatan", "<p>Model DT015 Pro mempunyai laporan ujian IEC 60601-1 dan IEC 62471 (DE25040077 / DE25040080), ISO 10993, FCC ID 2BNHB-DT015PRO dan RED/UKCA. <a href=\"/compliance/\">Lihat butiran</a></p>")])

page(path="/markets/indonesia/", crumb="Indonesia", parent=("/markets/", "Thị trường"), eyebrow="Indonesia", lang="id",
     title="Alat IPL rumahan URMINE: Trinity i15 Pro, spesifikasi, cara pakai, garansi",
     desc="URMINE (dibaca you are mine) alat IPL rumahan. Trinity i15 Pro 27J, permukaan safir dingin 2°C, PHR 4 pulsa, aplikasi CTONE, garansi 24 bulan.",
     h1="URMINE, alat IPL untuk di rumah",
     answer="URMINE (dibaca “you are mine”) adalah merek alat penghilang bulu IPL untuk di rumah. Model unggulan Trinity i15 Pro (model DT015 Pro) memiliki energi maksimum 27J, lampu ganda dengan PHR 4 pulsa, permukaan safir 16,6 cm² yang dingin hingga 2°C, aplikasi CTONE, dan garansi 24 bulan.",
     body=[kv([("Model", "Trinity i15 Pro / DT015 Pro"), ("Energi maksimum", "27J"), ("Daya", "100W"), ("Teknologi", "IPL lampu ganda + PHR 4 pulsa"),
               ("Pendinginan", "Safir 16,6 cm², 2°C, hingga 60 menit"), ("Panjang gelombang", "560–1200 nm"), ("Level energi", "1–5"),
               ("Mode", "Wajah, tubuh, bikini, PHR"), ("Aplikasi", "CTONE via Bluetooth"), ("Manual", "Termasuk Bahasa Indonesia"), ("Garansi", "24 bulan")]),
           sec("Cara pakai", "<ol><li>Cukur bulu hingga bersih. Jangan waxing atau memakai krim perontok.</li><li>Mulai di level 1–2, tempelkan alat tegak 90° ke kulit dan pakai kacamata pelindung.</li><li>Gunakan 3–4 kali per minggu selama 4 minggu, lalu lanjutkan untuk perawatan.</li><li>Hindari sinar matahari 48 jam setelah pemakaian dan gunakan SPF 30+.</li></ol>"),
           sec("Jangan digunakan", "<ul><li>Di dekat mata atau alis.</li><li>Pada tato, tanda lahir gelap, tahi lalat gelap, luka, atau kulit yang iritasi.</li><li>Pada kulit sangat gelap, atau bulu pirang muda, merah, abu-abu, atau putih.</li></ul>"),
           sec("Keamanan", "<p>Model DT015 Pro memiliki laporan uji IEC 60601-1 dan IEC 62471 (DE25040077 / DE25040080), ISO 10993, FCC ID 2BNHB-DT015PRO, dan RED/UKCA. <a href=\"/compliance/\">Lihat detail</a></p>")])
